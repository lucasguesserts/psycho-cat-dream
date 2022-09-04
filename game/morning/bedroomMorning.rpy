image bedroomMorningImage = "images/bedRoomMorning.jpg"

menu actionsBedroomMorning:
    "Ir para o corredor":
        jump corridorMorning
    "Fazer carinho no gato":
        "%(player_name)s faz carinho no gato"
        cat "purrr"
        jump actionsBedroomMorning
    "Ler um livro":
        player "Nope. Tenho 10 anos, não vou ler! Vou jogar videogame."
        "%(player_name)s jogou videogame por alguns minutos"
        jump actionsBedroomMorning
    "Dormir" if(visited_bathroom and visited_kitchen and visited_livingroom and visited_parents_bedroom):
        "%(player_name)s dormiu por várias horas"
        return


label bedroomMorning:
    scene bedroomMorningImage at center:
        zoom 0.19
    with zoomin

    player normal "Ah que preguiça!"
    
    show player at right:
        xalign 0.7
        zoom 0.05

    show cat normal at center: 
            zoom 0.025

    with pixellate

    player happy "Já está de manhã"

    jump actionsBedroomMorning

