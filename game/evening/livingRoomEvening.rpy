image livingRoomEveningImage = "images/livingRoomEvening.jpg"

menu actionsLivingRoomEvening:
    "Assistir TV" if not has_watched_tv_in_the_evening:
        $ has_watched_tv_in_the_evening = True
        jump televisionEvening
    "Ir para corredor":
        if has_watched_tv_in_the_evening:
            jump corridorEvening
        else:
            "A porta está trancada"
            jump actionsLivingRoomEvening

label livingRoomEvening:
    scene livingRoomEveningImage at center:
        zoom 0.28
    jump actionsLivingRoomEvening
