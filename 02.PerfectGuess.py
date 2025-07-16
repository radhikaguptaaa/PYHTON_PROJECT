from random import randint

n = randint(1, 100)
print("Game Begins :")
count = 0 
x = -1 
while(x != n ):
    count += 1 
    x = int(input("Guess the number "))
    if(x > n):
        print("AHH, the number is lower ")
    elif(x<n):
        print("AHH , the number is higher") 
print( f"HURRAY !!!! ...You have guessed the number in {count} no of guesses")       

  
