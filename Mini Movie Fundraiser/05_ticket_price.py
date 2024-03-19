# Calculate ticket price based on the age
def calc_ticket_price(var_age):...
















# loop for testing...
while True: 

    # Get age (assume users input a valid integer) 
    age = int(input("Age: "))

# calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))
    
