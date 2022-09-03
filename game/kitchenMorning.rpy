image kitchenMorning = "images/kitchenMorning.jpg"

init python:
    cookies_eaten = 0;

label kitchenMorningTime:
    scene kitchenMorning at center:
        zoom 0.19
    with pixellate

    player "Que fome!"

    menu actionsKitchenMorning:
        "Comer maçã":
            "A maçã sumiu!"
            jump actionsKitchenMorning

        "Roubar biscoitos no armário":
            player "que delícia!"
            $ player_weight += 2**cookies_eaten
            $ cookies_eaten += 1
            jump actionsKitchenMorning

        "Ir para o quarto":
            call bedroomMorningTime

    return