ll = []

n1 = int(input('Enter a number'))
n2 = int(input('Enter a number'))
n3 = int(input('Enter a number'))

ll.extend([n1, n2, n3])
ll.sort()

print(ll[::-1])
