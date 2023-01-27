year=int(input("enter the year:"))
if( year%4==0):
    if(year%100==0 and year%400==0):
        print('the year is a leap year ')
    elif(year%100==0 and year%400!=0):
        print('the year is not a leap year')
    else:
        print('the year is a leap year')    
else:
    print('the year is not a leap year')            