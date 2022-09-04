image tvUnsynced = "images/unsyncedTV.png"
image tvGamutoImage = "images/GamutoTV.png"
image tvCookieMonsterImage = "images/CookieMonsterTV.png"

init python:
    channel_watched = [False for i in range(8)]
    see_gamuto = False
    see_unsynced = False

menu actionTvChannels:
    "Parar de assistir televisão":
        player sad "Acho que já vi TV demais por hoje..."
        $ has_watched_all_channels_in_the_evening = all(channel_watched)
        jump livingRoomEvening
    "Channel 0":
        $ channel_watched[0] = True
        jump televisionEvening
    "Channel 1":
        $ channel_watched[1] = True
        jump televisionEvening
    "Channel 2":
        $ channel_watched[2] = True
        jump televisionGamuto
    "Channel 3":
        $ channel_watched[4] = True
        jump televisionGamuto
    "Channel 4" if not channel_watched[3]:
        $ channel_watched[3] = True
        jump televisionCookieMonster
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
    scene tvUnsynced at center
    with pixellate
    if not see_unsynced:
        player sad "Talvez seja melhor eu assistir a todos os canais para ver se descubro o que está acontecendo..."
        $see_unsynced = True
    else:
        player sad "Não está funcionando também"
    jump actionTvChannels

label televisionGamuto:
    scene tvGamutoImage at center
    with pixellate
    if not see_gamuto:
        player sad "Quem é esse bicho estranho?"
        $see_gamuto = True
    else:
        player sad "Está em todos os canais?!"
    jump actionTvChannels

label televisionCookieMonster:
    # TODO: jumpscare
    "TÁ FALTANDO UM JUMP SCARE AQUI!!!!"
    scene tvCookieMonsterImage at center
    with pixellate
    player scare "aaaahhh!"
    jump actionTvChannels

