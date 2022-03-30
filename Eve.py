from copy import copy, deepcopy
from hashlib import new
import queue


class Eve:
    def __init__(self, exchange):
        self.exchange = exchange

    def crack_code(self):
        generator = self.exchange.get_generator()
        alice = self.exchange.get_Alice()
        bob = self.exchange.get_Bob()

        alice_key = self.solve_scp(generator, alice)
        bob_key = self.solve_scp(generator, bob)

        alice_key_inv = self.exchange.inverse(alice_key)
        bob_key_inv = self.exchange.inverse(bob_key)
        return self.exchange.operator(alice_key_inv, self.exchange.operator(bob_key_inv, self.exchange.operator(alice_key, bob_key)))

    def solve_scp(self, x, y):
        n = len(x[0])

        #get x label
        minimumx = self.get_code(x)
        conj_x = self.exchange.get_identity()
        for i in range(n):
            curr = self.relabel(x, i)
            curr_code = self.get_code(curr[0])
            if curr_code.compare(minimumx):
                minimumx = curr_code
                conj_x = curr[1]
        
        #get y label
        minimumy = self.get_code(y)
        conj_y = self.exchange.get_identity()
        for i in range(n):
            curr = self.relabel(y, i)
            curr_code = self.get_code(curr[0])
            if curr_code.compare(minimumy):
                minimumy = curr_code
                conj_y = curr[1]
        

        return self.exchange.operator(conj_x, self.exchange.inverse(conj_y))


            
        
    def relabel(self, graph, v):
        n = self.exchange.get_n()
        d = self.exchange.get_size()
        ret = self.exchange.get_identity()
        ret[v] = 0
        visited = [v]
        q = queue.Queue()
        q.put(v)
        while len(visited) < n:
            curr = q.get()
            for i in range(d):
                if graph[i][curr] not in visited:
                    visited.append(graph[i][curr])
                    ret[graph[i][curr]] = len(visited) - 1
                    q.put(graph[i][curr])
        
        
        ret_inv = self.exchange.inverse(ret)
        new_graph = []
        for i in graph:
            new_graph.append(self.exchange.operator(ret, self.exchange.operator(i, ret_inv)))

        return (new_graph, ret_inv)

    
    def get_code(self, graph):
        code = Code()
        for i in graph:
            for j in i:
                code.add_char(j)
        
        return code



class Code:
    def __init__(self):
        self.array = []
    
    def add_char(self, c):
        self.array.append(c)
    
    def compare(self, other_code):
        for i in range(len(self.array)):
            if self.array[i] < other_code.array[i]:
                return True
            elif self.array[i] > other_code.array[i]:
                return False
        
        return False
