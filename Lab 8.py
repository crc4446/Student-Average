#This Program will get students' grades and calculate each student's average and a class average.
#Created by: Chris Caponi

grades = int(input("How many grades are there? "))
#the following variables will keep track of the sum of the student averages, the amount of students entered, and the average of all of those student averages.
theSum = 0
count = 0
classAvg = 0
#this while loop is used to repeat the program based on whether or not the user has more students to enter.
more = True
while more:
    stuName = input("What is the student's name? ")
    avg=0
    print("What are the student's grades? ")
#the for loop here will allow the user to enter a certain amount of grades based on the data collected above and calculate the student's average.
    for x in range(grades):
        stuGrades = int(input())
        while stuGrades < 0 or stuGrades > 100:
            print("Please re-enter a valid grade. ")
            stuGrades = int(input())
        avg += stuGrades/grades
    print(stuName,"'s average is ",(format(avg,"0.2f")),sep="")

#If the user enters no, the program will end, if yes the program will allow the user to enter more students.
    answer = input("Enter yes or no if you would like to calculate another student's average. ")
    while answer != "yes" and answer != "no":
        answer = input("Enter yes or no if you would like to calculate another student's average. ")
    if (answer == "no"):
        more = False
        
#below are the calculations for finding the class average based on the while loop data collected.
    theSum += float(avg)
    count += 1
classAvg = theSum / count

print("The class average:",format(classAvg,"0.2f"))

