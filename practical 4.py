name = input("Enter first and last name of student: ")
n = []
n = name.split()
firstN = n[0]
lastN = n[1]

#a
l = 0
for i in range(len(n)):
    if l < len(n[i]):
        l = len(n[i])
print(f"Name with longest length is:{n[i]}")

#b
sub1 = list(firstN)
sub2 = list(lastN)

ch = input("Enter character to be searched in string: ")

for i in range(len(sub1)):
    if ch == sub1[i]:
        print(f"Character found in first name at index {i}")

for i in range(len(sub2)):
    if ch == sub2[i]:
        print(f"Character found in last name at index {i}")


#c
i = 0
j = len(n)-1

for i in range(len(n)):
    if n[i] == n[j]:
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome ")
        break

#d
print(f"Index of first substring is {0}")

count = 0
for i in range(len(n)):
    if firstN == lastN:
        count = count + 1
    else:
        print("Word not repeated")