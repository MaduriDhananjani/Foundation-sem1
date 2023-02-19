# User Inputs
num = int(input('Please Enter the Amount -: '))

print ('To convert to word representation enter ‘W’, to convert to USD currency enter ‘C’')

# Option from user
Option = str(input('Please enter your Option -: '))


if Option == 'W' :

    Digit = ['','One','Two','Three','Four','Five','Six','Seven','Eight', 'Nine']
    Teens = ['Ten','Eleven','Twelve','Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    Tens = ['','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']


    if (num < 10):
        print (Digit[num])

    elif (num < 20):
        if num % 10 == 0:
            print (Tens[num // 10])
        else :
            print (Teens[num % 10])
        
    elif (num < 100):
            if num % 10 == 0:
                print (Tens [num // 10])
            else :
                print (Tens [num // 10] + ' ' + Digit[num % 10])

    elif (num < 1000):
            if num % 100 == 0:
                print (Digit [num // 100] + ' Hundred ')
            elif 10 < num % 100 < 20:
                print (Digit [num // 100] + ' Hundred and ' + Teens [num % 10])
            else :
                print (Digit [num // 100] + ' Hundred and ' + Tens [num // 10 % 10] + ' ' + Digit[num % 10])

    elif (num < 10000):
            if num % 1000 == 0:
                print (Digit [num // 1000] + ' Thousand ')
            elif num % 100 == 0:
                print (Digit [num // 1000] + ' Thousand and ' + Digit [num // 100 % 10] + ' Hundred ')
            elif num % 1000 < 10:
                print (Digit [num // 1000] + ' Thousand and ' + Digit [num % 1000])
            elif num % 1000 < 20:
                print (Digit [num // 1000] + ' Thousand and ' + Teens [num % 10])
            elif 10 < num % 100 < 20:
                print (Digit [num // 1000] + ' Thousand, ' + Digit [num // 100 % 10] + ' Hundred and ' +  Teens [num % 10])
            else :
                print (Digit [num // 1000] + ' Thousand, ' + Digit [num // 100 % 10] + ' Hundred and ' + Tens[num % 100 // 10] + ' ' + Digit[num % 10])

    elif (num < 20000) :
            if num % 1000 == 0:
                print (Teens [num // 1000 % 10] + ' Thousand ')
            elif num % 100 == 0 :
                print (Teens [num // 1000 % 10] + ' Thousand and ' + Digit [num // 100 % 10] + ' Hundred ')
            elif num % 1000 < 10:
                print (Teens [num // 1000 % 10] + ' Thousand and ' + Digit [num % 1000])
            elif num % 1000 < 20:
                print (Teens [num // 1000 % 10] + ' Thousand and ' + Teens [num % 10])
            elif 10 < num % 100 < 20:
                print (Teens [num // 1000 % 10] + ' Thousand, ' + Digit [num // 100 % 10] + ' Hundred and ' + Teens [num % 10])
            else :
                print (Teens [num // 1000 % 10] + ' Thousand, ' + Digit[num // 100 % 10]+ ' Hundred and ' + Tens[num // 10 % 10] + ' ' + Digit[num % 10] )

    else :
            if num % 10000 == 0:
                print (Tens [num // 10000] + ' Thousand ')
            elif num % 1000 == 0 :
                print (Tens [num // 10000 ] +' ' + Digit [num // 1000 % 10] + ' Thousand ')
            elif num % 100 == 0 :
                print (Tens [num // 10000 ] +' ' + Digit [num // 1000 % 10]+ ' Thousand and ' + Digit [num // 100 % 10] + ' Hundred ')
            elif num % 1000 < 10:
                print (Tens [num // 10000 ] +' ' + Digit [num // 1000 % 10] + ' Thousand and ' + Digit [num % 10])
            elif num % 1000 < 20:
                print (Tens [num // 10000 ] +' ' + Digit [num // 1000 % 10]+ ' Thousand and ' + Teens [num % 10])
            elif 10 < num % 100 < 20:
                print (Tens [num // 10000 ] +' ' + Digit [num // 1000 % 10]+ ' Thousand, ' + Digit [num // 100 % 10] + ' Hundred and ' + Teens [num % 10])
            else :
                print (Tens [num // 10000] + ' ' + Digit [num // 1000 % 10]+ ' Thousand, ' + Digit[num // 100 % 10] + ' Hundred and ' + Tens[num // 10 % 10] + ' ' + Digit[num % 10] )

elif Option == 'C' :

    d = num / 200

    print ('USD',round(d))
