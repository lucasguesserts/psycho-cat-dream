image bathroomMorningImage = Image("images/bathroomMorning.jpg")

menu actionsBathroomMorning:
    "Ir para o corredor":
        jump corridorMorning
    
    "Tomar banho":
        player normal "Já tomei banho semana passada"
        jump actionsBathroomMorning
    
    "Pesar-se":
        "balança" "%(player_weight)d Kg"
        jump actionsBathroomMorning

label bathroomMorning:
    $ visited_bathroom = True

    scene bathroomMorningImage

    "%(player_name)s entrou no banheiro"

    jump actionsBathroomMorning
