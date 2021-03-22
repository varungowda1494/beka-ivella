import random

class cresource:
    def __init__(self, id, name="name"):
        self.__id = id
        self.name = "name"
    def getResourceID(self):
        print (self.__id)

#vid = cresource(24)
#print(vid.getResourceID())

def flush_batch():
	open('takenf.txt', 'w').close()

def assignID(option="res"):
	taken = [line.strip() for line in open("takenf.txt", 'r')]
	tryid = str(random.randint(1,1000))

	while(tryid in list(taken)):
		tryid = str(random.randint(1,1000))
	
	taken.append(tryid)
	print("Assigned RID:",tryid)
	takenf= open("takenf.txt",'w')  #later, make persistent
	for ele in taken:
		takenf.write(str(ele) + "\n")

	takenf.close()


assignID()
#print("Yakkow, please give 7")
