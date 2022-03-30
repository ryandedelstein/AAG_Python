import Alice
import Bob
import Eve
import exchange


n = int(input("Input n:"))

d = int(input("Input the number of generators:"))

ex = exchange.PublicInformation(n)

generators = []
for i in range(d):
    string = input("Input the next generator in cycle form separated by spaces. Ex. (1 3 4 2) (7 5):")
    cycles = []
    curr = []
    i = 0
    while i < len(string):
        if string[i] == "(":
            curr = []
            i = i + 1
        elif string[i] == ")":
            cycles.append(curr)
            i = i + 1
        elif string[i].isdigit():
            num = ""
            while string[i].isdigit():
                num = num + string[i]
                i = i + 1
            curr.append(int(num))
        else:
            i = i + 1
            continue
    
    generators.append(ex.cycle_form_to_map(cycles))

ex.update_generator(generators)



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
