## 6.0001 Pset 1: Part b
## Name: Olivia Dias
## Time Spent:0:10
## Collaborators: None

##########################################################################################
## Get user input for annual_salary, portion_saved, total_cost, semi_annual_raise below ##
##########################################################################################
annual_salary = float(input("Enter your yearly salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
# initialize portion down payment, current savings, 
# annual rate(r), months, and down payment
portion_down_payment = 0.25
current_savings = 0
r = 0.05
months = 0
down_payment = total_cost*portion_down_payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
# while loop to find the number of months to reach the down payment for dream house 
while current_savings < down_payment:
    current_savings += current_savings*(r/12)
    # checks to see if 6 months have gone by
    if months%6==0 and months!=0:
        annual_salary += annual_salary*semi_annual_raise    
    
    current_savings += portion_saved*(annual_salary/12)
    months +=1

print("Number of months:", months)

