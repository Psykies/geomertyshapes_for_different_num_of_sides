import turtle

# Function to draw a polygon with n sides
def draw_polygon(n):
    angle = 360 / n
    for _ in range(n):
        turtle.forward(100)  # Adjust length as needed
        turtle.right(angle)

# Get user input for the number of sides
num_sides = int(input("Enter the number of sides for the geometric shape: "))

# Create a turtle object
pen = turtle.Turtle()

# Set speed and shape
pen.speed(1)
pen.shape("turtle")

# Handle special cases
if num_sides == 0:
    # Draw a circle
    pen.circle(100)
elif num_sides == 1:
    # Draw a dot
    pen.dot(20)
elif num_sides == 2:
    # Draw a straight line
    pen.forward(200)
else:
    # Draw a polygon with the given number of sides
    draw_polygon(num_sides)

# Keep the window open
turtle.done()
