from linkedQFile import LinkedQ
import sys

indata = sys.stdin.readline()

def card_trick():
    queue=LinkedQ() #the cards as they come
    
    table=[] #the table we will put the cards on

    #guesser=input('Vilken ordning ligger korten i? ') 
    cards = indata.split()  #divides into different elements in the cards list

    for element in cards: #cards puts into LinkedQ object
        queue.enqueue(element)

    while queue.isEmpty()==False: #as long as the Linked has elements in it
        main=queue.dequeue() #takes the first element of the deck   
        queue.enqueue(main) #appends the first element to the last place

        side = queue.dequeue() #takes the first element of the queue
        table.append(side) #puts it on the 'table'
    print(*table) #prints all the 'table' cards

card_trick()