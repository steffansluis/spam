from git import *
import os.path
from os import rename

class Shelf(object):
	def __init__(self, shelfdir):
		self.shelfdir = shelfdir
		self.repo = Repo(shelfdir)

	def store(self, can):
		can.clone()
		c.save(self.shelfdir)

	def clone(self, can, clone_location):
		other = Can.from_hash(self.to_hash())
		other.location = clone_location + self.name

	def move(self, can, other_shelf):
		other_location = other_shelf.location
		can.clone(other_location)
		can.destroy()

	def install(self):
		pass

	def remove(self):
		pass

	def to_hash():
		return info

	def save():
		to_hash()


	@staticmethod
	def from_hash(info):
		instance = Can()


		brand = getattr(__import__(info["brand"], globals(), locals(), [info["brand"]]), info["brand"])
		instance.product = brand(**info["product"])
		return instance

	@staticmethod
	def load(location):

		paths = [
			os.path.realpath(os.path.expanduser(location)),
			os.path.realpath(os.path.expanduser("./.shelf/")),
			os.path.realpath(os.path.expanduser("~/.shelf/")),
		]

		result = None

		for path in paths:
			print path
			if os.path.exists(path):
				result = path
				break

		if result:
			instance = Shelf(result)

			return instance

		else:
			raise Exception("No shelf found for:", result)
