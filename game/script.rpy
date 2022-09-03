init python:
    player_name = "Asha Tenebris"
    cat_name = "Bartolomeu"
    player_weight = 30
    visited_bathroom = False
    visited_kitchen = False
    visited_parents_bedroom = False
    visited_livingroom = False

define player = Character(player_name)
define cat = Character(cat_name)

image playerNormal = "images/player.png"
image cat = "images/cat.png"

label start:
    "Begin Game"
    
    call morning

    "End Game"
    return
