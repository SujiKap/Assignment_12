# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
import os
import pandas as pd

def init_browser():
    executable_path = {'executable_path': r"C:\Users\kapali_s\Documents\SMU\chromedriver.exe"}
    return Browser('chrome', **executable_path, headless=False)

#do work
def scrape():
    masterDict = {}
    
    #call sub scrape functions
    news = scrape_news()
    featured = scrape_featured()    
    weather =scrape_weather()
    facts = scrape_facts()
    hemis = scrape_hemis()
    
    
    #create master dict for mongo
    masterDict["news_title"] = news["news_title"]
    masterDict["news_p"] = news["news_p"]
    masterDict["featured_image_url"] = featured["featured_image_url"]
    masterDict["tweet_text"] = weather["js-tweet-text"]
    masterDict["html_table"] = facts["html_table"]
    masterDict["title_1"] = hemis["title_1"]
    masterDict["title_2"] = hemis["title_2"]
    masterDict["title_3"] = hemis["title_3"]
    masterDict["title_4"] = hemis["title_4"]
    
    
    return masterDict


def scrape_news():
    browser = init_browser()
    listings = {}
    
  # NASA MARS NEWS

    #Url of the page to be scraped
    url = 'https://mars.nasa.gov/news/'

    browser.visit(url)
    html = browser.html
    #Create BeautifulSoup object; parse 
    soup = bs(html, 'html.parser')

    #Extract title texts
    listings["news_title"] = soup.find('div', class_='content_title').text
    #Paragraph Text. 
    listings["news_p"] = soup.find('div', class_='article_teaser_body').text
    browser.quit()
    return listings


# # JPL Mars Space Images - Featured Image

# +
#executable_path = {'executable_path': r"C:\Users\kapali_s\Documents\SMU\chromedriver.exe"}
#browser = Browser('chrome', **executable_path, headless=False)
# -

def scrape_featured():
    browser = init_browser()
    listings = {}
    
    # Mars Space Images
    url = 'https://www.jpl.nasa.gov/spaceimages'
    browser.visit(url)
    html = browser.html
    #Create BeautifulSoup object; parse 
    soup = bs(html, 'html.parser')

    #image url of the current featured Mars Image
    featured_image = soup.find('a', class_='button fancybox')['data-fancybox-href']
    featured_image

    featured_image_url = 'https://www.jpl.nasa.gov/' + featured_image
    featured_image_url

    #Extract images
    listings["featured_image_url"] = 'https://www.jpl.nasa.gov/' + featured_image
    browser.quit()
    return listings


# # Mars Weather
#

# +
#executable_path = {'executable_path': r"C:\Users\kapali_s\Documents\SMU\chromedriver.exe"}
#browser = Browser('chrome', **executable_path, headless=False)
# -

def scrape_weather():
    browser = init_browser()
    listings = {}

    #url to be scraped
    url = 'https://twitter.com/marswxreport'
    browser.visit(url)
    html = browser.html

    #Create BeautifulSoup object; parse 
    soup = BeautifulSoup(html, 'html.parser')

    #Print all classes
    results = soup.find(class_="js-tweet-text")
    for result in results:
        print(result)

    #Extract test
    listings["js-tweet-text"] = soup.find(class_="js-tweet-text").text
    browser.quit()
    return listings


# # Mars Facts

# +
#executable_path = {'executable_path': r"C:\Users\kapali_s\Documents\SMU\chromedriver.exe"}
#browser = Browser('chrome', **executable_path, headless=False)
# -

def scrape_facts():
    browser = init_browser()
    listings = {}

    #url to be scraped
    url = 'https://space-facts.com/mars/'

    #Use pandas 'read_html' to parse the url
    tables = pd.read_html(url)
    tables

    #make a table
    df = tables[0]
    df.columns = ["Description", "Values"]
    df.head(9)

    #Convert to html string
    html_table = df.to_html()
    html_table

    #Extract table
    listings["html_table"] = html_table
    browser.quit()
    return listings



# # Mars Hemispheres

def scrape_hemis():
    browser = init_browser()
    listings = {}
    #urls to be scraped by order

    url_1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_1)
    html = browser.html
    #Create BeautifulSoup object; parse 
    soup = bs(html, 'html.parser')#image url of the current featured Mars Image
    title_1 = soup.find('h2', class_='title').text
    title_1
    image_1 = soup.find('img', class_='wide-image')['src']
    featured_image_1 = 'https://astrogeology.usgs.gov' + image_1
    featured_image_1

    url_2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_2)
    html = browser.html
    #Create BeautifulSoup object; parse 
    soup = bs(html, 'html.parser')#image url of the current featured Mars Image
    title_2 = soup.find('h2', class_='title').text
    title_2
    image_2 = soup.find('img', class_='wide-image')['src']
    featured_image_2 = 'https://astrogeology.usgs.gov' + image_2
    featured_image_2

    url_3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_3)
    html = browser.html
    #Create BeautifulSoup object; parse 
    soup = bs(html, 'html.parser')#image url of the current featured Mars Image
    title_3 = soup.find('h2', class_='title').text
    title_3
    image_3 = soup.find('img', class_='wide-image')['src']
    featured_image_3 = 'https://astrogeology.usgs.gov' + image_3
    featured_image_3

    url_4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_4)
    html = browser.html
    #Create BeautifulSoup object; parse 
    soup = bs(html, 'html.parser')#image url of the current featured Mars Image
    title_4 = soup.find('h2', class_='title').text
    title_4
    image_4 = soup.find('img', class_='wide-image')['src']
    featured_image_4 = 'https://astrogeology.usgs.gov' + image_4
    featured_image_4

    hemisphere_image_urls  = [{"title": title_1, "img_url": featured_image_1},
                                      {"title": title_2, "img_url": featured_image_2},
                                      {"title": title_3, "img_url": featured_image_3},
                                      {"title": title_4, "img_url": featured_image_4}

                             ]

    #Extract images
    listings["title_1"] = 'https://astrogeology.usgs.gov' + image_1
    listings["title_2"] = 'https://astrogeology.usgs.gov' + image_2
    listings["title_3"] = 'https://astrogeology.usgs.gov' + image_3
    listings["title_4"] = 'https://astrogeology.usgs.gov' + image_4
    browser.quit()
    return listings

