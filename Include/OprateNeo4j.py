# coding:utf-8
from py2neo import Graph, Node, Relationship

# 对数据库进行处理
class Operate():
    def __init__(self, uri, username, password):
        self.graph = Graph(uri, username=username, password=password)

    def clear_all_data(self):
        self.graph.delete_all()

    def add_new_node(self, nodetype, nodename):
        node = Node(nodetype, name=nodename)
        self.graph.create(node)

    def add_new_relationship(self, basenode, relationtype, linknode):
        relationship = Relationship(basenode, relationtype, linknode)
        self.graph.create(relationship)