import random
i=0
while(i<10):
    i=i+1
    a=random.randint(1,20)
    b=random.randint(1,10)
    c=int(input(f'question {i}: {a} X {b}:'))
    if(c== a*b):
        print("Right!")
    else:
        print(f"Wrong! The answer is {a*b}")
        
