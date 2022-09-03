image kitchenMorning = "images/kitchenMorning.jpg"

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
            $ player_weight += 1
            jump actionsKitchenMorning

        "Ir para o quarto":
            call wakeUpMorning

    return