image bathroomMorning = Image("images/bathroomMorning.jpg")

label bathroomMorningTime:
    "E então %(player_name)s entrou no banheiro"

    scene bathroomMorning

    menu sairBanheiro:
        "corredor":
            call corridorMorningTime