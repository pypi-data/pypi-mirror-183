from scinode.daemon.base_daemon import BaseDaemon
from scinode.engine import EngineNodeTree, EngineNode
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from scinode.utils.db import update_one
import os
from pathlib import Path
import datetime

home = Path.home()


class ScinodeDaemon(BaseDaemon):
    """Daemon that fetch nodetree from database and call the
    engine to execute it.

    name: str
        Name of the daemon.
    pool: float
        Pool type: ThreadPoolExecutor or ProcessPoolExecutor
    worker: int
        Number of worker. Default 100 for ThreadPoolExecutor.
        4 for ProcessPoolExecutor.
    sleep: float
        Time interval to fetch data. Default 1.0

    """

    def __init__(self, name, pool="thread", worker=0, sleep=None):
        self.name = name
        self.sleep = sleep if sleep is not None else self.data["sleep"]
        if pool.upper() == "THREAD":
            # print("Use ThreadPoolExecutor.")
            self.Pool = ThreadPoolExecutor
            self.worker = worker if worker != 0 else 100
        else:
            # print("Use ProcessPoolExecutor.")
            self.Pool = ProcessPoolExecutor
            self.worker = worker if worker != 0 else 4
        logfile = os.path.join(home, ".scinode/daemon-{}.log".format(name))
        super().__init__(logfile)

    def run(self):
        """Call engine to submit the job and collect the returned futures."""
        import time
        from scinode.database.client import scinodedb

        self.db = scinodedb
        self.update_data()
        # check the old process
        self.clean_old_process()
        self.futures = {}
        with self.Pool(max_workers=self.worker) as pool:
            step = 0
            while True:
                print("{} {}".format(self.name, step))
                update_one(
                    {"name": self.name, "lastUpdate": datetime.datetime.utcnow()},
                    self.db["daemon"],
                    key="name",
                )
                # --------------------------------------------------
                self.process_nodetree()
                # ----------------------------------------------------------
                self.process_node(pool)
                # f.close()
                step += 1
                time.sleep(self.sleep)

    def process_nodetree(self):
        """Process nodetree"""
        query = {
            "action": {"$nin": ["NONE", "NEED_HELP"]},
            "state": {"$nin": ["FINISHED", "FAILED", "CANCELLED"]},
        }
        query["meta.daemon_name"] = self.name
        db_nodetrees = self.db["nodetree"].find(query, {"name": 1, "uuid": 1})
        for dbdata in db_nodetrees:
            # f.write("Handle node: {}".format(db['uuid']))
            # print("-" * 60)
            print("\nNodetree: {}".format(dbdata["name"]))
            nodetree = EngineNodeTree(uuid=dbdata["uuid"])
            nodetree.process()
            del nodetree
        del db_nodetrees

    def process_node(self, pool):
        """Process node"""
        # the entrance point is nodetree
        # if a nodetree is paused, all the child nodes will not be look at.
        query = {"action": {"$nin": ["NEED_HELP"]}}
        db_nodetrees = list(
            self.db["nodetree"].find(query, {"_id": 0, "name": 1, "uuid": 1})
        )
        nodetrees = {nt["uuid"]: nt for nt in db_nodetrees}
        # print("db_nodetrees: ", db_nodetrees)
        # query nodes
        query = {
            "action": {"$in": ["LAUNCH", "GATHER", "CANCEL"]},
            "state": {"$in": ["READY", "RUNNING"]},
        }
        query["meta.daemon_name"] = self.name
        dbdatas_nodes = list(
            self.db["node"].find(
                query,
                {"name": 1, "uuid": 1, "meta.nodetree_uuid": 1, "meta.node_type": 1},
            )
        )
        # print("dbdatas_nodes: ", dbdatas_nodes)
        for ndata in dbdatas_nodes:
            # the entrance point is nodetree
            # if a nodetree is paused, all the child nodes will not be look at.
            if ndata["meta"]["nodetree_uuid"] not in nodetrees or ndata["meta"][
                "node_type"
            ] in ["REF", "COPY"]:
                continue
            # print("-" * 60)
            # print("\nRunning node: {}".format(ndata["name"]))
            node = EngineNode(dbdata=ndata, daemon_name=self.name)
            future = node.process(pool, self.futures.get(ndata["uuid"]))
            self.futures[ndata["uuid"]] = future
            del node
        del dbdatas_nodes

    def clean_old_process(self):
        """Clean old process.

        When daemon is interupted, the old process is persist in a fake `running` state.
        """
        from scinode.core.db_node import DBNode

        # query nodes
        query = {
            "action": {"$in": ["NONE", "GATHER"]},
            "state": {"$in": ["RUNNING"]},
        }
        query["meta.daemon_name"] = self.name
        dbdatas_nodes = list(
            self.db["node"].find(
                query,
                {"name": 1, "uuid": 1, "meta.nodetree_uuid": 1, "meta.node_type": 1},
            )
        )
        print("Reset: ")
        for ndata in dbdatas_nodes:
            print("Node: {}, uuid: {}".format(ndata["name"], ndata["uuid"]))
            node = DBNode(uuid=ndata["uuid"])  # , self.daemon_name)
            node.reset()
            node.action = "LAUNCH"

    def showlog(self, limit=100):
        with open(self.logfile) as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())

    def update_data(self):
        """Update data in the database.
        - pid
        - worker
        - sleep
        """
        pid = os.getpid()
        data = {
            "name": self.name,
            "pid": pid,
            "worker": self.worker,
            "sleep": self.sleep,
            "lastUpdate": datetime.datetime.utcnow(),
        }
        # print("udpate: ", data)
        update_one(data, self.db["daemon"], key="name")
        # print("Write pid to database")

    def validate_name(self, name):
        from scinode.database.client import scinodedb

        data = scinodedb["daemon"].find_one({"name": name})
        if data is not None:
            return True
        else:
            print("Daemon {} is not setup.".format(name))
            return False

    @property
    def data(self):
        from scinode.database.client import scinodedb

        data = scinodedb["daemon"].find_one({"name": self.name})
        return data

    @property
    def lastUpdate(self):
        return self.get_lastUpdate()

    def get_lastUpdate(self):
        dt = (datetime.datetime.utcnow() - self.data["lastUpdate"]).total_seconds()
        return dt

    def get_pid(self):
        data = self.data
        pid = data.get("pid", 0)
        worker = data.get("worker", 0)
        # print("name: {}, pid: {}".format(self.name, pid))
        return pid


if __name__ == "__main__":
    daemon = ScinodeDaemon("localhost")
    daemon.start(daemonize=False)
