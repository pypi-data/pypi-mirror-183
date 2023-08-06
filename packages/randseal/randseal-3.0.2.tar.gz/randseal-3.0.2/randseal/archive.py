"""Removed features"""

import discord, io, random
def File():
	"""
	Returns a `discord.File()` of a seal for py-cord in a potentially blocking way
	"""
	import requests
	sealrand = f"{random.randrange(0, 82)}"
	r = requests.get(
		f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg", stream=True)
	return discord.File(fp=io.BytesIO(r.content), filename=sealrand + ".jpg")