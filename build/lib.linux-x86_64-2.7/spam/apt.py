import subprocess

class apt(object):
	def __init__(self, package):
		self.package = package

	def install(self):
		subprocess.call("sudo apt-get install "+self.package, shell=True)

	def remove(self):
		subprocess.call("sudo apt-get remove "+self.package, shell=True)