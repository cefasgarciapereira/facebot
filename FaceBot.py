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
            print('['+str(self.id)+'] - '+str(msg))

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
        self.log('Navigating to post')
        self.driver.get(utils.post_url(id))
        is_valid = True
        
        try:
            is_valid = self.driver.find_element_by_xpath("//i[contains(@class,'img _7nyv')]")
            is_valid = False
        except:
            pass
        sleep(2)
        
        return is_valid
    
    def post_content(self):
        sleep(1)
        self.log('Extracting post content')
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


        return str(post_content)
    
    def post_reactions(self):
        self.log('Extracting post reactions')
        all_reactions = 0
        likes = 0
        love = 0
        wow = 0
        haha = 0
        sad = 0
        angry = 0
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
        gtens = {'K': 10e3, 'M': 10e6, 'B': 10e9}
        g = lambda x: int(float(x[:-1])*gtens[x[-1]])

        
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
            likes = self.driver.find_element_by_xpath(utils.likes_xpath).text
            likes = g(likes)
            likes = ''.join([n for n in likes if n.isdigit()])
        except:
            pass

        try:
            love = self.driver.find_element_by_xpath(utils.love_xpath).text
            love = g(love)
            love = ''.join([n for n in love if n.isdigit()])
        except:
            pass

        try:
            wow = self.driver.find_element_by_xpath(utils.wow_xpath).text
            wow = g(wow)
            wow = ''.join([n for n in wow if n.isdigit()])
        except:
            pass

        try:
            haha = self.driver.find_element_by_xpath(utils.haha_xpath).text
            haha = g(haha)
            haha = ''.join([n for n in haha if n.isdigit()])
        except:
            pass

        try:
            sad = self.driver.find_element_by_xpath(utils.sad_xpath).text
            sad = g(sad)
            sad = ''.join([n for n in sad if n.isdigit()])
        except:
            pass

        try:
            angry = self.driver.find_element_by_xpath(utils.angry_xpath).text
            angry = g(angry)
            angry = ''.join([n for n in angry if n.isdigit()])
        except:
            pass

        try:
            care = self.driver.find_element_by_xpath(utils.care_xpath).text
            care = g(care)
            care = ''.join([n for n in care if n.isdigit()])
        except:
            pass
        
        response = {
            "all": all_reactions,
            "likes": likes,
            "love": love,
            "wow": wow,
            "haha": haha,
            "sad": sad,
            "angry": angry,
            "care": care
        }
        
        return response
    
    def post_shares(self):
        self.log('Extracting post shares')
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
        
        return str(int(shares))
    
    def post_comments_deprecated(self):
        self.log('Extracting post comments')
        comments = []
        sleep(1)
        see_more = False
        total_time = 0

        def last_element_arr(arr):
            arr_size = len(arr)
            return arr[arr_size - 1]
        
        try:
            self.driver.find_element_by_class_name('_108_').get_property('href')
            see_more = True
        except:
            pass

        #load comments while the see_more is True and stop after 1 minute loading
        while (see_more and (total_time < 60)):
            last_post = last_element_arr(self.driver.find_elements_by_class_name('_2b06'))
            self.driver.find_element_by_class_name('_108_').click()
            sleep(2)
            total_time = total_time + 2

            #if the last post didn't change stop trying
            if(last_post == last_element_arr(self.driver.find_elements_by_class_name('_2b06'))):
                see_more = False
            
        try:
            comments = self.driver.find_elements_by_class_name('_2b06')
        except:
            self.log('Error during extract comments')
            pass

        if(see_more):
            self.log('Stoped because it was taking too long')
            return str(len(comments))+' +'

        return str(len(comments))
    
    def post_comments(self):
        self.log('Extracting post comments')
        self.driver.get('https://www.facebook.com/'+self.id)
        sleep_time = 1
        trying = True
        tries = 0
        comments = 0
        
        while trying and sleep_time <= 15 and comments == 0:
            tries = tries + 1
            sleep(sleep_time)
            self.log(str(tries)+'º try')
            try:
                comments = self.driver.find_element_by_xpath(utils.comments_xpath).text
                comments = comments.replace('Comments','')
                comments = comments.replace('K','000')
                comments = ''.join([n for n in comments if n.isdigit()])
                trying = False
            except Exception as err:
                sleep_time = sleep_time + 1
                pass
        
        return str(comments)


    def post_author(self):
        self.log('Extracting post author')
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

        return str(author)
    
    def post_date(self):
        self.log('Extracting post date')
        date = ''
        sleep(2)

        try:
            date = self.driver.find_element_by_tag_name("abbr").text
        except:
            pass

        return str(date)
    
    def is_fact_checked(self):
        self.log('Checking if the post is fact checked')
        response = False

        try:
            self.driver.find_element_by_xpath(utils.false_information_xpath).text
            response = True
        except:
            pass
        
        return response
    
    def post_info(self, is_valid=True):
        self.log('Extracting post info')
        fact_checked = self.is_fact_checked()
        author = self.post_author()
        date = self.post_date()
        content = self.post_content()
        shares = self.post_shares()
        reactions = self.post_reactions()
        comments = self.post_comments()

        info = {
            "id": self.id,
            "author": author,
            "date": date,
            "content": content,
            "comments": comments,
            "shares": shares,
            "reactions": reactions,
            "is_valid": is_valid,
            "fact_checked": fact_checked
        }
        self.log('\n')
        return info
    
    def set_post_id(self, id):
        self.id = id
    
    def close(self):
        self.log('Quiting facebook')
        self.driver.quit()