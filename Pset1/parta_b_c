# PART A

def part_a(annual_salary, portion_saved, total_cost):
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
	    current_savings += portion_saved*(annual_salary/12)
	    months +=1
	
	return months


# PART B

def part_b(annual_salary, portion_saved, total_cost, semi_annual_raise):
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
	
	return months


# PART C
def part_c(initial_deposit):
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
	        #print("hello in loop")
	        # resets current savings 
	        current_savings = 0
	        # calculates how much will be saved after 3 years
	        # using the compound interest formula
	        r = (low+upper)/2
	        current_savings = initial_deposit*((1+ r/12)**36)
	        #print(f"this is the current_savings: {current_savings}")
	        # bisection search
	        # if statement to check if current savings do
	        if (down_payment - current_savings) > 100:
	            
	            #low = (upper + r)/2
	            low = r
	            '''print(f"(after)this is upperbound: {upper}")
	            print(f"(after)this lower bound: {low}")
	            print(f"(after)this is annual rate: {r}")
	            '''
	        else:
	        #elif down_payment - current_savings < 100:
	            #r = (low+r)/2
	            upper = r  
	        '''
	        print(f"this is the upper bound: {upper}")
	        print(f"this is the lower bound: {low}")
	        print(f"this is annual rate: {r}")
	        print(f"the calculation")
	        '''
	        steps+=1
	
	return r, steps
