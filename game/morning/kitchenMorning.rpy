image kitchenMorningImage = "images/kitchenMorning.png"

menu actionsKitchenMorning:
    "Comer maçã":
        player "A maçã sumiu!"
        $ has_eaten_the_apple_in_the_kitchen_in_the_morning = True
        jump actionsKitchenMorning

    "Roubar biscoitos no armário":
        call audioCookie
        player happy "Que delícia!"
        stop sound
        player "Mas eu tô me sentindo mais pesada..."
        $ has_eaten_cookies = True
        $ player_weight += 2**cookies_eaten
        $ cookies_eaten += 1
        jump actionsKitchenMorning
        

    "Ir para a sala":
        call audioOpenDoorMorning
        jump livingRoomMorning

label kitchenMorning:
    $visited_kitchen = True

    scene kitchenMorningImage at truecenter:
        zoom 0.72
    with pixellate

    "%(player_name)s entrou na cozinha"

    player normal "Que fome!"
    
    jump actionsKitchenMorning

