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

    player normal "Ah que preguiça!"
    
    show player normal at right:
        xalign 0.7
        zoom 0.05

    with pixellate

    player "Já está de manhã"

    call actionsBedroomMorning

    return
