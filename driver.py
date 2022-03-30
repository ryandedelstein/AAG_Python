import Alice
import Bob
import Eve
import exchange


ex = exchange.PublicInformation(21, [[1,5,20,2,8,13,3,6,12,10,14,7,16,15,17,11,19,0,9,18,4], [1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]])
alice = Alice.Alice(ex)
bob = Bob.Bob(ex)
eve = Eve.Eve(ex)

alice.set_private()
bob.set_private()

alice.transmit()
bob.transmit()

alice.compute_shared_key()
bob.compute_shared_key()
print("Eve found the key:")
print(eve.crack_code())