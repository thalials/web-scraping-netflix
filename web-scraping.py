# imports
from selenium import webdriver # web scraping
import random
from time import sleep

# url que você quer acessar
url = 'https://www.netflix.com/browse'

##### ALTERE ESSES CAMPOS ######
email = 'coloque aqui seu email'
senha = 'coloque aqui sua senha'
################################

# escreva aqui alguns gêneros 
# aleatórios de sua preferência
generos = ["romance", "terror", "comedia", "ação", "drama", "policiais", "documentário"]

# função que será chamada no final 
def assistir_filme():

	# Aqui são feitas algumas configurações 
	# para evitar que apareça a barra de 
	# notificações que pergunta se você
	# permite ou não mostrar a sua localização 
	chrome_options = webdriver.ChromeOptions()
	pref = {"profile.default_content_setting_values.notifications":2}
	chrome_options.add_experimental_option("pref",pref)
	driver = webdriver.Chrome(chrome_options=chrome_options,
							 executable_path="C:/webdrivers/chromedriver")

	# A função .get() é responsável por "ler" todo
	# o HTML da url que você quer acessar. 
	# Enquanto você vê imagens, o seu código vê o HTML :) 
	driver.get(url)

	# maximiza a tela para ficar de acordo com
	# o tamanho da tela do seu PC
	driver.maximize_window()

	### login e escolha do perfil ### 
	# find_element_by_xpath() é uma função do selenium 
	# que te permite acessar o caminho que você 
	# quer achar. Nesse caso, queremos o campo de login.
	# Para achar o caminho, você deve olhar o html
	# do site (use o Inspect)
	login = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
	login.send_keys(email)
	password = driver.find_element_by_id('id_password')
	password.send_keys(senha)
	
	# a função click() server para clicar em algum botão! 
	# nesse caso, o botão de login
	driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()

	# Você vai ver diversas vezes a função sleep() por aqui.
	# Ela serve pra fazer com que o código "durma" (literalmente)
	# enquanto a página carrega. Caso não fosse usada a função,
	# poderia ocorrer de a página não ser carregada completamente 
	# (internet não cooperando, por exemplo), o que impediria 
	# seu código de achar o xpath (caminho) abaixo.
	sleep(5)

	# Selecione o perfil que você quer acessar encontrando o 
	# xpath dele no HTML (Use o Inspect) =]
	driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a').click()

	# Aqui você vai levar seu programa para clicar na barrinha 
	# de pesquisa da netflix
	source = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button')
	source.click()

	# essa biblioteca random te ajuda a escolher um gênero ALEATÓRICO
	# da lista "generos" que declaramos lá em cima!
	genero_escolhido = random.choice(generos)

	# Com o genero escolhido, é possivel colocar ele la barrinha 
	# de pesquisa e achar filmes que estão associados a esse gênero
	# (por isso, escolha genêros que vc gosta hehe)
	input_genero = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/input')
	input_genero.send_keys(genero_escolhido)

	# olha o sleep de novo por aqui
	sleep(2)

	# nessa parte, é escolhido um filme aleatória dentre 
	# as 50 primeiras linhas com filmes que existem na sua pagina!
	# OBS: Altere esse valor se vc quiser mais filmes!
	linhas = list(range(0, 50))
	linha_escolhida = random.choice(linhas)

	filme = driver.find_element_by_xpath(
		'//*[@id="title-card-0-{0}"]/div[1]/a'.format(linha_escolhida))
	filme.click()

	# Clique no botão de assistir! Agora é só curtir 
	# e assistir o seu filme enquanto come uma pipoquinha :)
	sleep(2)
	assistir = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[1]/a')
	assistir.click()

	# AH! SEU FILME VAI DURAR SÓ 100 segundos. Então, 
	# sugiro fortemente que altere esse valor rsrs
	sleep(100)

# chamada da função pra que tudo acima 
# possa rodar de boa
assistir_filme()