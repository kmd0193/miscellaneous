#! /usr/bin/env python3
# stopwatch.py - Use time module to see how long it takes for user to type full name

# Import time module
import time


# Introduce the game:
print("Let's see how long it takes you to type your full name."),time.sleep(3)
print('Once the timer starts, begin typing...'),time.sleep(3)
print("Hit 'enter' once you're done, and we will see how long it took!"),time.sleep(3)
print('Starting the timer... NOW!'),time.sleep(1)
# Get the start time:
start = time.time()
# Get user input:
print('Enter your full name:')
full_name = input()


# Get end time:
end = time.time()

# Calculate how long it took:
total_time = end - start

# Print how long it took
print('It took you ' + str(total_time) + ' seconds to type your full name.')
