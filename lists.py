fruits= ["apple", "banana", "mango"]

fruits.append ("orange")
print (fruits)
print (fruits[0])
print (fruits[1])
print (fruits[2])
print (fruits[3])

fruits[1]="grape"
print (fruits)

fruits.remove("mango")
print (fruits)

for fruit in fruits:
    print (fruit)

print(len(fruits))

if  "apple"in fruits:
    print ("apple is in list")
if "pineapple" in fruits:
       print ("pineapple is in list")
else:
    print ("pineapple is not in list")

if "banana" not in fruits:
       print ("banana is missing")
else:
    print ("banana is in list")
fruits.sort()   
print(fruits) 

fruits= ["orange", "apple", "grape"]
fruits.sort(reverse=False)   
print(fruits) 

fruits.sort(reverse=True)   
print(fruits)         

numbers= [8,3,12,1,6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)   

scores= [75,40,100,65,90]
scores.sort()
print(scores)
print(min(scores))
print(max(scores))
print(sum(scores))
average=sum(scores) / len(scores)
print(average)

   
scores= (85,75,60,95)   
for score in scores:
    if score >=90: 
     print ("grade A")   
    elif score>=80:
     print ("grade b")     
    elif score>=70:
     print ("grade c")  
    else:
     print ("fail")  
  