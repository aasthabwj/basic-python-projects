import matplotlib.pyplot as plt
a = int(input('Enter any positive number : '))
b = []
while True:
    if a%2 == 0:
        a = a/2
        b.append(a)

    elif a%2 == 1:
        a = 3*a + 1
        b.append(a)
    if a == 1 :
        break
plt.plot(b)
plt.grid(True)
plt.show()