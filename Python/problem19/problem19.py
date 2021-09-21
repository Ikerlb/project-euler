class Date:
	def __init__(self,year,dow,dom,month,months):
		self.year=year
		self.dow=dow
		self.dom=dom
		self.month=month
		self.months=months

	def str(self):
		m=["January","Februaru","March","April","May","June","July","August","September","October","November","December"]
		dow=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
		return "{}: {},{},{}".format(dow[self.dow],self.dom,m[self.month],self.year)

def next(date):
	if date.dom==date.months[date.month]:
		if date.month==len(date.months)-1:
			date.year+=1
			if date.year%400==0 or (date.year%4==0 and date.year%100!=0):
				date.months[1]=29
			else:
				date.months[1]=28 
			date.month=0
		else:
			date.month+=1
		date.dom=1
	else:
		date.dom+=1
	date.dow=(date.dow+1)%7


	