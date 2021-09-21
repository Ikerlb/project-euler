def stringify_digits(d):
	if d==1:
		return "one"
	elif d==2:
		return "two"
	elif d==3:
		return "three"
	elif d==4:
		return "four"
	elif d==5:
		return "five"
	elif d==6:
		return "six"
	elif d==7:
		return "seven"
	elif d==8:
		return "eight"
	else:
		return "nine"

def stringify_sub_20(d):
	if d<10:
		return stringify_digits(d)
	elif d==10:
		return "ten"
	elif d==11:
		return "eleven"
	elif d==12:
		return "twelve"
	elif d==13:
		return "thirteen"
	elif d==14:
		return "fourteen"
	elif d==15:
		return "fifteen"
	elif d==16:
		return "sixteen"
	elif d==17:
		return "seventeen"
	elif d==18:
		return "eighteen"
	elif d==19:
		return "nineteen"

def stringify_sub_100(n):
	if n<20:
		return stringify_sub_20(n)
	s=""
	fst_digit=int(str(n)[0])
	snd_digit=int(str(n)[1])

	if fst_digit==3:
		s+="thirty"
	elif fst_digit==4:
		s+="forty"
	elif fst_digit==5:
		s+="fifty"
	elif fst_digit==6:
		s+="sixty"
	elif fst_digit==7:
		s+="seventy"
	elif fst_digit==8:
		s+="eighty"
	else:
		s+="ninety"
	if snd_digit!=0:
		s+=stringify_digits(snd_digit)
	return s

def stringify_sub_1000(n):
	if n<100:
		return stringify_sub_100(n)
	s=""
	fst_digit=int(str(n)[0])
	s+=stringify_digits(fst_digit)+"hundred"
	if n%100!=0:
		s+="and"+stringify_sub_100(n%100)
	return s

def stringify_sub_10000(n):
	if n<1000:
		return stringify_sub_1000(n)
	s=""
	fst_digit=int(str(n)[0])
	s+=stringify_digits(fst_digit)+"thousand"
	return s

s=0
for i in range(1,1000+1):
	s+=len(stringify_sub_10000(i))
	


