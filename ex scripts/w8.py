from bs4 import BeautifulSoup
import requests, re, json
 
#here is the URL to the browse collection pages
start_url = "https://digitalcollections.nypl.org/collections/art-and-artifacts-division-button-collection#/?tab=navigation" 
#lets ask requests to get that page, we can turn off the SSL too
collection_page = requests.get(start_url, verify=False)

urls = []
page_html = collection_page.text
soup = BeautifulSoup(page_html, "html.parser")
 
all_item_divs = soup.find_all("div", attrs = {"class": "item"})
for a_div in all_item_divs:
# find the first <a> link
   item = a_div.find("a")
   a_item = item['href']
   base_url = "https://digitalcollections.nypl.org" 
   lets_go = base_url + a_item
   urls.append(lets_go)
   urls = list(set(urls))

all_data = []

for get_names in urls:
   # Make a get request
   one_item = requests.get(get_names, verify=False)
   a_page_html = one_item.text
   soup = BeautifulSoup(a_page_html, "html.parser")
   title = soup.find("h1")
   print(title.text)


   all_item_list = soup.find('div', attrs = {"id": "item-content-data"})
   all_dts = all_item_list.find_all("dt")
   all_dds = all_item_list.find_all("dd")

   counter = 0

   for a_dt in all_dts:
      counter = counter + 1
      # print(a_dt)
      if a_dt.text == "Topics":
         print(a_dt.text)
         value = all_dds[counter]
         print(value)

# add it to our list, make a dict for this entry
   # this_data = {'title': title.text, 'topic': value} 
   # 'data': a_fact.text}
#    all_data.append(this_data)


# json.dump(all_data,open('pin_data.json','w'),indent=4)

        


# # # #find all the spans with class grid-item-inner
# # all_item_divs = soup.find_all("div", attrs = {"class": "item"})
# # for a_div in all_item_divs:
# # # find the first <a> link
# #    title = a_div.find("a")
# #    print(title['title'])
# #    print(title['href'])
