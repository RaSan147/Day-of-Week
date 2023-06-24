################################################################################
# Name of Date version 3.0 (Fixed Bugs & Errors)							   #
#			  Completed on: 12.04.2019(Friday)								#
################################################################################
# 1.For SoloLearn Users,													   #
#		Type the year first & Press Enter									 #
#		Then the name of the month & Enter									#
# **You can use number or name of the month									#
# Words you can use are in allmonths										   #
#		Then the number of the day & Enter									#
#		Finally type no (to stop loop) & Submit							   #
################################################################################
# 2. Example:  For 16 December, 1971										   #
#					Code Playground										   #
#			   1971	   ........................   (ENTER)				  #
#			   12 / December / dec / etc.  .......   (ENTER)				  #
#			   16		 ........................   (ENTER)				  #
#			   no				   →Submit								   #
#------------------------------------------------------------------------------#
# Output	||				  Thursday									   #
################################################################################
#   This CODE is more USEFUL& POWERFUL										 #
#								   for the									#
#						**IDLE & Pydroid 3(For Android) USERS**			   #
################################################################################
#				Thank YOU. Please UPVote									  #
################################################################################
#				This code was creater by,									 #
#					  Ratul Hasan											 #
################################################################################

import datetime

allmonths=  [["January", "Jan", "01", "1", "one", "january", "jan"],["February", "Feb", "02", "2", "two", "february", "feb"], ["March", "Mar", "03", "3", "march", "mar"], ["April", "Apr", "04", "4", "april", "apr"], ["May", "may", "05", "5"], ["June", "Jun", "06", "6","june","jun"], ["July", "Jul", "07", "7", "july", "jul"], ["August", "Aug", "08", "8", "august", "aug"], ["September", "Sep", "09", "9", "september", "sep"], ["October", "Oct", "10", "ten", "october", "oct"], ["November", "Nov", "11", "noveember", "nov"], ["December", "Dec", "12", "december", "dec"]]

jan=allmonths[0]
feb=allmonths[1]
mar=allmonths[2]
apr=allmonths[3]
may=allmonths[4]
jun=allmonths[5]
jul=allmonths[6]
aug=allmonths[7]
sep=allmonths[8]
oct =allmonths[9]
nov=allmonths[10]
dec=allmonths[11]
leap=jan+feb
enmonth=jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dec
xday=jan+mar+may+jul+aug+oct+dec
yday=apr+jun+sep+nov
yes=["y","yes","yeah","Yes","Yeah","sure","Sure","ok","Ok","lets go","Lets go","let's go","Let's go","start","Start"]
no=["n","no","No","na","Na","nah","Nah","nope","Nope","stop","Stop","quit","Quit","exit","Exit"]
condition=yes+no
escape=["exit","close","shut down","quit"]
retry=1
reply=0
opt=0
year="ok"

while retry==1:
	while year=="ok":
		year=input("Enter the year (YYYY): ")
		try:
			
			if int(year)/1==float(year) or int(year)==0:
				year=int(year)
				while year<=0 or year>=10000:
					print("I can't calculate before the year 1 or after 9999, yet.'")
					year="ok"
		except:
			if year in escape:
				opt="quit"
				retry=0
			else:
				 print("\nYou have entered an invalid year. Please re-enter the year in Number or digits.\nIf you wanna exit type: quit\n")
				 year="ok"
		
		  
	if year not in escape:
		month=input("\nEnter the month (MM): ")

		if month in escape:
			break

		while month not in enmonth:
			print("\nYou have entered an invalid month. Please ensure that the month is entered as name or number.")
			opt = input("1. Need help? Type: help\n2. Want to quit, type: quit\n3. Want to try again, just re-enter the month. \n >> ")
			if opt in escape:
				break
			elif opt in enmonth: month = opt
			elif opt == "help":
				print("Here are the options for the English Months: \n\nJanuary: ",jan,"\n\nFebruary: ",feb,"\n\nMarch: ",mar,"\n\nApril: ",apr,"\n\nMay: ",may,"\n\nJune:",jun,"\n\nJuly",jul,"\n\nAugust:",aug,"\n\nSeptember:",sep,"\n\nOctober: ",oct,"\n\nNovember: ",nov,"\n\nDecember: ",dec)
	if opt in escape:
		retry=0
	if opt not in escape:
		day=0
		while day ==0:
			try:
				day = int(input("\nEnter the day (DD): "))
			except (ValueError,TypeError):
				print("Sorry. Numbers only.  Try Again")
				day=0


		y0=year-0
		y1=False
		if ((y0%4==0) and (y0%100!=0 or y0%400==0)):
			y1=True

		while day>=32:
			print("\nThere is no month where the day is more than 31 days.")
			day= int(input("\nTry again (DD): "))

		while day>=31 and month in yday:
				print("\nThis month has only 30")
				day= int(input("\nTry again (DD): "))

		if month in feb:
			if y1==True:
				while day>=30:
					print("\nOn leap year February month has 29 day only")
					day= int(input("\nTry again (DD): "))
			else:
				while day>=29:
					print("\nFebruary month has 28 day only")
					day= int(input("\nTry again (DD): "))

		x=0
		y=0
		z=0

		if month in jan:
			MM=1
		elif month in feb:
			MM=2
		elif month in mar:
			MM=3
		elif month in apr:
			MM=4
		elif month in may:
			MM=5
		elif month in jun:
			MM=6
		elif month in jul:
			MM=7
		elif month in aug:
			MM=8
		elif month in sep:
			MM=9
		elif month in oct:
			MM=10
		elif month in nov:
			MM=11
		else:
			MM=12

		name = datetime.datetime(year, MM, day)
		print("\nThe name of the date is ", name.strftime("%A"), "\n")


		reply=input("\n\nWanna try again? \n >> ")

		while reply not in condition:
			try:
				if int(reply)/1==int(reply):
					year=int(reply)
					retry=1
					reply="y"
			except ValueError:
				print("I don't get it. Answer in yes or no")
				reply=input("Try to write clearly.  \n >> ")
		if reply in condition:
			if reply in yes and year!="ok":
				retry=1
				year="ok"
			elif reply in no or reply in escape:
				retry=0




print("\n\nBye!")
