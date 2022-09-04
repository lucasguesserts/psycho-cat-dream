image bathroomEveningImage = Image("images/bathroomEvening.png")
image bathroomMirrorImage = Image("images/bathroomMirror.png")
image bathroomBloodyMirrorImage = Image("images/bathroomBloodyMirror.png")
image bathroomBloodSinkImage = Image("images/bathroomEveningBloodSink.png")

init python:
    is_sink_open = False
    closed_sink = False

menu actionsBathroomEvening:
    "Ir para o quarto":
        if(not closed_sink):
            player normal "Droga! A porta está trancada."
            jump actionsBathroomEvening
        else:
            call audioOpenDoorEvening
            jump corridorEvening

    "Abrir torneira" if(not is_sink_open):
        scene bathroomBloodSinkImage
        call audioFaucet
        "Um líquido vermelho começa a fluir da torneira"
        $is_sink_open = True
        player normal "ihh"
        scene bathroomEveningImage
        jump actionsBathroomEvening
        
    "Fechar torneira" if(is_sink_open and not closed_sink):
        stop loopinSFX
        "%(player_name)s fecha a torneira, com dificuldade"
        player normal "ugh!"
        scene bathroomEveningImage
        $closed_sink = True
        $player_courage += 100
        jump actionsBathroomEvening
        
    "Olhar-se no espelho" if(not has_seen_herself_on_the_mirror_in_the_evening):
        $ has_seen_herself_on_the_mirror_in_the_evening = True
        "%(player_name)s olha no espelho mas, estranhamente, não vê seu reflexo"
        show bathroomMirrorImage at top:
            zoom 0.25
        player sad "..."
        hide bathroomMirrorImage
        scene darkRoomImage
        "As luzes se apagam"
        player sad "uh?"
        jump actionsDarkRoomBathroom
        
    "Pesar-se":
        "Balança" "666 kg"
        player sad "que estranho..."
        $ has_checked_her_weight_in_the_evening = True
        jump actionsBathroomEvening

menu actionsDarkRoomBathroom:
    "Acender as luzes":
        scene bathroomEveningImage
        show bathroomBloodyMirrorImage at top:
            zoom 0.25
        "As palavras 'Sorria pra mim' estão escritas no espelho em vermelho"
        player scare "aaaahhhh!"
        hide bathroomBloodyMirrorImage
        jump actionsBathroomEvening

label bathroomEvening:
    scene bathroomEveningImage
    with pixellate

    "%(player_name)s entrou no banheiro"

    player normal "Como vim parar aqui?"
    player normal "Quero sair daqui!"

    jump actionsBathroomEvening
        