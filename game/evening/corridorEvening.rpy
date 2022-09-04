image corridorEveningImage = Image("images/corridorEvening.png")

init python:
    first_time_in_corridor_evening = True

menu actionsCorridorEvening:
    "Sala":
        call audioOpenDoorEvening
        jump kitchenEvening
    "Quarto dos pais":
        if has_watched_tv_in_the_evening:
            call audioOpenDoorEvening
            jump parentsBedroomEvening
        else:
            call audioOpenDoorEvening
            jump bathroomEvening
    "Quarto":
        call audioOpenDoorEvening
        jump livingRoomEvening
    "Banheiro":
        call audioOpenDoorEvening
        jump bedroomEvening

label corridorEvening:
    scene corridorEveningImage at center:
        zoom 0.625
    with pixellate
    
    "%(player_name)s entrou no corredor"

    if vase_is_broken and first_time_in_corridor_evening:
        player normal "Eu não acredito!"
        player normal "Vaso estava quebrado!"
        player normal "Agora ele está inteiro"
        player normal "O que será que está acontecendo?"

    $ first_time_in_corridor_evening = False

    jump actionsCorridorEvening