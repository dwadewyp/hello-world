import uuid


f = open("random.txt","wb")

for i in range(200):
    f.write(str(uuid.uuid1()) + "\n")


f.close()






