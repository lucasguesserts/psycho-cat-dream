image livingMorningImage = "images/livingroomMorning.jpg"
image TV = "images/TV.png"

init python:
    running_at_livingroom = False
    in_livingroom = False

menu actionsLivingroomMorning:
    "Correr na Sala" if running_at_corridor and not running_at_livingroom:
        "%(player_name)s brincou de correr em volta do sofá"
        player normal "Estou entediada"
        $running_at_livingroom = True
        jump actionsLivingroomMorning
    "Assistir TV":
        player normal "Quero ver um desenho"
        hide livingMorningImage
        
        scene TV at center:
            zoom 1.3

        player normal "Mãe, a TV não ta funcionando!!"
        hide TV
        with pixellate

        jump livingRoomMorning
    "Ir para corredor":
        $in_livingroom = False
        jump corridorMorning
    "Ir para Cozinha":
        $in_livingroom = False
        jump kitchenMorning

label livingRoomMorning:
    $visited_livingroom = True

    if not in_livingroom:
        scene livingMorningImage at center:
            zoom 0.28
        with zoomin
        "%(player_name)s entrou na sala"

        $in_livingroom = True
    else:
        scene livingMorningImage at center:
            zoom 0.28

    jump actionsLivingroomMorning
