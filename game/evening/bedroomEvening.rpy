image bedroomEveningImage = "images/bedroomEvening.jpg"

label bedroomEvening:
    scene bedroomEveningImage at center:
        zoom 0.19
    with zoomin

    show player normal at right:
        xalign 0.7
        zoom 0.05

    player normal "Cadê o meu gato?"
    player normal "Esse quarto está muito estranho!"
    player normal "Eu quero meu pai!"

    menu actionsBedroomEvening:
        "Ir para o corredor":
            jump corridorEvening

