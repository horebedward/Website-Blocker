import time
from datetime import datetime as dt
# host_temp = r'C:\Users\Horeb edward\Desktop\Python-projects\Website_blocker Project\hosts'
host_path = r'C:\Windows\System32\drivers\etc\hosts'
website_list = ['www.facebook.com','facebook.com']
redirect_path = '127.0.0.1'

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,00) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,6):
		print('Working hours...')
		time.sleep(5)
		with open(host_path, 'r+') as file:
			data = file.read()
			for website in website_list:
				if website in data:
					pass
				else:
					file.write(redirect_path+ ' '+website+'\n')
	else:
		
		with open(host_path, 'r+') as file:
			data = file.readlines()
			file.seek(0)
			for line in data:
				if not any(website in line for website in website_list):
					file.write(line)

			file.truncate()
		print('Fun hours...')
		time.sleep(5)



	