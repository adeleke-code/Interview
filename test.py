from collections import Counter
import statistics
import psycopg2
import random





data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

colors = []


# Question 1
#Finding the mean colour
for day, color_string in data.items():
    color_list = color_string.split(", ")
    colors.extend(color_list)

color_counts = Counter(colors)

most_common_color = color_counts.most_common(1)[0][0]

print("The mean color is:", most_common_color)
## The mean color is: BLUE
##The logic behind the code is to create a dictionary of keys being the days and values being the colors. 
##Then we split the colors by comma and add them to a list. 
##Then we use the Counter module to count the number of times each color appears in the list.
##Then we use the most_common function to find the most common color and print it out.



# Question 2
# The colour most worn throughout the week

color_counts = Counter(colors)
most_common_color = color_counts.most_common(1)[0][0]

print("The color mostly worn throughout the week is:", most_common_color)
## The color mostly worn throughout the week is: BLUE
## Just as similar to the first question, we have dictionary of keys being the days and values being the colors.
## Then we split the colors by comma and add them to a list.
## Then we use the Counter module to count the number of times each color appears in the list.
## Then we use the most_common function to find the most common color and print it out.



# Question 3
## Which color is the median?

sorted_colors = sorted(colors)

n = len(sorted_colors)
if n % 2 == 0:
    middle_index = n // 2
    median_color = sorted_colors[middle_index - 1]
    next_color = sorted_colors[middle_index]
    median_color = f"{median_color}/{next_color}"
else:
    middle_index = n // 2
    median_color = sorted_colors[middle_index]

print("The color that represents the median is:", median_color)
## The color that represents the median is: GREEN
## Just as similar to the first question, we have dictionary of keys being the days and values being the colors.
## Then I split the colors by comma and add them to a list.
## Then I use the sorted function to sort the colors in alphabetical order.
## Then I create a logic that if the length of the sorted colors is even, then the median color is the middle index minus 1 and the next color.


# Question 4 BONUS!!!!!
## Calculate the variance of the colors

color_values = {
    "GREEN": 1,
    "YELLOW": 2,
    "BROWN": 3,
    "BLUE": 4,
    "PINK": 5,
    "ORANGE": 6,
    "CREAM": 7,
    "RED": 8,
    "WHITE": 9,
    "ARSH": 10,
    "BLEW": 11,
    "BLACK": 12
}

numeric_colors = []
for day, color_string in data.items():
    color_list = color_string.split(", ")
    numeric_colors.extend([color_values.get(color, 0) for color in color_list])

mean_color = statistics.mean(numeric_colors)

squared_diffs = [(color - mean_color) ** 2 for color in numeric_colors]

variance = statistics.mean(squared_diffs)

print("The variance of the colors is:", variance)
## The variance of the colors is: 7.541274238227147
## I had to add numeric values to the colors in order to calculate the variance.
## using the dictionary of the colors and their numeric values, I created a list of the numeric values of the colors.
## Then I calculated the mean of the numeric values.
## Then I calculated the squared difference of each numeric value from the mean.
## Then I calculated the variance of the squared differences.


# Question 5 BONUS!!!!!
## if a colour is chosen at random, what is the probability that the color is red?

red_count = 0
total_count = 0

for color_string in data.values():
    color_list = color_string.split(", ")
    red_count += color_list.count("RED")
    total_count += len(color_list)

# Calculate the probability of choosing red
probability_red = red_count / total_count

print("The probability of choosing the color red is:", probability_red)
## The probability of choosing the color red is:  0.09473684210526316
## I created a logic that counts the number of times the color red appears in the list of colors.
## Then I calculated the probability of choosing red by dividing the number of times red appears by the total number of colors.



# Question 6.      
# Save the colours and their frequencies in postgresql database

colors = {
    "GREEN": 5,
    "YELLOW": 3,
    "BLUE": 8,
    "RED": 6,
    "BROWN": 2,
    "PINK": 4,
    "ORANGE": 7,
    "CREAM": 1,
    "ARSH": 1,
    "BLEW": 1,
    "BLACK": 1,
    "WHITE": 9
}


