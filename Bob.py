import random
import exchange
class Bob:
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
        print("Bob's private key:")
        print(ret)
    
    def transmit(self):
        ret = []
        b = self.private
        b_inv = self.exchange.inverse(b)
        generator = self.exchange.get_generator()
        for i in generator:
            ret.append(self.exchange.operator(b_inv, self.exchange.operator(i, b)))
        self.exchange.transmit_Bob(ret)
        print("Bob transmitted:")
        print(ret)

    def compute_shared_key(self):
        b = self.private
        b_inv = self.exchange.inverse(b)
        shared_key = self.exchange.get_identity()
        alice_transmits = self.exchange.get_Alice()
        for i in self.private_word:
            if i[1] % 2 == 0:
                shared_key = self.exchange.operator(alice_transmits[i[0]], shared_key)
            else:
                shared_key = self.exchange.operator(self.exchange.inverse(alice_transmits[i[0]]), shared_key)
        
        shared_key = self.exchange.inverse(shared_key)
        shared_key = self.exchange.operator(shared_key, b)
        self.shared_key = shared_key
        print("Bob computed shared key:")
        print(shared_key)
