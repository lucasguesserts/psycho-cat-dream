image bathroomMorningImage = Image("images/bathroomMorning.jpg")

menu actionsBathroomMorning:
    "Ir para o corredor":
        jump corridorMorningTime
    
    "Tomar banho":
        player "Já tomei banho semana passada"
        jump actionsBathroomMorning
    
    "Pesar-se":
        "balança" "%(player_weight)d Kg"
        jump actionsBathroomMorning

label bathroomMorning:
    "E então %(player_name)s entrou no banheiro"

    scene bathroomMorningImage

    jump actionsBathroomMorning
