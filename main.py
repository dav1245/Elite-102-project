#import sqlite3

# Connect to a local database (or create one if it doesn't exist)
#conn = sqlite3.connect("demo.db")
#cursor = conn.cursor()

# Create a simple table
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS users (
 #   id INTEGER PRIMARY KEY AUTOINCREMENT,
  #  name TEXT,
   # pin TEXT
#)
#""")

# Insert a sample record
#cursor.execute("INSERT INTO users (name, pin) VALUES (?, ?)", ("Alice", "1234"))
#conn.commit()

# Retrieve and print the data
#cursor.execute("SELECT * FROM users")
#rows = cursor.fetchall()

#print("All users in database:")
#for row in rows:
 #   print(row)

# Clean up
#conn.close()

print ("Welcome to the banking app!")
Menu = ['C: Create', 'M: Modify', 'D: Delete']
for i in sorted(Menu):
    print(i)
    
options = input ("Enter C to create an account, M to modify an existing account, or D to delete an existing account: ")

#This is for creating an account
if options == "C": 
    name = input("Great! Give your account a new name: ")
password = input(name + " is a cool name. Give your account a password: ")
print("Perfect! Your new account is " + name + ", and the account password is " + password + ".")

#This is for modifying
elif options == "M":
name = input("Great! If you'd like to change the name, enter a different one. If not, enter the original one: ")
password = input("Next, if you'd like to change the password, enter a new one. If not, enter the original one: ")
#There would be some code here actually going into the database and changing this
print("Your new or original account is " + name + ", and your new or original password is " + password + "!")

#This is for deleting
elif options == "D":
#There should be some code deleting the account from the database here
print("Your account " + name + " and its password " + password + " is deleted.")

#After the account functions come the actual banking functions

balance = 0

print ("Now that we're done with the account process, it's time to get to what truly matters: the money!")
Menu = ['Ch: Check Balance', 'W: Withdraw', 'MD: Make a deposit']
for i in sorted(Menu):
    print(i)
    
banking = input ("Enter Ch to check your balance, W to withdraw money from your account, or MD to deposit money into your account: ")

#To check balance
if banking == "Ch":
    print("Your current balance is " + balance + " dollars.")

#To take money from account
elif banking == "W":
    if balance == 0:
        print("Sorry, you can't withdraw anything. You have nothing in your account.")
    else:
        withdraw = input("How much would you like to withdraw?: ")
        if withdraw > balance:
            print ("Sorry, that's more than your balance.")
        else:
            balance = balance - withdraw
            print("Your new balance is " + balance + ".")

#To add money into the account
elif banking == "MD":
    deposit = input("How much would you like to add?: ")
    balance = balance + deposit
print("Your new balance is " + balance + ".")

#I'm still trying to link VSC to a database and I don't really know how
