from .models import Database,Newinternship
from bs4 import BeautifulSoup
import requests
import re
import schedule
import time
import datetime

def scrap_domain(variable,domain):
    url="/internships/keywords-"+domain
    new_intern=0
    while len(url) > 1:
        url="http://internshala.com"+url
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
        container=soup.find_all("div",{"class":"container-fluid individual_internship"})
        e_date=datetime.datetime.now().date()+datetime.timedelta(15)
        present_date=(datetime.datetime.now().date())
        present_date=str(present_date)
	for items in container:
            date=items.find("div",{"class":"individual_internship_details"}).find("div",{"class":"table-responsive"}).find("table",{"class":"table"})
            end_date=date.find_all("td")[4].string.strip()
            header=items.find("div",{"class":"individual_internship_header"}).find_all("div",{"class":"table-cell"})
            category= (header[0].find_all("h4"))[0].string.strip()
            company=(header[0].find_all("h4"))[1].string.strip()
            url= "http://internshala.com"+(items.find("div",{"class":"button_container"}).find("a")["href"]).strip()
            variable=variable+1
            posted_date=date.find_all("td")[3].string.strip()
            posted_date=datetime.datetime.strptime(posted_date, '%d %b, %Y').strftime("%Y-%m-%d")
            if posted_date == present_date:
                new_intern=new_intern+1            
   		try:
	            if datetime.datetime.strptime(end_date, '%d %b, %Y'):
                        s=datetime.datetime.strptime(end_date, '%d %b, %Y')
		        end_date=s.strftime("%Y-%m-%d") 
		        d=Database(domain=domain,categary=category,company=company,url=url,end_date=end_date)
                        d.save()
                except ValueError:
             	    d=Database(domain=domain,categary=category,company=company,url=url,end_date=e_date)
		    d.save()
        url=soup.find("a",{"id":"navigation-forward"})["href"]
    Newinternship.objects.filter(domain=domain).delete
    d=Newinternship(domain=domain,newintern=new_intern)
    d.save()
    return variable

class Scrap:
    def scrap_full(self):
	count_full=0
        domain=["python","java","php","android","data_science","angular","node","ruby","javascript","cloud"]
        for i in domain:
            count_full=count_full+scrap_domain(0,i)
    def delete_full(self):
        present_date=(datetime.datetime.now().date())
        Database.objects.filter(end_date=present_date).delete()
            

