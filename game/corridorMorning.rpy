image corridorMorning = Image("images/corridorMorning.jpg")

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
            call parentsBedroomMorning
        
        "Sala":
            "In development"
            jump actionsCorridorMorning
        