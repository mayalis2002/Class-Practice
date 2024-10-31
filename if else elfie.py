# START if-else
num: int = int(input("enter num"))

if num > 0:
    # YES
    print(num, 'is positive')
else:
    # NO
    if num == 0:
        print('negative')

# STOP

# START ELIF
num: int = int(input("enter num"))

if num > 0:
    # YES
    print(num, 'is positive')
elif num == 0:
    # YES
    print('negative')

# STOP

# EXRESIZE
a: int = int(input('enter num'))
b: int = int(input('enter num'))
c: int = int(input('enter num'))

if b < a > c:
    print(a, "correct")
elif  b > c:
    print(b)
else:
    print(c)
# end
