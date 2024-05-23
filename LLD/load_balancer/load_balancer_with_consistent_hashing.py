import lib2to3.pgen2.tokenize
import random


class AppServer:

    def __init__(self, name, weight):
        self.id = name
        self.replicas = weight
        self.request_processed = 0

    def process_request(self, request_id):
        print(f"Appserver: {self.id} is processing request with id: {request_id}")
        self.request_processed += 1


class LoadBalancer:

    def __init__(self):
        self.nodes = []
        self.cycle = [0] * 360
        self.node_map = {}

    def get_weights(self):
        res = 0
        for each in self.nodes:
            res += each.replicas

        return res

    def add_node(self, node):
        self.nodes.append(node)
        self.rehash_nodes()

    def rehash_nodes(self):
        self.node_map = {}
        weight_strength = 360 // self.get_weights()
        prev = 0
        for node in self.nodes:
            self.node_map[node] = (prev, prev + (node.replicas * weight_strength))
            prev = prev + (node.replicas * weight_strength)

    def remove_node(self, node):
        self.nodes.remove(node)
        self.rehash_nodes()

    def get_node(self):
        pass

    def distribute_request(self, no):
        for i in range(1, no + 1):
            self.process_request()

    def process_request(self):
        hash_id = random.randint(10000, 99999)
        weight_no = hash_id % 360
        for node in self.node_map:
            if self.node_map.get(node)[1] >= weight_no > self.node_map.get(node)[0]:
                node.process_request(hash_id)


l1 = LoadBalancer()
l1.add_node(AppServer(1, 1))
l1.add_node(AppServer(2, 2))
l1.add_node(AppServer(3, 3))
l1.process_request()
l1.distribute_request(100)
for each in l1.nodes:
    print(each.request_processed)

# improvement make it thread safe
# implement a queue kind of system for request
# update rehashing algorithm
