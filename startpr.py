#!/usr/bin/python2


import  os,time,commands,sys,socket,getpass

print   "Welcome  To world  of  data  !!"
print   "_______________________________"
print   "_______________________________"
print   "_______________________________"
print   "###############################"
time.sleep(2)
#wrong authentication count initialisation
count = 1

#entering username and password for authentication
def access():
	user=raw_input("enter  username to access project  :  ")
	password=getpass.getpass("enter password  :  ")

	if  user  ==  'root' and  password  ==  'redhat' :
		print  "access granted  !!"
		time.sleep(2)
		#switch the menu selection
		execfile('menu.py')
	else   :
		print   " opps\n wrong authentication!!! "
		time.sleep(2)
		print 	"Want to try again (y/n) : "
		#ch for storing  choice
		choice = raw_input()
		if choice=='y' :
			global count
			count+=1
			if count == 3 :
				print  	"cross limit!!"
				time.sleep(1)
				print	"Permision denied"
				exit()
			access()

		else :
			time.sleep(1)
			print "Thank you"
			exit()


access()

			


