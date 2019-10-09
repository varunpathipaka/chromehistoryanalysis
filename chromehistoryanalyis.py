# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:10:07 2019

@author: RROSHAN
"""

import os
import sqlite3

import operator

from collections import OrderedDict

import matplotlib.pyplot as plt




def parse_url(url):
    try:
        dom=url.split("//")
        web_name=dom[1].split("/",1)
        site=web_name[0].replace("www.","")
        return site
    except:
        printf("URL FORMAT ERROR!!!!!")

def plot_results(results):
   
    plt.bar(*zip(*results.items()))
    plt.xticks(rotation=90)
    
    plt.show()
   
        

    

data_path=os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
files=os.listdir(data_path)
history_db=os.path.join(data_path,'history')
print("trying to establish a database connection")
try:
    c=sqlite3.connect(history_db,timeout=10)
    cursor=c.cursor()
    select_statement="SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    cursor.execute(select_statement)
    result =cursor.fetchall()
    print("database connection is established")
    print(result[0])
    site_content={}
    for url,count in result:
        url=parse_url(url)
        if url in site_content:
            site_content[url]+=1
        else:
            site_content[url]=1
    #print(site_content)
    sites_count_sorted = OrderedDict(sorted(site_content.items(), key=operator.itemgetter(1), reverse=True))
   # print(sites_count_sorted)
    #Splot_results(sites_count_sorted)
    top_list={}
    count=0
    for k,v in sites_count_sorted.items():
        if count==10:
            break
        else:
            top_list[k]=v
            count=count+1
    plot_results(top_list)
            
        
  
        
        
    
except sqlite3.OperationalError:
    print("database is locked !!")
    print("close google chrome and run the script again")
    #quit()



    
    
    
    


