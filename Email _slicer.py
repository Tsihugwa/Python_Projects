# First, we'll import the necessary libraries
import os
import re

# Next, we'll prompt the user for their email address
email = input("Enter your email address: ")

# We'll use a regular expression to validate the email address
pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
if not re.match(pattern, email):
  print("Invalid email address. Please try again.")
  exit()

# If the email address is valid, we'll slice it to get the username and domain
username = email[:email.index("@")]
domain = email[email.index("@")+1:]

# Now we can customize and send a message to the user with this information
message = f"Your email address is: {email}\nYour username is: {username}\nYour domain is: {domain}"
print(message)

# Finally, we can use the `os` library to send an email to the user
# You'll need to customize the `sendmail` command with the appropriate email addresses and message
os.system(f"echo {message} | mail -s 'Email Slicer Results' {email}")
