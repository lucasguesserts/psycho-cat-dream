image parentsBedroomEveningImage = Image("parentsBedroomEvening.jpg")
image darkRoomImage = Image("darkRoom.jpg")

menu actionsParentsBedroomEvening:
    "Fugir":
        "%(player_name)s está paralizada de medo"
        jump actionsParentsBedroomEvening

label parentsBedroomEvening:
    scene parentsBedroomEveningImage:
        zoom 0.68
    with zoomin

    show cat normal at center:
        zoom 0.025

    show father angry:
        xalign 0.8
        yalign 0.7
        zoom 0.04
    with pixellate

    player normal "Papai, estou com medo!"

    scene darkRoomImage

    hide cat normal
    hide father
    "As luzes se apagaram"

    scene parentsBedroomEveningImage:
        zoom 0.68
    with pixellate

    hide darkRoomImage
    
    show fatherEveningDeadImage:
        xalign 0.8
        yalign 0.7
        zoom 0.4
    
    "o pai de %(player_name)s está morto"

    jump actionsParentsBedroomEvening