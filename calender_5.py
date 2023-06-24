import datetime
from sys import stdout

allmonths=  [
["january", "jan", "01", "1", "one"],
["february", "feb", "02", "2", "two"],
["march", "mar", "03", "3"], 
["april", "apr", "04", "4"], 
["may", "05", "5"], 
["june","jun", "06", "6",], 
["july", "jul" , "07", "7"], 
["august", "aug", "08", "8"], 
["september", "sep", "09", "9"], 
["october", "oct", "10", "ten"],
["november", "nov", "11"], 
["december", "dec", "12"]]

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


enmonth= []
for m in allmonths:
	enmonth.extend(m)
	
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
def calenders(year='ok',month=0):
	retry=1
	while retry==1:
		while year=='ok':
			try:
				year=input("Enter the year (YYYY): ")
				if int(year)/1==int(year) or int(year)==0:
					year=int(year)
					while year<=0 or year>=10000:
						print("\nI can't calculate before the year 1 or after 9999, yet.'")
						year="ok"
			except:
				if year in escape:
					opt="quit"
					retry=0
				else:
					 print("\nYou have entered an invalid year. Please re-enter the year in Number or digits.\nIf you wanna exit type: quit\n")
					 year="ok"


		if year not in escape and month==0:
			month=input("\nEnter the month (MM): ").lower()

			if month in escape:
				break

			while month not in enmonth:
				print("\nYou have entered an invalid month. Please ensure that the month is entered as name or number.")
				opt = input("1. Need help? Type: help\n2. Want to quit, type: quit\n3. Want to try again, just re-enter the month.\n >> ").lower()
				if opt in escape:
					break
				elif opt in enmonth: month = opt
				elif opt == "help":
					print("Here are the options for the English Months: \n\nJanuary: ",jan,"\n\nFebruary: ",feb,"\n\nMarch: ",mar,"\n\nApril: ",apr,"\n\nMay: ",may,"\n\nJune:",jun,"\n\nJuly",jul,"\n\nAugust:",aug,"\n\nSeptember:",sep,"\n\nOctober: ",oct,"\n\nNovember: ",nov,"\n\nDecember: ",dec)

		day=1
		y0=int(year)
		
		y1=False
		if ((y0%4==0) and (y0%100!=0 or y0%400==0)):
			y1=True

		x=0
		y=0
		z=0

		for n, i in enumerate(allmonths):
			if month in i:
				MM = n+1

		name = datetime.datetime(year, MM, day)
		nod= int(name.strftime("%w"))
		xtab= 6-nod
		print('\n\033[7m Sat | Sun | Mon | Tue | Wed | Thu | Fri \033[0m', flush= True)
		tab=(nod+1)%7
		print('      '*tab, end='')

		for i in range(1,10):
			if i%7==xtab: print('\033[0;31;48m',end='', flush= True)
			if i%7==xtab+1:
				print('\033[0m', flush= True, end='')
				if i!=1:
					print()
			print("   ",i,"  ",sep="",end="")

		if month in xday: daterange=31
		elif month in feb:
			if y1== True: daterange=29
			else: daterange=28
		else: daterange=30
		for i in range(10,daterange+1):
			if i%7==xtab:
				print('\033[31m', end = '', flush= True)
			if i%7==xtab+1: print('\033[0m', flush= True)
			print("  ",i,"  ",sep="", end="")
			#if i%7==xtab: print('\033[0;37;40m')

		retry=0
		print()
		reply=input("\n\033[0;37;40mWanna try again? ")

		while reply not in condition:
			try:
				if int(reply)/1==int(reply):
					year=int(reply)
					retry=1
					reply="y"
			except ValueError:
				print("I don't get it. Answer in yes or no")
				reply=input("Try to write clearly.  ")
		if reply in condition:
			if reply in yes and year!="ok":
				retry=1
				year="ok"
				month=0
			elif reply in no or reply in escape:
				retry=0
	print("\n\nBye!")
if __name__=='__main__':
	calenders()
