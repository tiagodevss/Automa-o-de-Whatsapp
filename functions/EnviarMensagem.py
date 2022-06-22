import time

def Enviar(Cursor, Driver, Mensagem, Whatsapp):
    '''
    Esta função envia a mensagem para o número de whatsapp, entretanto só funciona quando o atendimento já está criado através da URL.
    '''
    try:
        time.sleep(2)
        cliqueBarraMensagem = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        cliqueBarraMensagem.click()
        time.sleep(1)
        cliqueBarraMensagem.send_keys(Mensagem)

        cliqueEnviar = Driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        cliqueEnviar.click()
        time.sleep(3)

        Cursor.execute(f"UPDATE ``.`` SET `PrimeiroContato` = 'Mensagem enviada' WHERE (`Whatsapp` = {Whatsapp});")
    except:
        Cursor.execute(f"UPDATE ``.`` SET `PrimeiroContato` = 'Núm Bloqueado' WHERE (`Whatsapp` = {Whatsapp});")