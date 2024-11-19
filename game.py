from browser import document, window

canvas = document["gameCanvas"]
ctx = canvas.getContext("2d")

player = {"x": 375, "y": 500, "width": 50, "height": 50, "speed": 5}
keys = set()

# Handle key press events
def key_down(event):
    keys.add(event.key)

def key_up(event):
    keys.discard(event.key)

document.bind("keydown", key_down)
document.bind("keyup", key_up)

# Main game loop
def game_loop(timestamp):
    ctx.clearRect(0, 0, canvas.width, canvas.height)  # Clear canvas

    # Handle player movement
    if "ArrowLeft" in keys and player["x"] > 0:
        player["x"] -= player["speed"]
    if "ArrowRight" in keys and player["x"] < canvas.width - player["width"]:
        player["x"] += player["speed"]
    if "ArrowUp" in keys and player["y"] > 0:
        player["y"] -= player["speed"]
    if "ArrowDown" in keys and player["y"] < canvas.height - player["height"]:
        player["y"] += player["speed"]

    # Draw the player
    ctx.fillStyle = "red"
    ctx.fillRect(player["x"], player["y"], player["width"], player["height"])

    # Call the next frame
    window.requestAnimationFrame(game_loop)

# Start the game loop
window.requestAnimationFrame(game_loop)
