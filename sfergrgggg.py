'''
print(f'NameError - {type(NameError)}- {issubclass(NameError,BaseException)}')


try:
    print('start code')
    print(error)
    print('No errors')

except:
    print('We have an error')

print('Code after capsule')
'''
'''
try:
    print(error)
except NameError:
    print('u have NameError')
    
try:
    print(10/0)
except ZeroDivisionError:
    print('ZeroDivisionError') 
'''
try:
    a=int(input('first number'))
    b=int(input('second number'))
    c = a / b
    print(c)
except ValueError:
    print(' not corect value  ')
except ZeroDivisionError:
    print('U can not divide by zero')
