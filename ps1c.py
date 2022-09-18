## 6.0001 Pset 1: Part c
## Name: Olivia Dias
## Time Spent: 1:30
## Collaborators: TA 

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit:"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
# initialize portion down payment, current savings, 
# annual rate(r), down payment, and the
# upper and lower bound of the bisection search
portion_down_payment = 0.25
current_savings = 0
months = 0
r = 0.5    # start with 1% annual rate
low = 0  # the lower bound of bisection search(using 1% to not mess up calculations)
upper = 1.0   # the upper bound of bisection search (100%)
down_payment = 800000*portion_down_payment
steps = 0   # steps taken in bisection search
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
# if statement to check if initial deposit will reach the down payment amount
if (down_payment - (initial_deposit*((1+ 1/12)**36)))-100 > 0:
    r = None
    print("Best savings rate:", r)
    print("Steps in bisection search:", steps)
     
# elif statement to check if annual rate should be 0    
elif (down_payment < initial_deposit) or (abs(down_payment - initial_deposit) <= 100):
    r = 0
    print("Best savings rate:", r)
    print("Steps in bisection search:", steps)

# else statement to find the smallest annual rate to be within +/- 100 of the down_payment
else:
    # while loop to find the lowest annual rate to reach within +/-$100
    # of the downpayment within 3 years(36 months)
    while abs(down_payment - current_savings) > 100: 
        # resets current savings to check a new annual rate value
        current_savings = 0
        
        # updates r to be in between the upper and lower bound        
        r = (low+upper)/2

        # calculates how much will be saved after 3 years
        # using the compound interest formula
        current_savings = initial_deposit*((1+ r/12)**36)
        
        # bisection search
        # if statement to check if current savings is too small
        if (down_payment - current_savings) > 100:
            low = r
        # else statement to check if current savings is too big
        else:
            upper = r  
        # increments the number of steps taken in the bisection search
        steps+=1
    # print section
    print("Best savings rate:", r)
    print("Steps in bisection search:", steps) 

