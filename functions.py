import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.minimize_window()

def registro_spider(correo):
    driver.maximize_window()
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
    driver.maximize_window()
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

def reestablecer_spider(correo):
    driver.maximize_window()
    driver.get("https://www.spider.cl/")
    clk = driver.find_element_by_id("onesignal-slidedown-cancel-button").click()
    time.sleep(1)
    clk = driver.find_element_by_xpath("//*[@id='header']/div/nav/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a").click()
    time.sleep(1)
    clk = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[1]/form/div[5]/div[2]/a').click()
    time.sleep(5)
    usuario = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[1]/div/form/div[3]/input')
    usuario.clear()
    usuario.send_keys(correo)
    clk = driver.find_element_by_xpath('//*[@id="index"]/div[6]/div/div/div[2]/div[1]/div[1]/div/form/div[4]/button').click()

def cambiarPW_spider(correo, pw):
    letters = string.ascii_letters
    numbers = string.digits
    inicio_spider(correo, pw)
    clk = driver.find_element_by_xpath('//*[@id="header"]/div/nav/div[2]/div/div/div/div/div[2]/div/ul/li[1]/a').click()
    clk = driver.find_element_by_xpath('//*[@id="identity-link"]').click()
    pw_ant = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[4]/div[1]/div/input')
    pw_ant.clear()
    pw_ant.send_keys(pw)
    pw_new = driver.find_element_by_xpath('//*[@id="customer-form"]/section/div[5]/div[1]/div/input')
    pw_new.clear()
    pw_in = ''.join(random.choice(letters+numbers) for j in range(5))
    pw_new.send_keys(pw_in)
    print('Hay un campo Captcha que no permite realizar el cambio')

def ataque_spider(correo, intentos):
    driver.maximize_window()
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

    driver.maximize_window()
    letters = string.ascii_letters
    numbers = string.digits
    driver.get("https://www.atmosferasport.es/inicio-sesion")
    time.sleep(5)
    try:
        clk = driver.find_element_by_xpath("//*[@id='authentication']/div[6]/div/div/a").click()
    except:
        print("")
    usuario = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[1]/form/div/div[1]/input")
    usuario.clear()
    usuario.send_keys(correo)
    passwd = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[1]/form/div/div[2]/input")
    passwd.clear()
    pw_in = ''.join(random.choice(letters+numbers) for j in range(5))
    passwd.send_keys(pw_in)
    clk = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[1]/form/div/p[2]/button").click()
    time.sleep(5)
    for i in range(intentos-1):
        usuario = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[4]/div[1]/form/div/div[1]/input")
        usuario.clear()
        usuario.send_keys(correo)
        passwd = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[4]/div[1]/form/div/div[2]/input")
        passwd.clear()
        pw_in = ''.join(random.choice(letters+numbers) for j in range(5))
        passwd.send_keys(pw_in)
        clk = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[4]/div[1]/form/div/p[2]/button").click()
        time.sleep(2)
    time.sleep(5)
    driver.quit()


def reestablecer_atmosferasport(correo):
    driver.maximize_window()
    driver.get("https://www.atmosferasport.es/recuperacion-contrasena")
    
    #clk = driver.find_element_by_xpath('///*[@id="form_forgotpassword"]/fieldset/p/button').click()

def registro_atmosferasport(correo):
    driver.maximize_window()
    letters = string.ascii_letters
    numbers = string.digits
    pw_in = ''.join(random.choice(letters+numbers) for j in range(5))
    driver.get('https://www.atmosferasport.es/inicio-sesion')
    time.sleep(5)
    try:
        clk = driver.find_element_by_xpath('//*[@id="authentication"]/div[6]/div/div/a').click()
    except:
        print("")
    time.sleep(3)
    clk = driver.find_element_by_xpath('//*[@id="create-account_form_desktop"]/span').click()
    nombre = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/div[1]/div[1]/input')
    nombre.clear()
    nombre.send_keys('Tarea')
    apellido = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/div[1]/div[2]/input')
    apellido.clear()
    apellido.send_keys('Tarea')
    mail = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/div[1]/div[3]/input')
    mail.clear()
    mail.send_keys(correo)
    pw = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/div[1]/div[4]/input')
    pw.clear()
    pw.send_keys(pw_in)
    confirm_pw = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/div[1]/div[5]/input')
    confirm_pw.clear()
    confirm_pw.send_keys(pw_in)
    for i in range(5):
        try:
            clk = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/p[2]/input').click()
            break
        except:
            time.sleep(1)

    clk = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/form/div/div[2]/button').click()
    return correo, pw_in