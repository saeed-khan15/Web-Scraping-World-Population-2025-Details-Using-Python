
# coding: utf-8

# In[2]:


#importing important libraries

import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[3]:


# URL of the page to scrape
url= 'https://www.worldometers.info/world-population/population-by-country/'


# Fetch page content
page= requests.get(url)

requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup)


# In[3]:





# In[4]:


# Locate the table

Table_class="datatable w-full border border-zinc-200"
    
table =   soup.find('table', class_= Table_class)


# In[5]:


# Extract table headers/column titles

table_head = table.find('thead')
table_head


# In[6]:


table_titles = []
for x in table_head.find_all('tr'):
    for y in x.find_all('th'):
        table_titles.append(y.text)
table_titles
        


# In[7]:


# Extract table rows/cell data

table_body = table.find('tbody')
table_data = []
for x in table_body.find_all('tr'):
    td_tags = x.find_all('td')
    td_val = [y.text for y in td_tags]
    table_data.append(td_val)
table_data


# In[8]:


# Create DataFrame

df = pd.DataFrame(table_data, columns=table_titles)
df.head()


# In[10]:


# Save to Excel and csv file

df.to_csv(r"E:\World_population_web_scraping\World_Population_Details.csv", index=False)
df.to_excel(r"E:\World_population_web_scraping\World_Population_Details.xlsx", index=False)

