
<p align="center">
  <img src="https://blog.theodo.com/static/daf0a6158eac76e700891058b02de9cc/a79d3/facebook2.png" width="154">
  <h1 align="center">FaceBot</h1>
  <p align="center">
This project aims to circumvent the bureaucracy of using Facebook's GraphAPI. The idea is to be able to collect data from posts using your personal Facebook account.
</p>

## How to use it?
### Minimal Example
In this example, we log into Facebook and print the text content from one of Bill Gates' post.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
facebot.set_post_id('715923879327714')
post_content = facebot.post_content()
print(post_content)
facebot.close()

Output:
A lot has changed over the last 25 years (like the connected technology that has transformed society). A lot hasn’t (like my wardrobe): https://gatesnot.es/2Jnn0JR
```
### Post Content
Extracts the text content from a post, given its ID.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
facebot.set_post_id('715923879327714')
post_content = facebot.post_content()
print(post_content)
facebot.close()
```

### Post Reactions
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
facebot.set_post_id('post-id')
post_reactions = facebot.post_reactions()
print(post_reactions)
facebot.close()

Output:
'reactions': {
	'all': 1328, 
	'sad': 0, 
	'angry': 0, 
	'wow': 464, 
	'likes': 853, 
	'haha': 0, 
	'love': 11
}
```
### Post Date
Extracts the publication date of a post, given its id.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
facebot.set_post_id('715923879327714')
post_date = facebot.post_date()
print(post_date)
facebot.close()

Output:
November 29, 2020 at 4:15 PM
```
### Post Author
Extracts the publication author of a post, given its id.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
facebot.set_post_id('715923879327714')
poast_author = facebot.post_author()
print(post_author)
facebot.close()

Output:
Bill Gates
```

### Post Info
This method extract all the previous data and returns an object containing the result.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
facebot.set_post_id('715923879327714')
post_info = facebot.post_info()
print(post_info)
facebot.close()

Output:
{
'id': '715923879327714', 
'author': 'Bill Gates', 
'date': 'November 29, 2020 at 4:15 PM', 
'content': 'A lot has changed over the last 25 years (like the connected technology that has transformed society). A lot hasn’t (like my wardrobe): https://gatesnot.es/2Jnn0JR',
'reactions': {
		'all': 1328, 
		'sad': 0, 
		'angry': 0, 
		'wow': 464, 
		'likes': 853, 
		'haha': 0, 
		'love': 11
	}
}
```
### Multiple Posts
  You should always enter the `post_id`, perform all the interactions you want, and then inform the new id. This was thought to prevent you from having to log in to Facebook a lot and browsing becomes more natural.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here')
post_ids = ['first-post-id','second-post-id', 'third-post-id']

for post_id in post_ids:
	facebot.set_post_id(post_id)
	post_info = facebot.post_info()
	print(post_info)

facebot.close()
```

### Logging
  If you want to follow the steps of the program, you can set `FaceBot(log=True)` and the program will output the info about the execution.
```
from FaceBot import FaceBot

facebot = FaceBot('your-username-here','your-password-here', log=True)
...
facebot.close()
```

## Built With

* [Python](https://www.python.org/) - Python is a programming language that lets you work more quickly and integrate your systems more effectively.
* [Selenium](https://selenium-python.readthedocs.io/) - Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver.

## Author

* **Cefas Garcia Pereira** -- [GitHub](https://github.com/cefasgarciapereira)