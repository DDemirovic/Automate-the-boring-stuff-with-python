#! python 3
#https://www.w3schools.com/python/python_regex.asp
import re

#regex for strong password detection
passwordLengthRegex = re.compile(r"^\w{8,}$", re.VERBOSE)
passwordUpperCaseRegex = re.compile(r"[A-Z]+")
passwordLowerCaseRegex = re.compile(r"[a-z]+")
passwordDigitRegex = re.compile(r"\d+")

password = "a"

checkLength = passwordLengthRegex.search(password)
checkUpperCase = passwordUpperCaseRegex.search(password)
checkLowerCase = passwordLowerCaseRegex.search(password)
checkDigit = passwordDigitRegex.search(password)

if not checkLength:
    print("Your passwords needs at least eight characters.")

if not checkUpperCase:
    print("Your passwords needs at least one uppercase character.")

if not checkLowerCase:
    print("Your passwords needs at least one lowercase character.")

if not checkDigit:
    print("Your passwords needs at least one digit.")