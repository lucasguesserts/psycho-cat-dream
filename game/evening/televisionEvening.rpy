image tvEveningImage = "images/TVevening.png"
image tvGamutoImage = "images/tvGamuto.png"
image tvCookieMonsterImage = "images/tvCookieMonster.png"

init python:
    channel_watched = [False for i in range(8)]

menu actionTvChannels:
    "Parar de assistir televisão":
        player sad "Acho que já vi TV demais por hoje..."
        $ has_watched_all_channels_in_the_evening = all(channel_watched)
        jump livingRoomEvening
    "Channel 0":
        $ channel_watched[0] = True
        player sad "Quem é esse bicho estranho?"
        jump televisionGamuto
    "Channel 1":
        $ channel_watched[1] = True
        jump televisionGamuto
    "Channel 2":
        $ channel_watched[2] = True
        player sad "Está em todos os canais?!"
        jump televisionGamuto
    "Channel 3" if not channel_watched[3]:
        $ channel_watched[3] = True
        jump televisionCookieMonster
    "Channel 4":
        $ channel_watched[4] = True
        jump televisionGamuto
    "Channel 5":
        $ channel_watched[5] = True
        jump televisionGamuto
    "Channel 6":
        $ channel_watched[6] = True
        jump televisionGamuto
    "Channel 7":
        $ channel_watched[7] = True
        jump televisionGamuto

label televisionEvening:
    scene tvEveningImage at center:
        zoom 1.3
    with pixellate
    player sad "Talvez seja melhor eu assistir a todos os canais para ver se descubro o que está acontecendo..."
    jump actionTvChannels

label televisionGamuto:
    scene tvGamutoImage at center:
        zoom 1.3
    with pixellate
    jump actionTvChannels

label televisionCookieMonster:
    # TODO: jumpscare
    "TÁ FALTANDO UM JUMP SCARE AQUI!!!!"
    scene tvCookieMonsterImage at center:
        zoom 1.3
    with pixellate
    player scare "aaaahhh!"
    jump actionTvChannels

