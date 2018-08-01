userRoom = 'R1'
print ("You are in Room 1.")
print ("Press L,R,B,F to move.")
ip = raw_input()
while ( ip != "N" ):
	if ( userRoom == "R1" and ip == "F"):
		userRoom = "R2"
		print ("You are in Room 2.")
	elif ( userRoom == "R2" and ip == "B"):
		userRoom = "R1"
		print ("You are in Room 1.")
	elif ( userRoom == "R2" and ip == "F"):
		userRoom = "R3"
		print ("You are in Room 3.")
	elif ( userRoom == "R2" and ip == "R"):
		userRoom = "R4"
		print ("You are in Room 4.")
	elif ( userRoom == "R3" and ip == "B"):
		userRoom = "R2"
		print ("You are in Room 2.")
	elif ( userRoom == "R3" and ip == "R"):
		userRoom = "R4"
		print ("You are in Room 4.")
	elif ( userRoom == "R4" and ip == "R"):
		userRoom = "R3"
		print ("You are in Room 3.")
	elif ( userRoom == "R4" and ip == "L"):
		userRoom = "R2"
		print ("You are in Room 2.")
	elif ( userRoom == "R4" and ip == "B"):
		userRoom = "R5"
		print ("You are in Room 5.")
	elif ( userRoom == "R5" and ip == "L"):
		userRoom = "R1"
		print ("You are in Room 1.")
	elif ( userRoom == "R5" and ip == "B"):
		userRoom = "R6"
		print ("You are in Room 6.")
	elif ( userRoom == "R6" and ip == "F"):
		userRoom = "R5"
		print ("You are in Room 5.")
	else:
		print ("It's wall you can't move in that direction.")
	print ("Press L,R,B,F to move or Press N to exit game.")
	ip = raw_input()
		
