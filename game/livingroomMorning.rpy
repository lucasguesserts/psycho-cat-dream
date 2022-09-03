image livingMorningImage = "images/livingroomMorning.jpg"
image TV = "images/TV.png"

init python:
    running_at_livingroom = False
    in_livingroom = False

menu actionsLivingroomMorning:
    "Correr na Sala" if running_at_corridor and not running_at_livingroom:
        "%(player_name)s brincou de correr em volta do sofá"
        "%(player_name)s ficou entediada"
        $running_at_livingroom = True
        jump actionsLivingroomMorning
    "Assistir TV":
        player "Quero ver um desenho"
        hide livingMorningImage
        scene TV at center:
            zoom 1.3
        with pixellate
        player "Mãe, a TV não ta funcionando!!"
        hide TV
        jump LivingRoomMorning
    "Ir para corredor":
        jump corridorMorningTime

label LivingRoomMorning:
    if not in_livingroom:
        scene livingMorningImage at center:
            zoom 0.28
        with zoomin
        show playerNormal at right:
            xalign 0.7
            zoom 0.05
        with pixellate

        "%(player_name)s entrou na sala"
        $in_livingroom = True
    else:
        scene livingMorningImage at center:
            zoom 0.28
    
        show playerNormal at right:
            xalign 0.7
            zoom 0.05

    call actionsLivingroomMorning

    return
