def post_url(id):
    return 'https://m.facebook.com/story.php?story_fbid='+id+'&id=415518858611168&_rdr'

all_reactions_xpath = [
    "/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div/div/div/span[1]/span", 
    '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[5]/div/div/div/div[2]/a/div/div'
    ]
sad_xpath = "//*[@id='u_7_16']/span[1]"
love_xpath = "//*[@id='u_7_1b']/span[1]"
haha_xpath = "//*[@id='u_7_1a']/span[1]"
care_xpath = "/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div/div/div/span[5]/span/span"
likes_xpath = "//*[@id='u_7_19']"
wow_xpath = "//*[@id='u_7_18']"
angry_xpath = "//*[@id='u_7_17']/span[1]"
shares_xpath = "//div[@class='_43lx _55wr']//span[1]"
author_xpath = "//h3[contains(@class,'bh bi')]//a[1]"