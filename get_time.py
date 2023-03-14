# Import the datetime module
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the date and time in a formatted string
print(f"The current date and time is {now:%Y-%m-%d %H:%M:%S}")