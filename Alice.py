import random
import exchange
class Alice:
    def __init__(self, exchange):
        self.exchange = exchange
    
    def set_private(self):
        self.private_word = []
        number = random.randrange(1, 100)
        ret = self.exchange.get_identity()
        generator = self.exchange.get_generator()
        for i in range(number):
            curr = random.randrange(1,4)
            index = random.randrange(self.exchange.get_size())
            self.private_word.append((index, curr))
            if curr % 2 == 0:
                ret = self.exchange.operator(generator[index], ret)
            else:
                ret = self.exchange.operator(self.exchange.inverse(generator[index]), ret)
        self.private = ret
        print("Alice's private key:")
        print(ret)
    
    def transmit(self):
        ret = []
        a = self.private
        a_inv = self.exchange.inverse(a)
        generator = self.exchange.get_generator()
        for i in generator:
            ret.append(self.exchange.operator(a_inv, self.exchange.operator(i, a)))
        self.exchange.transmit_Alice(ret)
        print("Alice transmitted:")
        print(ret)

    def compute_shared_key(self):
        a = self.private
        a_inv = self.exchange.inverse(a)
        shared_key = self.exchange.get_identity()
        bob_transmits = self.exchange.get_Bob()
        for i in self.private_word:
            if i[1] % 2 == 0:
                shared_key = self.exchange.operator(bob_transmits[i[0]], shared_key)
            else:
                shared_key = self.exchange.operator(self.exchange.inverse(bob_transmits[i[0]]), shared_key)
        
        shared_key = self.exchange.operator(a_inv, shared_key)
        self.shared_key = shared_key
        print("Alice computed shared key:")
        print(shared_key)
