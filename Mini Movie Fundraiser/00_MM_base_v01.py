# functions go here

# Checks user has entered yes / no to a question
def yes_no (question):
    while True:
      response = input (question)

# if the response is blank, outputs error
      if response == "":
        print("Sorry this can't be blank. Please try again.")
      else:
        if response == "yes" or response == "y":
          response = "yes"
          valid = True
        
        
        elif response == "no" or response == "n":
          print("We are done ")
          valid=True

        else: 
          print ("Please answer yes / no")
          
        
      return response

# main routine starts here

# Ask the user if they want to see the instructions
show_instructions = yes_no ("Do you want to "
                            "read the instructions? ")

# checks users enter a integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response 

        except ValueError:
            print("Please enter an integer")


if show_instructions=="yes":
  print("Instructions go here")

  print()

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# loop to sell tickets

while tickets_sold < MAX_TICKETS:
    name = not_blank ("Enter your name (or 'xxx' to quit.) ")

    if name == 'xxx':
        break
    


    age = num_check("Age: ")
    
    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s "
          "remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))