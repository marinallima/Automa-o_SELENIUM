#!/usr/bin/env python
# coding: utf-8

# # Automação Web com Selenium
# 
# ## Python + Selenium
# 
# 2 requisitos:
# 
# Instalar o Selenium
# Webdriver Manager

# In[1]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)


# In[2]:


# Passo 1:
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium")


# In[3]:


# Passo 2:
navegador.find_element('xpath', 
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Marina")


# In[4]:


navegador.find_element('xpath', 
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("lima.marinacosta@gmail.com")


# In[5]:


navegador.find_element('xpath', 
                       '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("6234567897")


# In[6]:


# Passo 3:
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()


# In[ ]:




