import telepot
import json
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

load = open("token.json")   # Lendo o Json que contém o token do bot
token = json.loads(load.read()) # Inserindo o token bot a variavel "token"
bot = telepot.Bot(token['token'])   # Inserindo o token no Bot

'''SOBRE: condicoes
Pega o a interacao do usuario (via mensagem ou botao), e faz alguma tomada de acao
'''
def condicoes(chatID, msg):
            if(msg == '/start'):
                    inicio(chatID, bot)

############################### Horário ###############################
            elif(msg == 'Horário'):
                    bot.sendMessage(
                        chatID,
                        "Escolha o curso",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Análise e Desenvolvimento de Sistemas", callback_data='ADS')],
                                #[InlineKeyboardButton(text="Automação e Manufatura Digital", callback_data='ATM')],
                                #[InlineKeyboardButton(text="Banco de Dados", callback_data='BD')],
                                #[InlineKeyboardButton(text="Gestão da Produção Industrial", callback_data='GPI')],
                                #[InlineKeyboardButton(text="Gestão Empresarial", callback_data='GE')],
                                #[InlineKeyboardButton(text="Logística", callback_data='LOG')],
                                #[InlineKeyboardButton(text="Manutenção de Aeronaves", callback_data='MA')],
                                [InlineKeyboardButton(text="Projetos de Estruturas Aeronáuticas", callback_data='PEA')]
                            ]
                        )
                    )

              
          
            elif(msg == 'ADS'):
                    bot.sendMessage(
                        chatID,
                        'Qual o semestre?',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="1° Semestre", callback_data='1SEMADS')],
                                [InlineKeyboardButton(text="2° Semestre", callback_data='2SEMADS')],
                                [InlineKeyboardButton(text="3° Semestre", callback_data='3SEMADS')]
                            ]
                        )
                    )

