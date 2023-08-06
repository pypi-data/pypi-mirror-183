## @package signal_cli

import requests, json, os, pathlib, base64, filetype
from typing import Union

## @brief signal-cli client object
# @details A client object building an instance of the module, containing the configuration for the session
# @param	address	The address where the signal-cli-rest-api is accessible
# @param	port	The port where the signal-cli-rest-api is accessible
# @param	number	<b>(Optional)</b> The phone number to be used for this object, 
# has to be registered in the signal-cli-rest-api. This argument defaults to "+441189998819991197253"
# @author Felix Hune
# @version 1.0
# @date 2022-12-25
class Client:
	
	def __init__(self, address: str, port: int, number: str="+441189998819991197253"):
		self.address = address
		self.port = port
		self.number = number
	
	## @brief get address
	# @return A @p str containing the address
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-25
	def get_address(self) -> str:
		return self.address
	
	## @brief set address
	# @param	address	The address to set
	# @return @p None
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-25
	def set_address(self, address: str):
		self.address = address
	
	## @brief get port
	# @return A @p int containing the port
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-25
	def get_port(self) -> int:
		return self.port
	
	## @brief set port
	# @param	port	The port to set
	# @return @p None
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-25
	def set_port(self, port: int):
		self.port = port
	
	## @brief get number
	# @return A @p str containing the number
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-25
	def get_number(self) -> str:
		return self.number
	
	## @brief set number
	# @param	number	The number to set
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-25
	def set_number(self, number: str):
		self.number = number
	
