m = int(input('Choose M: '))
a = int(input('Choose A: '))
x = int(input('Choose X: '))
c = int(input('Choose C: '))
count = int(input('How many numbers print on display: '))

x1 = (a * x + c) % m
file = open("numbers.txt", 'w')
for i in range(m):
    if i < count:
        print(x)
    file.write(str(x) + ', ')
    x = (a * x + c) % m
    if i > 0 and x == x1:
        print("Period: {0}".format(i + 1))
        file.write("Period: {0}".format(i + 1))
        break

print("End.")
