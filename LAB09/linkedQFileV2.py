class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class LinkedQ:
    def __init__(self, first=None, last=None):
        self._first=first
        self._last=last 

    def enqueue(self, value): #sets new item as last element
        #adding element to the queue
        tmp=Node(value) #creates an object, no matter the scenario bellow, local
      
        if self.isEmpty():#queue is empty
            #doesnt need .next because we know its empty
            self._first=tmp 
            self._last=tmp
            #first and last element are then the same
        else :#queue has elements in it, needs to connect to last element
            self._last.next=tmp #points to the new next Node
            self._last=tmp #last node
        
    def dequeue(self): #picks up the _first element in the queue
        #it needs to connect all the node objects together
        tmp=self._first.value #points to data of the Node-object
        self._first=self._first.next #points to the next Node-object
        return tmp
 
        
    def isEmpty(self):
        if self._first==None: #if there isnt any first element it means the queue is empty
            return True
        else:
            return False
    
    def peeknext(self): #looks at the next elemnent in the queue
        current = self._first
        if self._first == None:
            next_string = None
        elif current.next is not None:
            next_string = current.next.value
            return next_string
        
    def peek(self):
        if self.isEmpty()!=True:
            return self._first.value
        else:
            return False
        
    def __str__(self):
        current = self._first
        values=[]
        while current.value !='/':
            values.append(current.value)
            current=current.next
        space=''
        final=space.join(values).strip()
        return final
        
    def printq(self):
        current = self._first
        values=[]
        while current !=None :
            values.append(current.value)
            current=current.next
        space=''
        final=space.join(values).strip()
        return final
    

    
    
