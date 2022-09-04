image livingroomEveningImage = "images/livingRoomEvening.png"

menu actionsLivingRoomEvening:
    "Assistir TV" if not has_watched_tv_in_the_evening:
        player normal "A televisão está estranha..."
        $ has_watched_tv_in_the_evening = True
        $ is_watching_tv_in_the_evening = True
        jump televisionEvening
    "Ir para corredor":
        if has_watched_tv_in_the_evening:
            call audioOpenDoorEvening
            jump corridorEvening
        else:
            "A porta está trancada"
            jump actionsLivingRoomEvening

label livingRoomEvening:
    scene livingroomEveningImage at center
    if(is_watching_tv_in_the_evening):
        $is_watching_tv_in_the_evening = False
    else:
        "%(player_name)s entrou na sala"
    jump actionsLivingRoomEvening
