import random

#this algorithm works by selecting the second digit of my list and comparing the previous element, and swapping if necessary 
#this call, insertion sort

def insertion_sort(mylist):
    
    for index in range(1, len(mylist)):
        while index>0 and mylist[index-1] > mylist[index]:
            mylist[index], mylist[index-1] = mylist[index-1], mylist[index] 

    return mylist


def run():
    mylist = [random.randint(1, 100) for i in range(100)]
    print(mylist)

    sort_list = insertion_sort(mylist)
    print(sort_list)

if __name__ == '__main__':
    run()