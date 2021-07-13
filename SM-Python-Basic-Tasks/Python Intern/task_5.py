# Task 5

# Use the BeautifulSoup and requests Python packages to print out a list of all the news titles on the https://news.ycombinator.com/.

#######################################################################################################################################################################

from bs4 import BeautifulSoup
import requests
  
# Website URL
URL = 'https://news.ycombinator.com/'

page = requests.get(URL)
#print(page.content)                                    # Page content from Website URL with HTML tags
soup = BeautifulSoup(page.content, "html.parser" )      # Page content from Website URL without HTML tags
all_news_titles = soup.find_all(class_="storylink")     # Finding only title of news on Website
for tag in all_news_titles:
    print(tag.getText())

