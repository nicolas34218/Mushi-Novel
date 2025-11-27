# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg librarybookshelves = "images/bg/librarybookshelves.png"
image mushinormal = "images/mushi/mushinormal.png"

define m = Character("Mushi", color="#c8ffc8")
define e = Character("Eu", color="#c8c8ff")

default knows_secret = False
default date_marked = False
default points_mushi = 0

# The game starts here.

label start:

    scene bg librarybookshelves with dissolve
    play music "audio/piano.mp3" fadein 2.0

    "CAPÍTULO 1: O Livro Proibido"

    "A biblioteca da faculdade. O cheiro de papel velho e café me acalma."
    "Mas, se sou honesto, não venho aqui apenas pelos livros."
    
    show mushinormal with dissolve
    
    "Mushi está no balcão. Quieta, eficiente, quase invisível para a maioria."
    "Eu preciso falar com ela, mas não quero parecer invasivo."

    menu:
        "O que devo fazer?"

        "Pedir uma recomendação de romance.":
            $ points_mushi += 1
            jump c1_conversa_livro

        "Não incomodar e procurar sozinho.":
            jump c1_ignorar

label c1_conversa_livro:
    e "Com licença, Mushi? Estou meio perdido. Tem algum romance bom?"

    m "Romance...?"
    "Ela franze o nariz levemente. É uma expressão nova."
    
    m "Bem, 'Orgulho e Preconceito' sai bastante. Mas..."
    
    e "Mas?"
    
    show mushi happy with dissolve
    m "Sinceramente? Eu acho romance chato. Ninguém morre no final."
    
    stop music fadeout 0.5
    "O silêncio na biblioteca parece ficar mais pesado."
    
    e "Espera... você gosta de gente morrendo?"
    
    play music "audio/misterio.mp3" fadein 2.0
    
    m "Eu gosto de Terror. Stephen King, Junji Ito, Lovecraft."
    m "O terror é honesto. O medo não mente."
    
    $ knows_secret = True
    $ renpy.notify("Segredo Descoberto: Fã de Terror")
    
    e "Uau. Eu nunca imaginaria. Achei que você fosse..."
    m "...uma bibliotecária tímida e delicada? É, todo mundo acha."
    
    "Conversamos por mais dez minutos. Ela fala com uma paixão assustadora."
    jump c1_casa

label c1_ignorar:
    "Melhor não. Ela parece ocupada."
    "Pego um livro qualquer na estante e faço o checkout na máquina automática."
    "Saio sem olhar para trás."
    jump c1_casa

label c1_casa:
    scene black with dissolve
    stop music fadeout 2.0
    
    "Mais tarde, no meu quarto..."
    
    if knows_secret:
        "Não consigo tirar a Mushi da cabeça. Aquela conversa sobre terror foi incrível."
    else:
        "Mais um dia em que não tive coragem de falar com ela direito."

    "Pego meu celular. Tenho o número dela do grupo de estudos."

    menu:
        "Devo chamá-la para sair?"

        "Mandar mensagem agora (Convidar para Café)":
            if knows_secret:
                jump c1_mensagem_sucesso
            else:
                jump c1_mensagem_neutra

        "Esperar para falar pessoalmente (Hesitar)":
            jump c1_esperar


label c1_mensagem_sucesso:
    "Digito: 'Oi Mushi. Achei um sebo que vende livros de terror antigos. Quer ir lá e depois tomar um café amanhã?'"
    "..."
    "BZZT."
    "Mushi: 'Terror antigo? Estou dentro. 14h?'"
    
    $ date_marked = True
    e "Isso! Vai dar certo."
    jump capitulo_2

label c1_mensagem_neutra:
    "Digito: 'Oi Mushi. Quer tomar um café amanhã?'"
    "..."
    "Demora uma hora, mas ela responde."
    "Mushi: 'Pode ser. Preciso sair um pouco da rotina.'"
    
    $ date_marked = True
    jump capitulo_2

label c1_esperar:
    "Não... mandar mensagem do nada é estranho."
    "Vou esperar encontrar com ela na biblioteca de novo."
    "Coloco o celular de lado e vou dormir."
    jump capitulo_2


# Capitulo 2: As Consequencias 
label capitulo_2:
    scene black
    with Pause(1.0)
    
    "CAPÍTULO 2: Desencontros e Encontros"
    
    if date_marked:
        jump c2_o_encontro
    else:
        jump c2_o_desencontro

label c2_o_encontro:
    scene bg coffeshop
    play music "audio/piano_calmo.mp3"
    
    "Chego na cafeteria. Mushi já está lá."
    
    if knows_secret:
        show mushi happy
        "Ela está lendo um livro com uma capa preta e vermelha."
        e "Deixa eu adivinhar... alguém morreu na página 10?"
        m "Página 3. É um novo recorde."
        "Ela sorri. É o sorriso mais bonito que já vi."
        
        m "Obrigada por me convidar. Eu não costumo sair muito."
        e "Fico feliz que veio. É bom compartilhar... hobbies peculiares."
        
        $ points_mushi += 2
        "O encontro flui perfeitamente. Sinto que criamos uma conexão real."
        
    else:
        show mushinormal
        "Ela está tomando chá, olhando para a janela."
        e "Oi, Mushi."
        m "Oi. Obrigada pelo convite."
        "O clima é um pouco tímido, já que não temos muito assunto em comum ainda."
        
    "Fim do Capítulo 2 - Rota do Encontro."
    return

label c2_o_desencontro:
    scene bg biblioteca
    play music "audio/piano_calmo.mp3"
    
    "Dois dias depois, volto à biblioteca."
    "Procuro por Mushi no balcão."
    
    show mushinormal
    
    e "Oi, Mushi."
    
    m "Ah. Oi."
    "Ela nem levanta a cabeça dos livros."
    
    e "Tudo bem?"
    
    m "Tudo. Só... muito trabalho."
    
    "Sinto um gelo na voz dela. Parece que ela estava esperando algo de mim que não veio."
    
    if knows_secret:
        m "Achei que você fosse comentar mais sobre aquele livro de terror."
        e "Ah, eu ia, mas..."
        m "Entendo. Deixa pra lá."
    else:
        "O silêncio é constrangedor. Perdi o 'timing' completamente."
    
    "Vou ter que trabalhar duro para recuperar a atenção dela."
    
    "Fim do Capítulo 2 - Rota da Friendzone."
    return
