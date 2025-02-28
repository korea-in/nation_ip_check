import random

f = open("./data.txt", "w")

for i in range(1000000):
    octet1 = random.randint(1, 254)
    octet2 = random.randint(1, 254)
    octet3 = random.randint(1, 254)
    octet4 = random.randint(1, 254)
    
    f.write("%d.%d.%d.%d\n" % (octet1, octet2, octet3, octet4))