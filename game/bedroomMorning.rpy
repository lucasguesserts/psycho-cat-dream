image bedroomMorning = "images/bedRoomMorning.jpg"

menu actionsBedroomMorning:
    "Ir para o Banheiro":
        player "Preciso fazer xixi"
        call corridorMorningTime
        return
    "Ir para a cozinha":
        player "Estou morta de fome"
        call kitchenMorningTime
        return

label wakeUpMorning:
    scene bedroomMorning at center:
        zoom 0.19
    with zoomin

    player "Ah que preguiça!"
    
    show playerNormal at right:
        xalign 0.7
    with pixellate

    player "Já está de manhã"

    call changeRoomBedroom

    return
