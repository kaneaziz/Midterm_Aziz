#QUESTION 1

a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3

#QUESTION 2
print((2+3)*6/2 and 18.0)


#QUESTION 3
import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
#print(d)


#QUESTION 4
def palindrome(word):
    return word == word[::-1]

numbers = {
    "A": "7489617719749244646336564429479177169847",
    "B": "6593036601359343374664733439531066303956",
    "C": "5485839837501070045005400701057389385845",
    "D": "8025833559061079503003059701609553385208",
}

non_palindromes = [key for key, num in numbers.items() if not palindrome(num)]
print(non_palindromes)



#QUESTION 5
def count_pattern_occurrences(text):
    count = 0  # Counter for matches

    words = text.split()  # Split the text into words

    for word in words:  # Loop through each word
        if word.startswith("C") and word.endswith("jeb"):  # Check start and end
            count += 1  # Increase count if it matches

    return count  # Return total matches


# Example usage
text = "Cblablajeb Ctestjeb Ccooljeb randomword Cnotmatchjeb C123jeb"
print(count_pattern_occurrences(text))  # Should return 5


#QUESTION 6
my_list = [1, 2, 3]
print("Before:", my_list)

my_list[1] = 99  # Changing an element
print("After:", my_list)

#word = "cat"
#word[0] = "b"

word = "cat"
new_word = "b" + word[1:]  # Create a new string
print(new_word)  # Output: "bat"


#QUESTION 7

#import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original list:", random_numbers)

# Step 2: Modify the list based on conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers less than or equal to 50 with "XX"
        random_numbers[i] = "XX"

# Step 3: Print the modified list
print("Modified list:", random_numbers)


#QUESTION 8
def is_valid_url(url):
 #   extensions = ["com", "org", "net", "edu", "gov", "io"]

    # Step 1: Check if it starts with "http://", "https://", or "www."
    if url.startswith("http://") or url.startswith("https://") or url.startswith("www."):

        # Step 2: Check if it contains at least one dot "."
        if "." in url:

            # Step 3: Get the last part after the last dot
            parts = url.split(".")
            last_part = parts[-1]  # The last part after the last "."

            # Step 4: Check if the last part is in the valid extensions list
            if last_part in extensions:
                return True  # It is a valid URL

    return False  # If any condition fails, return False


# Examples
print(is_valid_url("https://example.com"))  # True
print(is_valid_url("example.website"))  # False (No valid extension)
print(is_valid_url("https//wrongformat.com"))  # False (Missing ":")
print(is_valid_url("random text"))  # False (Not a URL)

#QUESTION 9
def days_since_birthday(birthday):
     #Split the birthday string into day, month, and year
    parts = birthday.split("-")
    birth_year = int(parts[2])  # Convert year to an integer

    # Assume the current year is 2025
    current_year = 2025

    # Count full years in between (excluding birth year and current year)
    full_years = 0
    for year in range(birth_year + 1, current_year):  # From the next year after birth to the year before current
        full_years += 1  # Count each full year

    # Each full year has 365 days (ignoring leap years)
    total_days = full_years * 365

    return total_days

# Example usage
print(days_since_birthday("30-03-2005"))   #Should return number of days

