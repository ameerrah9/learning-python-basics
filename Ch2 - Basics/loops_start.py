#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while(x < 5):
        print(x)
        x = x + 1

    # TODO: define a for loop
    # We have an iterator
    # Range going from 5 to 10
    # Within the range but not including the 10
    for x in range(5, 10):
        print(x)

    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for day in days:
        print(day)
    # TODO: use the break and continue statements
    # Break the execution of a loop if a condition is met
    for x in range(5, 10):
        if x == 7:
            break # When x gets to 7 it will break the loop
        if x % 2 == 0:
            continue # Skip the rest of the loop and do the next iteration # Skipping whatever meets that condition
        print(x)
        
    # TODO: using the enumerate() function to get index 
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, d in enumerate(days): # Enumerate will iterate over the collection and returns the index and the item
        print(i, d)

if __name__ == "__main__":
    main()
