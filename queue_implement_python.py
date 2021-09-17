# Queue Implementation using Python
# Push/Post multiple or 100 of items in a list(deque) at a time also remove/ delete multiple or 
# 100 of items from a list
# Also, Check the order in which an item/ json are entered in the list.


# from collections import deque
# import time

# dq_List = deque()
# print(dq_List)

# def push_queue(lis):
#     x = 'I am Nimish Pathak!'
#     y = 'Looking for a job oppertunity in Python Development.'
    
#     for i in range(100):
#         lis.append(x)
#         lis.append(y)
#     print(lis)    
#     x, y = lis[0], lis[1]
#     return x, y
# print(push_queue(dq_List))

# x, y = dq_List[0], dq_List[1]
# print()

# def pop_queue(lis1):
#     for i in range(len(lis1) ):
#         if x == lis1[0]: 
#             lis1.popleft()
#         elif y == lis1[1]:
#             lis1.popleft()
#         else:
#             return 'The Order of the string is not sequential!'
#     print('The queue strings are in Sequential order!')
#     return (lis1)
# t1 = time.time()
# print(pop_queue(dq_List))
# t2 = time.time()
# print()
# print(t2 - t1)



from collections import deque

dq_List = deque()
print(dq_List)

str1 = 'Nimish Pathak'
str2 = 'Looking for a job Oppertunity in Python Development!'

def push_Queue(list1):
    
    for i in range(100):
        list1.append(str1)
        list1.append(str2)
    print(list1)
    
    x, y = list1[0], list1[1]
    print()
    return x, y

print(push_Queue(dq_List))

x, y = dq_List[0], dq_List[1]

def pop_Queue(lis_):
    dict1 = {}
#     lis2 = []
#     lis3 = []
    for string in lis_:
        if x == string and string not in dict1:
            dict1[string] = 1
            
        elif y == string and string not in dict1:
            dict1[string] = 1
        else: #   string in dict1:
            dict1[string] += 1 
            
#     print()
    print(dict1)
    
    for key in dict1:
        for i in range(dict1[key]):
            lis_.popleft()
            
    return lis_
print(pop_Queue(dq_List))

        
        