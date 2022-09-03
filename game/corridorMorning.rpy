image corridorMorning = Image("images/corridorMorning.jpg")

label corridorMorningTime:
    "E então %(player_name)s entrou no corredor"

    scene corridorMorning:
        zoom 2

    menu actionsCorridorMorning:
        "Banheiro":
            jump bathroomMorning
        
        "Quarto":
            jump bedroomMorning


        "Quarto dos pais":
            jump parentsBedroomMorning
        
        "Sala":
            "In development"
            jump actionsCorridorMorning
        