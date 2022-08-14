import time
from datetime import datetime

class DomainsBlocker:
	"""
		this is a class for blocking domains on a computer

		example:
			object = DomainsBlocker([domain,])
			object.start()

		setters:
			setdomain([domain,])
			settimeframe(start_time, finish_time)
	"""
	hosts = r'C:\Windows\System32\drivers\etc\hosts'

	def __init__(self, blocked_sites,
			start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour), 
			finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour + 1)):

		self.blocked_sites = blocked_sites
		self._start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, start_time)
		self._finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, finish_time)

	def setdomain(self, blocked_sites):
		self.blocked_sites = blocked_sites

	def settimeframe(self, start_time, finish_time):
		self._start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, start_time)
		self._finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, finish_time)

	def start (self):
		print(f'start_time: {self._start_time}\nfinish_time: {self._finish_time}')

		redirect_url = '127.0.0.1'

		while True:
			if self._start_time < datetime.now() < self._finish_time:
				print('Access closed!')

				with open(self.hosts, 'r+') as file:
					src = file.read()

					for site in self.blocked_sites:
						if site in src:
							pass
						else:
							file.write(f'{redirect_url} {site}\n')
			else:
				with open(self.hosts, 'r+') as file:
					src = file.readlines()
					file.seek(0)

					for line in src:
						if not any(site in line for site in self.blocked_sites):
							file.write(line)
					file.truncate()
				print('Access is open!')
			time.sleep(5)