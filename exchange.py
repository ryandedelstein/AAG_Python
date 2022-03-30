class PublicInformation:
    def __init__(self, n, generator):
        self.n = n
        self.X = generator
        self.size = len(self.X)
    
    def get_n(self):
        return self.n

    def get_size(self):
        return self.size

    def get_generator(self):
        return self.X
    
    def transmit_Alice(self, A):
        self.Alice = A
    
    def transmit_Bob(self, B):
        self.Bob = B

    def get_Alice(self):
        return self.Alice

    def get_Bob(self):
        return self.Bob    

    def operator(self, a, b):
        ret =[]
        for i in range(self.n):
            ret.append(a[b[i]])
        return ret
    
    def inverse(self, a):
        ret = self.get_identity()
        for i in range(self.n):
            ret[a[i]] = i
        return ret

    def get_identity(self):
        ret = []
        for i in range(self.n):
            ret.append(i)
        return ret


    def cycle_form_to_map(self, cycles):
        ret = self.get_identity()