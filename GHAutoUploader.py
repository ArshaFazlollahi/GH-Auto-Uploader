from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os

replink = input("Please enter the link to your GitHub repository: ")
usr = input("Please enter your GitHub username/email: ")
pss = input("Please enter your GitHub password: ")
folname = input("The name of the folder being uploaded: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(replink)
print(driver.title)

link = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a')
link.click()

user = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_field"]')))
user.send_keys(usr)

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(pss)

sign = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]')
sign.click()

add = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[1]/div[2]/details')))
add.click()

create = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[1]/div[2]/details/div/ul/li[3]/form/button')
create.click()

folder = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/form[2]/div/div[1]/span/input')
folder.send_keys(folname + "/ignore")

commit = driver.find_element(By.XPATH, '//*[@id="submit-file"]')
commit.click()

add2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[1]/div[4]/details[1]/summary/span[1]/span')
add2.click()

upload = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[1]/div[4]/details[1]/div/ul/li[4]/a')
upload.click()

upload2 = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[2]/form[2]/file-attachment/p')))
upload2.click()

time.sleep(1)

d = os.getcwd()

pyautogui.write(d + r'\ ' + folname)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('down')
pyautogui.press('up', presses = 100)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyDown('shiftleft')
pyautogui.keyDown('shiftright')
pyautogui.press('right', presses = 99)
pyautogui.keyUp('shiftleft')
pyautogui.keyUp('shiftright')
pyautogui.press('enter')


progress = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[2]/div')

while True:

	if progress.is_displayed():

		while progress.is_displayed():
			print("Uploading...")

		commit2 = driver.find_element(By.XPATH,'//*[@id="repo-content-pjax-container"]/div/form/button');
		commit2.click()
		break

lst = os.listdir(d + r'\ '.strip() + folname)
nof = len(lst)

nouf = 0
count = 0

while nouf < nof:

	nouf = count * 99 + 99

	add3 = WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/span/a')))
	add3.click()

	add4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[1]/div[4]/details[1]/summary/span[1]/span')))
	add4.click()

	add5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[1]/div[4]/details[1]/div/ul/li[4]/a')))
	add5.click()

	#add5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repo-content-turbo-frame"]/div/div/div[1]/div[3]/details[1]/div/ul/li[4]/a')))
	#add5.click()

	upload3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[2]/form[2]/file-attachment/p')))
	upload3.click()

	time.sleep(1)

	d = os.getcwd()

	pyautogui.write(d + r'\ ' + folname)
	pyautogui.press('enter')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('tab')
	time.sleep(0.5)
	pyautogui.press('right')
	pyautogui.press('right')
	pyautogui.press('down')
	pyautogui.press('up', presses = 100)
	pyautogui.press('enter')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('right', presses = nouf)
	pyautogui.keyDown('shiftleft')
	pyautogui.keyDown('shiftright')
	pyautogui.press('right', presses = 99)
	pyautogui.keyUp('shiftleft')
	pyautogui.keyUp('shiftright')
	pyautogui.press('enter')

	progress = driver.find_element(By.XPATH, '//*[@id="repo-content-pjax-container"]/div/div[2]/div')

	while True:

		if progress.is_displayed():

			while progress.is_displayed():
				print("Uploading...")

			commit2 = driver.find_element(By.XPATH,'//*[@id="repo-content-pjax-container"]/div/form/button');
			commit2.click()
			break
	count = count + 1
