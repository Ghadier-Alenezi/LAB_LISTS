## LISTS
### Q1: Write a Python program to sum all the items in a list.
lst = [1,2,3]

def sum(lst:list):
    answer = 0
    for item in lst:
        answer += item
    print("sum of the all the items in a list = ", answer)

sum(lst)
#--------------------------------------------------#
### Q2: Write a Python program to get the largest number from a list.
lst = [1,2,3]

def largestNum(lst:list):
    answer = 0
    for item in lst:
        if item > answer:
            answer = item
    print("the largest number from a list = ", answer)

largestNum(lst)
#--------------------------------------------------#
### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, 
# using list comprehension.
oddNum = [item for item in range(1200, 2000, 125) if not item % 2 == 0]
print("list of the odd numbers between 1200 & 2000 with 125 steps =", oddNum)

#--------------------------------------------------#

## TUPLES
### Q1: Create a tuple with duplicate elements and find the index of the duplicate item.
t = ("A", "B", "C", "A")
for i in range(len(t)-1):
    if t.count(t[i])>1:
        print("index of the duplicated element = ", i)

#--------------------------------------------------#
### Q2: Write a Python program to remove duplicates from a tuple
t = ("A", "B", "C", "A")

def reomveTuble(t:tuple):
    t2 = list(t)
    for i in range(len(t2)-1):
        if t2.count(t2[i])>1:
            t2.remove(t2[i])
            t = tuple(t2)
            print("the new tuple without duplicates, ", t)

reomveTuble(t)
#--------------------------------------------------#