## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the General section
# @details This class handles a collection of all functions that are listed in the General section in the documentation of the signal-cli-rest-api.
# There is no function for /v1/health because it's just an internal request for the docker container
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class General:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief List API information
	# @details Calls the API to get informations about the API
	# @return A @p dict in json format
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def about(self) -> dict:
		
		r = requests.get(f"{self.address}:{self.port}/v1/about", headers={'Content-Type': 'application/json'})
		return r.json()
		
	## @brief List global configuration
	# @details Calls the API to get the current global configuration of the API
	# @return A @p dict in json format
	# @author Felix Hunne
	# @version 1.0
	# @date 2022-12-18
	def get_configuration(self) -> dict:
		
		r = requests.get(f"{self.address}:{self.port}/v1/configuration", headers={'Content-Type': 'application/json'})
		
		r = r.json()
		return r
	
	## @brief Set global configuration
	# @details Calls the API to set the global configuration of the API
	# @param	data	The data that should be set as global configuration, has to be a @p dict in json format
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def set_configuration(self, data: dict) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/configuration", headers={'Content-Type': 'application/json'}, json=data)
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief List number configuration
	# @details Calls the API to get the current number configuration
	# @return A @p dict in json format
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def get_number_configuration(self) -> dict:
		
		r = requests.get(f"{self.address}:{self.port}/v1/configuration/{self.number}/settings", headers={'Content-Type': 'application/json'})
		return r.json()
	
	## @brief Set number configuration
	# @details Calls the API to set the number configuration
	# @param	data	Teh data that should be set as number configuration, has to be a @p dict in json format
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def set_number_configuration(self, data: dict) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/configuration/{self.number}/settings", headers={'Content-Type': 'application/json'}, json=data)
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	
		
		
