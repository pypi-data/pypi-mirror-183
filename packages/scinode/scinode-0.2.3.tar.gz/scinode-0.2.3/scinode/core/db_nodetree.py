"""
"""
from scinode.core import DBItem
from scinode.core.db_node import DBNode
from scinode.database.client import db_node
from pprint import pprint
import logging


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def skip_ref_node(func):
    def wrapper(self, name, **kwargs):
        if self.record["nodes"][name]["node_type"] == "REF":
            raise Exception("Can not change state of a reference node")
        return func(self, name, **kwargs)

    return wrapper


class DBNodeTree(DBItem):
    """DBNodeTree Class.
    Nodetree with the data from the database.

    uuid: str
        uuid of the nodetree.

    Example:

    >>> # load nodetree data from database
    >>> nodetree = DBNodeTree(uuid=uuid)
    >>> nodetree.reset_node("add1")
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

    def update_nodetree_state(self, state, action):
        self.update_db_keys({"state": state, "action": action})

    def launch(self):
        """Launch nodetree."""
        self.state = "READY"
        self.action = "LAUNCH"
        for name, node in self.nodes.items():
            node.action = "LAUNCH"

    @classmethod
    def save(self, ntdata):
        """Save nodetree to database."""
        from scinode.engine.nodetree_launch import LaunchNodeTree

        logger.debug("save_to_db: {}".format(ntdata["name"]))
        ntdata["state"] = "CREATED"
        lnt = LaunchNodeTree(ntdata)
        lnt.save()

    def edit_from_yaml(self, filename=None, string=None):
        from scinode.utils import load_yaml
        from scinode.utils.nodetree import get_nt_full_data

        new_data = load_yaml(filename=filename, string=string)
        ntdata = get_nt_full_data({"uuid": self.uuid})
        for ndata in new_data["nodes"]:
            ntdata["nodes"][ndata["name"]] = DBNode.update_from_dict(ndata)
        self.save(ntdata)

    def edit_node_from_yaml(self, uuid, filename=None, string=None):
        """Edit node from yaml file.

        Args:
            uuid (str): uuid the node be edited.
            filename (str, optional): _description_. Defaults to None.
            string (str, optional): _description_. Defaults to None.

        Returns:
            node: _description_
        """
        from scinode.utils import load_yaml
        from scinode.utils.nodetree import get_nt_full_data

        ndata = load_yaml(filename=filename, string=string)
        ndata = DBNode.update_from_dict(ndata)
        ntdata = get_nt_full_data({"uuid": self.uuid})
        ntdata["nodes"][ndata["name"]] = ndata
        self.save(ntdata)

    def set_node_property(self, name, data):
        """Edit node from yaml file.

        Args:
            uuid (str): uuid the node be edited.
            filename (str, optional): _description_. Defaults to None.
            string (str, optional): _description_. Defaults to None.

        Returns:
            node: _description_
        """
        from scinode.utils.nodetree import get_nt_full_data
        from scinode.utils.node import get_node_data
        import pickle

        query = {"uuid": self.record["nodes"][name]["uuid"]}
        ndata = get_node_data(query, {})
        # properties
        for name, p in data.items():
            ndata["properties"][name]["value"] = p
        # results
        ntdata = get_nt_full_data({"uuid": self.uuid})
        # print("ndata: ", ndata)
        ntdata["nodes"][ndata["name"]] = ndata
        # pprint(ntdata)
        self.save(ntdata)

    @property
    def dbdata_nodes(self):
        """Fetch node data from database
        1) node belongs to this nodetree
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
            node = DBNode(dbdata)
            node.update_db_keys({"action": "CANCEL"})
        self.action = "NONE"

    @property
    def daemon_name(self):
        return self.dbdata.get("daemon_name")

    def copy(self, name, node_groups=None, is_child=False, scatter_node=None):
        """Copy a nodetree and insert it into the database.

        Args:
            name (str): name of the new nodetree
            node_groups (list): names of the nodes that
                used to build this nodetree.

        Returns:
            DBNodeTree: an instance of DBNodeTree class
        """
        import uuid
        import pickle

        record = self.db.find_one({"uuid": self.uuid}, {"_id": 0})
        # change name and uuid
        record["name"] = name
        record["uuid"] = str(uuid.uuid1())
        record["state"] = "CREATED"
        record["action"] = "NONE"
        # scatter subnodetree
        if is_child:
            record["meta"]["parent"] = self.uuid
            record["meta"]["scatter_node"] = scatter_node
            is_scattered_node = True
        else:
            is_scattered_node = False
        #
        record_nodes = record["nodes"]
        record["nodes"] = {}
        self.insert_one(record)
        nodetree = self.__class__(uuid=record["uuid"])
        # copy all nodes
        # remove all nodes include other nodes not in node_groups
        node_datas = {}
        nodes = {}
        if node_groups is None:
            node_groups = record_nodes.keys()
        for name in node_groups:
            ndata = record_nodes[name]
            node = DBNode(uuid=ndata["uuid"])
            node = node.copy(
                name=ndata["name"],
                nodetree_uuid=record["uuid"],
                is_scattered_node=is_scattered_node,
            )
            nodes[name] = node
            ndata["uuid"] = node.uuid
            node_datas[name] = ndata
        # remove all link include other nodes not in node_groups
        links = []
        for link in record["links"]:
            if link["from_node"] in node_groups and link["to_node"] in node_groups:
                links.append(link)
        record["links"] = links
        nodetree.update_db_keys({"nodes": node_datas, "links": links})
        # print(nodes)
        # update links inside node
        for name, node in nodes.items():
            dbdata = node.dbdata
            inputs = dbdata["inputs"]
            outputs = dbdata["outputs"]
            node.update_db_keys({"inputs": inputs, "outputs": outputs})
        # update connectivity
        from scinode.utils.nt_analysis import ConnectivityAnalysis

        nc = ConnectivityAnalysis(nodetree.dbdata)
        connectivity = nc.build_connectivity()
        nodetree.update_db_keys({"connectivity": connectivity})
        # update record
        nodetree.record = nodetree.dbdata
        return nodetree

    @property
    def nodes(self):
        return self.get_nodes()

    def get_nodes(self):
        dbdata_nodes = self.dbdata_nodes
        nodes = {}
        for name, dbdata in dbdata_nodes.items():
            node = DBNode(uuid=dbdata["uuid"])  # , self.daemon_name)
            nodes[node.name] = node
        return nodes

    @skip_ref_node
    def pause_node(self, name):
        """Pause node.

        Args:
            name (str): name of the node to be paused
        """
        uuid = self.record["nodes"][name]["uuid"]
        logger.debug("pause node, name={}, uuid={}".format(name, uuid))
        newvalues = {"$set": {"state": "PAUSED", "action": "NONE"}}
        db_node.update_one({"uuid": uuid}, newvalues)

    @skip_ref_node
    def play_node(self, name):
        """Play node.

        Args:
            name (str): name of the node to be played
        """
        uuid = self.record["nodes"][name]["uuid"]
        logger.debug("play node, name={}, uuid={}".format(name, uuid))
        newvalues = {"$set": {"state": "READY", "action": "LAUNCH"}}
        db_node.update_one({"uuid": uuid}, newvalues)

    @skip_ref_node
    def skip_node(self, name):
        """Skip node.

        Args:
            name (str): name of the node to be skipd
        """
        logger.debug("skip node, name: {}".format(name))
        child_nodes = self.record["connectivity"]["children"][name][0]
        for name in child_nodes:
            logger.debug("skip child node, name: {}".format(name))
            uuid = self.record["nodes"][name]["uuid"]
            newvalues = {"$set": {"state": "SKIPPED", "action": "NONE"}}
            db_node.update_one({"uuid": uuid}, newvalues)

    @skip_ref_node
    def reset_node(self, name, launch=False):
        """Reset node and all its child nodes.

        Args:
            name (str): name of the node to be paused
        """
        nodes_to_reset = [name]
        child_nodes = self.record["connectivity"]["children"][name][0]
        nodes_to_reset.extend(child_nodes)
        logger.debug("reset node, name: {}".format(name))
        for name in nodes_to_reset:
            node = DBNode(uuid=self.record["nodes"][name]["uuid"])
            node.reset(launch=launch)

    @skip_ref_node
    def cancel_node(self, name):
        """Cancel node."""
        uuid = self.record["nodes"][name]["uuid"]
        logger.debug("cancel node, name={}, uuid={}".format(name, uuid))
        newvalues = {"$set": {"action": "CANCEL"}}
        db_node.update_one({"uuid": uuid}, newvalues)

    def reset(self):
        """Reset nodetree and all its nodes.

        Args:
            name (str): name of the node to be paused
        """
        dbdata_nodes = self.dbdata_nodes
        logger.debug("Reset nodetree: {}".format(self.name))
        for name, node in dbdata_nodes.items():
            node = DBNode(uuid=self.record["nodes"][name]["uuid"])
            node.reset()
        self.state = "CREATE"
        self.action = "NONE"

    def write_log(self, log, daemon=False, database=True):
        if daemon:
            print(log)
        if database:
            old_log = self.db.find_one({"uuid": self.uuid}, {"_id": 0, "log": 1})["log"]
            log = old_log + log
            self.update_db_keys({"log": log})
