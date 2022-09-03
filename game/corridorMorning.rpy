image corridorMorningImage = Image("images/corridorMorning.jpg")

label corridorMorning:
    "E então %(player_name)s entrou no corredor"

    scene corridorMorningImage:
        zoom 2

    menu actionsCorridorMorning:
        "Banheiro":
            jump bathroomMorning
        
        "Quarto":
            jump bedroomMorning


        "Quarto dos pais":
            jump parentsBedroomMorning
        
        "Sala":
            jump livingRoomMorning
        