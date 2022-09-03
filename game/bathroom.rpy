image bathroomMorning = Image("images/bathroomMorning.jpg")

label bathroomMorningTime:
    "E então %(player_name)s entrou no banheiro"

    scene bathroomMorning

    menu actionsBathroomMorning:
        "Ir para o corredor":
            call corridorMorningTime
        
        "Tomar banho":
            player "Já tomei banho semana passada"
            jump actionsBathroomMorning
        
        "Pesar-se":
            "balança" "%(player_weight)d Kg"
            jump actionsBathroomMorning
    return
