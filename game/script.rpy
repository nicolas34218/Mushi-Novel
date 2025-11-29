# The script of the game goes in this file.

# Declare the images that will be used in game indicating the name and folder

image bg librarybookshelves = "images/bg/librarybookshelves.png"
image mushinormal = "images/mushi/mushinormal.png"

# Declare characters used by this game. The color argument colorizes the name of the character

define m = Character("Mushi", color="#c8ffc8")
define e = Character("Eu", color="#c8c8ff")

default knows_secret = False
default date_marked = False
default points_mushi = 0

# The game starts here.

label start:

    scene bg librarybookshelves with fade

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
            jump route_book_talk

        "Não incomodar e procurar sozinho.":
            jump ignore

label route_book_talk:
    e "Com licença, Mushi? Estou meio perdido. Tem algum romance bom?"

    m "Romance...?"
    "Ela franze o nariz levemente. É uma expressão nova."
    
    m "Bem, 'Orgulho e Preconceito' sai bastante. Mas..."
    
    e "Mas?"
    
    show mushinormal with dissolve
    m "Sinceramente? Eu acho romance chato. Ninguém morre no final."
    
    "O silêncio na biblioteca parece ficar mais pesado."
    
    e "Espera... você gosta de gente morrendo?"
    
    m "Eu gosto de Terror. Stephen King, Junji Ito, Lovecraft."
    m "O terror é honesto. O medo não mente."
    
    $ knows_secret = True
    $ renpy.notify("Segredo Descoberto!")
    
    e "Uau. Eu nunca imaginaria. Achei que você fosse..."
    m "...uma bibliotecária tímida e delicada? É, todo mundo acha."
    
    "Conversamos por mais dez minutos. Ela fala com uma paixão assustadora."
    jump house

label ignore:
    "Melhor não. Ela parece ocupada."
    "Pego um livro qualquer na estante e faço o checkout na máquina automática."
    "Saio sem olhar para trás."
    jump house

label house:
    scene black with fade
    
    "Mais tarde, no meu quarto..."
    
    if knows_secret:
        "Não consigo tirar a Mushi da cabeça. Aquela conversa sobre terror foi incrível."
    else:
        "Mais um dia em que não tive coragem de falar com ela direito."

    "Pego meu celular. Tenho o número dela do grupo de estudos."

    menu:
        "Devo chamá-la para sair?"

        "Mandar mensagem agora":
            if knows_secret:
                jump success_message
            else:
                jump neutral_message

        "Esperar para falar pessoalmente":
            jump wait

label success_message:
    "Digito: 'Oi Mushi. Achei um sebo que vende livros de terror antigos. Quer ir lá e depois tomar um café amanhã?'"
    "..."
    "BZZT."
    "Mushi: 'Terror antigo? Estou dentro. 14h?'"
    
    $ date_marked = True
    e "Isso! Vai dar certo."

    $ renpy.notify("Capítulo concluído!")
    jump chapter_2



label neutral_message:
    "Digito: 'Oi Mushi. Quer tomar um café amanhã?'"
    "..."
    "Demora uma hora, mas ela responde."
    "Mushi: 'Pode ser. Preciso sair um pouco da rotina.'"
    
    $ date_marked = True

    $ renpy.notify("Capítulo concluído!")    
    jump chapter_2

label wait:
    "Não... mandar mensagem do nada é estranho."
    "Vou esperar encontrar com ela na biblioteca de novo."
    "Coloco o celular de lado e vou dormir."

    $ renpy.notify("Capítulo concluído!")
    jump chapter_2

# Capitulo 2: As Consequencias 
label chapter_2:
    scene black with fade
    
    "CAPÍTULO 2: Desencontros e Encontros"
    
    if date_marked:
        jump c2_date
    else:
        jump c2_mismatch

label c2_date:
    scene bg coffeshop with fade
    
    "Chego na cafeteria. Mushi já está lá."
    
    if knows_secret:
        show mushinormal with dissolve
        "Ela está lendo um livro com uma capa preta e vermelha."
        e "Deixa eu adivinhar... alguém morreu na página 10?"
        m "Página 3. É um novo recorde."
        "Ela sorri. É o sorriso mais bonito que já vi."
        
        m "Obrigada por me convidar. Eu não costumo sair muito."
        e "Fico feliz que veio. É bom compartilhar... hobbies peculiares."
        
        $ points_mushi += 2
        "O encontro flui perfeitamente. Sinto que criamos uma conexão real."
        
    else:
        show mushinormal with dissolve 
        "Ela está tomando chá, olhando para a janela."
        e "Oi, Mushi."
        m "Oi. Obrigada pelo convite."

        # hide mushinormal
        # hide is good for when the character leaves the scene but does not change the scenario

        "O clima é um pouco tímido, já que não temos muito assunto em comum ainda."
        
    "Fim do Capítulo 2 - Rota do Encontro."

    return

label c2_mismatch:
    scene bg biblioteca with fade
    
    "Dois dias depois, volto à biblioteca."
    "Procuro por Mushi no balcão."
    
    show mushinormal with dissolve 
    
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
 