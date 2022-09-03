image livingRoomMorningImage = Image("images/livingRoomMorning.jpg")

menu actionsLivingRoomMorning:
    "Ir para o corredor":
        jump corridorMorning
    
    "Ir para a cozinha":
        jump kitchenMorning

    "Assistir TV":
        player "O desenho estava muito legal"
        jump actionsLivingRoomMorning

label livingRoomMorning:
    $visited_livingroom = True

    "E então %(player_name)s entrou na sala"

    scene livingRoomMorningImage at center:
        zoom 2
    with zoomin

    jump actionsLivingRoomMorning
