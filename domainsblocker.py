import time
from datetime import datetime

class DomainsBlocker:
	"""
		this is a class for blocking domains on a computer

		example:

		object = DomainsBlocker([domain, ])
		object.start(time start, time finish)
	"""
	hosts = r'C:\Windows\System32\drivers\etc\hosts'

	def __init__(self, blocked_sites):
		self.blocked_sites = blocked_sites

	def start (self, start, stop):
		self.start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, start)
		self.finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, stop)

		print(self.start_time)
		print(self.finish_time)

		redirect_url = '127.0.0.1'

		while True:
			if self.start_time < datetime.now() < self.finish_time:
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


block = DomainsBlocker(["www.youtube.com", "youtube.com"])
block.start(2, 10)