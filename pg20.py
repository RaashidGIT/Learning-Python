import time

# Ask the user to input time in seconds
my_time = int(input("Enter the time in seconds: "))

# Countdown loop from given time to 1
for x in range(my_time, 0, -1):
    # Convert seconds to hours, minutes, and seconds
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600
    
    # Display the time in HH:MM:SS format with zero-padding
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    # Wait for 1 second before next update
    time.sleep(1)

print("TIME'S UP!")
