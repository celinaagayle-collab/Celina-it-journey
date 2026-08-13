score=float(input("enter your score"))
if score>= 80:
    print ("Grade: A")
elif score>= 70:
    print ("Grade: B")
elif score>= 60:
    print("Grade: C")
elif score>= 50:
    print("Grade: D")
else:
    print("Grade: F")

average= int(input("enter your average"))
if average>= 90:
    print (average, "excellent")
elif average>= 70:
    print (average, "pass")
else:
   print (average, "fail")

if average>=90: 
     print ("grade A")   
elif average>=80:
     print ("grade b")     
elif average>=70:
     print ("grade c")  
else:
     print ("fail")      

score= (85,75,60,95)   
print (min(score))  
print (max(score))
print (sum(score))
average=sum (score) / len (score)
if average>=90: 
     print ("grade A")   
elif average>=80:
     print ("grade b")     
elif average>=70:
     print ("grade c")  
else:
     print ("fail")  