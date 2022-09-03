init python:
    player_name = "Asha Tenebris"
    player_weight = 30
    visited_bathroom = False
    visited_kitchen = False
    visited_parents_room = False
    visited_livingroom = False

define player = Character(player_name)

image playerNormal = "images/player.png"

label start:
    "Begin Game"
    
    call wakeUpMorning

    "End Game"
    return
