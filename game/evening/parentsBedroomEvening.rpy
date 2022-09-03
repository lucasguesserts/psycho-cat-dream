image parentsBedroomEveningImage = Image("parentsBedroomEvening.jpg")
image darkRoomImage = Image("darkRoom.jpg")

menu actionsParentsBedroomEvening:
    "Fugir":
        "%(player_name)s está paralizada de medo"
        jump actionsParentsBedroomEvening

label parentsBedroomEvening:
    scene parentsBedroomEveningImage

    show catImage at center:
        zoom 0.025

    show fatherMorningImage:
        xalign 0.8
        yalign 0.7
        zoom 0.4

    player normal "Papai, estou com medo!"

    scene darkRoomImage

    hide catImage
    hide fatherMorningImage
    "As luzes se apagaram"

    scene parentsBedroomEveningImage
    hide darkRoomImage
    
    show fatherEveningDeadImage:
        xalign 0.8
        yalign 0.7
        zoom 0.4
    
    "o pai de %(player_name)s está morto"

    jump actionsParentsBedroomEvening