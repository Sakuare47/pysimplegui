import PySimpleGUI as sg 
import random


sg.theme('dark green 7')


layout = [
	[sg.Text("Consulta a Ìfá")],
	[sg.Button("Consultar",key="consultar"), sg.Button("Limpar")],
	[sg.Text("", key="tefa_ifa")],
]



janela = sg.Window("TÉFÁ ÌFÁ", layout, size=(300,400), element_justification="center")


while True:
	
	evento, valores = janela.read()
	if evento == sg.WIN_CLOSED or evento == "Limpar":
		break

	if evento == "Consultar":
		codigo_consulta = valores["consultar"]
	



	def tefa_ifa():
	    caminho = random.randint(1,16)
	    sg.Print(caminho)

	    odus = {
	        'Odu 1':'OKÀNRÀN',
	        'Odu 2':'ÈJÌÒKÒ',
	        'Odu 3':'OGBÈYONÚ',
	        'Odu 4':'ÌROSÙN',
	        'Odu 5':'OSE',
	        'Odu 6':'OBÀRÀ',
	        'Odu 7':'ODÍ',
	        'Odu 8':'ÈJÌ-OGBÈ',
	        'Odu 9':'OSÁ',
	        'Odu 10':'OFÚN',
	        'Odu 11':'OWONRÍN',
	        'Odu 12':'ÈJÌILA-ASEBORA',
	        'Odu 13':'ÌKÁ',
	        'Odu 14':'OTÚRÚPÓN',
	        'Odu 15':'OFÚN-OKÀNRÀN',
	        'Odu 16':'ÌRETÈ',
	        }

	    if(caminho == 1):
	        sg.Print(odus['Odu 1'])
	        sg.Print('')
	        sg.Print('Coragem, persistência, paz, progresso, rivalidade, esperança, superação de derrotas, final de um período de sofrimentos, sucesso e lucratividade.')
	    elif(caminho == 2):
	        sg.Print(odus['Odu 2'])
	        sg.Print('')
	        sg.Print('Consulente possui desejo de viver inúmeras experiências ao mesmo tempo: dois ou mais trabalhos, tendência a estabelecer relacionamentos duplos, desejo de mais progresso, mais prosperidade e de estar em dois lugares ao mesmo tempo.')
	    elif(caminho == 3):
	        sg.Print(odus['Odu 3'])
	        sg.Print('')
	        sg.Print('O consulente deve ser levado a reconhecer seu próprio potencial e facilidades que tem na vida. Mas não se pode esquecer que tudo o que uma pessoa tem de bom, tem também um lado paralelo, como disputa, inveja, rupturas e obstáculos.')
	    elif(caminho == 4):
	        sg.Print(odus['Odu 4'])
	        sg.Print('')
	        sg.Print('Este é o odu da vitória e também da derrota, pois as duas andam em paralelo. Neste odu se adquire a noção do esforço, do trabalho e da estratégia na luta pelo sucesso. Sinaliza, ainda, a necessidade de cuidado para manter o conquistado. Pode indicar também mudanças, novas possibilidades, novos caminhos e renovações.')
	    elif(caminho == 5):
	        sg.Print(odus['Odu 5'])
	        sg.Print('')
	        sg.Print('A energia deste odu é de atração para o amor e, com a mesma base energética, atrai trabalho, prosperidade e dinheiro. Este consulente tem sorte à vista nos âmbitos afetivo e profissional. Quando Ọ̀ ẹ́ aparece é indicativo de que algo que esse consulente tem vai se multiplicar. Em Ọ̀ ẹ́ há também questões de fertilidade, sexualidade e distúrbios referentes a estes.')
	    elif(caminho == 6):
	        sg.Print(odus['Odu 6'])
	        sg.Print('')
	        sg.Print('Este odu indica potencial criativo do consulente, que pode ser tanto artístico como para encontrar soluções para sua vida. Fala também da questão da paz e de sua capacidade de manter-se tranquilo e equilibrado. A inquietação é o desafio desse consulente, mas é também o estímulo para que se mova e o que o leva ao desejo de mudança - podendo este ser referente a alguma situação ou mesmo a um espaço físico. Observe que para Ọ̀bàrà ser interpretado como odu principal ele tem que cair duas vezes sucessivas. Se isso não ocorrer, ele deverá ser desconsiderado.')
	    elif(caminho == 7):
	        sg.Print(odus['Odu 7'])
	        sg.Print('')
	        sg.Print('aparece em situações nas quais algo está bom e outros se incomodam com isso, levando a possíveis traições, rupturas e boicotes. Quando aparece muitas vezes no jogo, significa que o consulente é um líder nato; também pode indicar que ele é abiku. Geralmente as pessoas falam que este odu é negativo. Uma lição básica é a seguinte: não existe odu negativo, odu ruim. Existem, sim, odus mal compreendidos, situações que podem ser consideradas negativas e que determinado odu aparece para esclarecer, alertar e mostrar saídas.')
	    elif(caminho == 8):
	        sg.Print(odus['Odu 8'])
	        sg.Print('')
	        sg.Print('Este odu traz muitos elementos ricos a serem estudados. É considerado “o pai de todos os odus”. Ele serve de base para entendimento da questão do destino, que é o objetivo maior do jogo de búzios. Èjì-Ogbè revela que o consulente possui realeza, é portador de um Ori nobre, de riqueza, liderança e espiritualidade. A preocupação do orientador é a de desvendar e compreender as mensagens que Èjì-Ogbè traz para esse destino e quais aspectos está priorizando.')
	    elif(caminho == 9):
	        sg.Print(odus['Odu 9'])
	        sg.Print('')
	        sg.Print('Este odu trata de questões familiares, de relacionamento familiar e do quanto a família influencia a vida das pessoas, seu progresso e sua prosperidade. É o odu de relacionamento, de aproximação, ou até mesmo afastamento, entre pessoas da mesma família.')
	    elif(caminho == 10):
	        sg.Print(odus['Odu 10'])
	        sg.Print('')
	        sg.Print('Este odu anuncia que uma renovação está chegando à vida do consulente: algo novo, uma nova chance, a possibilidade de reaver algo perdido. É o odu da esperança, de novas possibilidades nas relações afetivas, profissionais e sociais.')
	    elif(caminho == 11):
	        sg.Print(odus['Odu 11'])
	        sg.Print('')
	        sg.Print('Este odu trata da ancestralidade, reveladora de nossos potenciais e das influências por nós recebidas dos nossos antepassados nos âmbitos de nossa existência. Ọ̀wọ́nrín também retrata a espiritualidade individual de cada um e revela surpresas, positivas ou negativas.')
	    elif(caminho == 12):
	        sg.Print(odus['Odu 12'])
	        sg.Print('')
	        sg.Print('Èjìila-Asẹbọra é o último odu “interpretável”. Este odu pede paciência, resistência, bom senso e discernimento. É o odu que fala de questões que nos afligem e que muitas vezes vão parar num tribunal de justiça.')
	    elif(caminho == 13):
	        sg.Print(odus['Odu 13'])
	        sg.Print('')
	        sg.Print('Quando esse odu aparece, deve-se saudar Obaluaiê para que traga cura e solução para enfermidades e outros problemas humanos. Quando ele aparece, só ganha peso se o consulente estiver doente e, nesse caso, ele reafirma a gravidade da doença. Mas se o consulente não estiver enfermo, Ìká poderá estar indicando que alguém da família adoecerá ou que o consulente precisa encontrar seus caminhos no âmbito das relações de amizade, sendo preciso, no entanto, que tome muito cuidado com elas')
	    elif(caminho == 14):
	        sg.Print(odus['Odu 14'])
	        sg.Print('')
	        sg.Print('A observação mais importante desse odu é relativa às suas amizades. Esse odu recomenda ao consulente que tome cuidado com suas parcerias e com as armadilhas que amigos podem preparar para ele. Como Ìká, também pode indicar algum problema com a saúde do consulente ou de algum de seus familiares. O orientador interpretará o odu Òtúrúpọ̀n caso tenha notado durante a consulta que esse consulente tem carga energética pesada - muita tristeza, muitos aborrecimentos, derrotas e sofrimentos. Caso note isso, valerá a pena dar mais ênfase a esse odu e caberá a Obaluaiê prover soluções para atenuar esse sofrimento.')
	    elif(caminho == 15):
	        sg.Print(odus['Odu 15'])
	        sg.Print('')
	        sg.Print('Além de Obaluaiê, Ori aparece neste odu informando que este consulente está desnorteado, sem rumo, sem sentido existencial e projeta em outras pessoas a responsabilidade por seus problemas. O orientador deve contribuir para que o consulente compreenda que a causa de seus desencontros e dificuldades não se encontra fora dele, que não há algo ou alguém responsável por seus desencontros e dificuldades. Òfún-Ọ̀kànràn diz que todas as dificuldades, falhas e fracassos de sua vida têm muito a ver com a percepção que tem de si mesmo, com o modo de tratar a si mesmo e com o modo de colocar-se diante da própria realidade. A recomendação ao consulente é que olhe para si e promova as mudanças necessárias. Caso ele não faça isso, a solução de seus problemas demorará muito mais do que o necessário. É preciso que ele tome cuidado para não fazer em anos o que poderia fazer em meses.')
	    elif(caminho == 16):
	        sg.Print(odus['Odu 16'])
	        sg.Print('')
	        sg.Print('Quando aparece o odu Ìrẹtẹ̀ o jogo deverá ser encerrado. É praticamente nula a possibilidade de Ìrẹtẹ̀ abrir um jogo devidamente preparado do ponto de vista litúrgico. Sua compreensão depende de informações trazidas anteriormente pelo jogo. É muito preocupante quando algum desses quatro últimos odus acompanha uma situação problemática, conflitante, de muita aflição e muito desespero. Quando temos qualquer um deles no jogo de uma pessoa cuja realidade de vida seja de muito sofrimento, angústia, depressão e doença, aí sim, a interpretação relativa ao estado emocional do consulente não nos deixa muito esperançosos. Mas se o consulente está bem, vivendo uma fase serena em sua vida, embora Ìrẹtẹ̀ tenha Obaluiaê e trate da questão da enfermidade, permanece a esperança de sorte e bem-estar.')


	    sg.Print('')    
	    sg.Print('Odu de Boa Sorte!!!')


	   
	tefa_ifa()

	#janela.close()
