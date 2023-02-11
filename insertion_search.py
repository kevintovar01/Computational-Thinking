import random

def insertion_search(mylist):
    
    for index in range(1, len(mylist)):
        actual_value = mylist[index]
        position_actual = index

        while position_actual>0 and mylist[position_actual-1] > actual_value:
            mylist[position_actual] = mylist[position_actual-1]
            position_actual -= 1

        mylist[position_actual] = actual_value

    return mylist


def run():
    mylist = [random.randint(1, 100) for i in range(100)]
    print(mylist)

    sort_list = insertion_search(mylist)
    print(sort_list)

if __name__ == '__main__':
    run()