image bathroomMorningImage = Image("images/bathroomMorning.jpg")

menu actionsBathroomMorning:
    "Ir para o corredor":
        call audioOpenDoorMorning
        jump corridorMorning
    
    "Tomar banho":
        player normal "Já tomei banho semana passada"
        jump actionsBathroomMorning
    
    "Pesar-se":
        "balança" "%(player_weight)d Kg"
        if has_eaten_cookies:
            $ has_checked_her_weight_after_getting_heavier = True
        jump actionsBathroomMorning

label bathroomMorning:
    $ visited_bathroom = True

    scene bathroomMorningImage

    "%(player_name)s entrou no banheiro"

    jump actionsBathroomMorning
