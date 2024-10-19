#Cristian Garcia
#10/16/2024

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = (currentTimeInt + waitTimeInt)
print("Final time:", finalTimeInt)
