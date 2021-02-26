def post_url(id):
    return 'https://m.facebook.com/story.php?story_fbid='+str(id)+'&id=415518858611168&_rdr'

all_reactions_xpath = [
    "/html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div/div/div/span[1]/span", 
    '/html/body/div[1]/div/div[4]/div/div[1]/div/div/div/div[5]/div/div/div/div[2]/a/div/div'
    ]
likes_xpath = "//span[@data-store='{\"reactionType\":1}']//span"
love_xpath = "//span[@data-store='{\"reactionType\":2}']//span"
wow_xpath = "//span[@data-store='{\"reactionType\":3}']//span"
haha_xpath = "//span[@data-store='{\"reactionType\":4}']//span"
sad_xpath = "//span[@data-store='{\"reactionType\":7}']//span"
angry_xpath = "//span[@data-store='{\"reactionType\":8}']//span"
care_xpath = "//span[@data-store='{\"reactionType\":16}']//span"

shares_xpath = "//div[@class='_43lx _55wr']//span[1]"
author_xpath = "//h3[contains(@class,'bh bi')]//a[1]"
comments_xpath=["/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span", 
                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[5]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span",
                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div/span"
                ]
false_information_xpath = "//button[@value='See Why']"