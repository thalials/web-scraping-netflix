from selenium import webdriver
import random
from time import sleep

url = 'https://www.netflix.com/browse'

############# ALTERE ESSES CAMPOS ###################
email = 'coloque aqui seu email'
senha = 'coloque aqui sua senha'
#######################################################

generos = ["romance", "terror", "comedia", "ação", "drama", "policiais", "documentário"]

def get_data():
	# driver = webdriver.Chrome("C:/webdrivers/chromedriver")
	chrome_options = webdriver.ChromeOptions()
	prefs = {"profile.default_content_setting_values.notifications" : 2}
	chrome_options.add_experimental_option("prefs",prefs)
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/webdrivers/chromedriver")
	driver.get(url)
	driver.maximize_window()

	# login e escolha do perfil 
	login = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
	print(login)
	login.send_keys(email)
	password = driver.find_element_by_id('id_password')
	password.send_keys(senha)
	driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()

	sleep(5)
	driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a').click()

	source = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button')
	source.click()

	genero_escolhido = random.choice(generos)
	input_genero = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/input')
	input_genero.send_keys(genero_escolhido)
	sleep(2)

	linhas = list(range(0, 50))
	linha_escolhida = random.choice(linhas)

	filme = driver.find_element_by_xpath('//*[@id="title-card-0-{0}"]/div[1]/a'.format(linha_escolhida))
	filme.click()

	sleep(2)
	assistir = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[1]/a')
	assistir.click()
	sleep(100)
	# full_screen = driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div > div > div.nfp.AkiraPlayer > div > div.PlayerControlsNeo__layout.PlayerControlsNeo__layout--inactive.PlayerControlsNeo__layout--dimmed > div > div.PlayerControlsNeo__core-controls > div.PlayerControlsNeo__bottom-controls.PlayerControlsNeo__bottom-controls--faded > div.PlayerControlsNeo__button-control-row > button.touchable.PlayerControls--control-element.nfp-button-control.default-control-button.button-nfplayerFullscreen')
	# full_screen.click()

	# while(True):
	# 	time_remainder = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div[5]/div[2]/div[1]/div/div[2]/time').text

	# 	if  time_remainder == '0:00':
	# 		break

get_data()