image parentsBedroomMorningImage = "images/parentsBedroomMorning.jpg"

label parentsBedroomMorning:
    $visited_parents_bedroom = True

    scene parentsBedroomMorningImage at center
    with zoomin
    
    show fatherMorningImage:
        xalign 0.8
        yalign 0.7
        zoom 0.4

    with pixellate

    fatherMorning "Aqui não é o seu quarto."
    fatherMorning "Vá brincar em outro local."

    jump corridorMorning
