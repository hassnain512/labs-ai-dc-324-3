#1.	Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# a = 1500
# b = 2700
# for i in range(a,b+1):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)

arr = []
a = 1500
b = 2700
for i in range(a,b+1):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
        arr.append(i)
print("arr: " , arr)


