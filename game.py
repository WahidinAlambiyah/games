from browser import document, window, html

# Use JavaScript's Math object for trigonometry
js_math = window.Math

# Canvas setup
canvas = document["wheelCanvas"]
ctx = canvas.getContext("2d")
radius = 280
center = {"x": 300, "y": 300}

# Default wheel segments
segments = ["$100", "$200", "$300", "$400", "$500", "Lose Turn", "Free Spin", "Bankrupt"]
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "pink"]
segment_angle = 2 * js_math.PI / len(segments)
current_angle = 0

# State
is_spinning = False
spin_speed = 0
history = []

# DOM Elements
result_element = document["result"]
history_list = document["historyList"]
prize_input = document["prizeInput"]
prize_list = document["prizeList"]

# Draw the arrow indicator
def draw_arrow():
    """Draws a bold, prominent arrow above the wheel."""
    arrow_height = 60  # Increased height for better visibility
    arrow_width = 40   # Increased width for a wider base
    arrow_top_y = center["y"] - radius - 60  # Position above the wheel

    # Draw the arrow (triangle)
    ctx.beginPath()
    ctx.moveTo(center["x"], arrow_top_y)  # Arrow tip
    ctx.lineTo(center["x"] - arrow_width / 2, arrow_top_y + arrow_height)  # Bottom-left corner
    ctx.lineTo(center["x"] + arrow_width / 2, arrow_top_y + arrow_height)  # Bottom-right corner
    ctx.closePath()

    # Fill with bright color and add a bold border
    ctx.fillStyle = "yellow"  # Bright yellow for visibility
    ctx.fill()
    ctx.strokeStyle = "black"  # Thick black outline
    ctx.lineWidth = 4  # Thicker outline
    ctx.stroke()

# Draw the wheel
def draw_wheel():
    """Draws the wheel with segments and updates the angle."""
    global segment_angle
    segment_angle = 2 * js_math.PI / len(segments) if segments else 0

    for i, segment in enumerate(segments):
        start_angle = i * segment_angle + current_angle
        end_angle = start_angle + segment_angle
        ctx.beginPath()
        ctx.moveTo(center["x"], center["y"])
        ctx.arc(center["x"], center["y"], radius, start_angle, end_angle)
        ctx.fillStyle = colors[i % len(colors)]
        ctx.fill()
        ctx.stroke()
        ctx.closePath()

        # Add text to the segments
        mid_angle = (start_angle + end_angle) / 2
        text_x = center["x"] + js_math.cos(mid_angle) * (radius - 50)
        text_y = center["y"] + js_math.sin(mid_angle) * (radius - 50)
        ctx.fillStyle = "white"
        ctx.font = "18px Arial"
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillText(segment, text_x, text_y)

    draw_arrow()  # Draw the arrow on top of the wheel

# Spin the wheel
def spin_wheel(event):
    global is_spinning, spin_speed
    if is_spinning or not segments:
        return
    spin_speed = js_math.random() * 0.3 + 0.2
    is_spinning = True
    result_element.textContent = "Spinning..."

def animate_wheel(timestamp):
    """Animates the spinning of the wheel."""
    global current_angle, spin_speed, is_spinning
    if is_spinning:
        current_angle += spin_speed
        spin_speed *= 0.98

        if spin_speed < 0.01:
            is_spinning = False
            spin_speed = 0
            determine_result()

    ctx.clearRect(0, 0, canvas.width, canvas.height)
    draw_wheel()
    window.requestAnimationFrame(animate_wheel)

# Determine the result
def determine_result():
    """Determines the segment where the arrow points."""
    if not segments:
        result_element.textContent = "No prizes left!"
        return

    result_index = int((2 * js_math.PI - current_angle % (2 * js_math.PI)) / segment_angle) % len(segments)
    prize = segments.pop(result_index)
    history.append(prize)

    result_element.textContent = f"You won: {prize}!"
    update_history()
    update_prize_list()
    draw_wheel()

# Update history display
def update_history():
    """Updates the prize history with the option to re-add prizes."""
    history_list.clear()
    for prize in history:
        li = html.LI(prize)
        add_back_button = html.BUTTON("Add Back", Class="prize-controls")

        def add_back(event, prize=prize):
            segments.append(prize)
            history.remove(prize)
            update_history()
            update_prize_list()
            draw_wheel()

        add_back_button.bind("click", add_back)
        li <= add_back_button
        history_list <= li

# Update the prize list
def update_prize_list():
    """Updates the dynamic prize list."""
    prize_list.clear()
    for i, prize in enumerate(segments):
        li = html.LI(prize)
        edit_button = html.BUTTON("Edit", Class="prize-controls")
        delete_button = html.BUTTON("Delete", Class="prize-controls")

        def edit_prize(event, index=i):
            new_prize = window.prompt("Edit prize:", segments[index])
            if new_prize:
                segments[index] = new_prize
                update_prize_list()
                draw_wheel()

        def delete_prize(event, index=i):
            segments.pop(index)
            update_prize_list()
            draw_wheel()

        edit_button.bind("click", edit_prize)
        delete_button.bind("click", delete_prize)
        li <= edit_button
        li <= delete_button
        prize_list <= li

# Add a prize
def add_prize(event):
    """Adds a new prize to the wheel."""
    global segments
    prize = prize_input.value.strip()
    if prize:
        segments.append(prize)
        prize_input.value = ""
        update_prize_list()
        draw_wheel()

# Bind buttons
document["spinButton"].bind("click", spin_wheel)
document["addPrize"].bind("click", add_prize)

# Initialize
update_prize_list()
window.requestAnimationFrame(animate_wheel)
