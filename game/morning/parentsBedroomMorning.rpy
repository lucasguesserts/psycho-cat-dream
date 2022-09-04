image parentsBedroomMorningImage = "images/parentsBedroomMorning.jpg"

label parentsBedroomMorning:
    $visited_parents_bedroom = True

    scene parentsBedroomMorningImage at center:
        zoom 0.68
    with zoomin
    
    show father angry:
        xalign 0.8
        yalign 0.7
        zoom 0.04

    with pixellate


    "%(player_name)s entrou no quarto dos pais"

    father angry "Aqui não é o seu quarto."
    father angry "Vá brincar em outro local."
    player sad "Ta bom, papai."

    call audioOpenDoorMorning
    jump corridorMorning
