#--------------- Importações ---------------#
from functions import Db, Webdriver, CriarAtendimento, EnviarMensagem, EnviarMídia
#--------------- Principal ---------------#




Mensagem = ""
Mídia = (f"")






Driver = Webdriver.conectar()
#--------------- Não mexa daqui para baixo! ---------------#
def main():

    #Impulso inicial
    Cursor = Db.conectar()
    Whatsapp = Db.buscar(Cursor)

    #Loop - Só quebra quando não tiver mais números
    while Whatsapp != "None":
        try:
            Whatsapp = Db.buscar(Cursor)
            CriarAtendimento.Abrir(Cursor, Driver, Whatsapp)
            EnviarMensagem.Enviar(Cursor, Driver, Mensagem, Whatsapp)
            EnviarMídia.Enviar(Driver, Mídia)
        except:
            main()

    else:
        print("Programa finalizado!")
        Driver.quit()
        quit()
main()