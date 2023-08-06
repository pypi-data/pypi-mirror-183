"""
"""
from scinode.core import DBItem
from scinode.engine.node_engine import EngineNode
from scinode.database.client import db_node
import logging


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class EngineNodeTree(DBItem):
    """EngineNodeTree Class.
    Process the nodetree with the data from the database.
    It can be called by the daemon or called manually.

    uuid: str
        uuid of the nodetree.

    Example:

    >>> # load nodetree data from database
    >>> query = {"uuid": "your-nodetree-uuid"}
    >>> dbdata = scinodedb["nodetree"].find_one(query)
    >>> nodetree = EngineNodeTree(uuid=dbdata["uuid"])
    >>> nodetree.process()
    """

    db_name: str = "nodetree"

    def __init__(self, uuid=None) -> None:
        """_summary_

        Args:
            uuid (_type_, optional): _description_. Defaults to None.
            dbdata (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(uuid)
        self.record = self.dbdata
        self.name = self.record["name"]

    def process(self):
        """process the nodetree from database.
        1) apply_nodetree_action
        2) apply_node_action
        3) update_node_state
        """
        try:
            # apply action to nodetree
            self.apply_nodetree_action()
            # do action for each node
            dbdata_nodes = self.dbdata_nodes
            self.apply_node_action(dbdata_nodes)
            # analysze node states
            dbdata_nodes = self.dbdata_nodes
            node_states = self.analyze_node_state(dbdata_nodes)
            # update nodetree state
            state, action = self.analyze_nodetree_state(node_states)
            self.update_nodetree_state(state, action)
            # update node state
            self.update_node_state(node_states, dbdata_nodes)
        except Exception:
            import traceback

            error = traceback.format_exc()
            print(
                "xxxxxxxxxx Failed xxxxxxxxxx\nNode {} failed due to: {}".format(
                    self.name, error
                )
            )
            self.update_db_keys({"state": "FAILED"})
            self.update_db_keys({"action": "NONE"})
            self.update_db_keys({"error": str(error)})

    def apply_nodetree_action(self):
        """Apply action to nodetree"""
        action = self.action
        if action.upper() == "UPDATE":
            pass
        elif action.upper() == "LAUNCH":
            self.action = "UPDATE"
            self.state = "RUNNING"
        elif action.upper() == "PAUSE":
            self.pause()
        elif action.upper() == "PLAY":
            self.play()
        elif action.upper() == "CANCEL":
            self.cancel()
        else:
            print("Action {} is not supported.".format(self.action))

    def apply_node_action(self, dbdata_nodes):
        """apply action to all nodes"""
        for name, dbdata in dbdata_nodes.items():
            if dbdata["action"] == "PAUSE":
                self.pause_node(name)
            elif dbdata["action"] == "PLAY":
                self.play_node(name)
            elif dbdata["action"] == "SKIP":
                self.skip_node(name)
            elif dbdata["action"] == "RESET":
                self.reset_node(name)

    def analyze_node_state(self, dbdata_nodes):
        """Analyze node states.

        - check if node is ready (input nodes finished)
        - if one node fails, is cancelled or is paused, change
            all its children nodes to hanging.

        Args:
            dbdata_nodes (_type_): _description_
        """
        # "FINISHED",  "CANCELLED",  "FAILED",  "RUNNING",  "PAUSED",  "CREATED",  "WAITING",  "SKIPPED",  "UNKNOWN"
        # fake state: "HANGING"
        #
        node_states = {}
        for name, dbdata in dbdata_nodes.items():
            node_states[name] = dbdata["state"]
        #
        # TODO control node needs special treatment.
        # update node will ignore the "Update" socket for the first run
        for name, dbdata in dbdata_nodes.items():
            # check parent nodes
            if node_states[name] in ["CREATED", "WAITING"]:
                ready = self.check_parent_state(name, dbdata_nodes)
                if ready:
                    node_states[name] = "READY"
            elif node_states[name] in ["SCATTERED"]:
                state, action = self.check_scattered_state(name)
                node_states[name] = state
            # update child nodes
            if dbdata["state"] in ["FAILED", "SKIPPED", "CANCELLED"]:
                children = self.record["connectivity"]["children"][name][0]
                for c in children:
                    node_states[c] = "HANGING"
        return node_states

    def update_node_state(self, node_states, dbdata_nodes):
        """update node state

        Args:
            node_states (_type_): _description_
            dbdata_nodes (_type_): _description_
        """

        for name, dbdata in dbdata_nodes.items():
            query = {"uuid": dbdata["uuid"]}
            newvalues = {"$set": {"state": node_states[name]}}
            db_node.update_one(query, newvalues)

    def analyze_nodetree_state(self, node_states):
        """analyze nodetree state

        Args:
            node_states (_type_): _description_
        """
        states = list(node_states.values())
        state_list = [
            "CREATED",
            "READY",
            "FINISHED",
            "FAILED",
            "PAUSED",
            "SKIPPED",
            "RUNNING",
            "WAITING",
            "SCATTERED",
            "CANCELLED",
        ]

        counts = {x: states.count(x) for x in state_list}
        s = ""
        # s += "    Created: {}, Ready: {}, FINISHED: {}, Failed: {}, Paused: {}, Skipped: {}, Running: {}, Waiting: {}, Scattered: {}, Cancelled: {}\n".format(
        s += "{:4d} {:4d} {:4d} {:4d} {:4d} {:4d} {:4d} {:4d} {:4d} {:4d}\n".format(
            counts["CREATED"],
            counts["READY"],
            counts["RUNNING"],
            counts["FINISHED"],
            counts["FAILED"],
            counts["PAUSED"],
            counts["SKIPPED"],
            counts["WAITING"],
            counts["SCATTERED"],
            counts["CANCELLED"],
        )
        log = "{}".format(s)
        self.write_log(log)
        # get nodetree state
        if (
            counts["CREATED"] == 0
            and counts["READY"] == 0
            and counts["RUNNING"] == 0
            and counts["FAILED"] == 0
            and counts["PAUSED"] == 0
            and counts["WAITING"] == 0
            and counts["SCATTERED"] == 0
        ):
            state = "FINISHED"
            action = "NONE"
        elif (
            counts["CREATED"] == 0
            and counts["RUNNING"] == 0
            and counts["FAILED"] != 0
            and counts["PAUSED"] == 0
            and counts["WAITING"] == 0
            and counts["SCATTERED"] == 0
        ):
            state = "FAILED"
            action = "NEED_HELP"
        elif (
            counts["CREATED"] == 0
            and counts["RUNNING"] == 0
            and counts["PAUSED"] == 0
            and counts["CANCELLED"] != 0
        ):
            state = "CANCELLED"
            action = "NEED_HELP"
        else:
            state = "RUNNING"
            action = "UPDATE"
        return state, action

    def update_nodetree_state(self, state, action):
        self.update_db_keys({"state": state, "action": action})

    def launch(self):
        """Launch nodetree."""
        self.state = "READY"
        self.action = "LAUNCH"
        self.load_nodes()
        for name, node in self.nodes.items():
            node.action = "LAUNCH"

    @property
    def dbdata_nodes(self):
        """Fetch node data from database
        1) node belong to this nodetree
        2) reference node used in this nodetree

        Returns:
            dict: node data from database
        """
        query = {"meta.nodetree_uuid": self.dbdata["uuid"]}
        project = {"_id": 0, "uuid": 1, "name": 1, "state": 1, "action": 1}
        datas = list(db_node.find(query, project))
        dbdata_nodes = {data["name"]: data for data in datas}
        # find the ref nodes
        ref_nodes = [
            node["name"]
            for node in self.record["nodes"].values()
            if node["node_type"] == "REF"
        ]
        # populate the ref nodes
        for name in ref_nodes:
            query = {"uuid": self.record["nodes"][name]["uuid"]}
            data = db_node.find_one(query, project)
            dbdata_nodes[name] = data

        return dbdata_nodes

    def cancel(self):
        dbdata_nodes = self.dbdata_nodes
        for name, dbdata in dbdata_nodes.items():
            node = EngineNode(dbdata)
            node.update_db_keys({"action": "CANCEL"})
        self.action = "NONE"

    @property
    def daemon_name(self):
        return self.dbdata.get("daemon_name")

    def check_parent_state(self, name, dbdata_nodes):
        """Check parent states

        Args:
            name (str): name of node to be check
            dbdata_nodes (dict): data of all nodes

        Returns:
            ready (bool): ready to launch or not
        """
        ready = True
        # control node needs special treatment.
        # update node will ingore the "Update" socket for the first run
        inputs = self.record["connectivity"]["inputs"][name]
        # print("node_type: ", self.record["nodes"][name]["node_type"])
        if self.record["nodes"][name]["node_type"] == "Update":
            record = db_node.find_one(
                {"uuid": self.record["nodes"][name]["uuid"]},
                {"_id": 0, "meta.counter": 1},
            )
            counter = record["meta"]["counter"]
            print("counter: ", counter)
            if counter == 0:
                inputs.pop("Update", None)
        # scatter node will always ingore the "Stop" socket
        elif self.record["nodes"][name]["node_type"] == "Scatter":
            inputs.pop("Stop", None)
        #
        for socke_name, input_nodes in inputs.items():
            for input_node_name in input_nodes:
                if dbdata_nodes[input_node_name]["state"] != "FINISHED":
                    ready = False
                    return ready
        return ready

    def check_scattered_state(self, name):
        """Check scattered states

        Args:
            name (str): name of node to be check
            dbdata_nodes (dict): data of all nodes

        Returns:
            ready (bool): ready to launch or not
        """
        state = "SCATTERED"
        action = "GATHER"
        node_states = {}
        children = db_node.find(
            {"meta.scattered_from": self.record["nodes"][name]["uuid"]},
            {"uuid": 1, "name": 1, "state": 1},
        )
        print("    \nCheck scattered node states: ")
        for child in children:
            node_states[child["name"]] = child["state"]
        s = ""
        states = list(node_states.values())
        state_list = [
            "CREATED",
            "READY",
            "FINISHED",
            "FAILED",
            "PAUSED",
            "SKIPPED",
            "RUNNING",
            "WAITING",
            "SCATTERED",
            "CANCELLED",
        ]

        counts = {x: states.count(x) for x in state_list}
        s = ""
        s += "    Created: {}, Ready: {}, FINISHED: {}, Failed: {}, Paused: {}, Skipped: {}, Running: {}, Waiting: {}, Scattered: {}, Cancelled: {}\n".format(
            counts["CREATED"],
            counts["READY"],
            counts["FINISHED"],
            counts["FAILED"],
            counts["PAUSED"],
            counts["SKIPPED"],
            counts["RUNNING"],
            counts["WAITING"],
            counts["SCATTERED"],
            counts["CANCELLED"],
        )
        if (
            counts["CREATED"] == 0
            and counts["RUNNING"] == 0
            and counts["FAILED"] == 0
            and counts["PAUSED"] == 0
            and counts["WAITING"] == 0
            and counts["SCATTERED"] == 0
        ):
            state = "READY"
            action = "GATHER"
        elif (
            counts["CREATED"] == 0
            and counts["RUNNING"] == 0
            and counts["FAILED"] != 0
            and counts["PAUSED"] == 0
            and counts["WAITING"] == 0
            and counts["SCATTERED"] == 0
        ):
            state = "FAILED"
            action = "NEED_HELP"
        elif (
            counts["CREATED"] == 0
            and counts["RUNNING"] == 0
            and counts["PAUSED"] == 0
            and counts["CANCELLED"] != 0
        ):
            state = "CANCELLED"
            action = "NEED_HELP"

        return state, action

    def load_nodes(self):
        dbdata_nodes = self.dbdata_nodes
        nodes = {}
        for name, dbdata in dbdata_nodes.items():
            node = EngineNode(uuid=dbdata["uuid"])  # , self.daemon_name)
            nodes[node.name] = node
        self.nodes = nodes

    def write_log(self, log, daemon=False, database=True):
        if daemon:
            print(log)
        if database:
            old_log = self.db.find_one({"uuid": self.uuid}, {"_id": 0, "log": 1})["log"]
            log = old_log + log
            self.update_db_keys({"log": log})
