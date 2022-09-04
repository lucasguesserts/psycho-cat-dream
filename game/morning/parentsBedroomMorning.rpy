image parentsBedroomMorningImage = "images/parentsBedroomMorning.jpg"

label parentsBedroomMorning:
    $visited_parents_bedroom = True

    scene parentsBedroomMorningImage at center
    with zoomin
    
    show father angry:
        xalign 0.8
        yalign 0.7
        zoom 0.04

    with pixellate

    father angry "Aqui não é o seu quarto."
    father angry "Vá brincar em outro local."

    jump corridorMorning
