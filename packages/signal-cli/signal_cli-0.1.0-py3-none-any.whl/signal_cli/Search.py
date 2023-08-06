## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Search section
# @details This class handles a collection of all functions that are listed in the Search section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Search:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief Search numbers
	# @details Calls the API checking if the given numbers are registered with the Signal service or not. This isn't working correctly (2022-12-18)
	# @param	numbers	List of phone numbers to check
	# @return Either a @list with @dicts or a @dict
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def search(self, numbers: list[str]) -> Union[list[dict],dict]:
		
		r = requests.get(f"{self.address}:{self.port}/v1/search", headers={"Content-Type": "application/json"}, params={"numbers": numbers})
		
		r = r.json()
		return r
	
