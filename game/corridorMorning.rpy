image corridorMorning = Image("images/corridorMorning.jpg")

init python:
    running_at_corridor = True

label corridorMorningTime:
    "E então %(player_name)s entrou no corredor"

    scene corridorMorning:
        zoom 2

    menu actionsCorridorMorning:
        "Banheiro":
            call bathroomMorningTime
            return
        
        "Quarto":
            call wakeUpMorning

        "Quarto dos pais":
            "In development"
            jump actionsCorridorMorning
        
        "Sala":
            jump LivingRoomMorning
        