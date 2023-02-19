import random

def merge_sort(mylist):
    if len(mylist) > 1:
        middle = len(mylist)//2
        left = mylist[:middle]
        ritgh = mylist[middle:]

        merge_sort(left)
        merge_sort(ritgh)


        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(ritgh):
            if left[i] < ritgh[j]:
                mylist[k] = left[i]
                i+=1
            else:
                mylist[k] = ritgh[j]
                j += 1
            k += 1

        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1
        while j < len(ritgh):
            mylist[k] = ritgh[j]
            j += 1
            k += 1
        
        return mylist
        
        


def run():
    mylist = [random.randint(1, 100) for i in range(10)]
    print(f"Unordered list: {mylist}")
    
    merge_sort(mylist)
    print(f"Sorted list: {mylist}")



if __name__ == '__main__':
    run()