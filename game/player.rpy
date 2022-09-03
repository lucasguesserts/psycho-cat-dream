init python:
    player_name = "Asha Tenebris"
    player_weight = 30
    player_courage = 0 #Coragem é utilizada para matar o gato. 100 pontos são necessários para vencer

define player = Character(player_name, image = "player")

image player normal = "images/player.png"
image side player normal = im.Scale("images/playerPicture.png", 250, 250)

image playerImage = "images/player.png"
