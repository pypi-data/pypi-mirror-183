## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Profiles section
# @details This class handles a collection of all functions that are listed in the Profiles section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Profiles:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief Update profile
	# @details Calls the API to update the profile
	# @param	**name		<b>(Optional)</b> The new name of the user associated with the number in the config. 
	# As this is a keyword argument, it has to be specified with <tt>name=\<name\></tt>, the data type is @p str. <b>One of the both arguments is necessary, two are optional!</b>
	# @param	**avatar	<b>(Optional)</b> The new avatar of the user associated with the number in the config as base64 string.
	# As this is a keyword argument, it has to be specified with <tt>avatar=\<avatar\></tt>, the data type is @p str. <b>One of the both arguments is necessary, two are optional!</b>
	# @return Either a @p dict in json format or a @p str. 
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18	
	def update_profile(self, **kwargs) -> Union[dict, str]:
		for key, value in kwargs.items():
			name = None
			avatar = None
			if key == "name":
				name = value
			elif key == "avatar":
				avatar = value
		if name == None and avatar == None:
			return {"error": "No changes to be made"}
		elif name != None and avatar == None:
			payload = {"name": name}
		elif name == None and avatar != None:
			payload = {"base64_avatar": avatar}
		else:
			payload = {"base64_avatar": avatar, "name": name}
		
		r = requests.put(f"{self.address}:{self.port}/v1/profiles/{self.number}", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
			
