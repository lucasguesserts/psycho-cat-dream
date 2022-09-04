image bedroomMorningImage = "images/bedRoomMorning.png"
image videoGameImage = "images/gameConsole.png"

init python:
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
        call audioOpenDoorMorning
        jump corridorMorning
    "Fazer carinho no gato":
        "%(player_name)s faz carinho no gato"
        call audioPurr
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

    "Dormir" if(visited_bathroom and visited_kitchen and visited_livingroom and visited_parents_bedroom):
        $wake_up = True
        return

label bedroomMorning:
    $cat_happy = False

    call audioBackgroundMorning

    scene bedroomMorningImage at center:
        zoom 1.6
    with fade
    
    if wake_up:
        player normal "Ah que preguiça!"
        call showCat
        show player at right:
            xalign 0.7
            zoom 0.05
        with pixellate
    else:
        call showCat
        show player at right:
            xalign 0.7
            zoom 0.05
        with pixellate
        "%(player_name)s entrou no quarto"

    if wake_up:
        player happy "Já está de manhã"
        $wake_up = False

    jump actionsBedroomMorning

