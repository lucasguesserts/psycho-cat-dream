menu changeRoomBedRoom:
    "Ir para o Banheiro":
        player "Preciso fazer xixi"
        call corridorMorningTime
        return
    "Ir para a cozinha":
        player "Estou morta de fome"
        return

label wakeUpMorning:
    scene bedRoomMorning at center:
        zoom 0.19
    with zoomin

    player "Ah que preguiça!"
    
    show elaineNormal at right:
        xalign 0.7
    with pixellate

    player "Já está de manhã"

    call changeRoomBedRoom

    return
