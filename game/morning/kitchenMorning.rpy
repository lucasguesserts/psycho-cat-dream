image kitchenMorningImage = "images/kitchenMorning.jpg"

init python:
    cookies_eaten = 0;

menu actionsKitchenMorning:
    "Comer maçã":
        player "A maçã sumiu!"
        jump actionsKitchenMorning

    "Roubar biscoitos no armário":
        player "que delícia!"
        $ player_weight += 2**cookies_eaten
        $ cookies_eaten += 1
        jump actionsKitchenMorning

    "Ir para a sala":
        jump livingRoomMorning

label kitchenMorning:
    $visited_kitchen = True

    scene kitchenMorningImage at center:
        zoom 0.19
    with pixellate

    "%(player_name)s entrou na cozinha"

    player normal "Que fome!"
    
    jump actionsKitchenMorning

