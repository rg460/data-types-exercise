# Instructions

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8



# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")

# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Plan

# check the type of two_digit_number[done]
# split the two numbers by calling the index and save in a new variable[done]
digit_one = two_digit_number[0];
digit_two = two_digit_number[1];
# find the type of digit_one and digit_two and convert each to intgers and store  in variable[done]
digit_one_integer = int(digit_one);
digit_two_integer = int(digit_two);
# sum the two integer values of digit_one  and digit_two and store in a varaible
sum = digit_one_integer + digit_two_integer
# print output of sum 
print(sum)



