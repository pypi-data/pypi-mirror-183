## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Identities section
# @details This class handles a collection of all functions that are listed in the Identities section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Identities:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief List indentities
	# @details Calls the API to list all identities of known numbers
	# @return A @p list with dicts
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18	
	def list_identites(self) -> list[dict]:
		r = requests.get(f"{self.address}:{self.port}/v1/identities/{self.number}", headers={"Content-Type": "application/json"})
		
		r = r.json()
		return r
	
	## brief Trust identity
	# @details Calls the API to trust an identity
	# @param	number_to_trust			The number that should be trusted
	# @param	safety_number			The safety number between this and the to be trusted account
	# @param	trust_all_known_keys	<b>(Optional)</b> This sets if all known keys should be trusted. This argument defaults to @p False.
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def trust_identity(self, number_to_trust: str, safety_number: str, trust_all_known_keys: bool=False) -> Union[dict, str]:
		payload = {"trust_all_known_keys": trust_all_known_keys, "verified_safety_number": safety_number}
		
		r = requests.put(f"{self.address}:{self.port}/v1/identities/{self.number}/trust/{number_to_trust}", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