############################### 1 SEMESTRE ADS ###############################                   

            elif(msg == '1SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='1SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='1SEMTurmaB')]
                            ]
                        )
                    ) 
            elif(msg == '1SEMTurmaA'):
                    txt = open('CursosOferecidos/ADS1.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds1A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds1A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds1A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds1A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds1A')],
                            ]
                        )
                    )
                    txt.close()
            
            elif(msg == '1SEMTurmaB'):
                
                    bot.sendMessage(
                        chatID,
                 
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds1B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds1B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds1B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds1B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds1B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds1A'):
                    txt = open('Horario/1Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds1A'):
                    txt = open('Horario/1Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds1A'):
                   txt = open('Horario/1Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds1A'):
                   txt = open('Horario/1Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds1A'):
                   txt = open('Horario/1Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds1B'):
                   txt = open('Horario/1Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds1B'):
                   txt = open('Horario/1Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds1B'):
                   txt = open('Horario/1Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds1B'):
                   txt = open('Horario/1Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds1B'):
                   txt = open('Horario/1Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 1 SEMESTRE ADS ^^^^^^^ ###############################


############################### 2 SEMESTRE ADS #######################################                   

            elif(msg == '2SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='2SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='2SEMTurmaB')]
                            ]
                        )
                    ) 
            elif(msg == '2SEMTurmaA'):
                    txt = open('CursosOferecidos/ADS1.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds2A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds2A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds2A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds2A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds2A')],
                            ]
                        )
                    )
                    txt.close()
            
            elif(msg == '2SEMTurmaB'):
                
                    bot.sendMessage(
                        chatID,
                 
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds2B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds2B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds2B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds2B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds2B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds2A'):
                    txt = open('Horario/2Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds2A'):
                    txt = open('Horario/2Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds2A'):
                   txt = open('Horario/2Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds2A'):
                   txt = open('Horario/2Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds2A'):
                   txt = open('Horario/2Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds2B'):
                   txt = open('Horario/2Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds2B'):
                   txt = open('Horario/2Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds2B'):
                   txt = open('Horario/2Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds2B'):
                   txt = open('Horario/2Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds2B'):
                   txt = open('Horario/3Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 2 SEMESTRE ADS ^^^^^^^ ###############################


                    
############################### 3 SEMESTRE ADS #######################################                   

            elif(msg == '3SEMADS'):
                    bot.sendMessage(
                        chatID,
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Turma A", callback_data='3SEMTurmaA')],
                                [InlineKeyboardButton(text="Turma B", callback_data='3SEMTurmaB')]
                            ]
                        )
                    ) 
            elif(msg == '3SEMTurmaA'):
                    txt = open('CursosOferecidos/ADS1.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds3A')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds3A')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds3A')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds3A')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds3A')],
                            ]
                        )
                    )
                    txt.close()
            
            elif(msg == '3SEMTurmaB'):
                
                    bot.sendMessage(
                        chatID,
                 
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Segunda-Feira", callback_data='SegAds3B')],
                                [InlineKeyboardButton(text="Terça-Feira", callback_data='TerAds3B')],
                                [InlineKeyboardButton(text="Quarta-Feira", callback_data='QuaAds3B')],
                                [InlineKeyboardButton(text="Quinta-Feira", callback_data='QuiAds3B')],
                                [InlineKeyboardButton(text="Sexta-Feira", callback_data='SexAds3B')],
                            ]
                        )
                    )
                 

            elif(msg == 'SegAds3A'):
                    txt = open('Horario/3Semestre/TurmaA/SFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	

                    
            elif(msg == 'TerAds3A'):
                    txt = open('Horario/3Semestre/TurmaA/TFA.md','r')	
                    bot.sendMessage(chatID,txt.read(),'Markdown')   
                    txt.close()	
                    
            elif(msg == 'QuaAds3A'):
                   txt = open('Horario/3Semestre/TurmaA/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'QuiAds3A'):
                   txt = open('Horario/3Semestre/TurmaA/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                    
            elif(msg == 'SexAds3A'):
                   txt = open('Horario/3Semestre/TurmaA/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                                        

            elif(msg == 'SegAds3B'):
                   txt = open('Horario/3Semestre/TurmaB/SFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'TerAds3B'):
                   txt = open('Horario/3Semestre/TurmaB/TFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuaAds3B'):
                   txt = open('Horario/3Semestre/TurmaB/QFA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'QuiAds3B'):
                   txt = open('Horario/3Semestre/TurmaB/QFIA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()	
                    
            elif(msg == 'SexAds3B'):
                   txt = open('Horario/3Semestre/TurmaB/SXTA.md','r')	
                   bot.sendMessage(chatID,txt.read(),'Markdown')   
                   txt.close()
                   
############################### 3 SEMESTRE ADS ^^^^^^^ ###############################

            elif(msg == 'ATM'):
                    txt = open('CursosOferecidos/ATM.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matATM')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matATM'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurATM.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'BD'):
                    txt = open('CursosOferecidos/BD.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matBD')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matBD'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurBD.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'GPI'):
                    txt = open('CursosOferecidos/GPI.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matGPI')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matGPI'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurGPI.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()


            elif(msg == 'GE'):
                    txt = open('CursosOferecidos/GE.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                    )
                    txt.close()

            elif(msg == 'LOG'):
                    txt = open('CursosOferecidos/LOG.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matLOG')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matLOG'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurLOG.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()


            elif(msg == 'MA'):
                    txt = open('CursosOferecidos/MA.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matMA')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matMA'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurMA.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

            elif(msg == 'PEA'):
                    txt = open('CursosOferecidos/PEA.md','r')
                    bot.sendMessage(
                        chatID,
                        txt.read(),
                        'Markdown',
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Matriz Curricular", callback_data='matPEA')]
                            ]
                        )
                    )
                    txt.close()

            elif(msg == 'matPEA'):
                    bot.sendMessage(chatID, "Enviando Matriz Curricular...")
                    doc = open ("CursosOferecidos/matCurPEA.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

##########################################################################################################

########################### COMO SER ALUNO
            elif (msg == 'Calendário'):
                bot.sendMessage(chatID, "Enviando calendário...")
                doc = open ("Calendário/calendario_2019-1.pdf",'rb')
                bot.sendDocument(chatID, doc)
                doc.close()
                keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                #KeyboardButton(text="Calendário"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],resize_keyboard=True
                    )
                bot.sendMessage(chatID,"O seu calendário estudantil está pronto...", reply_markup=keyboard)

          #  elif(msg == 'Calendário'):
                  


########################### COMO CHEGAR
            elif (msg == 'Como Chegar'):
                    txtHelp = open('ComoChegar/Textos/txt01.md','r')

                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Fatec no Mapa"),
                                KeyboardButton(text="Imagens"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],
                        resize_keyboard=True
                    )

                    bot.sendMessage(chatID,	txtHelp.read(),'Markdown', reply_markup=keyboard)

                    txtHelp.close()	#Fecha o arquivo

            elif(msg == 'Fatec no Mapa'):
                    bot.sendMessage(chatID,"Enviando localização...")
                    bot.sendLocation(chatID, -23.162578,-45.7967319)

            elif (msg == 'Imagens'):
                    bot.sendMessage(chatID, "Enviando imagem...")
                    imgFatec = open("ComoChegar/Imagens/VistaFatec01.jpg","rb")
                    bot.sendPhoto(chatID, imgFatec)
                    imgFatec.close()
##########################################################################################################

########################### SOBRE A FATEC
            elif (msg == 'Sobre a Fatec'):
                    txtHelp = open('SobreFatecSjc/Textos/introducaoSobreAFatec.md','r')
                    keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="+ Sobre Fatec"),
                                KeyboardButton(text="Projetos"),
                                KeyboardButton(text="Regulamento Interno"),
                                KeyboardButton(text="Voltar")
                            ]
                        ],resize_keyboard=True
                    )
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown', reply_markup=keyboard)
                    txtHelp.close()

            elif (msg == '+ Sobre Fatec'):
                    txtHelp = open('SobreFatecSjc/Textos/sobreFatec.md','r')
                    bot.sendMessage(chatID, txtHelp.read(), 'Markdown')
                    txtHelp.close()
                    bot.sendContact(chatID, "551239054979", "FatecSJC", "01")
                    bot.sendContact(chatID, "551239052423", "FatecSJC", "02")
                    bot.sendContact(chatID, "551239054699", "FatecSJC", "03")

            elif (msg == 'Regulamento Interno'):
                    bot.sendMessage(chatID, "Enviando regulamento...")
                    doc = open ("RegulamentoInterno/regulamentoGeral.pdf",'rb')
                    bot.sendDocument(chatID, doc)
                    doc.close()

#### Projetos
            elif (msg== 'Projetos'):
                    bot.sendMessage(
                        chatID,
                        "Projetos atuais da Fatec Profº Jessen Vidal",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Agencia Inova CPS", callback_data='Agencia Inova')],
                                [InlineKeyboardButton(text="BAJA", callback_data='BAJA')],
                                [InlineKeyboardButton(text="Relações Internacionais", callback_data='Relações Internacionais')],
                                [InlineKeyboardButton(text="Cimatech", callback_data='Cimatech')],
                                [InlineKeyboardButton(text="Escola de Inovadores", callback_data='Escola de Inovadores')],
                                [InlineKeyboardButton(text="Escritório de Carreiras", callback_data='Escritório de Carreiras')],
                                [InlineKeyboardButton(text="Fatec Business Mentoring", callback_data='FBM')],
                                [InlineKeyboardButton(text="Projeto IBM HACKaTruck", callback_data='Projeto IBM HACKaTruck')],
                                [InlineKeyboardButton(text="Vestec", callback_data='Vestec')],
                                [InlineKeyboardButton(text="Megazord", callback_data='Megazord')],
                            ]
                        )
                    )

            elif (msg=="Agencia Inova"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/agenciaInovaPaulaSouza.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgAgenciaInovaPaulaSouza.jpg","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txtPP = open('SobreFatecSjc/Textos/Projetos/agenciaInovaPaulaSouzaPP.md','r')
                    bot.sendMessage(chatID,txtPP.read(),'Markdown')
                    txtPP.close()

                    bot.sendContact(chatID, "5512987456578", "Renato", "Galvão")

            elif (msg=="BAJA"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/baja.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgBajaSaeBrasil.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txtPP = open('SobreFatecSjc/Textos/Projetos/bajaPP.md','r')
                    bot.sendMessage(chatID,txtPP.read(),'Markdown')
                    txtPP.close()

                    bot.sendMessage(chatID, "Aguarde um momento, estamos carregando a foto do projeto...")

                    imgPP = open("SobreFatecSjc/imgProjetosInternos/imgBaja01.jpg","rb")
                    bot.sendPhoto(chatID, imgPP, "Foto do projeto em 2015")
                    imgPP.close()

            elif (msg=="Relações Internacionais"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/nucleoDeRelacoesInternacionais.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgNucleoDeRelacoesInternacionais.jpg","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/nucleoDeRelacoesInternacionaisPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Cimatech"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/cimatech.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgCimatech.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txtPP = open('SobreFatecSjc/Textos/Projetos/cimatechPP.md','r')
                    bot.sendMessage(chatID,txtPP.read(),'Markdown')
                    txtPP.close()

            elif (msg=="Escola de Inovadores"):
                    bot.sendMessage(chatID, "Aguarde um instante...")
                    bot.sendSticker(chatID, "CAADAQADNQYAAjN-VQp9fRoNVhK8sQI")

                    txt = open('SobreFatecSjc/Textos/Projetos/escolaDeInovadores.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgEscoladeInovadores.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/escolaDeInovadoresPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Escritório de Carreiras"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/escritorioDeCarreiras.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgEscritorioDeCarreiras.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/escritorioDeCarreirasPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="FBM"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/fbm.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgFBM.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/fbmPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    bot.sendContact(chatID, "551239054979", "ContatoFBM", "01")
                    bot.sendContact(chatID, "551239052423", "ContatoFBM", "02")
                    bot.sendContact(chatID, "551239054699", "ContatoFBM", "03")


            elif (msg=="Projeto IBM HACKaTruck"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruck.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgHackTruck03.jpg","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruckPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruckLink.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/projetoIBMHACKaTruckYT.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Vestec"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/vestec.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgVestec.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    txt.close()
                    img.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/vestecPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif (msg=="Megazord"):
                    bot.sendMessage(chatID, "Aguarde um instante...")

                    txt = open('SobreFatecSjc/Textos/Projetos/megazord.md','r')
                    img = open("SobreFatecSjc/imgProjetosInternos/imgMegazord.png","rb")
                    bot.sendPhoto(chatID, img, txt.read())
                    img.close()
                    txt.close()

                    txt = open('SobreFatecSjc/Textos/Projetos/megazordPP.md','r')
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

                    img = open("SobreFatecSjc/imgProjetosInternos/imgMegazord01.jpg","rb")
                    bot.sendPhoto(chatID, img)
                    img.close()

                    img = open("SobreFatecSjc/imgProjetosInternos/imgMegazord02.jpg","rb")
                    bot.sendPhoto(chatID, img)
                    img.close()

                    bot.sendMessage(chatID,"https://www.youtube.com/user/MegazordAerodesign")
                    bot.sendMessage(chatID,"https://www.facebook.com/megazordaerodesign?hc_ref=ARTOOGrhjaoVa14Y36pTJtl6rInOIgA928tr-YknVHuiL2RRHBKKQwji2kGgggUb89o")
                    bot.sendMessage(chatID,"Para mais informações entre em contato com: Carlos ou Murilo")

                    bot.sendContact(chatID, "5512988281517", "Carlos", "Megazord")
                    bot.sendContact(chatID, "5512997527525", "Murilo", "Megazord")

##########################################################################################################

            elif (msg == 'Voltar'):
                    inicio(chatID, bot)

'''SOBRE: callback
O parametro desta funcao eh um Json enviado do message_loop com os campos referente a interacao feita via a chave 'callback_query', ou seja, esta funcao eh responsavel por
por pegar o que foi emitido pelo usuario (texto iniline_keyboard) e seu respectivo ID, e repassar para a funcao 'condicoes' e que sera processado a requisicao
e sera emitido o devido comportamento que o usuario quer em relacao ao bot
'''
def callback(msg):
            query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave callback_queryt' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...

            chatID = from_id
            #ID do usuario que apertou o botao

            texto = query_data
            #o valor do botao que foi apertado

            print(chatID)

            bot.answerCallbackQuery(query_id, text="Só um instante")
            #retorna um POP-UP para o usuario quando ele digitou alguma coisa

            print("callback query", query_id, from_id, query_data)

            condicoes(chatID, texto)
            # pega o que foi clicado pelo usuario (callback_data) e seu ID manda para a funcao 'condicoes' que vai processar o clique


'''SOBRE: ir
O parametro desta funcao eh um Json enviado do message_loop com os campos referente a interacao via a chave 'chat', ou seja, esta funcao eh responsavel por
por pegar o que foi emitido pelo usuario (texto via mensagem) e seu respectivo ID, e repassar para a funcao  'condicoes' e que sera processado a requisicao
e sera emitido o devido comportamento que o usuario quer em relacao ao bot
'''
def ir(msg):
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave 'chat' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...
            tipoMsg, tipoChat, chatID = telepot.glance(msg)

            texto = msg['text']     #variavel Auxiliar para receber a texto que o usuario digitou, fiz ela porque se eu chamasse --condicoes(chatID, msg['text'])--
                                    #tava dando erro

            condicoes(chatID, texto)    # pega o que foi digitado pelo usuario e seu ID manda para a funcao 'condicoes' que vai processar o a mensagem

'''SOBRE: inico
Esta funcao eh uma forma de facilitar o a primeira interacao ao usuario
'''
def inicio(chatID, bot):
            keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="Calendário"),
                                KeyboardButton(text="Como Chegar"),
                                KeyboardButton(text="Horário"),
                                KeyboardButton(text="Sobre a Fatec"),
                            ]
                        ],resize_keyboard=True
                    )

            txt = open('Inicializacao/Hello.md','r')    #Abre o arquivo Hello.md com o atributo leitura
            bot.sendMessage(chatID,txt.read(),'Markdown',reply_markup=keyboard)
            txt.close()

''' SOBRE: message_loop
o message_loop eh o "listenen" das interacoes dos usuarios com o bot, ele retorna um Json, que quando uma interacao eh feita via mensagem,
recorre a chave 'chat' e redireciona o comportamento do bot para a funcao "ir", e quando uma interacao eh feita via inline_keyboard (callback_query)
recorre a chave callback
'''
bot.message_loop(
    {
        'chat': ir,
        'callback_query': callback,
    }
)

#responsavel por deixa o programa sempre em execucao, mas quando ocorre uma interacao, o message_loop e invocado, e quebra este laco infinito,
#e faz o comportamento requirido pelo usuario
while True:
            pass
