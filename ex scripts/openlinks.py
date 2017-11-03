#we want to load the beautiful soup module that we installed so we can use it in our script
#the module is named bs4 and it has multiple parts, but we just want to use the BeautifulSoup part
from bs4 import BeautifulSoup, 
import webbrowser
 
#we also want to have a way to talk to the internet so we need the request module too
import requests, re
 
#here is the URL to the browse button pages
all_urls = "https://digitalcollections.nypl.org/collections/art-and-artifacts-division-button-collection#/?tab=navigation" 
#lets ask requests to get that page, we can turn off the SSL too
button_page = requests.get(all_urls, verify=False)
 
#just let us know if that failed
if button_page.status_code != 200:
    print ("There was an error with", all_urls)
 
#we are storing the HTML of the page into the variable page_html using the .text attribute of the request result
page_html = button_page.text
urls = []
 
#now we are going to ask BS to parse the page
soup = BeautifulSoup(page_html, "html.parser")

all_item_divs = soup.find_all("div", attrs = {"class": "item"})
for a_div in all_item_divs:
# find the first <a> link
	title = a_div.find("a")
	urls.append(title['href'])
	# removes duplicate URLs-->https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
	urls = list(set(urls))
		
for a_url in urls:
	base_url = "https://digitalcollections.nypl.org" 
	lets_go = base_url + a_url 

	webbrowser.open(lets_go)


   # link = base_link+str(i)
   #  html_doc = requests.get(link, headers={'Cookie': 'PHPSESSID=notimportant'})
   #  soup = BeautifulSoup(html_doc.text,"lxml")
   #  bs_tags = soup.find_all("div",{"class":"msgline"})
   #  posts=[]
   #  for post in bs_tags:
   #      posts.append(post.text)
   #  print link
   #  print posts[0]



