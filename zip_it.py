list1 = [1,2,3]
list2 = ['a','b','c']
list3 = list(zip( list1, list2))
print(list3)

llist1 = [10,20,30,40,50]
llist2 = [100,200,300,400,500]
for x, y in zip(llist1, llist2[::-1]):
    print(x,y)

lllist1 = ['reliance', 'thing', 'staticme']
lllist2 = [1234, 23446, 75484]
newdict = {lllist1: lllist2 for lllist1,
           lllist2 in zip(llist1, lllist2)}
print('\n{}'.format(newdict))