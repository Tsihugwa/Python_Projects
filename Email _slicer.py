import re

def slice_email(email):
  # Use a regular expression to extract the username and domain from the email
  username, domain = re.match(r"([^@]+)@([^@]+)", email).groups()
  return username, domain

def customize_and_send_message(email, message):
  # Slice the email address
  username, domain = slice_email(email)
  
  # Customize the message
  customized_message = f"Dear {username},\n\n{message}\n\nBest regards,\nYour friendly Email Slicer"
  
  # Send the message
  send_email(email, customized_message)

# Example usage
customize_and_send_message("user@example.com", "Thank you for using our Email Slicer service!")
