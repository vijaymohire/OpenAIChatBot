def greet_with_time():
  """
  Prompts the user for their name, greets them, and displays the current time.
  """

  # Get the current date and time in desired format
  from datetime import datetime
  current_time = datetime.now().strftime("%I:%M:%S %p")

  # Ask for the user's name
  name = input("What is your name? ")

  # Print the greeting with name and time
  print(f"Hello, {name}! The time is {current_time}.")

# Call the function
greet_with_time()
