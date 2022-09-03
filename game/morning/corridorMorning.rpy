image corridorMorningImage = Image("images/corridorMorning.jpg")

init python:
    running_at_corridor = False
    running_at_corridor_second_time = False

menu actionsCorridorMorning:
    "Correr" if not running_at_corridor:
        $ running_at_corridor = True
        "%(player_name)s corre no corredor"
        fatherMorning "Não corra no corredor!"
        jump actionsCorridorMorning

    "Correr" if running_at_corridor and not running_at_corridor_second_time:
        $ running_at_corridor_second_time = True
        $ vase_is_broken = True
        "%(player_name)s quebrou um vaso de R$100.000,00"
        jump actionsCorridorMorning

    "Banheiro":
        jump bathroomMorning
    
    "Quarto":
        jump bedroomMorning

    "Quarto dos pais":
        jump parentsBedroomMorning
    
    "Sala":
        jump livingRoomMorning

label corridorMorning:
    "E então %(player_name)s entrou no corredor"

    scene corridorMorningImage:
        zoom 2

    jump actionsCorridorMorning