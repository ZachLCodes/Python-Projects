import math
choice = int(input("Is the data a population(0) or sample(1)"))
size = int(input("What is the size of the data set?"))
data = [0]*size
mean = 0.00
for i in range (size):
    data[i] = float(input("Item "+str(i)+": "))
    mean = mean+data[i]
mean = mean/size
total = 0.00
for i in range (size):
    data[i] = math.pow(data[i]-mean,2)
    total = total + data[i]
if(choice == 0):
    total = total/size
elif(choice == 1):
    total = total/(size-1)
total = math.sqrt(total)
print("The standard deviation for your data set is "+str(total))
