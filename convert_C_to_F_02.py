# FILE NAME - convert_C_to_F_02.py

# NAME: Sheri Facey
# DATE: 10/1/25
# BRIEF DESCRIPTION:  c to f 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Temperature Converter =====\n')
print('  1. Convert from Celsius to Fahrenheit')
print('  2. Convert from Fahrenheit to Celsius\n')


number_choice = int(input('Please choose from the above menu: '))

temperature = float(input('Enter a temperature to convert: '))

C_to_F = (temperature) * 9/5 + 32
F_to_C = (temperature) - 32  * 5/9

if number_choice == 1:
  print(f'\n{temperature} degrees Celsius is {C_to_F} degrees Fahrenheit.')

else:
  print(f'\n{temperature} degrees Fahrenheit is {F_to_C} degrees Celsius.')










########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?



learning the formula to conver celcius to fahrenheit



'''
