define audio.backgroundMorning = "<loop 0.0>audio/morningBackground.mp3"
define audio.backgroundEvening = "<loop 0.0>audio/eveningBackground.mp3"
define audio.doorOpeningEvening = "audio/doorOpeningEvening.mp3"
define audio.doorOpeningMorning = "audio/doorOpeningMorning.mp3"
define audio.staticTV = "audio/staticTVEvening.mp3"
define audio.audioNightmare = "audio/terror.mp3"
define audio.purr = "audio/catPurr.mp3"
define audio.cookie = "audio/cookieEating.mp3"
define audio.vase = "audio/breakingVase.mp3"
define audio.faucet = "audio/faucet.mp3"
define audio.running = "<from 2.0>audio/corridorRunning.mp3"


label audioOpenDoorMorning:
    play sound doorOpeningMorning
    return

label audioOpenDoorEvening:
    play sound doorOpeningEvening
    return

label audioBackgroundMorning:
    play music audio.backgroundMorning fadein 1.0
    return

label audioBackgroundEvening:
    play music backgroundEvening fadein 1.0
    return

label audioStaticTV:
    play loopinSFX staticTV volume 0.1
    return

label audioNightmare:
    play sound audioNightmare
    return

label audioPurr:
    play sound purr
    return

label audioCookie:
    play sound cookie
    return

label audioVase:
    play sound vase
    return

label audioFaucet:
    play loopinSFX faucet
    return

label audioRunning:
    play sound running
    return