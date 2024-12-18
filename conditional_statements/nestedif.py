#wap to check if the user entered character is vowel only if cahracter is an alpha
char=input("enter the character :")
if char.isalpha():
    if char in 'aeiouAEIOU':
        print('it is a vowel')
    else:
        print('consonant')
else:
    print('not an alpha')

#wap to check if the user entered integer is multiple of 5 only if it is a even no
num=int(input('enter number :'))
if num%2==0:
    if num%5==0:
        print(f"{num} is even and multiple of 5")
    else:
        print(f"{num} is even and not multiple of 5")
else:
    print(f"{num} is not even" )

#wap to validate username and password entered by the user to login to an application
credentials={'Asha':'mypsd@991','appa':'psd#009','shashi':'dreamgirl@121'}
username=input('enter username:')
password=input("enter password :")
if username in credentials:
    actual_password=credentials[username]
    if password==actual_password:
        print('logged in successfully')
    else:
        print('wrong password')
else:
    print('username does not exist')

#wap to check user entered number is two digit only if it is a number
number=int(input("enter a number:"))
if number.is_integer():
    if 9<number<100 or -100<number<-9:
        print('two digit number')
    else:
        print('not two digit number')
else:
    print("not a number")


