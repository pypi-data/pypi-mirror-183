from importlib import metadata
import aiohttp
import aiofiles
import io
import json
from .errors import two_hundred_error as error
from typing import TYPE_CHECKING, Union, Optional
if TYPE_CHECKING:
	from typing_extensions import Self
	from typing import Any, Protocol
	from os import PathLike

	class FileLike(Protocol):
		def __call__(
			self,
			fp: Union[str, bytes, PathLike[Any], io.BufferedIOBase],
			filename: Optional[str] = None,
			**kwargs: Any,
		) -> Self:
			...

	class EmbedLike(Protocol):
		def __call__(
			self,
			**kwargs: Any,
		) -> Self:
			...
		def set_image(self, *, url: str) -> Self:
			pass

class Client:
	"""
	The client class for the randseal package containing everything (new in version 2.0.0)
	"""

	def __init__(self, session: aiohttp.ClientSession = None, session2: aiohttp.ClientSession = None):
		self.session = aiohttp.ClientSession(auto_decompress=False) or session
		self.session2 = aiohttp.ClientSession() or session2

	async def File(self, cls: FileLike):
		"""
		Returns a `File` of a seal (new in version 2.0.0, renamed in version 2.4.1)
		"""
		async with self.session.get(self.url) as r:
			if r.status == 200:
				hi = io.BytesIO(await r.read())
				return cls(fp=hi, filename=self.number + ".jpg")
			else:
				raise error


	def Embed(self, cls: EmbedLike):
		"""
		Returns an `Embed` of a seal which can be edited or used in a message

		Parameters
		----------

		:class:`cls`

		A py-cord `File` or a discord.py `File`
		"""
		return cls(colour=self.blank).set_image(url=self.url)

	@property
	def blank(self) -> int:
		return 0x2f3136

	async def jsonload(self, fp:
					aiofiles.threadpool.text.AsyncTextIOWrapper,
					**kwds,
					) -> dict | Any:
		"""Asynchronous `json.load()` using the `aiofiles` package (New in 1.3.0)"""
		return json.loads(s=await fp.read(), **kwds)

	async def jsondump(
		self,
		obj: dict | Any,
		fp: aiofiles.threadpool.text.AsyncTextIOWrapper,
		**kwds
	):
		"""Asynchronous `json.dump()` using the `aiofiles` package (New in 1.3.0)"""
		e = json.dumps(obj, **kwds)
		await fp.write(e)
		return e

	def __hash__(self):
		return hash(self)

	@property
	def advlink(self):
		import advlink
		return advlink.Link(f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg", session=self.session, session2=self.session2)

	@property
	def url(self):
		return f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg"

	@property
	def number(self):
		import random
		return f"{random.randrange(0, 82)}"

	def __str__(self):
		return f"https://raw.githubusercontent.com/mariohero24/randsealimgs/main/{self.number}.jpg"

	def __eq__(self, obj: object) -> bool:
		return str(self) == str(obj)

	def __int__(self):
		return int(self.number)

	def __ne__(self, obj: object) -> bool:
		return str(self) != str(obj)


__author__: str = "Guard Boi"
"""The author of the package"""

__description__: str = "Generates a random seal image for py-cord"
"""A short description of the package"""

__licence__: str = "MIT"
"""The licence type of the package"""

__version__ = metadata.version("randseal")
"""The version of the package"""

# python3 -m twine upload --repository pypi dist/*
