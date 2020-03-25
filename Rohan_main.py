"""Created on Wed Mar 25 16:29:13 2020
@author: Arafat Rohan
"""
from selenium import webdriver
from time import sleep

class InstBot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.pw = pw
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys(pw)     
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath('//html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        sleep(2)
        #sugs = self.driver.find_element_by_xpath("//h4[contains(text(),Suggestions)]")
        #sleep(2)
        #self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht,ht = 0,1
        while last_ht != ht:
            last_h = ht
            sleep(1)
            ht = self.driver.execute_script("""
                                           arguments[0].scrollTo(0,arguments[0].scrollHeight);
                                          return arguments[0].scrollHeight;
                                            """,scroll_box)
            
        
#InstBot()       
my_bot = InstBot('YOUR_USERNAME','YOUR_PASSWORD')
my_bot.get_unfollowers()                 
        


#//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a
#/html/body/div[1]/section/main/div/header/section/ul/li[3]/a