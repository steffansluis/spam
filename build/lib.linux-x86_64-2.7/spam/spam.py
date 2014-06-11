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
	def install(self,can_location):
		print "Installing can:",can_location
		c = Can.load(can_location)

		c.install()

	@cli_command
	def remove(self,can_location):
		print "Removing can:",can_location
		c = Can.load(can_location)

		c.remove()

	@cli_command
	def register(self, can_location, shelf_location = None):
		c = Can.load(can_location)
		s = Shelf.load(shelf_location)
		s.store(c)

