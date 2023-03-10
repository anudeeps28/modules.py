import random

uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXUZ"
lowercaseLetters = uppercaseLetters.lower()
digits = "0123456789"
symbols = "`~!@#$%^&*()_+-=[]{};:'/"

# we want to include all types of characters in our password. If you don't want any of them, just turn them False
upper, lower, nums, syms = True, True, True, True 

all = ""

if upper:
    all += uppercaseLetters
if lower:
    all += lowercaseLetters
if nums:
    all += digits
if syms:
    all += symbols

lengthOfPassword = 20
numberOfPasswords = 10

for i in range(numberOfPasswords):
    password = "".join(random.sample(all, lengthOfPassword)) # taking 20 random sample from "all" string 
    print(password)
