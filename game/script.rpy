# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg librarybookshelves = "images/bg/librarybookshelves.png"
image mushinormal = "images/mushi/mushinormal.png"

define m = Character("Mushi", color="#c8ffc8")
define e = Character("Eu", color="#c8c8ff")

default knows_secret = False
default points_mushi = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg librarybookshelves

    "A biblioteca está silenciosa, vejo Mushi orfegando entre as estantes de livros."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mushinormal 

    e "Ela parece muito concentrada.. o que devo fazer?"

    # These display lines of dialogue.

    menu:
        "Aproximar-se e pedir recomendação de livro":
            $ points_mushi += 1
            jump rota_recomendacao

        "Continuar buscando livros sozinho":
            jump rota_ignorar

label rota_recomendacao:
    e "Com licença, Mushi? Você poderia me recomendar um romance?"
    
    m "Oh... romance?"
    "Ela parece hesitar um pouco."
    m "Bem, tem os clássicos... mas se quer minha opinião sincera..."
    m "Eu prefiro histórias de terror."
    
    # Ativando a variável de segredo
    $ knows_secret = True
    $ renpy.notify("Segredo Descoberto!")

    e "Sério? Você gosta de terror?"
    m "Sim. É muito mais... emocionante."
    
    "Conversamos um pouco sobre livros assustadores."
    jump cena_casa

label rota_ignorar:
    "Decido não incomodar. Ela está trabalhando."
    "Pego um livro qualquer e vou embora."
    
    jump cena_casa

label cena_casa:
    # O comando scene sem imagem deixa a tela preta (bom para transição)
    scene black 
    
    "Mais tarde, em casa..."
    
    if knows_secret:
        "Não consigo parar de pensar que a Mushi gosta de terror. Quem diria?"
    else:
        "Foi um dia normal na biblioteca."

    # This ends the game.
    "Fim do capitulo 'A Biblioteca'."
    return
