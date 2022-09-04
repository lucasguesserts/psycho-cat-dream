image bathroomEveningImage = Image("images/bathroomEvening.jpg")
image bathroomMirrorImage = Image("images/bathroomMirror.png")
image bathroomBloodyMirrorImage = Image("images/bathroomBloodyMirror.png")

init python:
    is_sink_open = False
    looked_on_mirror = False
    closed_sink = False

label bathroomEvening:
    "%(player_name)s entrou no banheiro"

    scene bathroomEveningImage

    player normal "Como vim parar aqui?"
    player normal "Quero sair daqui!"

    menu actionsBathroomEvening:
        "Ir para o quarto":
            if(not closed_sink):
                player normal "Droga! A porta está trancada."
                jump actionsBathroomEvening
            else:
                "%(player_name)s sai do banheiro"
                jump corridorEvening

        "Abrir torneira" if(not is_sink_open):
            "Um líquido vermelho começa a fluir da torneira"
            $is_sink_open = True

            player normal "ihh"
            jump actionsBathroomEvening
        
        "Fechar torneira" if(is_sink_open and not closed_sink):
            "%(player_name)s fecha a torneira, com dificuldade"
            player normal "ugh!"
            $closed_sink = True
            $player_courage += 100
            jump actionsBathroomEvening
        
        "olhar no espelho" if(not looked_on_mirror):
            $looked_on_mirror = True
            "%(player_name)s olha no espelho mas, estranhamente, não vê seu reflexo"
            
            show bathroomMirrorImage at top
            player sad"..."
            hide bathroomMirrorImage

            scene darkRoomImage
            "As luzes se apagam"
            player sad "uh?"
            menu actionsdarkRoomBathroom:
                "Acender as luzes":
                    scene bathroomEveningImage
                    "As palavras 'Sorria pra mim' estão escritas no espelho em vermelho"

                    show bathroomBloodyMirrorImage at top
                    player scare "aaaahhhh!"
                    hide bathroomBloodyMirrorImage

                    jump actionsBathroomEvening
        
        "Pesar-se":
            "Balança" "666 kg"
            jump actionsBathroomEvening
        