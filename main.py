num = input('Enter a number (decimal only): ')
# type your code here

count = num.find('.')
new_num = num[count+1:]
dp = len(new_num)

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
