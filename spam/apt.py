import subprocess

class apt(object):

	self.default_values:

	def __init__(self, packages):
		self.packages = packages.split()

	def install(self):
		subprocess.call("sudo apt-get install "+self.package, shell=True)

	def remove(self):
		subprocess.call("sudo apt-get remove "+self.package, shell=True)

	def to_hash(self):
		return {"packages": " ".join(self.packages) }

	@cli_attribute("-n", "Package name")
	def set_package_name(self, ):
