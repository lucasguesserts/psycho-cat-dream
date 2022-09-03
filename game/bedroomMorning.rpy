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
    "Fazer carinho no gato":
        "%(player_name)s faz carinho no gato"
        jump actionsBedroomMorning
    "Ler um livro":
        player "Nope, Tenho 10 anos, não vou ler! Vou jogar videogame."
        "%(player_name)s jogou videogame por alguns minutos"
        jump actionsBedroomMorning

label wakeUpMorning:
    scene bedroomMorning at center:
        zoom 0.19
    with zoomin

    player "Ah que preguiça!"
    
    show playerNormal at right:
        xalign 0.7
        zoom 0.05

    with pixellate

    player "Já está de manhã"

    call actionsBedroomMorning

    return

label bedroomMorningTime:
    scene bedroomMorning at center:
        zoom 0.19

    "De volta ao quarto..."

    call actionsBedroomMorning