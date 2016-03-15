import requests
import lxml
import json
from bs4 import BeautifulSoup
tree={}
fw=open('d.json','w')
tree['scholarships']={}
url_1='http://www.buddy4study.com/allscholarships'
url_2='http://www.buddy4study.com/scholarships/school'
url_3='http://www.buddy4study.com/scholarships/college'
url_4='http://www.buddy4study.com/scholarships/international'
url_5='http://www.buddy4study.com/scholarships/research'
tree['scholarships']['allscholarships']=[]
def scraping_1(url):
	response=requests.get(url)
	source=response.text
	soup=BeautifulSoup(source)
	for links in soup.findAll('div',attrs={'id':'scholarship-ajax'}):
		rows=links.findAll('div',attrs={'class':'row'})
		for row in rows:
			data=row.findAll('a')
			link=  data[0].get('href')
			#print data[0].get('href')
# 			name = data[1].text.strip()
# 			tree['scholarships']['allscholarships'].append(name)
scraping_1(url_1)
tree['scholarships']['schools']=[]		
def scraping_2(url):
	response=requests.get(url)
	source=response.text
	soup=BeautifulSoup(source)
	for links in soup.findAll('div',attrs={'id':'scholarship-ajax'}):
		rows=links.findAll('div',attrs={'class':'row'})
		for row in rows:
			data=row.findAll('a')
			node={}
			link= 'http://www.buddy4study.com'+data[1].get('href')
#			print link
 			name = data[1].text.strip()
 			node[link]=name
 			tree['scholarships']['schools'].append(node)
			

scraping_2(url_2)
tree['scholarships']['college']=[]		
def scraping_3(url):
	response=requests.get(url)
	source=response.text
	soup=BeautifulSoup(source)
	for links in soup.findAll('div',attrs={'id':'scholarship-ajax'}):
		rows=links.findAll('div',attrs={'class':'row'})
		for row in rows:
			node={}
			data=row.findAll('a')
			link= 'http://www.buddy4study.com'+data[0].get('href')
			name = data[1].text.strip()
			node[link]=name
			tree['scholarships']['college'].append(node)

			
scraping_3(url_3)
tree['scholarships']['international']=[]		
def scraping_4(url):
	response=requests.get(url)
	source=response.text
	soup=BeautifulSoup(source)
	for links in soup.findAll('div',attrs={'id':'scholarship-ajax'}):
		rows=links.findAll('div',attrs={'class':'row'})
		for row in rows:
			node={}
			data=row.findAll('a')
			link= 'http://www.buddy4study.com'+data[0].get('href')
			name = data[1].text.strip()
			node[link]=name
			tree['scholarships']['international'].append(node)

scraping_4(url_4)
tree['scholarships']['research']=[]		
def scraping_5(url):
	response=requests.get(url)
	source=response.text
	soup=BeautifulSoup(source)
	for links in soup.findAll('div',attrs={'id':'scholarship-ajax'}):
		rows=links.findAll('div',attrs={'class':'row'})
		for row in rows:
			data=row.findAll('a')
			link= 'http://www.buddy4study.com'+data[0].get('href')
			node={}
			name = data[1].text.strip()
			node[link]=name
			tree['scholarships']['research'].append(node)

scraping_5(url_5)		
fw=open('scrape.json','w')
json.dump(tree,fw,indent=2)
fw.close()
