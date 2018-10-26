import random
choices=['rock','paper','scissors']
yourscore=0
scoreofpc=0
while(yourscore!=3 and scoreofpc!=3):
	a=input("my choice is ")
	b=(random.choice(choices))
	print(b)
	if(b=="rock" and a=="paper" ):
		yourscore=yourscore+1
		print("your score is ",yourscore)
		print("pc score is ",scoreofpc)
	elif(b=="rock" and a=="scissors"):
		scoreofpc=scoreofpc+1
		print("your score is ",yourscore)
		print("pc score is ",scoreofpc)
	elif(b=="paper" and a=="rock"):
		scoreofpc=scoreofpc+1
		print("your score is ",yourscore)
		print("pc score is ",scoreofpc)
	elif(b=="paper" and a=="scissors"):
		yourscore=yourscore+1
		print("your score is ",yourscore)
		print("pc score is ",scoreofpc)
	elif(b=="scissors" and a=="rock"):
		yourscore=yourscore+1
		print("your score is ",yourscore)
		print("pc score is ",scoreofpc)		
	elif(b=="scissors" and a=="paper"):
		scoreofpc=scoreofpc+1
		print("your score is ",yourscore)
		print("pc score is ",scoreofpc)
if(scoreofpc==3):
	print("you loose")
else:
	print("you win")
	
	
	