try:
    connection = psycopg2.connect(
        user="postgres",
        password="jWyKnByFMFlcUjm3sKrA",
        host="containers-us-west-47.railway.app",
        port="5918",
        database="railway"
    )
    cursor = connection.cursor()
except Exception as error:
    print("Error while connecting to PostgreSQL", error)

print("Connection successful")

##Note: I had to create a database on railway.app and use the credentials to connect to the database.
## You can use the credentials to connect to the database and see the table I created.
## It would be up for 7 days from the time of submission of this assignment.


create_table = """
CREATE TABLE IF NOT EXISTS colors (
    color_name VARCHAR(255) PRIMARY KEY,
    frequency INTEGER
)
"""
cursor.execute(create_table)
connection.commit()

insert_query = "INSERT INTO colors (color_name, frequency) VALUES (%s, %s)"

for color, frequency in colors.items():
    record_to_insert = (color, frequency)
    cursor.execute(insert_query, record_to_insert)
connection.commit()

print("Colors inserted successfully")

cursor.close()
connection.close()
## The logic behind the code is:
## I created a dictionary of the colors and their frequencies.
## Then I created a connection to the postgresql database.
## Then I created a table in the database.
## Then I created a logic that inserts the colors and their frequencies into the table.
## Then I closed the connection to the database.



# Question 7 BONUS!!!!!
## write a recursive searching algorithm to search for a number entered by user in a list of numbers.


def recursive_search(number, num_list, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if num_list[mid] == number:
        return True
    elif num_list[mid] > number:
        return recursive_search(number, num_list, low, mid - 1)
    else:
        return recursive_search(number, num_list, mid + 1, high)


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

target = int(input("Enter a number to search:>>> "))

found = recursive_search(target, numbers, 0, len(numbers) - 1)

if found:
    print("Number is present in the list.")
else:
    print("Number is not present in the list.")

## The logic behind the code is:
## I created a function that takes in the number to search, the list of numbers, the lowest index and the highest index.
## Then I created a logic that if the lowest index is greater than the highest index, then the number is not present in the list.
## Then I created a logic that if the middle index is equal to the number, then the number is present in the list.
## Then I created a logic that if the middle index is greater than the number, then the number is present in the first half of the list.
## Then I created a logic that if the middle index is less than the number, then the number is present in the second half of the list.
## Then I created a list of numbers.
## Then I created a logic that takes in the number to search from the user.
## Then I created a logic that calls the recursive function and passes in the number to search, the list of numbers, the lowest index and the highest index.
## Then I created a logic that if the number is found, then print that the number is present in the list.
## Then I created a logic that if the number is not found, then print that the number is not present in the list.






# Question 8 
## Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
def generate_binary():
    binary_num = ''.join(random.choice(['0', '1']) for _ in range(4))

    return binary_num

def binary_converter(binary):
    decimal_num = int(binary, 2)
    return decimal_num

binary_num = generate_binary()
decimal_num = binary_converter(binary_num)

print("Generated Binary Number:", binary_num)
print("Equivalent Decimal Number:", decimal_num)

## The logic behind the code is:
## I created a function that generates a random binary number of 4 digits.
## I created a function that converts the binary number to decimal number.
## I created a logic that calls the function that generates the binary number.
## I created a logic that calls the function that converts the binary number to decimal number.
## I created a logic that prints both the generated binary number and the equivalent decimal number.




# Question 9
# Write a program to sum the first 50 fibonacci sequence.
def fibonacci_sum_generator(n):
    fib_sum = 0
    a, b = 0, 1
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    return fib_sum

sum = fibonacci_sum_generator(50)
print("Sum of the first 50 Fibonacci numbers:", sum)

## The logic behind the code is:
## I created a function that takes in the number of fibonacci numbers to sum.
## I created a variable that stores the sum of the fibonacci numbers.
## I created a logic that generates the fibonacci numbers and adds them to the sum variable.
## I created a logic that returns the sum of the fibonacci numbers.
## I created a logic that calls the function that generates the sum of the fibonacci numbers and prints the result.

