from django.test import TestCase
from concept_map.models import Node, Connection

class NodeModelTests(TestCase):
    def test_node_str(self):
        node = Node(name="Test Node")
        self.assertEqual(str(node), node.name)

class ConnectionModelTests(TestCase):
    def test_connection_str(self):
        from_node = Node(name="From Node")
        to_node = Node(name="To Node")
        connection = Connection(from_node=from_node, to_node=to_node)
        self.assertEqual(str(connection), f"{from_node} -> {to_node}")
