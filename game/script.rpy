init python:
    visited_bathroom = False
    visited_kitchen = False
    visited_parents_bedroom = False
    visited_livingroom = False
    player_name = "Asha Tenebris"
    player_weight = 30

define player = Character(player_name, image = "player")

image player normal = "images/player.png"
image side player normal = im.Scale("images/playerPicture.png", 250, 250)

label start:
    "Begin Game"
    
    call morning

    "End Game"
    return
