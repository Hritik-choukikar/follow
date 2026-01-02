from neo4j import GraphDatabase
from config import setting

driver = GraphDatabase.driver(
    setting.NEO4J_URI,
    auth=(setting.NEO4J_AUTH, setting.NEO4J_PASSWORD)
)

def get_driver():
    return driver

driver=get_driver()
