# File name: warmupDay9.py
count = 1
for i in range(1,5):
  count *= i 
  print(count)

largestnum = 0 
for i in range(10):
  if i > largestnum:
    largestnum = i
  print(largestnum)

userinput = input('Enter a string:')
inputlength = len(userinput)
print(inputlength-1)

foodlist = ['milk', 'juice', 'cookies']
listlength = len(foodlist)
if listlength == 0:
  print('Your list is empty')
else:
  print('Your list is not empty')

listone = [1, 3, 5, 7]
listtwo = [1, 2, 4, 6]