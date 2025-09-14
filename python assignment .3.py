# Blessing Gijima R247779H
# Assignment 3

# Questuion 1
def classify_number(number):
    """Classify a number as Positive, Negative, or Zero."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        result = classify_number(number)
        print("The number is:", result)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Question 2

def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
    *args : int or float
        Any number of integers or floats passed into the function.

    Returns:
    float
        The average value of the given numbers.
        Returns 0 if no numbers are provided.
    """
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print("Welcome to the Average Calculator Project!")
print("You can enter as many numbers as you want, separated by spaces.")

while True:
    user_input = input("\nEnter numbers (or type 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Goodbye! Thanks for using the Average Calculator.")
        break

    try:

        numbers = [float(num) for num in user_input.split()]


        avg = calculate_average(*numbers)

        print(f"The average of {numbers} is: {avg:.2f}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

#Question 3


while True:
    try:

        user_input = input("Enter a number: ")


        number = float(user_input)

        print(f"You entered a valid number: {number}")
        break

    except ValueError:

        print("Invalid input! Please enter a valid number.")

#Question 4


names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names have been written to names.txt.")


print("\nReading names from the file:")
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())

# question 5

celsius_temps = [0, 20, 37, 100]


fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))


print("Celsius temperatures: ", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)


#Question 6

def divide_numbers(numerator, denominator):
    """
    Divide two numbers safely.

    Parameters:
    numerator (int or float): The top number in the division.
    denominator (int or float): The bottom number in the division.

    Returns:
    float: The result of the division if successful.
    Prints an error message if an exception occurs.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")


# -------- Main Program --------
print("Division Program with Error Handling")

# Test cases
print("10 ÷ 2 =", divide_numbers(10, 2))   # Valid
print("5 ÷ 0 =", divide_numbers(5, 0))     # ZeroDivisionError
print("8 ÷ 'a' =", divide_numbers(8, "a")) # TypeError


#Question 7

class NegativeNumberError(Exception):
    """Custom exception raised when a negative number is encountered."""
    pass


def check_positive(number):
    """
    Check if a number is positive.

    Raises:
        NegativeNumberError: If the number is negative.
    """
    if number < 0:
        raise NegativeNumberError(f"Error: {number} is a negative number!")
    else:
        print(f"{number} is positive (or zero).")


# -------- Main Program --------
print("Custom Exception Demo")

try:
    num = int(input("Enter a number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter a valid integer.")


#Question 8

import random

def generate_random_numbers(count=10, start=1, end=100):
    """
    Generate a list of random integers.

    Parameters:
        count (int): Number of random integers to generate.
        start (int): Minimum value of the random integers.
        end (int): Maximum value of the random integers.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(start, end) for _ in range(count)]


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): List of integers or floats.

    Returns:
        float: The average of the numbers.
    """
    return sum(numbers) / len(numbers) if numbers else 0


# -------- Main Program --------
print("Random Number Generator and Average Calculator\n")


random_numbers = generate_random_numbers()

average = calculate_average(random_numbers)


print("Generated numbers:", random_numbers)
print(f"Average of numbers: {average:.2f}")

# Question 9

import re


def extract_emails(text):
    """
    Extract all email addresses from the given text.
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)



def validate_date(date_string):
    """
    Validate if a date is in YYYY-MM-DD format.
    """
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_string))



def replace_word(text, old_word, new_word):
    """
    Replace all occurrences of old_word with new_word in a string.
    """
    pattern = rf"\b{old_word}\b"
    return re.sub(pattern, new_word, text)


def split_non_alphanumeric(text):
    """
    Split a string by all non-alphanumeric characters.
    """
    return re.split(r"\W+", text)



if __name__ == "__main__":
    print("=== Regular Expressions Demo ===\n")


    sample_text = "Contact us at support@example.com or sales@company.org for more info."
    print("Extracted emails:", extract_emails(sample_text))


    print("\nDate validation:")
    test_date1 = "2025-09-14"
    test_date2 = "2025-99-14"
    print(test_date1, "->", validate_date(test_date1))
    print(test_date2, "->", validate_date(test_date2))


    sentence = "Python is great and Python is fun."
    new_sentence = replace_word(sentence, "Python", "Java")
    print("\nOriginal:", sentence)
    print("Modified:", new_sentence)


    messy_string = "Hello, world! Python_3 is awesome."
    print("\nSplit result:", split_non_alphanumeric(messy_string))


# Question 10



def start_server(host="127.0.0.1", port=65432):
    """
    Start a simple TCP server that sends a greeting message.
    """
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()

            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print("Connected by:", addr)
                conn.sendall(b"Hello from server!")
    except Exception as e:
        print("Server error:", e)


if __name__ == "__main__":
    start_server()

import socket


def start_client(host="127.0.0.1", port=65432):
    """
    Connect to the server and receive a message.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            message = client_socket.recv(1024)
            print("Message from server:", message.decode())
    except Exception as e:
        print("Client error:", e)


if __name__ == "__main__":
    start_client()






#Question 11

#An API is a communication mechanism between software applications,defining rules for requesting and sending data. For instance,a weather app may receive data from a weather API,allowing seamless interaction between applications.

import requests


url = "https://api.agify.io?name=Alice"

try:

    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        print("API Response:", data)
    else:
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)


import sqlite3


connection = sqlite3.connect("example.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))


connection.commit()


cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)


connection.close()
