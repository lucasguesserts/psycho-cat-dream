menu changeRoomBedRoom:
    "Ir para o Banheiro":
        e "Preciso fazer xixi"
        call bathroomMorningTime
        return
    "Ir para a cozinha":
        e "Estou morta de fome"
        return

label wakeUpMorning:
    scene bedRoomMorning at center:
        zoom 0.19
    with zoomin

    e "Ah que preguiça!"
    
    show elaineNormal at right:
        xalign 0.7
    with pixellate

    e "Já está de manhã"

    call changeRoomBedRoom

    return
