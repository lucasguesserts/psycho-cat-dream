image corridorEveningImage = Image("images/corridorEvening.jpg")

menu actionsCorridorEvening:
    "Sala":
        "Under development"
        # jump kitchenEvening
    "Quarto dos pais":
        "Under development"
        # jump bathroomEvening
    "Quarto":
        "Under development"
        # jump livingRoomEvening
    "Banheiro":
        "Under development"
        # jump bedroomEvening
    "Quarto dos pais" if has_watched_tv_in_the_evening:
        "Under development"
        # jump parentsBedroomEvening

label corridorEvening:
    scene corridorEveningImage:
        zoom 2

    if vase_is_broken:
        player normal "Eu não acredito!"
        player normal "Vaso estava quebrado!"
        player normal "Agora ele está inteiro"
        player normal "O que será que está acontecendo?"

    jump actionsCorridorEvening