import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,5))
    count += 1
    
print ourList
