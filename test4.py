def accum_sum(l):
    summ = 0
    for i in l:
        summ += i
        print(summ)
    return summ

li = []
while True:
    num = int(input('Enter a number (0 to end): '))
    if num < 0 or num > 999:
        print('Number is out of range.')
    elif num == 0:
        break
    else:
        li.append(num)
print('Original list:')
print(li)
print('Accumulative Sum:')
accum_sum(li)
