x = int(input("Enter a number: "))
if x <= 0 or x > 26:
    print("Invalid input, program terminates.")
else:
    a = ''
    count = 1
    while count <= x:
        a += chr(ord('A') + (count-1))
        print(a)
        count += 1
