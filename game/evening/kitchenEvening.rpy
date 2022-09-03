
image kitchenEveningImage = Image("images/kitchenEvening.jpg")

label kitchenEvening:
    "%(player_name)s entrou na cozinha"

    scene kitchenEveningImage at center:
        zoom 0.19

    menu actionsKitchenEvening:
        "Roubar biscoitos no armário":
            "Não há mais nenhum biscoito"
            jump actionsKitchenEvening

        "Ir para o corredor":
            jump corridorEvening