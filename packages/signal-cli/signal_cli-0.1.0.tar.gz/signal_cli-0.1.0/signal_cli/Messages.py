## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Messages section
# @details This class handles a collection of all functions that are listed in the Messages section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Messages:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief Receive messages
	# @details Calls the API to list all new incoming messages
	# @param	timeout	<b>(Optional)</b> Sets the timeout parameter. This argument defaults to @p 1.
	# @return Either a @p list with @p dicts or a @p dict
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def receive(self, timeout: int=1) -> Union[list[dict], dict]:
		
		r = requests.get(f"{self.address}:{self.port}/v1/receive/{self.number}", headers={'Content-Type': 'application/json'}, params={"timeout": str(timeout)})
		r = r.json()
		return r
	
	## @brief Show typing indicator
	# @details Calls the API to show the typing indicator in a specified conversation
	# @param	recipient	The phone number of the recipient, maybe also group id?
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def show_typing(self, recipient: str) -> Union[dict, str]:
		
		payload = {"recipient": recipient}
		r = requests.put(f"{self.address}:{self.port}/v1/typing-indicator/{self.number}", headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Hide typing indicator
	# @details Calls the API to hide the typing indicator in a specified conversation
	# @param	recipient	The phone number of the recipient, maybe also group id?
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18	
	def hide_typing(self, recipient: str) -> Union[dict, str]:
		
		payload = {"recipient": recipient}
		r = requests.delete(f"{self.address}:{self.port}/v1/typing-indicator/{self.number}", headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Send message
	# @details Calls the API to send a message
	# @param	message		The message text
	# @param	recipients	The list of recipients to send the message to
	# @param	attachments	<b>(Optional)</b> A list of attachments encoded to base64. This argument defaults to <tt>[]</tt>
	# @return A @p dict in json format
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def send(self, message: str, recipients: list[str], attachments: list[str]=[]) -> dict:
		
		r = requests.post(f"{self.address}:{self.port}/v2/send", headers={'Content-Type': 'application/json'}, json={"base64_attachments": attachments, "message": message, "number": self.number, "recipients": recipients})
		
		r = r.json()
		return r
		
