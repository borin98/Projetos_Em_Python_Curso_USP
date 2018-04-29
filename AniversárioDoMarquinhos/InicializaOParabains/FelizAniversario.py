import sys, time, pygame
import webbrowser

class FelizAniversario ( object ) :

    def __init__(self) :

        self.musicaNervosa()

        string = "\nParabéns Marquinhos por esse dia especial !!!\n"
        self.leitura ( string )

        string = "\nPor Causa Disso, você não merece apenas um parabêns\n"
        self.leitura ( string )

        string = "\nMas sim, 10 horas de parabains !!!\n"
        self.leitura ( string )

        self.site()

    def leitura(self, string) :

        for char in string :
            print(char, end="")
            sys.stdout.flush()
            time.sleep(0.4)

    def site(self) :

        #while ( True ):

        webbrowser.open("https://www.youtube.com/watch?v=1Mcdh2Vf2Xk&t=27s")

    def musicaNervosa(self) :

        song =  ( "/home/borin/PycharmProjects/AniversárioDoMarquinhos/InicializaOParabains/OSTNervosa.mp3" )

        pygame.init()

        pygame.mixer.init()

        pygame.mixer.music.load( song )  # coloque o nome do arquivo de música desejado aqui

        pygame.mixer.music.play ( -1 )

    if ( __name__ == "main" ) :

        __init__ ( )