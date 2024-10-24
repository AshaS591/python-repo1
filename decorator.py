def sum(num1,num2,odd):
    print(num1+num2)
    def even_sum():
        if num1%2==0 and num2%2==0:
            print(f"Even sum is {num1+num2}")
            odd()
            print("Execution continues...")
    return even_sum
def odd():
    num=int(input('enter a number :'))
    if num%2:
        print(f"This is odd num {num}")
even_sum=sum(10,20,odd)
even_sum()

def 