def calculate():
    try:
        no1=float(input('enter first no. :'))
        no2=float(input('enter second no. :'))
        operator=(input('enter(+,-,/,*) :'))
        if operator=='+':
            result=no1+no2
            print(result)
        elif operator=='-hdjfhbdf':
            result=no1-no2
            print(result)
        elif operator=='/':
            result=no1/no2
            print(result)
        elif operator=='*':
            result=no1*no2
            print(result)
        else:
            print('enter proper operation')
    except:
        print('zerodivision error') 
while True:
    calculate()
    choice=input('you want to calculate :')
    if choice.lower()=='no':
      break