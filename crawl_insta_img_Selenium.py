#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# In[8]:


#Other imports here
import os
import wget


# In[10]:


#connect webdriver to our notebook ('the path we want to copy')
driver = webdriver.Chrome('/home/elnaz/apps/chromedriver') #the path of chromdriver
driver.get("https://www.instagram.com/") #get the url


# In[11]:


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys(input('enter user name: '))
password.send_keys(input('enter password: '))


# In[12]:


#make brand new variable for our loggin. after loggin in click on loggin
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = 'submit']"))).click()


# In[13]:


#save login info? which button? yes or Not Now?
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()


# In[31]:


not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()


# In[36]:


searchpage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchpage.clear()
keyword = "#iran"
searchpage.send_keys(keyword)


# In[37]:


searchpage.send_keys(Keys.ENTER)


# In[52]:


#scroll down the page and save the images on your pc
driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_elements(by=By.TAG_NAME, value='img')
images 


# In[53]:


images = [image.get_attribute('src') for image in images]
images


# In[4]:


#save images to pc
path = os.getcwd()   #get the path to save
path = os.path.join(path, keyword[1:])
os.mkdir(path)
path


# In[5]:


#download with wget
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1


# In[6]:


#save images to pc
path = os.getcwd()   #get the path to save
path = os.path.join(path, keyword[1:])
os.mkdir(path)
path


# In[ ]:




