from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class instaBot:
    def __init__(self , username , password):
        self.username  = username
        self.password  = password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        self.browser = webdriver.Chrome(options = chrome_options, executable_path = r'/home/aashutosh/Documents/webScrapingStuffs/chr webdriver/chromedriver')

    
    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com/')
        time.sleep(1)
        login_button = browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(1)
        input_username = browser.find_element_by_css_selector('input[name*="username"]')
        input_username.send_keys(self.username)
        time.sleep(1)
        input_password = browser.find_element_by_css_selector('input[name*="password"]')
        input_password.send_keys(self.password)
        time.sleep(1)
        input_password.send_keys(Keys.ENTER)
        
    def search_by_username(self , username ):
        time.sleep(2)
        self.username = username
        browser = self.browser
        browser.get('https://www.instagram.com/' +  username + '/')
        
    def search_by_hashtag(self , hashtag):
        time.sleep(2)
        self.hashtag = hashtag
        browser = self.browser
        browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        
    
    def scroll_and_collect_url(self):
        time.sleep(2)
        browser = self.browser
        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        last_height = browser.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
        time.sleep(2)    
        url = browser.find_elements_by_tag_name('a')
        global urls
        urls = [ u.get_attribute('href') for u in url if ('.com/p/') in u.get_attribute('href') ]
     
    def like(self):
        #like photos
        browser = self.browser
        for i in urls:
            browser.get(i)
            time.sleep(2)
            like_button = browser.find_element_by_css_selector('span[aria-label*="Like"]')
            time.sleep(1)
            like_button.click()
        
        
    def comment(self, my_comment):
        #comment photos
        browser = self.browser
        self.my_comment = my_comment
        for url in urls:
            browser.get(url)
            time.sleep(2)
            comment_input = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea')
            time.sleep(1)
            comment_input.click()
            time.sleep(1)
#             aria-label="Add a comment…"
            box = browser.find_element_by_class_name('Ypffh')
            time.sleep(1)
            box.send_keys(my_comment)
            time.sleep(1)
            box.send_keys(Keys.ENTER)
        

        
        
    def follow(self):
        #follow users
        browser = self.browser
        for url in urls:
            browser.get(url)
            time.sleep(2)
            follow_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/header/div[2]/div[1]/div[2]/button')
            time.sleep(1)
            follow_button.click()
        
    
        
        
ig = instaBot("USERNAME" , "PASSWORD")    
ig.login()
ig.search_by_username('techgirlhajar')
ig.scroll_and_collect_url()
# ig.like()
# ig.follow()
ig.comment('Hi Hajar!!')
