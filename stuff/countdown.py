import time

# Set the countdown time in seconds
countdown_time = 10

# Print the starting time
print(f"Starting countdown from {countdown_time}...")

# Loop until the countdown time has elapsed
while countdown_time > 0:
    # Print the current time remaining
    print(countdown_time)
    # Pause for one second
    time.sleep(1)
    # Decrement the countdown time
    countdown_time -= 1

# Print a message when the countdown is complete
print("Countdown complete!")
