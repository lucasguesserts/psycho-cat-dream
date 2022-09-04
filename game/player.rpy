init python:
    player_name = "Asha Tenebris"
    player_weight = 30
    player_courage = 0 #Coragem é utilizada para matar o gato. 100 pontos são necessários para vencer

define player = Character(player_name, image = "player")

image player normal = "images/player.png"
image player happy = "images/player.png"
image player sad = "images/player.png"
image player scare = "images/player.png"

image side player normal = im.Scale("images/playerPicture.png", 250, 250)
image side player happy = im.Scale("images/playerHappyPicture.png", 250, 250)
image side player sad = im.Scale("images/playerSadPicture.png", 250, 250)
image side player scare = im.Scale("images/playerScarePicture.png", 250, 250)

