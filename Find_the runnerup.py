if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list1=set(list(arr))  #Removes duplicates from the lisr arr
    list2=list(list1)     #Converting set back to the list so that it could be sorted
    list2.sort()
    print(list[-2])
