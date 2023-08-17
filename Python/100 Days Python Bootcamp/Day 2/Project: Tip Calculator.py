#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip Calculator')
bill = float(input('what was the total bill? $'))
percentage = float(input('what percentage would you like to give: %'))
people = int(input('How many People to split the bill:'))
total_bill = bill + ((bill*percentage)/100)
pay = total_bill /people
print("Each person should pay:$", round(pay,2))
