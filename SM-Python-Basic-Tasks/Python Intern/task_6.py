# Task 6

# Write the Task 5 titles to the text file.

# Extras:
# Ask the user to specify the name of the output file that will be saved.


#######################################################################################################################################################################



from bs4 import BeautifulSoup
import requests
  
# Website URL
URL = 'https://news.ycombinator.com/'

page = requests.get(URL)
# print(page.content)                                    # Page content from Website URL with HTML tags
soup = BeautifulSoup(page.content, "html.parser" )      # Page content from Website URL without HTML tags
all_news_titles = soup.find_all(class_="storylink")     # Finding only title of news on Website

# Path of the directory where text file will be created
directory = "C:\\Users\\666n6666666666666i66\\Desktop\\Web Scraping\\"
  
# Get fileName from user
filepath = directory + input("Enter filename: ")
  
# Create a new file
with open(filepath, 'w+') as fp:
    pass

# Write content to file
file = open(filepath, "w")
for tag in all_news_titles:
    file.write(tag.getText())
file.flush()
file.close
