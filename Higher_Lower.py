import random
from celebreties import fam_person

A=random.choice(fam_person)
B=random.choice(fam_person)

#To replay the game

def play_again():
    while True:
                again=input("If you want to play more Type 'y' or 'n' : ").lower()
                if again=='y':
                    A=random.choice(fam_person)
                    B=random.choice(fam_person)
                    B=check_duplicate(A,B)
                    person1(A)
                    person2(B)
                    return False
                elif again=='n':
                    print("Game over !")
                    return True
                else:
                    print("Invalid! Type 'y' or 'n'")
#checking for duplication of persons

def check_duplicate(A,B):
    while A==B:
        B=random.choice(fam_person)
    return B

check_duplicate(A,B)

def person1(A):
    print(f"compare A : {A['name']}, a {A['profession']}, from {A['country']}")

def person2(B):
    print(f"against B : {B['name']}, a {B['profession']}, from {B['country']}")

person1(A) 
person2(B)

def replace(score,current,other):
    if score%2==0:
        current=random.choice(fam_person)
        while current == other :
            current = random.choice(fam_person)
    return current

score=0
game=False
while not game:

    choose=input("Who has more follower? Type 'A' or 'B' : ").upper()

    if choose=='A':
        if A['follower_count']>B['follower_count']:
            score+=1
            print(f"You're right ! current score : {score}")
            A=replace(score,A,B)
            person1(A)
            B=random.choice(fam_person)
            B=check_duplicate(A,B)
            person2(B)

        else:
            print("you've lost")
            print(f"Final score : {score}")
            score=0
            game=play_again()
            
    elif choose=='B':
        if B['follower_count']>A['follower_count']:
            score+=1
            print(f"current score :  {score}")
            A=B
            B=replace(score,B,A)
            B=check_duplicate(A,B)
            person1(A)
            person2(B)

        else:
            print("you've lost")
            print(f"Final score : {score}")
            score=0
            game=play_again()
            
    else:
        print("Please Type 'A' or 'B'")
        print("Game over !")
        game=True