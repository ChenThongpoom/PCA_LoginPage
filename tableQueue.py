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

    def firstQueue(self):
        if len(self.queue) == 0:
            print('There is no one who is waiting for the table')
            return
        else:
            print(self.queue[0])
            return self.queue[0]

    def lastQueue(self):
        if len(self.queue) == 0:
            print('There is no one who is waiting for the table')
            return
        else:
            print(self.queue[-1])
            return self.queue[-1]

    def __queueSize__(self):
        if len(self.queue) == 0:
            print('The queue is empty')
        elif len(self.queue) == 1:
            print('The queue has one person waiting to use the table')
        elif len(self.queue) > 1:  
            print('The queue has',len(self.queue),'people waiting to use the table') 
        return

    def enqueue(self,name):
        self.queue.append(str(name))
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
    def __init__(self,tableSeat):
        self.table = []
        self.tableSeat = tableSeat
        for i in range(self.tableSeat):
            self.table.append(' ')

    def newUser(self,name):
        for i in range(len(self.table)):
            if self.table[i] == ' ':
                self.table.insert(i,str(name))
                return self.table
        print("No table is vacant for ",name," . This user will be put in a queue")
        return name
    
    def userEnd(self,name):
        for i in range(len(self.table)):
            if self.table[i] == str(name) :
                print(name," has end the table usage")
                self.table.insert(i,' ')
                return self.table
        print(name,' is not found within the table system')
        return
    
    def addTable(self):
        added = int(input('How many table will be installed into the system :'))
        for i in range(added):
            self.table.append(' ')
        return self.table

    def delTable(self):
        delete = int(input('How many table will be removed from the system :'))
        self.table = self.table[ : len(self.table) - delete ]
        return self.table

    def print(self):
        print(self.table)
        return

            


def mainQueue():
    a = input('Choose what command you want to execute ( Enqueue, Dequeue, Print, Clear, Queue Size, Check First, Check Last, Check People ) :')
    if 'Enqueue' in a or 'enqueue' in a:
        name = str(input('Input the user who is waiting to use the table :'))
        queue.enqueue(name)
        print(name, 'has successfully been enqueued.')
    elif 'Dequeue' in a or 'dequeue' in a:
        name = self.queue[-1]
        queue.dequeue()
        print(name, 'has successfully been dequeued.')    
    elif 'Print' in a or 'print' in a:
        queue.print()
    elif 'Clear' in a or 'clear' in a:
        queue.clear()
        print('Queue has been cleared successfully.')
    elif 'Queue Size' in a or 'queue size' in a:
        queue.__queueSize__()
    elif 'Check First' in a or 'first' in a or 'First' in a or 'Check first' in a:
        queue.firstQueue()
    elif 'Check Last' in a or 'Last' in a or 'last' in a or 'Check last' in a:
        queue.lastQueue()
    elif 'Check People' in a or 'people' in a or 'People' in a or 'Check people' in a:
        queue.inQueue()
    elif a == 'end' :
        print('Command completed.')
        return
    else:
        print("Invalid Command input, please try again.")
    print(' ')
    main()
    return queue

def mainTable():
    a = input('Choose what command you want to execute ( New , End , Add , Del ) : ' )
    if a in ['New','new']:
        user = str(input('What is the user which will be using the table : '))
        seat.newUser(user)
    elif a in ['End','end']:
        user = str(input('What is the user which will be leaving the table : '))
        seat.userEnd(user)
    elif a in ['Add','add']:
        seat.addTable()
    elif a in ['Del','del']:
        seat.delTable()
    seat.print()
    mainTable()
    return table
    
              


seat = Seating(4)
mainTable()
    
            
    