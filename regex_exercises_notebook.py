# TD RegEX - Regular Expression Exercises and Solutions

This notebook contains a collection of regular expression exercises with their solutions in Python.

## 1. Extract All Email Addresses

**Exercise:** Write a Python program to extract all email addresses from a given string:
"Contact us at support@example.com or sales@example.com."

```python
import re

text = "Contact us at support@example.com or sales@example.com."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)
```

**Explanation:**
- `\b` defines a word boundary
- `[A-Za-z0-9._%+-]+` matches one or more letters, numbers, or special characters before the @
- `@` matches the @ symbol
- `[A-Za-z0-9.-]+` matches one or more letters, numbers, periods, or hyphens for the domain name
- `\.` matches a literal dot
- `[A-Z|a-z]{2,}` matches the TLD (like com, org, net) with at least 2 characters
- `\b` defines a word boundary at the end

## 2. Validate Phone Number

**Exercise:** Check if a given phone number is in the format (XXX) XXX-XXXX.

```python
import re

phone = input("Enter your phone number: ")
pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
match = re.match(pattern, phone)
print(bool(match))
```

**Explanation:**
- `^` asserts the start of the string
- `\(` matches the opening parenthesis (escaped because parentheses are special in regex)
- `\d{3}` matches exactly 3 digits
- `\)` matches the closing parenthesis
- ` ` matches a space
- `\d{3}` matches exactly 3 digits
- `-` matches a hyphen
- `\d{4}` matches exactly 4 digits
- `$` asserts the end of the string

## 3. Find All Words Starting With "a"

**Exercise:** Extract all words that start with the letter "a" from a given text.

```python
import re

text = input("Enter your text: ")
words = re.findall(r'\ba\w+', text)
print(words)
```

**Example:**
```
Enter your text: "apple and apricot are delicious"
# Output: ['apple', 'and', 'apricot', 'are']
```

**Explanation:**
- `\b` defines a word boundary, ensuring that we only match whole words
- `a` matches the letter 'a'
- `\w+` matches one or more word characters (letters, numbers, or underscore)

## 4. Replace Multiple Spaces with a Single Space

**Exercise:** Replace multiple consecutive spaces with a single space.

```python
import re

text = input("Enter a text with multiple spaces: ")
cleaned_text = re.sub(r'\s+', ' ', text)
print(cleaned_text)
```

**Example:**
```
Enter a text with multiple spaces: "This    is  an    example   text."
#Output: "This is an example text."
```

**Explanation:**
- `\s+` matches one or more whitespace characters
- `re.sub()` replaces all matches with a single space

## 5. Validate a Password

**Exercise:** Check if a password meets the criteria: at least one uppercase letter, at least one lowercase letter, at least one digit, and at least 8 characters.

```python
import re

password = input("Enter your password: ")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
valid = bool(re.match(pattern, password))
print(valid)
```

**Example:**
```
Enter your Password: "StrongP@ss1"
# Output: True
```

**Explanation:**
- `^` and `$`: Start and end of the string
- `(?=.*[a-z])`: Positive lookahead assertion that ensures at least one lowercase letter
- `(?=.*[A-Z])`: Positive lookahead assertion that ensures at least one uppercase letter
- `(?=.*\d)`: Positive lookahead assertion that ensures at least one digit
- `.{8,}`: Ensures the password is at least 8 characters long

## 6. Extract Dates from a String

**Exercise:** Extract all dates in the format DD/MM/YYYY from a given text.

```python
import re

text = input("Enter your text: ")
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print(dates)
```

**Example:**
```
Enter your text: "Today's date is 16/05/2025 and tomorrow will be 17/05/2025."
# Output: ['16/05/2025', '17/05/2025']
```

**Explanation:**
- `\b` defines a word boundary
- `\d{2}` matches exactly 2 digits (for the day)
- `/` matches a forward slash
- `\d{2}` matches exactly 2 digits (for the month)
- `/` matches a forward slash
- `\d{4}` matches exactly 4 digits (for the year)
- `\b` defines a word boundary

## 7. Validate an IPv4 Address

**Exercise:** Check if a given IP address is valid.

```python
import re

ip = input("Enter an IPv4 address: ")
pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
valid = bool(re.match(pattern, ip))
print(valid)
```

**Example:**
```
Enter an IPv4 Address: "192.168.1.1"
# Output: True
```

**Explanation:**
- `^` asserts the start of the string
- `(\d{1,3}\.){3}` matches 3 occurrences of 1-3 digits followed by a dot
- `\d{1,3}` matches 1-3 digits for the last part of the IP address
- `$` asserts the end of the string

**Note:** This basic validation checks only the format. For complete IP validation, you should also check that each number is between 0 and 255.

## Enhanced IPv4 Validation (Bonus)

A more complete IPv4 validation that checks that each number is between 0 and 255:

```python
import re

def validate_ipv4(ip):
    # First check the pattern
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    
    # Check each number is between 0 and 255
    numbers = ip.split('.')
    for num in numbers:
        if int(num) > 255 or (num[0] == '0' and len(num) > 1):
            return False
    
    return True

# Test it
test_ip = input("Enter an IPv4 address for enhanced validation: ")
print(validate_ipv4(test_ip))
```