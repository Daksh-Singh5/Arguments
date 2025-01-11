bill = float(input("please enter your bill: "))
tipprc = float(input("please enter your tip(in %): "))

def tip(b,tprc):
    return ((tprc/100)*b)+b

totalCost = tip(bill,tipprc)
totalCost2 = tip(bill,tipprc)

if totalCost<1000:
    totalmoney=(totalCost*0.08)+totalCost
elif totalCost>1000 and totalCost<2000:
    totalmoney=(totalCost*0.15)+totalCost
elif totalCost>2000:
    totalmoney=(totalCost*0.28)+totalCost
    

print("your total amount to pay is",totalmoney,"with gst")