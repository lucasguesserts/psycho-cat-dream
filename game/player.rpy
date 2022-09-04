init python:
    player_name = "Asha Tenebris"

define player = Character(player_name, image = "player", color="#ededed")

image player normal = "images/player.png"
image player happy = "images/player.png"
image player sad = "images/player.png"
image player scare = "images/player.png"

image side player normal = im.Scale("images/playerPicture.png", 250, 250)
image side player happy = im.Scale("images/playerHappyPicture.png", 250, 250)
image side player sad = im.Scale("images/playerSadPicture.png", 250, 250)
image side player scare = im.Scale("images/playerScarePicture.png", 250, 250)

