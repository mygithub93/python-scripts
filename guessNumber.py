import random

choice = raw_input("Do you want to guess the number (Y/N)? ")

def checkGuessedNumber( n, randomNumber ):
    try:
        n = int(n)
    except:
        print "Please enter a valid number!"
    diff = randomNumber - n
    if diff == 0:
        print "Congrats!!! you guessed it right"
        print "Randon Number : " + str(randomNumber) + " Guessed Number : " + str(n)
    elif diff > 0 and diff > 50:
        print "Guessed number is too low!!!"
        print "Randon Number : " + str(randomNumber) + " Guessed Number : " + str(n)
    elif diff > 0 and diff < 50:
        print "You are too close!!!"
        print "Randon Number : " + str(randomNumber) + " Guessed Number : " + str(n)
    elif diff < 0 and diff < -50:
        print "Guessed number is too high!!!"
        print "Randon Number : " + str(randomNumber) + " Guessed Number : " + str(n)

while ( choice == "Y" ):
    randomNumber = random.randint(1,1000)
    print "Number generated Please guess the number!!!"
    guessedNumber = raw_input()
    checkGuessedNumber( guessedNumber, randomNumber )
    choice = raw_input("Do you want to guess the number again (Y/N)? ")

    