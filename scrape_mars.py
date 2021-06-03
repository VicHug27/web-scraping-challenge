#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import dependencies and setup
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pymongo
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Step1 Scraping

# In[3]:


#NASA Mars News
url = "https://mars.nasa.gov/news/"
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')


# In[4]:


# Search for news title
t_results = soup.find_all('div', class_='content_title')

# Search for paragraph text under news titles
p_results = soup.find_all('div', class_='article_teaser_body')

# Extract first title and paragraph, and assign to variables
title = t_results[0].text
paragraph = p_results[0].text

print(title)
print(paragraph)


# In[5]:


#JPL Mars image
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')
    
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
print(featured_image_url )


# In[6]:


#Mars Facts
url = 'https://space-facts.com/mars/'
facts = pd.read_html("https://space-facts.com/mars/")[0]
print(facts)


# In[7]:


#Mars Hemispheres
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# ### Step2 MongoDB and Flask

# In[ ]:




