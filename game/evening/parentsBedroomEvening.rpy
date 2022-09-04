image parentsBedroomEveningImage = Image("parentsBedroomEvening.jpg")
image darkRoomImage = Image("darkRoom.jpg")

label parentsBedroomEvening:
    scene parentsBedroomEveningImage:
        zoom 0.68
    with pixellate
    call courageousEndingMechanics
    call fathersDeathPrologue
    call fathersDeath
    call fathersDeathPost
    if is_courageus_enough:
        call parentsBedroomEveningCourageousEnding
        return
    else:
        call parentsBedroomEveningNotCourageousEnding
        call start
        return

label courageousEndingMechanics:
    $ is_courageus_enough = True
    $ is_courageus_enough = is_courageus_enough and has_eaten_the_apple_in_the_kitchen_in_the_morning
    $ is_courageus_enough = is_courageus_enough and has_eaten_cookies
    $ is_courageus_enough = is_courageus_enough and has_checked_her_weight_after_getting_heavier
    $ is_courageus_enough = is_courageus_enough and has_checked_her_weight_in_the_evening
    $ is_courageus_enough = is_courageus_enough and has_seen_herself_on_the_mirror_in_the_evening
    $ is_courageus_enough = is_courageus_enough and has_watched_all_channels_in_the_evening
    return

label fathersDeathPrologue:
    show cat normal at center:
        xalign 0.5
        yalign 0.6
        zoom 0.025
    show father angry:
        xalign 0.8
        yalign 0.7
        zoom 0.04
    player scare "Papai, estou com medo!"
    return

label fathersDeath:
    scene darkRoomImage
    with Fade(0.0, 0.0, 0.0)
    hide cat
    hide father
    "As luzes se apagaram"
    return

label fathersDeathPost:
    scene parentsBedroomEveningImage:
        zoom 0.68
    with Fade(0.0, 0.0, 2.0)
    show cat evil at center:
        xalign 0.5
        yalign 0.6
        zoom 0.025
    "O pai de %(player_name)s está morto"
    player scare "Papai!"
    player scare "PAPAI!!!!!"
    return

label parentsBedroomEveningNotCourageousEnding:
    player scare "O... Gato..."
    scene darkRoomImage
    with Fade(0.1, 0.0, 0.1, color="#700")
    "..."
    return

label parentsBedroomEveningCourageousEnding:
    player scare "O... Gato..."
    player scare "Eu..."
    player scare "Eu!"
    player scare "TEREI MINHA VINGANÇA!!!"
    $ killingCatDelay = 0.1
    scene darkRoomImage
    with Fade(killingCatDelay, 0.0, killingCatDelay, color="#700")
    scene darkRoomImage
    with Fade(killingCatDelay, 0.0, killingCatDelay, color="#700")
    scene parentsBedroomEveningImage:
        zoom 0.68
    with Fade(killingCatDelay, 0.0, killingCatDelay, color="#700")
    player scare "O que foi..."
    player scare "... que ..."
    player scare "... eu ..."
    player scare "... fiz ..."
    player scare "..."
    player scare "Eu não posso viver comigo mesmo assim!"
    player scare "..."
    scene darkRoomImage
    with Fade(0.4, 0.0, 0.4, color="#000")
    return