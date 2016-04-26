from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests

while(True):
	print("Choice option: ")
	print("1. Start")
	print("2. Exit")
	op=int(input())
	if(op==1):
		print("Vessel name: ")
		nombre=input()
		print("Select Vessel Country: ")
		print("1. Australia")
		print("2. Colombia")
		print("3. Ecuador")
		print("4. Japan")
		print("5. Any")
		flag=int(input())
		if(flag==1):
			y="Australia"
		elif(flag==2):
			y="Colombia"
		elif(flag==3):
			y="Ecuador"
		elif(flag==4):
			y="Japan"
		else:
			y=""
		driver = webdriver.PhantomJS(executable_path=r'C:\Users\andre\node_modules\phantomjs\lib\phantom\bin\phantomjs')

		driver.get("http://www.wcpfc.int/record-fishing-vessel-database")

		#assert "Python" in driver.title

		if(flag<5):
		
			elem = driver.find_element_by_name("flag")
			select = Select(elem)
			select.select_by_value(y)
		
		elem = driver.find_element_by_name("name")
		elem.send_keys(nombre)


		elem.send_keys(Keys.RETURN)


		url=str(driver.current_url)
		r = requests.get(url)

		s = BeautifulSoup(r.text,'html.parser')
		#s=s.encode('ascii', 'ignore')
		tabla = s.find("table")
		trs = tabla.find_all('tr')

		t=[]
		#x.append(trs.get_text())

		for tr in trs:
			tds = tr.findAll('td')
			x=[]
			for i in tds:
				
				h=str(i.get_text()).strip()
				h=h.split("\n")

				x.append(h[0])
			t.append(x)
		#x=tds[0].findAll("a")
		#x=x.getText(" ")
		#print(tds[1].get_text())
		t=t[1:]
		
		print("\n\n\nTABLA DE RESULTADOS\n\n")
		print("Name\tVessel Country\tRegistration number\tAuth Period\tVassel type\tIRCS\tWIN\tVID\n")
		for i in t:
			acum=""
			for j in i:
				acum+=j+"    "
			print(acum)
		assert "No results found." not in driver.page_source
		driver.close()
		input("")
	else:
		
		break