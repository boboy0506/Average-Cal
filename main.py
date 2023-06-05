def firstsem():
    oral  = int(input("Oral Communication                            : "))
    scie  = int(input("Eath and Life Science                         : "))
    etech = int(input("Empowerment Technology                        : "))
    math  = int(input("General Mathemathics                          : "))
    ucsp  = int(input("Understanding Social Community Politics       : "))
    eapp  = int(input("English For Academic and Professional Purposes: "))
    philo = int(input("Introduction to Philosophy                    : "))
    pe    = int(input("Physical Education                            : "))
    average = [oral, scie, etech, math, ucsp, eapp, philo, pe] 
    total = (oral + scie + etech + math + ucsp + eapp + philo + pe) /8
    print(total)
    highest = max(average)
    lowest = min(average)
    print(f"Your Highest grade in this sem is {highest}")
    print(f"Your Lowest grade in this sem is {lowest}")
    
    
def secondsem():
    pe       = int(input("Physical Education                         : "))
    century  = int(input("21st Century                               : "))
    rr       = int(input("Reading and Writting                       : "))
    scie     = int(input("Physical Science                           : "))
    stats    = int(input("Statistics and Probability                 : "))
    research = int(input("Practical Research                         : "))
    java     = int(input("JAVA                                       : "))

print("First sem  [1]\nSecond sem [2]\nWhole sem [3]")

while True:
    user = int(input("Enter a sem: "))
    if user == 1 or user == 2 or user == 3:
        break

if user == 1:
    firstsem()
if user == 2:
    secondsem()
if user == 3:
    firstsem()
    secondsem()
    
