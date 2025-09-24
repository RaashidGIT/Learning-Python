import time   # Import the time module to use sleep()

# Step 1: Ask the user to enter the countdown time in seconds
my_time = int(input("Enter the time in seconds: "))

# Step 2: Start a loop that counts down from my_time to 1
for remaining_time in range(my_time, 0, -1):
    
    # Step 3: Convert total seconds into hours, minutes, and seconds
    hours = remaining_time // 3600
    minutes = (remaining_time // 60) % 60
    seconds = remaining_time % 60
    
    # Step 4: Print the time in HH:MM:SS format
    # The "02" means two digits, with leading zeros if needed (e.g., 05 instead of 5)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    
    # Step 5: Wait for 1 second before showing the next countdown number
    time.sleep(1)

# Step 6: When the loop ends, print the final message
print("TIME'S UP!")
