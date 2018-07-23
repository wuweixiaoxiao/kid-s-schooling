   # -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:37:19 2018

@author: weixiao
"""

from bs4 import BeautifulSoup
import requests
#import numpy
sclName=[None]         # school name
sclWeb=[None]    # school website
sclAdd=[None]         # school address
sclType=[None]       # school type
sclHouse=[None]
for index0 in range(218):
    url='https://www.greatschools.org/search/search.page?page='+str(index0+1)+'&q=ma&state=MA'
    r = requests.get(url, timeout=30)   #convert url to html
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html=r.text

    soup=BeautifulSoup(html,"html.parser")

    sN=soup.find_all("a",class_="open-sans_sb mbs font-size-medium rs-schoolName")
    # <a style="line-height: 1.1em" class="open-sans_sb mbs font-size-medium rs-schoolName" 
    # href="/massachusetts/quincy/4597-BCBS--Ma-Center-For-Children/">BCBS- Ma Center for Children</a>
    sAdd=soup.find_all("div",class_="hidden-xs font-size-small rs-schoolAddress")
    #<div class="hidden-xs font-size-small rs-schoolAddress">1 Enterprise Dr, Quincy, MA 02171</div>
    sType=soup.find_all("div",class_="prs fl ")
    # <div class="prs fl ">Private</div>
    sHouse=soup.find_all("a",class_="btn btn-default zillow-button clearfix db phm")
    #<a class="btn btn-default zillow-button clearfix db phm" rel="nofollow" target="_blank" href="https://www.zillow.com/MA-02171?cbpartner=Great+Schools&amp;utm_source=GreatSchools&amp;utm_medium=referral&amp;utm_campaign=schoolsearch">
    #              <span class="iconx16 i-16-blue-home mrs vat"></span>
    #              <span class="prl vat tac">Homes&nbsp;for&nbsp;sale</span></a>

    nMax=len(sN)
    sclNameT=[None]*nMax
    sclWebT=[None]*nMax
    sclAddT=[None]*nMax
    sclTypeT=[None]*nMax
    sclHouseT=[None]*nMax
    for index in range(len(sN)-1):
        sclNameT[index]=sN[index].string          # school name
        sclWebT[index]=sN[index].get("href")      # school website
        sclAddT[index]=sAdd[index].string         # school address
        sclTypeT[index]=sType[index].string       # school type
        sclHouseT[index]=sHouse[index].get("href")
        
    sclName.append(sclNameT)         # school name
    sclWeb.append(sclWebT)    # school website
    sclAdd.append(sclAddT)         # school address
    sclType.append(sclTypeT)       # school type
    sclHouse.append(sclHouseT)
