import turtle
import time
from PIL import Image

# --------- THIS WAS TO RESIZE THE IMAGE ---------

# def resize_gif(input_image_path, output_image_path, scale_percent):
#     image = Image.open(input_image_path)
#     width, height = image.size
    
#     # Calculate the new dimensions
#     new_width = int(width * scale_percent)
#     new_height = int(height * scale_percent)
    
#     # Resize the image
#     resized_image = image.resize((new_width, new_height))
    
#     # Save the resized image
#     resized_image.save(output_image_path)

# Resize turtle.gif and beer.gif to 25% of their original size
# resize_gif("turtle.gif", "turtle_resized.gif", 0.25)
# resize_gif("beer.gif", "beer_resized.gif", 0.25)

# Set up the screen
screen = turtle.Screen()
screen.title("Beer O'clock")
screen.setup(width=800, height=600)

#registers beer gif and turtle gif
screen.register_shape("turtle_resized.gif")
screen.register_shape("beer_resized.gif")

# Create turtle object for the turtle
turtle_worker = turtle.Turtle()
turtle_worker.shape("turtle_resized.gif")  # or "turtle.gif" if you have an image
turtle_worker.penup()  # Don't draw a line when moving
turtle_worker.goto(-300, 0)  # Start far left, which represents 9 AM

# Create turtle object for the beer
beer = turtle.Turtle()
beer.shape("beer_resized.gif")  # or "beer.gif" if you have an image
beer.penup()
beer.goto(300, 0)  # Place beer far right, which represents 5 PM

# Create a turtle object to display percentage
percentage_display = turtle.Turtle()
percentage_display.hideturtle()  # Hide the pen (just used for writing text)
percentage_display.penup()

# Simulation parameters
start_time = 9 * 60  # Convert 9 AM to minutes (540 minutes)
end_time = 17 * 60  # Convert 5 PM to minutes (1020 minutes)
total_minutes = end_time - start_time  # 8 hours = 480 minutes
intervals = 32  # 32 intervals (each 15 minutes)
distance_to_travel = 600  # Total distance from turtle to beer in pixels
step_distance = distance_to_travel // intervals  # Distance to move each interval

# Get the current time
current_time = time.localtime()
current_hour = current_time.tm_hour
current_minute = current_time.tm_min

# Calculate the total minutes since 9 AM
current_total_minutes = (current_hour * 60 + current_minute)

# Ensure the time is between 9 AM and 5 PM
if start_time <= current_total_minutes <= end_time:
    # Calculate how many 15-minute intervals have passed since 9 AM
    minutes_passed = current_total_minutes - start_time
    intervals_passed = minutes_passed // 15  # Every 15 minutes is one interval

    # Calculate the percentage of completion
    percentage_complete = (intervals_passed / intervals) * 100

    # Move the turtle based on the number of intervals passed
    distance_moved = step_distance * intervals_passed
    turtle_worker.forward(distance_moved)

    # Display the percentage completion under the turtle
    turtle_position = turtle_worker.pos()  # Get current position of the turtle
    percentage_display.goto(turtle_position[0], turtle_position[1] - 50)  # Display below the turtle
    percentage_display.clear()  # Clear previous text
    percentage_display.write(f"{percentage_complete:.2f}% complete", align="center", font=("Arial", 12, "normal"))

    print(f"Current Time: {current_hour}:{current_minute} - Turtle moved {distance_moved} pixels towards the beer!")
else:
    print("It's not between 9 AM and 5 PM. The turtle only moves during work hours.")

#exit screen on click 
screen.exitonclick()
