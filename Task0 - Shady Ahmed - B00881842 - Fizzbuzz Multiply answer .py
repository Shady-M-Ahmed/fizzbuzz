
# Making Initial code design

# Initial time range values
X_first = int(1)  
X_last = int(101)   #Make the final count to 101

def FizzBuzzHandler(first,last):        # Create a function to handle FizzBuzz code
    
    for v in range(first,last): #For that include an if condition 
        if v %3 ==0 and v%5 ==0:
            print("FizzBuzz")
        elif v%3 == 0:
            print("Fizz")
        elif v%5 == 0:
            print("Buzz")
        else:
            print(int(v))

print("FizzBuzz Game starting to work from" , X_first, "to", X_last)    #Making the code look fancy and decent :)
FizzBuzzHandler(X_first,X_last) # Calling the function
            