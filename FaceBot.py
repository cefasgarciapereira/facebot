from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import utils

class FaceBot:
    
    def __init__(self, username, password, headless=False, log=False):
        self.username = username
        self.password = password
        self.id = ''
        self.loggin = log
        
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.headless = headless
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
        sleep(1)
        self.login()

    def log(self, msg):
        if(self.loggin):
            print(str(msg))

    def login(self):
        try:
            self.driver.get("https://www.facebook.com")
            sleep(2)
            self.driver.find_element_by_id("email").send_keys(self.username)
            self.driver.find_element_by_id("pass").send_keys(self.password)
            self.driver.find_element_by_name("login").click()
            self.log('Successfully logged into Facebook')
            sleep(2)
        except:
            self.log('Failed to log into Facebook')
    
    def navigate_to_post(self, id):
        self.id = id
        self.log('['+self.id+'] - Navigating to post')
        self.driver.get(utils.post_url(id))
        sleep(3)
    
    def post_content(self):
        self.log('['+self.id+'] - Extracting post content')
        content = self.driver.find_elements_by_tag_name('p')
        post_content = []

        try:
            for line in content:
                post_content.append(line.text)
            
            post_content = ' '.join(post_content)
        except:
            post_content = ''
        
        if(post_content == ''):
            try:
                post_content = self.driver.find_element_by_xpath("//div[@class='msg']//div").text
            except:
                post_content = ''


        return post_content
    
    def post_reactions(self):
        self.log('['+self.id+'] - Extracting post reactions')
        all_reactions = 0
        sad = 0
        angry = 0
        wow = 0
        likes = 0
        haha = 0
        love = 0
        care = 0
        sleep(1)

        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[2]/div/div/div[2]/a").click()
        except:
            try:
                self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[3]/a").click()
            except:
                try:
                    self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[2]/a").click()
                except:
                    self.log('[FAILED] - Extracting post reactions')
                    pass
        sleep(2)
        
        tens = {'K': 10e2, 'M': 10e6, 'B': 10e9}
        f = lambda x: int(float(x[:-1])*tens[x[-1]])
        
        try:
            all_reactions = self.driver.find_element_by_xpath(utils.all_reactions_xpath[0]).text
        except:
            try:
                all_reactions = self.driver.find_element_by_xpath(utils.all_reactions_xpath[1]).text
            except:
                pass

        try:
            all_reactions = all_reactions.replace('All','')
            all_reactions = f(all_reactions)
            all_reactions = ''.join([n for n in all_reactions if n.isdigit()])
        except:
            pass

        try:
            sad = self.driver.find_element_by_xpath(utils.sad_xpath).text
        except:
            pass

        try:
            angry = self.driver.find_element_by_xpath(utils.angry_xpath).text
            angry = ''.join([n for n in angry if n.isdigit()])
        except:
            pass

        try:
            wow = self.driver.find_element_by_xpath(utils.wow_xpath).text
            wow = ''.join([n for n in wow if n.isdigit()])
        except:
            pass

        try:
            likes = self.driver.find_element_by_xpath(utils.likes_xpath).text
            likes = ''.join([n for n in likes if n.isdigit()])
        except:
            pass
        
        try:
            haha = self.driver.find_element_by_xpath(utils.haha_xpath).text
            haha = ''.join([n for n in haha if n.isdigit()])
        except:
            pass
        
        try:
            love = self.driver.find_element_by_xpath(utils.love_xapth).text
            love = ''.join([n for n in love if n.isdigit()])
        except:
            pass

        try:
            care = self.driver.find_element_by_xpath(utils.care_xpath).text
            care = ''.join([n for n in love if n.isdigit()])
        except:
            pass

        reactions = {
            "all": all_reactions,
            "sad": sad,
            "angry": angry,
            "wow": wow,
            "likes": likes,
            "haha": haha,
            "love": love,
            "care": care
        }
        return reactions
    
    def post_shares(self):
        self.log('['+self.id+'] - Extracting post shares')
        shares = 0
        sleep(1)
        
        try:
            shares = self.driver.find_element_by_xpath(utils.shares_xpath).text
            shares = shares.replace('K', '000')
            shares = ''.join([n for n in shares if n.isdigit()])
        except:
            self.log('[FAILED] - Extracting post shares')
            pass
        sleep(1)
        
        return shares
    
    def post_author(self):
        self.log('['+self.id+'] - Extracting post author')
        author = ''  
        sleep(1)
        
        try:
            author = self.driver.find_element_by_xpath("//h3[contains(@class,'bh bi')]//a[1]").text
        except:
            pass
        
        if(author == ''):
            try:
                author = self.driver.find_element_by_tag_name("strong").text
            except:
                pass

        return author
    
    def post_date(self):
        self.log('['+self.id+'] - Extracting post date')
        date = ''
        sleep(2)

        try:
            date = self.driver.find_element_by_tag_name("abbr").text
        except:
            pass

        return date
    
    def post_info(self):
        self.log('\n['+self.id+'] - Extracting post info')
        author = self.post_author()
        date = self.post_date()
        content = self.post_content()
        shares = self.post_shares()
        reactions = self.post_reactions()

        info = {
            "id": self.id,
            "author": author,
            "date": date,
            "content": content,
            "shares": shares,
            "reactions": reactions
        }
        return info
    
    def set_post_id(self, id):
        self.id = id
    
    def close(self):
        self.log('Quiting facebook')
        self.driver.quit()
