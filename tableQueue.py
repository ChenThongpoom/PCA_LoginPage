

class Queue :
    def __init__(self):
        self.queue = []
        
    def inQueue(self):

        if len(self.queue) == 0 :
            print('There are no person waiting to use the table.')
        elif len(self.queue) == 1 :
            print(self.queue[0],' is waiting to use the table.')
        else:
            print(self.queue,' are waiting to use the table.')         

    def __queueSize__(self):
        
        if len(self.queue) == 0:
            print('The queue is empty --> ', self.queue)
            print('------------------------')
            return self.queue

        elif len(self.queue) == 1:
            print('The queue has one person waiting to use the table --> ', self.queue)
            print('------------------------')
            return self.queue

        elif len(self.queue) > 1:  
            print('The queue has',len(self.queue),'people waiting to use the table --> ', self.queue) 
            print('------------------------')
            return self.queue
        

    def enqueue(self,name):
        print("No table is vacant for ",name," --> This user will be put in a queue")
        self.queue.append(name)
        return self.queue

    def dequeue(self):
        if len(self.queue) == 0:
            print('There is no one who is waiting for the table')
            return
        else:
            user = self.queue[0]
            self.queue = self.queue[1:]
            return user

    def clear(self):
        self.queue = []
        return self.queue


    def print(self):
        print("F ",self.queue," R")


class Seating : 
    def __init__(self):
        self.table = []
        self.tableAvail = []
        self.que = Queue()

    def addUser(self,name):
        for i in range(len(self.tableAvail)):
            if self.tableAvail[i] == None:
                self.tableAvail[i] = name
                return self.tableAvail
        if None not in self.tableAvail:
            self.que.enqueue(name)
            print('----------------------')
            self.que.__queueSize__()
        return self.tableAvail
    
    def userDel(self,name):
        for i in range(len(self.tableAvail)):
            if self.tableAvail[i] == str(name) :
                print(name," has end the table usage")
                self.tableAvail[i] = self.que.dequeue()
                return self.tableAvail
                
            
        return print(name,' is not found within the table system')
    
    def addTable(self):
        added = int(input('How many table will be installed into the system :'))
        for i in range(added):
            self.tableAvail.append(None)
        return self.tableAvail

    def delTable(self):
        delete = int(input('How many table will be removed from the system :'))
        self.table = self.table[ : len(self.table) - delete ]
        return self.table

    def print(self):
        return self.tableAvail
        

            

def mainTable():
    print('Add your Table amount')
    print(seat.addTable())
    while True:
        a = input('Choose what command you want to execute ( Add ,Del, Show ) : ' )
        if a in ['Add','add']:
            user = str(input('What is the user which will be using the table : '))
            print(seat.addUser(user))
            
        elif a in ['Del','del']:
            user = str(input('What is the user which will be leaving the table : '))
            print(seat.userDel(user))
        elif a in ['Show','show']:
            print(seat.print())
            
            
              


seat = Seating()
mainTable()
    
            
    