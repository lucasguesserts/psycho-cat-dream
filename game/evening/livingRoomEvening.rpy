image livingroomEveningImage = "images/livingRoomEvening.png"
image livingroomTVEveningImage = "images/livingRoomTVEvening.png"

init python:
    TV_on = True

menu actionsLivingRoomEvening:
    "Assistir TV":
        player normal "A televisão está estranha..."
        $ has_watched_tv_in_the_evening = True
        $ is_watching_tv_in_the_evening = True
        jump televisionEvening
    "Ir para corredor":
        $TV_on = True
        stop sound
        if has_watched_tv_in_the_evening:
            call audioOpenDoorEvening
            jump corridorEvening
        else:
            "A porta está trancada"
            jump actionsLivingRoomEvening

label livingRoomEvening:
    if not TV_on:
        scene livingroomEveningImage at center
        with pixellate
    else:
        scene livingroomTVEveningImage at center
        with pixellate
        call audioStaticTV

    if(is_watching_tv_in_the_evening):
        $is_watching_tv_in_the_evening = False
    else:
        "%(player_name)s entrou na sala"
    jump actionsLivingRoomEvening
