#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Import libraries
import requests
from bs4 import BeautifulSoup


# In[77]:


# Collect first page of artists’ list
page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')


# In[78]:


# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')


# In[79]:


# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()


# In[80]:


import csv
f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])


# In[81]:


# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')


# In[82]:


# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find_all('a')


# In[83]:


#Use .contents to pull out the <a> tag’s children
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    links = 'https://web.archive.org' + artist_name.get('href')
    print(names)
    print(links)
    
# Add each artist’s name and associated link to a row
    f.writerow([names, links])


# In[ ]:





# In[ ]:




