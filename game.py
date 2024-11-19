from browser import document, html, window

# Set up the canvas
canvas = document["gameCanvas"]
ctx = canvas.getContext("2d")

# Game variables
player = {"x": 375, "y": 500, "width": 50, "height": 50, "speed": 5}
keys = set()

# Handle keyboard events
def key_down(event):
    keys.add(event.key)

def key_up(event):
    keys.discard(event.key)

document.bind("keydown", key_down)
document.bind("keyup", key_up)

# Game loop
def game_loop():
    ctx.clearRect(0, 0, canvas.width, canvas.height)  # Clear canvas

    # Player movement
    if "ArrowLeft" in keys and player["x"] > 0:
        player["x"] -= player["speed"]
    if "ArrowRight" in keys and player["x"] < canvas.width - player["width"]:
        player["x"] += player["speed"]
    if "ArrowUp" in keys and player["y"] > 0:
        player["y"] -= player["speed"]
    if "ArrowDown" in keys and player["y"] < canvas.height - player["height"]:
        player["y"] += player["speed"]

    # Draw player
    ctx.fillStyle = "red"
    ctx.fillRect(player["x"], player["y"], player["width"], player["height"])

    # Loop the game
    window.requestAnimationFrame(game_loop)

# Start the game loop
game_loop()
