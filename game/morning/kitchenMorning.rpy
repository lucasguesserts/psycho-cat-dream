image kitchenMorningImage = "images/kitchenMorning.jpg"

init python:
    cookies_eaten = 0;

menu actionsKitchenMorning:
    "Comer maçã":
        player "A maçã sumiu!"
        $ has_eaten_the_apple_in_the_kitchen_in_the_morning = True
        jump actionsKitchenMorning

    "Roubar biscoitos no armário":
        player "Que delícia!"
        player "Mas eu tô me sentindo mais pesada..."
        $ has_eaten_cookies = True
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

