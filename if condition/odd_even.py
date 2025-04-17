n=int(input("Enter a number :"))
print(n)

if n%2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")


if n > 10 and n % 2 == 0:
    print('yay')765
else:
    print('no')

if n > 10 or n%2 == 0:
    print('yay')
else:
    print('no')
