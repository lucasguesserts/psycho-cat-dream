image corridorMorningImage = Image("images/corridorMorning.png")
image corridorMorningBrokenImage = Image("images/corridorMorningBroken.png")

init python:
    running_at_corridor = False
    running_at_corridor_second_time = False

menu actionsCorridorMorning:
    "Correr" if not running_at_corridor:
        $ running_at_corridor = True
        "%(player_name)s corre no corredor"
        father angry "Não corra no corredor!"
        jump actionsCorridorMorning

    "Correr" if running_at_corridor and not running_at_corridor_second_time:
        $ running_at_corridor_second_time = True
        $ vase_is_broken = True
        scene corridorMorningBrokenImage
        call audioVase
        "%(player_name)s quebrou um vaso de R$100.000,00"
        player sad "Meus deus, o papai vai me matar!"
        jump actionsCorridorMorning

    "Banheiro":
        call audioOpenDoorMorning
        jump bathroomMorning
    
    "Quarto":
        call audioOpenDoorMorning
        jump bedroomMorning

    "Quarto dos pais":
        call audioOpenDoorMorning
        jump parentsBedroomMorning
    
    "Sala":
        call audioOpenDoorMorning
        jump livingRoomMorning

label corridorMorning:
    if not vase_is_broken:
        scene corridorMorningImage
        with pixellate
    else:
        scene corridorMorningBrokenImage
        with pixellate
        
    "E então %(player_name)s entrou no corredor"

    jump actionsCorridorMorning