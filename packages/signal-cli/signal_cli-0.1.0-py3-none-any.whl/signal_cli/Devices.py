## @package signal_cli

import requests, json, os, pathlib, base64
from typing import Union

## @brief Class holding the collection of functions from the Devices section
# @details This class handles a collection of all functions that are listed in the Devices section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Devices:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief Links another device
	# @details Calls the API to link another device to this device; this only works if this is the master device
	# @param	uri	The uri which is the content of the qr code that generates on the devices that should be linked when the linking is requested there
	# @return Either a @p dict in json format or a @str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def link_device(self, uri: str) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/devices/{self.number}", headers={'Content-Type': 'application/json'}, json={"uri": uri})
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Request linking of this device
	# @details Calls the API to request a linking of this device to another device;
	# therefore the API returns a qr-code, which gets temporarily saved on the disc, 
	# then the function generates a base64 string from the picture, deletes the picture and returns the base64 string
	# @param	device_name	The name by which this device should show up on the other device
	# @return Either a @p dict in json format or a @str with the bas64
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def qrcodelink(self, device_name: str) -> Union[dict, str]:
		
		r = requests.get(f"{self.address}:{self.port}/v1/qrcodelink", headers={'Content-Type': 'application/json'}, params={"device_name": device_name})
		try:
			r = r.json()
		except:
			img = str(os.getpid()) + ".png"
			with open(img, 'wb') as f:
				for chunk in r:
					f.write(chunk)
			with open(img, 'rb') as f:
				b64string = base64.b64encode(f.read()).decode('utf-8')
				ext = img.split('.')[-1]
				r = f'data:image/{ext};base64,{b64string}'
			os.remove(img)
				
		return r

	## @brief Register new number
	# @details Calls the API to register a new account with the number in the config;
	# this only works if it isn't already registered. 
	# @pre Generate a captcha at https://signalcaptchas.org/registration/generate.html, then copy the link from the 'Open Signal'-button 
	# @param	captcha		The link from the button, obtainable as described in the preconditions
	# @param	use_voice	<b>(Optional)</b> Defines if the verification code should be send as SMS or as a phone call. This argument defaults to @p False
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def register(self, captcha: str, use_voice: bool=False) -> Union[dict, str]:
		captcha = captcha.replace("signalcaptcha://", "")
		r = requests.post(f"{self.address}:{self.port}/v1/register/{self.number}", headers={'Content-Type': 'application/json'}, json={"captcha": captcha, "use_voice": use_voice})
		try:
			r = r.json()
		except:
			r = r.text
		return r

	## @brief Verify registration
	# @details Calls the API to verify the registration of a new number
	# @pre Starting the registring process by calling @link register() @endlink
	# @param	token	The registration token obtained via the registration process message or call
	# @param	**pin	<b>(Optional)</b> The pin to secure the signal account. As this is a keyword argument, it has to be specified with <tt>pin=\<pin\></tt>, the data type is @p int
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def verify(self, token: str, **kwargs) -> Union[dict, str]:
		
		pin = None
		for key, value in kwargs.items():
			if key == "pin":
				pin = str(value)
		
		if pin == None:	
			r = requests.post(f"{self.address}:{self.port}/v1/register/{self.number}/verify/{token}", headers={'Content-Type': 'application/json'})
		else:
			r = requests.post(f"{self.address}:{self.port}/v1/register/{self.number}/verify/{token}", headers={'Content-Type': 'application/json'}, json={"pin": pin})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
		
	## @brief Unregister number
	# @details Calls the API to unregister the number in the config
	# @param	delete_account		<b>(Optional)</b> Defines if the account should be deleted from the Signal server. This argument defaults to @p False
	# @param	delete_local_data	<b>(Optional)</b> Defines if the local data for this account should be deleted. This arguments defaults to @p False
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def unregister(self, delete_account: bool=False, delete_local_data: bool=False) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/unregister/{self.number}", headers={'Content-Type': 'application/json'}, json={"delete_account": delete_account, "delete_local_data": delete_local_data})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
			
