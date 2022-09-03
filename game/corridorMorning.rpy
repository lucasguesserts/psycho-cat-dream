image corridorMorning = Image("images/corridorMorning.jpg")

label corridorMorningTime:
    "E então %(player_name)s entrou no corredor"

    scene corridorMorning:
        zoom 2

    menu sairCorredor:
        "Banheiro":
            call bathroomMorningTime
            return
        
        "Quarto":
            call wakeUpMorning

        "Quarto dos pais":
            "In development"
            jump sairCorredor
        
        "Sala":
            "In development"
            jump sairCorredor
        