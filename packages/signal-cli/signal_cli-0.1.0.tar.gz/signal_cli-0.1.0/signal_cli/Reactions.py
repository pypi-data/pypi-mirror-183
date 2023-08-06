## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Reactions section
# @details This class handles a collection of all functions that are listed in the Reactions section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Reactions:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief Send Reaction
	# @details Calls the API to send a reaction on a message in a chat
	# @param	reaction		The reaction to send. This has to be the Emoji as the Emoji character, not a unicode code
	# @param	recipient		The number of the recipient chat, maybe also a chat id?
	# @param	target_author	The number of the target author who wrote the message
	# @param	timestamp		The timestamp when the message was sent
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def send_reaction(self, reaction: str, recipient: str, target_author: str, timestamp: int) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/reactions/{self.number}", headers={"Content-Type": "application/json"}, json={"reaction": reaction, "recipient": recipient, "target_author": target_author, "timestamp": timestamp})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r

	## @brief Delete reaction
	# @details Calls the API to delete a reaction from a message in a chat
	# @param	reaction		The reaction to remove. This has to be the Emoji as the Emoji character, not a unicode code
	# @param	recipient		The number of the recipient chat, maybe also a chat id?
	# @param	target_author	The number of the target author who wrote the message
	# @param	timestamp		The timestamp when the message was sent
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def delete_reaction(self, reaction: str, recipient: str, target_author: str, timestamp: int) -> Union[dict, str]:
		
		payload = {"reaction": reaction, "recipient": recipient, "target_author": target_author, "timestamp": timestamp}
		r  = requests.delete(f"{self.address}:{self.port}/v1/reactions/{self.number}", headers={"Content-Type": "application/json"}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
