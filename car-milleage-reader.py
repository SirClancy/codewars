#! /usr/bin/python
def num_interesting(number):
    
    # Check if number is 3 digit or more
    if number % 100 == number:
        print("It's not a big number")
        return False
        
    # Check for digit followed by all zeroes
    if number % 100 == 0:
        print("Followed by zeroes")
        return True
    
    number = str(number)
    
    # Dirty check for number having same digits
    if len(set(number)) == 1:
        print("Has same digits")
        return True
    
    # Dirty check for palindrome
    if number[::-1] == number:
        print("Palindrome")
        return True
        
    if number in '1234567890':
        print("Sequential increasing")
        return True
    
    if number in '9876543210':
        print("Sequential decreasing")
        return True
    
def is_interesting(number, awesome_phrases):
    # Check if mileage or following mileages are in awesome phrases
    if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1
        
    if number in awesome_phrases:
        return 2
        
    # Check for digit followed by all zeroes
    if num_interesting(number):
        return 2
        
    if num_interesting(number + 1) or num_interesting(number + 2):
        return 1
    
    return 0