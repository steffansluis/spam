from simpleCLI import simpleCLI
from can import can

class spam(simpleCLI):
	def __init__(self):
		super(spam, self).__init__()
		
		self.registerCommand(self.test)
		self.registerCommand(self.install)
		self.registerCommand(self.remove)

	def test(self, message):
		print "This canopener is fully operational."

	def install(self,canstring):
		print "Installing can:",canstring
		c = can(canstring)

		c.install()

	def remove(self,canstring):
		print "Removing can:",canstring
		c = can(canstring)

		c.remove()