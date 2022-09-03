image corridorEveningImage = Image("images/corridorEvening.png")

init python:
    first_time_in_corridor_evening = True

menu actionsCorridorEvening:
    "Sala":
        jump kitchenEvening
    "Quarto dos pais":
        if has_watched_tv_in_the_evening:
            jump parentsBedroomEvening
        else:
            jump bathroomEvening
    "Quarto":
        jump livingRoomEvening
    "Banheiro":
        jump bedroomEvening

label corridorEvening:
    scene corridorEveningImage:
        zoom 2

    if vase_is_broken and first_time_in_corridor_evening:
        player normal "Eu não acredito!"
        player normal "Vaso estava quebrado!"
        player normal "Agora ele está inteiro"
        player normal "O que será que está acontecendo?"

    $ first_time_in_corridor_evening = False

    jump actionsCorridorEvening