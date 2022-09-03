init python:
    player_name = "Asha Tenebris"

define player = Character(player_name)

image playerNormal = "images/elaineNormal.png"

label start:
    "Begin Game"
    
    call wakeUpMorning

    "End Game"
    return
