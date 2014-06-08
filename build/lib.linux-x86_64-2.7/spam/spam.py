from simpleCLI import *
from can import *
from shelf import *

class spam(simpleCLI):

	def __init__(self):
		super(spam, self).__init__()

		# self.registerCommand(self.test)
		# self.registerCommand(self.install)
		# self.registerCommand(self.remove)
		# self.registerCommand(self.register)

	@cli_command
	def test(self):
		print "This canopener is fully operational."

	@cli_command
	def install(self,canstring):
		print "Installing can:",canstring
		c = Can.load(canstring)

		c.install()

	@cli_command
	def remove(self,canstring):
		print "Removing can:",canstring
		c = Can.load(canstring)

		c.remove()

	@cli_command
	def register(self, canstring, shelfstring = "~/.shelf/"):
		c = Can.load(canstring)
		s = Shelf.load(shelfstring)
		s.store(c)

