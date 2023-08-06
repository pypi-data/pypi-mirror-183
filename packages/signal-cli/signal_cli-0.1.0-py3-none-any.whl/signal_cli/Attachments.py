## @package signal_cli

import requests, json, os, pathlib, filetype, base64
from typing import Union

## @brief Class holding the collection of functions from the Attachments section
# @details This class handles a collection of all functions that are listed in the Attachments section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Attachments:

	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
		
	## @brief List attachments
	# @details Calls the API to list the existing attachments
	# @return Either a @p list or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def list_attachments(self) -> Union[list, str]:
		
		r = requests.get(f"{self.address}:{self.port}/v1/attachments", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Serve attachments
	# @details Calls the api to get a specified attachment as file, writes it to disc, guesses and adds the file extension, encodes it to base64, deletes the file and returns the base64 string
	# @param	attachment	The id of the attachment to serve
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def serve_attachment(self, attachment: str) -> Union[dict, str]:

		r = requests.get(f"{self.address}:{self.port}/v1/attachments/{attachment}", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			img = attachment
			with open(img, 'wb') as f:
				for chunk in r:
					f.write(chunk)
			fileinfo = filetype.guess(img)
			try:
				fullimg = img + "." + fileinfo.extension
			except:
				fullimg = img + ".bin"
			os.rename(img, fullimg)
			with open(fullimg, 'rb') as f:
				b64string = base64.b64encode(f.read()).decode('utf-8')
				ext = fullimg.split('.')[-1]
				r = f'data:image/{ext};base64,{b64string}'
			os.remove(fullimg)
		return r
	
	## @brief Delete attachments
	# @details Calls the api to delete a specified attachment
	# @param	attachment	The id of the attachment to serve
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def delete_attachment(self, attachment: str) -> Union[dict, str]:
		
		r = requests.delete(f"{self.address}:{self.port}/v1/attachments/{attachment}", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
