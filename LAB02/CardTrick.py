#DD1320
#Michaela Jankulicova
#Lab02

from arrayQFile import ArrayQ


def card_trick():
    in_queue=ArrayQ() #the cards as they come
    out_queue=ArrayQ() #the cards that will show on the table

    guesser=input('Vilken ordning ligger korten i? ') 
    cards = guesser.split(' ')  #divides into different elements in the cards list
    cards=[int(i) for i in cards] #list elements turn into int
   
    for element in cards: #cards puts into ArrayQ object
        in_queue.enqueue(element)

    while in_queue.isEmpty()==False: #as long as the array has elements in it
        main=in_queue.dequeue() #takes the first element of the deck
        in_queue.enqueue(main) #appends the first element to the last place

        side = in_queue.dequeue() #takes the first element of the queue
        out_queue.enqueue(side) #puts it on the 'table'
    print(out_queue._array) #prints all the 'table' cards

card_trick()





