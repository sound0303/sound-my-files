#!/usr/bin/python3
import random
count=0
r=0
while count <=100:
	roll=input("press r to roll the dice")
	if roll=="r":
		r=random.randint(1,6)
		count=count+r
		print("your random num is",r)
		print("you are on count",count)
	if  count=="8":
			count=37
			print("you climb the ladder",count)
	elif count=="11":
			count=2
			print("down the ladder",count)
	elif count=="13":
		count=34
		print ("yes..pu the ladder",count)
	elif count=="25":
		count=4
		print("shit not again down the ladder",count)
		
	


		

	



