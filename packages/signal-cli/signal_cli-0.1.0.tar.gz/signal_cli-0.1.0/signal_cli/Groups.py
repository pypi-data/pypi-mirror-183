## @package signal_cli

import requests, json, os, pathlib
from typing import Union

## @brief Class holding the collection of functions from the Groups section
# @details This class handles a collection of all functions that are listed in the Groups section in the documentation of the signal-cli-rest-api
# @author Felix Hune
# @version 1.1
# @date 2022-12-25
class Groups:
	
	def __init__(self, Client):
		self.address = Client.get_address()
		self.port = Client.get_port()
		self.number = Client.get_number()
	
	## @brief List groups
	# @details Calls the API to list all groups this user is member in
	# @return Either a @p dict in json format or a @p list 
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def get_groups(self) -> Union[dict, list]:
		
		r = requests.get(f"{self.address}:{self.port}/v1/groups/{self.number}", headers={'Content-Type': 'application/json'})
		
		r = r.json()
		return r
	
	## @brief Create group
	# @details Calls the API to create a new group
	# @param	name				The name of the group
	# @param	description			The description of the group
	# @param	members				The members to be added to the group
	# @param	group_link			<b>(Optional)</b>Defines if a group link should be generated, this doesn't work correctly (2022-12-18). This argument defaults to @p disabled.
	# @param	perm_add_members	<b>(Optional)</b>Defines who is allowed to add new members. This argument defaults to @p only-admins.
	# @param	perm_edit_group		<b>(Optional)</b>Defines who is allowed to edit the group. This argument defaults to @p only-admins.
	# @return A @p dict in json format
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def create_group(
		self,
		name: str,
		description: str,
		members: list[str],
		group_link: str="disabled",
		perm_add_members: str="only-admins",
		perm_edit_group: str="only-admins"		
	) -> dict:
		r = requests.post(f"{self.address}:{self.port}/v1/groups/{self.number}", headers={'Content-Type': 'application/json'}, json={"description": description, "group_link": create_group, "members": members, "name": name, "permissions": {"add_members": perm_add_members, "edit_group": perm_edit_group}})
		
		r = r.json()
		return r
	
	## @brief Get group
	# @details Calls the API to list informations about a group
	# @param	groupid	The group ID
	# @return A @p dict in json format
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def get_group(self, groupid: str) -> dict:
		
		r = requests.get(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}", headers={'Content-Type': 'application/json'})
		
		r = r.json()
		return r
	
	## @brief Delete group
	# @details Calls the API to delete a group
	# @param	groupid	The group ID
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def delete_group(self, groupid):
		
		r = requests.delete(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Add admins
	# @details Calls the API to add admins
	# @param	groupid	The group ID
	# @param	admins	The members that should be made an admin
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def add_admins(self, groupid: str, admins: list[str]) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}/admins", headers={'Content-Type': 'application/json'}, json={"admins": admins})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Remove admins
	# @details Calls the API to remove admins
	# @param	groupid	The group ID
	# @param	admins	The admins that should be degraded to members
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def remove_admins(self, groupid: str, admins: list[str]) -> Union[dict, str]:
		payload = {'admins': admins}
		
		r = requests.delete(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}/admins", headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Block group
	# @details Calls the API to block a group
	# @param	groupid	The group ID
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def block_group(self, groupid: str) -> Union[dict, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/groups/{self.number}/{self.groupid}/block", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Join group
	# @details Calls the API to join a group
	# @param	groupid	The group ID
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def join_group(self, groupid: str) -> Union[list, str]:
		
		r = requests.post(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}/join", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Add members to group
	# @details Calls the API to add members to a group
	# @param	groupid	The group ID
	# @param	members	The members to be added to the group
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def add_members(self, groupid: str, members: list[str]) -> Union[list, str]:
		 
		r = requests.post(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}/members", headers={'Content-Type': 'application/json'}, json={"members": members})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Remove members from group
	# @details Calls the API to remove members from a group
	# @param	groupid	The group ID
	# @param	members	The members to be removed from the group
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18
	def remove_members(self, groupid: str, members: list[str]) -> Union[list, str]:
		payload = {'members': members}
		
		r = requests.delete(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}/members", headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
	
	## @brief Quit group
	# @details Calls the API to quit a group
	# @param	groupid	The group ID
	# @return Either a @p dict in json format or a @p str
	# @author Felix Hune
	# @version 1.0
	# @date 2022-12-18	
	def quit_group(self, groupid: str) -> Union[list, str]:
		r = requests.post(f"{self.address}:{self.port}/v1/groups/{self.number}/{groupid}/quit", headers={'Content-Type': 'application/json'})
		
		try:
			r = r.json()
		except:
			r = r.text
		return r
		
		
