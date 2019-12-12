#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: December 2019
# This program puts user inputs into a list
#  and calculates its sum


def sums(times):
    # This function takes the users numbers to calculate the sum
    # list that would be filled with users numbers
    list_of_numbers = []

    # process
    for number in range(times):
        numbers_as_string = input("Enter your number: ")
        numbers_as_int = int(numbers_as_string)
        list_of_numbers.append(numbers_as_int)
    # calculates sum of list
    total = sum(list_of_numbers)
    # returns list sum to the main function
    return total


def main():
    # This function takes the input of hw many numbers the user wishes to enter
    # this asks the user again if a false input was given
    while True:
        # input
        times_as_string = input("How many numbers do you wish to enter: ")
        print()
        try:
            # converts string to int
            times_as_int = int(times_as_string)
            # calls upon sums function
            value = sums(times_as_int)
            # prints sum after getting returned value
            print()
            print("The sum of your numbers are", value)
        # prevents crashes
        except ValueError:
            print("Invalid Input")
            print()
            continue
        # breaks out of loop
        else:
            break


if __name__ == "__main__":
    main()
