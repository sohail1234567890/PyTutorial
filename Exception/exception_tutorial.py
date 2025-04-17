x= input('Enter number 1:')
y = input('Enter number 2:')

try:
    d = int(x)/int(y)
    a = 'baby yoda' + 56
except ZeroDivisionError as ze:
    print('Exception occured', ze)
    d =-1

except TypeError as te:
    print('Exception occured',te)
    d = -1
except Exception as e:
    print('Generic Exception')

print('Division is :', d)