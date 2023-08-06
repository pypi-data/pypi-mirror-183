from scinode.core.executor import Executor


class ScinodeScatter(Executor):
    """Scatter nodes executor"""

    def run(self):
        """
        0) Find all subtrees created by this node, and delete them
        1) Find all children nodes after the scatter node
        2) Create a new nodetree nt1
        3) build all children node inside new nodetree nt1
        4) use REF node
        5) launch the nodetree
        """
        print("Run for scatter ".format(self.name))
        self.prepare()
        self.new_nodetree()
        self.set_gather_state()

    def prepare(self):
        from scinode.core.db_nodetree import DBNodeTree

        self.delete_sub_nodetree()
        self.nloop = len(self.kwargs["Input"])
        print("  Total Loops: ".format(self.nloop))
        # nodetree data
        self.nt = DBNodeTree(uuid=self.dbdata["meta"]["nodetree_uuid"])
        self.scattered_nodes = set(
            self.nt.record["connectivity"]["children"][self.name][1]
        )
        self.missing_nodes = self.find_missing_nodes(self.scattered_nodes)
        self.copy_nodes = self.scattered_nodes.union(self.missing_nodes)

    def delete_sub_nodetree(self):
        """Delete nodetrees which are scattered from this node."""
        from scinode.database.nodetree import NodetreeClient

        # Find all subtrees created by this node, and delete them
        client = NodetreeClient()
        query = {"scatter_node": self.uuid}
        client.delete(query)

    def find_missing_nodes(self, scattered_nodes):
        """Find the missing input nodes"""
        missing_nodes = []
        input_nodes = []
        for node in scattered_nodes:
            inputs = self.nt.record["connectivity"]["inputs"][node]
            for socket, input in inputs.items():
                input_nodes.extend(input)
        missing_nodes = set(input_nodes) - set(scattered_nodes)
        print("missing_nodes: ", missing_nodes)
        return missing_nodes

    def create_ref_nodes(self, nt, index):
        """Create ref nodes for the missing nodes.
        Check the missing input nodes
        1) if the input node is scatter node, set the input sockets for the nodes connect to the "scatter" node
        2) if the input node is not scatter node, make a ref node.
        """
        import pickle

        nodes = nt.dbdata["nodes"]
        for name, node in nt.nodes.items():
            print(f"Node {name}")
            if name in self.missing_nodes:
                if name == self.name:
                    print(
                        "    set the input socket for the nodes connect to the scatter node"
                    )
                    results = (
                        {"name": "Result", "value": self.kwargs["Input"][index]},
                    )
                    node.update_db_keys({"results": pickle.dumps(results)})
                    print(f"Node {name} is a COPY node.")
                    node.update_db_keys(
                        {
                            "meta.node_type": "COPY",
                            "state": "FINISHED",
                            "action": "NONE",
                        }
                    )
                    nodes[name]["node_type"] = "COPY"
                else:
                    print(
                        "Node {} is a REF node. ref_uuid: {}".format(
                            name, self.nt.record["nodes"][name]["uuid"]
                        )
                    )
                    node.update_db_keys(
                        {
                            "meta.node_type": "REF",
                            "state": "FINISHED",
                            "action": "NONE",
                            "meta.ref_uuid": self.nt.record["nodes"][name]["uuid"],
                        }
                    )
                    nodes[name]["node_type"] = "REF"
            # add label for all children nodes
            node.update_db_keys({"meta.scattered_label": str(index)})
        return nodes

    def new_nodetree(self):
        """Copy nodes to new nodetree"""
        for i in range(self.nloop):
            # add new nodetree
            name = "{}_{}".format(self.nt.name, i)
            print(
                "    Add nodetree: {}, has {} nodes. There {} REF nodes.".format(
                    name, len(self.copy_nodes), len(self.missing_nodes)
                )
            )
            nt = self.nt.copy(
                name,
                self.copy_nodes,
                is_child=True,
                scatter_node=self.uuid,
            )
            nodes = self.create_ref_nodes(nt, i)
            print("nodes: ", nodes)
            nt.update_db_keys({"nodes": nodes})
            #
            nt.launch()

    def set_gather_state(self):
        from scinode.database.client import db_node

        # all the children nodes should not run, instead the action should be gather.
        for name in self.scattered_nodes:
            print("    Set Node {} action to gather.".format(name))
            query = {
                "meta.nodetree_uuid": self.dbdata["meta"]["nodetree_uuid"],
                "name": name,
            }
            newvalues = {"$set": {"state": "SCATTERED", "action": "GATHER"}}
            db_node.update_one(query, newvalues)
        return (None,)
