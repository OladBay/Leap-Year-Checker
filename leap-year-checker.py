### LEAP YEAR CHECKER ###
print ("Welcome to the Leap Year Checker V1.0")
print ("########## DESIGNED BY OneDisruptor ##########")

year = int(input("Enter the year below:\n "))

if len(str(year))==4:
    #Century year block
    if year % 400 == 0:
        if year % 100 == 0:
            print (f"Wow, {year} is a Leap Year")
    #Non Century year block
    elif year % 4 == 0:
        if year % 100 !=0:
            print(f"Wow, {year} is a leap year")
        else:
            print (f"Sorry, {year} is not a Leap Year")
    else:
        print (f"Sorry, {year} is not a Leap Year")
else:
    print("Error, Please enter a complete year")