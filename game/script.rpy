init python:
    player_name = "Asha Tenebris"

define player = Character(player_name)

image elaineNormal = "images/elaineNormal.png"
image bedRoomMorning = "images/bedRoomMorning.jpg"

label start:
    "Begin Game"
    
    call wakeUpMorning

    "End Game"
    return
