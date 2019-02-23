import random
# Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)


def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')


# List Functions
class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None



def IsEmpty(L):
    return L.head == None


def Append(L, x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next


def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line


def Bubble_Sort(L,l,c):
    if IsEmpty(L) or L.head.next == None:
        return
    for x in range(l):
        current = L.head
        c_next = L.head.next
        while c_next != None:
            c+=1
            if current.item > c_next.item:
                temp = current.item
                current.item = c_next.item
                c_next.item = temp
            current = c_next
            c_next = c_next.next
    Print(L)
    return c


def Merge_Sort(L):
    if L == None or L.next == None:
        return L
    middle = Get_Middle(L)
    next_middle = middle.next
    middle.next = None
    left = Merge_Sort(L)
    right = Merge_Sort(next_middle)
    sorted_list = Sorted_Merge(left,right)
    return sorted_list


def Sorted_Merge(left,right):
    result = None
    if left == None:
        return right
    if right == None:
        return left
    if left.item <= right.item:
        result = left
        result.next = Sorted_Merge(left.next,right)
    else:
        result = right
        result.next = Sorted_Merge(left,right.next)
    return result


def Get_Middle(L):
    fast = L.next
    slow = L
    while fast != None:
        fast = fast.next
        if fast != None:
            slow = slow.next
            fast = fast.next
    return slow


def Quick_Sort(A,low,high):
    if low < high:
        pivot = Partition(A,low,high)
        Quick_Sort(A,low,pivot-1)
        Quick_Sort(A,pivot+1,high)
    L = List()
    for x in A:
        Append(L,x)
    Print(L)
    return Get_Middle(L).item


def Partition(A,low,high):
    i = low-1
    pivot = A[high]
    for j in range(low,high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j],A[i]
    A[i+1],A[high] = A[high],A[i+1]
    return i+1




n=12

print('Bubble Sort')
counter = 0
L = List()
lenght = random.randint(0,n)
for x in range(lenght):
    Append(L, random.randint(0,100))
Print(L)
counter = Bubble_Sort(L,lenght,counter)
print('Number of comparisons Bubble:',counter)



print('Merge Sort')
counter = 0
L = List()
lenght = random.randint(0,n)
for x in range(lenght):
    Append(L, random.randint(0,100))
Print(L)
L.head = Merge_Sort(L.head)
Print(L)







print('Quick Sort')
L = List()
l= []
lenght = random.randint(0,n)
for x in range(lenght):
    l.append(random.randint(0,100))
print(l)
L = Quick_Sort(l,0,len(l)-1)
Print(L)









