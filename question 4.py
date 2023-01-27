candies=int(input('guess the number of candies:'))
if candies%5==2 and candies%6==3 and candies%7==2 and candies<200:
    print('you guessed thr right no. of candies')
else:
    print('you guessed the wrong no. of candies')    