image bedroomMorningImage = "images/bedRoomMorning.jpg"

menu actionsBedroomMorning:
    "Ir para o Banheiro":
        player "Preciso fazer xixi"
        jump corridorMorning
    "Ir para a cozinha":
        player "Estou morta de fome"
        jump kitchenMorning

label bedroomMorning:
    scene bedroomMorningImage at center:
        zoom 0.19
    with zoomin

    player "Ah que preguiça!"
    
    show playerNormal at right:
        xalign 0.7
        zoom 0.05

    with pixellate

    player "Já está de manhã"

    jump actionsBedroomMorning
