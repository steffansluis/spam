import os.path
import json
from pprint import pprint
import subprocess

class can(object):
	def __init__(self, location):
		self.location = self.test_location(location)
		with open(self.location) as canfile:
			info = json.load(canfile) 
		
		brand = getattr(__import__(info["brand"], globals(), locals(), [info["brand"]]), info["brand"])
		self.product = brand(**info["product"])

	def install(self):
		self.product.install()
	
	def remove(self):	
		self.product.remove()

	def test_location(self, location):
		paths = [
			location, 
			location+".can",
			os.path.join(os.path.expanduser("~/.cans/"),location),
			os.path.join(os.path.expanduser("~/.cans/"),location+".can"),
		]
		result = None
		
		for path in paths:
			if os.path.exists(path):
				result = path

		if result:
			return result
		else:
			print "No canfile found for:",location