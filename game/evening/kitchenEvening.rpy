
image kitchenEveningImage = Image("images/kitchenEvening.png")

init python:
    tried_to_steal_cookie = False

menu actionsKitchenEvening:
    "Roubar biscoitos no armário":
        if(not tried_to_steal_cookie):
            player normal "Que estranho! O jarro está vazio..."
            $tried_to_steal_cookie = True
        player normal "Podia jurar que os biscoitos não tinham acabado"
        jump actionsKitchenEvening

    "Ir para o corredor":
        call audioOpenDoorEvening
        jump corridorEvening

label kitchenEvening:
    scene kitchenEveningImage at center:
        zoom 0.72
    with pixellate

    "%(player_name)s entrou na cozinha"

    jump actionsKitchenEvening