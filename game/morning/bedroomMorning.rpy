image bedroomMorningImage = "images/bedRoomMorning.jpg"
image videoGameImage = "images/gameConsole.png"

init python:
    wake_up = True
    cat_happy = False

label showCat:
    if cat_happy:
        show cat happy at center: 
            zoom 0.025
    else:
        show cat normal at center: 
            zoom 0.025
    return

menu actionsBedroomMorning:
    "Ir para o corredor":
        jump corridorMorning
    "Fazer carinho no gato":
        "%(player_name)s faz carinho no gato"
        cat "purrr"

        $cat_happy = True
        call showCat
        "%(cat_name)s ficou feliz"
        jump actionsBedroomMorning

    "Ler um livro":
        player "Nope. Tenho 10 anos, não vou ler! Vou jogar videogame."
        show videoGameImage at truecenter
        "%(player_name)s jogou videogame por alguns minutos"
        hide videoGameImage
        jump actionsBedroomMorning

    "Dormir":# if(visited_bathroom and visited_kitchen and visited_livingroom and visited_parents_bedroom):
        return

label bedroomMorning:
    $cat_happy = False

    scene bedroomMorningImage at center:
        zoom 0.19

    if wake_up:
        player normal "Ah que preguiça!"
    call showCat

    show player at right:
        xalign 0.7
        zoom 0.05
    with pixellate

    if wake_up:
        player happy "Já está de manhã"
        $wake_up = False

    jump actionsBedroomMorning

