from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import names
import string
from selenium.webdriver.common.proxy import Proxy, ProxyType

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

driver = webdriver.Firefox() # Creates browser to handle League registration
twitch = webdriver.Firefox() # Creates browser to handle Twitch registration

def genAccount(emailstr,usernamestr,passwordstr):
    
    # Starts by signing up on League site

    daystr = str(random.randrange(1,30))
    yearstr = str(random.randrange(1980,2001))
    time.sleep(5)
    driver.get("https://signup.na.leagueoflegends.com/en/signup/index#/")
    time.sleep(3)
    email = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[1]/input")
    email.click()
    email.send_keys(emailstr)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]").click()
    time.sleep(2)
    email.send_keys(Keys.ENTER)
    time.sleep(2)
    month = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[1]/div[2]/select")
    month.click()
    month.send_keys("A")
    day = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[1]/div[3]/select")
    day.click()
    day.send_keys(daystr)
    year = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[1]/div[4]/select")
    year.click()
    year.send_keys(yearstr)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[2]/button").click()
    time.sleep(2)
    username = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[1]/input")
    username.send_keys(usernamestr)
    password = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[2]/input")
    password.send_keys(passwordstr)
    password1 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[3]/input")
    password1.send_keys(passwordstr)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form/div[4]/label/div").click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/form/div[6]/button').click()

    input("Captcha Solved?")

    # Continues with creating account on Twitch

    twitch.get("https://www.twitch.tv/signup")
    time.sleep(3)
    username = twitch.find_element_by_xpath('//*[@id="signup-username"]')
    username.send_keys(usernamestr)
    password = twitch.find_element_by_xpath('//*[@id="password-input"]')
    password.send_keys(passwordstr)
    password1 = twitch.find_element_by_xpath('//*[@id="password-input-confirmation"]')
    password1.send_keys(passwordstr)

    month = twitch.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select')
    month.click()
    month.send_keys("A")

    day = twitch.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input')
    day.send_keys(daystr)

    year = twitch.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input')
    year.send_keys(yearstr)

    email = twitch.find_element_by_xpath('//*[@id="email-input"]')
    email.send_keys(emailstr)
    time.sleep(4)
    twitch.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div/div/div/div[3]/form/div/div[5]/button').click()
    input("Sign Up Completed?")

    twitch.get("https://www.twitch.tv/settings/connections#riot-connection")
    time.sleep(2)
    main_page = twitch.current_window_handle
    time.sleep(3)
    twitch.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div[2]/div[4]/div/div[2]/div[1]/button/div/div").click()
    time.sleep(6)

    # Trys to connect the League and Twitch account

    try:
        for handle in twitch.window_handles: 
            if handle != main_page: 
                login_page = handle 
        twitch.switch_to.window(login_page)
        try:
            time.sleep(1)
            twitch.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div[1]/button').click()
        except Exception:
            time.sleep(1)
            username = twitch.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/input')
            username.send_keys(usernamestr)
            password = twitch.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/input')
            password.send_keys(passwordstr)
            twitch.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/button').click()
            time.sleep(2)
            twitch.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/div[1]/button').click()
            time.sleep(3)
    except Exception:
        pass

    input("Connection Successful?")
    twitch.switch_to.window(main_page)
    time.sleep(3)

    twitch.get('https://www.twitch.tv/settings/profile')
    time.sleep(2)
    twitch.find_element_by_xpath('/html/body/div[1]/div/div[2]/nav/div/div[3]/div[6]/div/div/div/div[1]/button').click()
    time.sleep(2)
    twitch.delete_all_cookies()

def main():

    # Takes in email domain and generates random username, email, and password

    catchall = input("Catchall? ")
    while True:
        username = names.get_first_name() + names.get_last_name() + str(random.randrange(100,500))
        emailstr = username + "@" + str(catchall)
        usernamestr = username
        passwordstr = randomString(12) + str(random.randrange(1,300))
        print(emailstr, usernamestr, passwordstr)
        genAccount(emailstr, usernamestr, passwordstr)
        print("CHANGE PROXY ON TWITCH BROWSER!")
        input("Repeat? (if no ctrl+c)")

main()