init python:
    player_name = "Asha Tenebris"
    player_weight = 30

define player = Character(player_name, image = "player")

image player normal = "images/player.png"
image side player normal = im.Scale("images/playerPicture.png", 250, 250)
#add SideImage() #xalign 0.0 yalign 1.0 yoffset 50

label start:
    "Begin Game"
    
    call wakeUpMorning

    "End Game"
    return
