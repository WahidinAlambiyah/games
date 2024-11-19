from browser import document, window
import math, random

# Canvas setup
canvas = document["wheelCanvas"]
ctx = canvas.getContext("2d")
radius = 280  # Radius of the wheel
center = {"x": 300, "y": 300}  # Center of the canvas

# Wheel segments
segments = ["$100", "$200", "$300", "$400", "$500", "Lose Turn", "Free Spin", "Bankrupt"]
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "pink"]
segment_angle = 2 * math.pi / len(segments)
current_angle = 0  # Initial angle of the wheel

# Drawing the wheel
def draw_wheel():
    for i, segment in enumerate(segments):
        start_angle = i * segment_angle + current_angle
        end_angle = start_angle + segment_angle
        ctx.beginPath()
        ctx.moveTo(center["x"], center["y"])
        ctx.arc(center["x"], center["y"], radius, start_angle, end_angle)
        ctx.fillStyle = colors[i]
        ctx.fill()
        ctx.stroke()
        ctx.closePath()

        # Add text to the segments
        mid_angle = (start_angle + end_angle) / 2
        text_x = center["x"] + math.cos(mid_angle) * (radius - 50)
        text_y = center["y"] + math.sin(mid_angle) * (radius - 50)
        ctx.fillStyle = "white"
        ctx.font = "18px Arial"
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillText(segment, text_x, text_y)

# Spin the wheel
is_spinning = False
spin_speed = 0
result_element = document["result"]

def spin_wheel(event):
    global is_spinning, spin_speed
    if is_spinning:
        return  # Prevent multiple spins at once
    spin_speed = random.uniform(0.2, 0.5)  # Random initial speed
    is_spinning = True
    result_element.textContent = "Spinning..."

def animate_wheel(timestamp):
    global current_angle, spin_speed, is_spinning
    if is_spinning:
        current_angle += spin_speed
        spin_speed *= 0.98  # Gradual slowdown

        if spin_speed < 0.01:  # Stop spinning
            is_spinning = False
            spin_speed = 0
            determine_result()

    ctx.clearRect(0, 0, canvas.width, canvas.height)
    draw_wheel()
    window.requestAnimationFrame(animate_wheel)

# Determine the result
def determine_result():
    result_index = int((2 * math.pi - current_angle % (2 * math.pi)) / segment_angle) % len(segments)
    result_element.textContent = f"You landed on: {segments[result_index]}!"

# Event binding
document["spinButton"].bind("click", spin_wheel)

# Start animation loop
window.requestAnimationFrame(animate_wheel)
