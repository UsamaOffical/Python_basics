try:
    usr = int(input("Enter a number : "))
    result = 10/usr
    print(result)

except ZeroDivisionError:
    print('Please enter must 1!')
except ValueError:
    print('Please enter a number not a string!')    
