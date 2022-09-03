init python:
    player_name = "Asha Tenebris"
    player_weight = 30

define player = Character(player_name)

image playerNormal = "images/elaineNormal.png"

label start:
    "Begin Game"
    
    call wakeUpMorning

    "End Game"
    return
