import pymongo
from scinode.config.scinode_config import db_config_datas

scinode_client = pymongo.MongoClient(db_config_datas["db_address"])
scinodedb = scinode_client[db_config_datas["db_name"]]
db_nodetree = scinodedb["nodetree"]
db_node = scinodedb["node"]
