#  WAP to find the largest number among two
# a= int(input("Enter first number: "))
# b= int(input("Enter second number: "))
# if a > b:
#     print(f"{a} is the largest number") 
# else:
#     print(f"{b} is the largest number")

#What type of data 
# a = 22.99
# print(type(a))
# b = 33.88
# print(type(b))

#WAP to check whether a number is even or odd
# a=int(input("Enter a number: "))
# if a%2==0:
#     print(f"{a} is an even number")
# else:
#     print(f"{a} is an odd number")

#WAC to do sum of n numbers
# n = int(input("Enter the value of n: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("The sum of first n numbers is: ", sum)

#Find a Duplicate in an array
a = [2,5,3,2,7,5,9]
duplicates = []

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j] and a[i] not in duplicates:
            duplicates.append(a[i])

print("Duplicate elements in the array are:", duplicates)
