image livingroomMorningImage = "images/livingroomMorning.png"
image TV = "images/TV.png"

init python:
    running_at_livingroom = False
    in_livingroom = False

menu actionsLivingroomMorning:
    "Correr na Sala" if running_at_corridor and not running_at_livingroom:
        "%(player_name)s brincou de correr em volta do sofá"
        player "Estou entediada"
        $running_at_livingroom = True
        jump actionsLivingroomMorning
    "Assistir TV":
        player normal "Quero ver um desenho"
        hide player
        hide livingroomMorningImage
        
        scene TV at center:
            zoom 1.3

        player normal "Mãe, a TV não ta funcionando!!"
        hide TV
        with pixellate

        jump livingRoomMorning
    "Ir para corredor":
        $in_livingroom = False
        call audioOpenDoorMorning
        jump corridorMorning
    "Ir para Cozinha":
        $in_livingroom = False
        call audioOpenDoorMorning
        jump kitchenMorning

label livingRoomMorning:
    $visited_livingroom = True

    if not in_livingroom:
        scene livingroomMorningImage at center
        with zoomin
        "%(player_name)s entrou na sala"

        $in_livingroom = True
    else:
        scene livingroomMorningImage at center
    
        show player normal at right:
            xalign 0.7
            zoom 0.05

    jump actionsLivingroomMorning
