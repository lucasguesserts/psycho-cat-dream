image bedroomEveningImage = "images/bedroomEvening.jpg"

menu actionsBedroomEvening:
    "Ir para o corredor":
        if wake_up:
            $wake_up = False
            call audioOpenDoorEvening
            jump bathroomEvening
        else:
            call audioOpenDoorEvening
            jump corridorEvening

label bedroomEvening:

    if wake_up:
        scene bedroomEveningImage at center:
            zoom 0.19
        with pixellate
        call nightmare
        call audioBackgroundEvening
        "%(player_name)s dormiu por várias horas"
    else:
        scene bedroomEveningImage at center:
            zoom 0.19
        "%(player_name)s entrou no quarto"

    show player normal at right:
        xalign 0.7
        zoom 0.05
    with pixellate
    
    if wake_up:
        player scare "Que pesadelo terrível!?!"
        player normal "Cadê o meu gato?"
        player scare "Esse quarto está muito estranho!"
        player scare "Eu quero meu pai!"
    else:
        player scare "Meu deus, como vim parar no meu quarto? Eu queria ir pro banheiro!"
                
    jump actionsBedroomEvening