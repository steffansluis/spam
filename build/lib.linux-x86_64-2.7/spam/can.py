import os.path
import json
from pprint import pprint
import subprocess

class Can(object):
	def __init__(self, location=None):
		self.location = location
		if location:
			self.name = os.path.basename(location)

	def install(self):
		self.product.install()

	def remove(self):
		self.product.remove()


	def to_hash(self):
		return info

	def save(self):
		can = self.to_hash()
		

	def clone(self):
		other = Can.from_hash(self.to_hash())
		other.location = self.location
		return other

	def destroy(self):
		os.path.remove(self.location)

	@staticmethod
	def from_hash(info):
		instance = Can()


		brand = getattr(__import__(info["brand"], globals(), locals(), [info["brand"]]), info["brand"])
		instance.product = brand(**info["product"])
		return instance


	@staticmethod
	def load(location):

		paths = [
			location,
			location+".can",
			os.path.join(os.path.realpath("./.shelf/"),location),
			os.path.join(os.path.realpath("./.shelf/"),location+".can"),
			os.path.join(os.path.realpath("~/.shelf/"),location),
			os.path.join(os.path.realpath("~/.shelf/"),location+".can"),

		]
		result = None

		for path in paths:
			print path
			if os.path.exists(path):
				result = path
				break

		if result:
			with open(result) as canfile:
				info = json.load(canfile)
			can = Can.from_hash(info)
			can.location = location
			can.name = os.path.basename(location)
			return can


		else:
			raise Exception("No canfile found for:", location)





