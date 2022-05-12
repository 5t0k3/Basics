# Python program to swap two variables

x = 5
y = 10
print('x={}'.format(x))
print('y={}'.format(y))

# To take inputs from the user
#x = input('Enter the value of x: ')
#y = input('Enter the value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#z = input('Enter the value of z: ')
