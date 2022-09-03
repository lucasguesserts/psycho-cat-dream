image bathroomMorning = Image("images/bathroomMorning.jpg")

init python:
    player_name = "Asha Tenebris"

define player = Character(player_name)

label bathroomMorningTime:
    "E então %(player_name)s entrou no banheiro"

    scene bathroomMorning

    menu sairBanheiro:
        "corredor":
            call corridorMorningTime