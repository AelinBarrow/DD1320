#DD1320

#Lab02

from array import array

class ArrayQ:
    def __init__(self, item='i'):
        self._array=array(item)

    def enqueue(self,x):
        return self._array.append(x)
    
    def dequeue(self):
        return self._array.pop(0)

    def size(self):
        return len(self._array)


    def isEmpty(self):
        return len(self._array)==0
        
       

if __name__=="__main__":
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")
