import random
choice="Y"
wordList = ["apple","oranges","Titanic","Harbour","Chine"]
def checkInput(char,word):
	occurrence=0
	if (len(char) == 1 ):
		for w in word:
			if ( char.upper() == w.upper() ):
				occurrence = occurrence + 1
		print ("your guessed word - " + str(occurrence) )
	else:
		print ("Not valid input")
	return occurrence
while (choice == "Y" ):
	word = random.choice(wordList)
	charCount = len(word)
	occurrence = 0
	attempt = 0
	while ( attempt < 8 ):
		letter = raw_input("Please guess the letters!")
		occurrence = occurrence + checkInput(letter,word)
		if (occurrence == len(word)):
			print ("you guessed it right and word is " + word)
			break
		elif (attempt == 8):
			print ("You exhausted the attempt!!!")
		attempt = attempt + 1
		print ("Attempt remaining - " + str(8-attempt))
	choice = raw_input("Press Y to play it again and N to exit")