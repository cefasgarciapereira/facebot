from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class FaceBot:
    
    def __init__(self, username, password, headless=False, log=False):
        self.username = username
        self.password = password
        self.id = ''
        self.loggin = log
        
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

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
        except:
            self.log('Failed to log into Facebook')
    
    def post_content(self):
        self.log('['+self.id+'] - Extracting post content')
        sleep(1)
        self.driver.get('https://mbasic.facebook.com/story.php?story_fbid='+self.id+'&id=415518858611168')
        sleep(2)
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
        sleep(1)
        
        try:
            self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[3]/a").click()
        except:
            try:
                self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/div[2]/a").click()
            except:
                self.log('[FAILED] - Extracting post reactions')
                pass
        sleep(2)
        
        all_reactions = 0
        sad = 0
        angry = 0
        wow = 0
        likes = 0
        haha = 0
        love = 0
        
        try:
            all_reactions = self.driver.find_element_by_xpath("//a[@class='z ba']").text
            if(all_reactions.contains('K')):
                all_reactions = ''.join([n for n in all_reactions if n.isdigit()])
        except:
            pass

        try:
            sad = self.driver.find_element_by_xpath("//img[@alt='Sad']/following-sibling::span[1]").text
            sad = ''.join([n for n in sad if n.isdigit()])
        except:
            pass

        try:
            angry = self.driver.find_element_by_xpath("//img[@alt='Angry']/following-sibling::span[1]").text
            angry = ''.join([n for n in angry if n.isdigit()])
        except:
            pass

        try:
            wow = self.driver.find_element_by_xpath("//img[@alt='Wow']/following-sibling::span[1]").text
            wow = ''.join([n for n in wow if n.isdigit()])
        except:
            pass

        try:
            likes = self.driver.find_element_by_xpath("//img[@alt='Like']/following-sibling::span[1]").text
            likes = ''.join([n for n in likes if n.isdigit()])
        except:
            pass
        
        try:
            haha = self.driver.find_element_by_xpath("//img[@alt='Haha']/following-sibling::span[1]").text
            haha = ''.join([n for n in haha if n.isdigit()])
        except:
            pass
        
        try:
            love = self.driver.find_element_by_xpath("//img[@alt='Love']/following-sibling::span[1]").text
            love = ''.join([n for n in love if n.isdigit()])
        except:
            pass

        reactions = {
            "all": all_reactions,
            "sad": sad,
            "angry": angry,
            "wow": wow,
            "likes": likes,
            "haha": haha,
            "love": love
        }
        return reactions
    
    def post_shares(self):
        self.log('['+self.id+'] - Extracting post shares')
        sleep(1)
        self.driver.get('https://m.facebook.com/browse/shares?id='+self.id)
        sleep(2)
    
    def post_author(self, navigate=False):
        self.log('['+self.id+'] - Extracting post author')
        author = ''

        if(navigate):
            sleep(1)
            self.driver.get('https://mbasic.facebook.com/story.php?story_fbid='+self.id+'&id=415518858611168')        
        
        sleep(2)
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
    
    def post_date(self, navigate=False):
        self.log('['+self.id+'] - Extracting post date')
        date = ''

        if(navigate):
            sleep(1)
            self.driver.get('https://mbasic.facebook.com/story.php?story_fbid='+id+'&id=415518858611168')
        
        sleep(2)
        try:
            date = self.driver.find_element_by_tag_name("abbr").text
        except:
            pass

        return date
    
    def post_info(self):
        self.log('\n['+self.id+'] - Extracting post info')
        content = self.post_content()
        author = self.post_author()
        date = self.post_date()
        reactions = self.post_reactions()

        info = {
            "id": self.id,
            "author": author,
            "date": date,
            "content": content,
            "reactions": reactions
        }
        return info
    
    def set_post_id(self, id):
        self.id = id
    
    def logout(self):
        self.log('Quiting facebook')
        self.driver.quit()
