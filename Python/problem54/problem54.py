from collections import Counter
vals={'T':10,'J':11,'Q':12,'K':13,'A':14}
hierarchy={
            'High Card':0,
            'One Pair':1,
            'Two Pairs':2,
            'Three of a Kind':3,
            'Straight':4,
            'Flush':5,
            'Full House':6,
            'Four of a Kind':7,
            'Straight Flush':8,
            'Royal Flush':9,
        }

class Card:
    def __init__(self,s):
        if s[:-1] not in vals:
            self.value=int(s[:-1])
        else:
            self.value=vals[s[:-1]]
        self.suit=s[-1]

    def __str__(self):
        return f"%s%s"%(self.value,self.suit) 

hands=[]

def parse_line(l):
    ws=l.split(" ")
    hs=[]
    for w in ws:
        hs.append(Card(w))
    return (sorted(hs[:5],key=lambda x:x.value,reverse=True),sorted(hs[5:],key=lambda x:x.value,reverse=True))

#returns hand,extra info, untie
def hand(h):
    values=[c.value for c in h]
    suits=[c.suit for c in h]
    count=Counter(values)
    [(mc1,n1),(mc2,n2)]=count.most_common(2)
    s=set(values)
    if len(set(suits))==1:
        if is_straight(values):
            if values[-1]==10:
                return ("Royal Flush",[],[])
            else:
                return ("Straight Flush",[values[0]],[])
        return ("Flush",[values[0]],[])
    elif n1==4:
        return ("Four of a Kind",[mc1],[x for x in values if x!=mc1])
    elif n1==3:
        if n2==2:
            return ("Full House",[mc1,mc2],[])
        else:
            return ("Three of a Kind",[mc1],[x for x in values if x!=mc1])
    elif is_straight(values):
        return ("Straight",[values[0]],[])
    elif n1==2:
        if n2==2:
            return ("Two Pairs",[mc1,mc2],[x for x in values if x!=mc1 or x!=mc2])
        else:
            return ("One Pair",[mc1],[x for x in values if x!=mc1])
    return ("High Card",[values[0]],values)

def is_straight(vals):
    if vals[0]==14 and vals[1]==2 and vals[2]==3 and vals[4]==4:
        return True
    for i in range(1,5):
        if vals[i]!=vals[i-1]-1:
            return False
    return True

def compare(t):
    [p1,p2]=t
    (h1,ei1,t1)=hand(p1)
    (h2,ei2,t2)=hand(p2)
    if hierarchy[h1]>hierarchy[h2]:
        return 1
    elif hierarchy[h1]<hierarchy[h2]:
        return 2
    else:
        if h1=="High Card":
            return highest_card(t1,t2)
        elif h1=="One Pair":
            if ei1[0]>ei2[0]:
                return 1
            elif ei1[0]<ei2[0]:
                return 2
            return highest_card(t1,t2)
        elif h1=="Two Pair":
            maxp1=max(ei1)
            minp1=min(ei1)
            maxp2=max(ei2)
            minp2=min(ei2)
            if maxp1>maxp2:
                return 1
            elif maxp1<maxp2:
                return 2
            else:
                if minp1>minp2:
                    return 1
                if minp1<minp2:
                    return 2
                else:
                    return highest_card(t1,t2)
        elif h1=="Three of a Kind":
            if ei1[0]>ei2[0]:
                return 1
            elif ei1[0]<ei2[0]:
                return 2
        elif h=="Straight":
            if ei1[0]>ei2[0]:
                return 1
            else:
                return 2
        elif h=="Flush":
            if ei1[0]>ei2[0]:
                return 1
            else:
                return 2
        elif h1=="Full House":
            if ei1[0]>ei2[0]:
                return 1
            else:
                return 2
        elif h1=="Four of a Kind":
            if ei1[0]>ei2[0]:
                return 1
            else:
                return 2
        elif h1=="Straight Flush":
            if ei1[0]>ei2[0]:
                return 1
            elif ei1[0]<ei2[0]:
                return 2
            else:
                return 0
        else:
            return 0


def highest_card(t1,t2):
    for (ut1,ut2) in zip(t1,t2):
        if ut1>ut2:
            return 1
        elif ut1<ut2:
            return 2
    return 0


with open("p054_poker.txt","r") as f:
    hands=list(map(parse_line,f.read().split("\n")[:-1]))

p1=0
for hs in hands:
    if compare(hs)==1:
        print("player one wins")
        p1+=1
    else:
        print("player two wins")
    

#with open("p054_poker.txt","r") as f:
    #r=f.read().replace("T","10").replace("J","11").replace("Q","12").replace("K","13").replace("A","14")

#lines=list(map(lambda l:l.split(" "),r.split("\n")))[:-1]
#hands=list(map(lambda x:(sorted(x[:5],key=lambda x:int(x[:-1])),sorted([5:],key=lambda x:int(x[:-1]))),lines))

#sorted(hands[0][0],key=lambda x:int(x[:-1]),reverse=True)


