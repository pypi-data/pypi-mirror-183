#!/usr/bin/python
# -*- coding: utf-8 -*-
##
## @author Edouard DUPIN
##
## @copyright 2023, Edouard DUPIN, all right reserved
##
## @license MPL v2.0 (see license file)
##
import enum
import requests
import json
from typing import Dict, Optional

class KarangeSendError(Exception):
    def __init__(self, message, error_id, error_message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
            
        # Now for your custom code...
        self.error_id = error_id
        self.error_message = error_message
    
    def __str__(self):
        return f"{Exception.__str__(self)} Status={self.error_id} message='{self.error_message}'"

class StateSystem(enum.Enum):
    OK = "OK"
    FAIL = "FAIL"
    DOWN = "DOWN"



## Generic karanage sending system.
class KaranageREST:
    def __init__(self, url: str, group: str, token: str) -> None:
        """ 
        @brief Initialize the communication class.
        @param[in] url URL of the karanage API server.
        @param[in] group Group of the message (token need to have the autorisation to pubhied on it).
        @param[in] token Token to validate the access on the application.
        """
        self.url = url
        self.group = group
        self.token = token
        self.root_url = f"{self.url}/{self.group}"


    def send_to_server(self, topic: str, data: Optional[Dict], state: StateSystem = StateSystem.OK) -> None:
        """
        @brief Send a message to the server.
        @param[in] topic Topic where to publish the data.
        @param[in] data: Data to send to the server
        @param[in] state: State of the current system
        """
        if data is None:
            data = {}
        param = {
            "state": state,
            }
        header = {}
        if self.token is not None and len(self.token) >15:
            header['Authorization'] = f"zota {self.token}"
        try:
            ret = requests.post(f"{self.root_url}/{topic}", json=data, headers=header, params=param)
        except requests.exceptions.ConnectionError as ex:
            raise KarangeSendError(f"Fail connect server: {self.root_url}/{topic}", 0, str(ex))
        if 200 <= ret.status_code <= 299:
            pass
        else:
            raise KarangeSendError(f"Fail send message: {self.root_url}/{topic}", ret.status_code, ret.content.decode("utf-8"))
    
    def get_all(self) -> Dict:
        """
        @brief Get all the topic fom the server.
        @return A dictionnary with the requested data.
        """
        param = { }
        header = { }
        if self.token is not None and len(self.token) >15:
            header['Authorization'] = f"zota {self.token}"
        ret = requests.get(self.root_url, headers=header, params=param)
        if 200 == ret.status_code:
            return json.loads(ret.content.decode('utf-8'))
        raise KarangeSendError(f"Fail get data: {self.root_url}", ret.status_code, ret.content.decode("utf-8"))

    def get_topic(self, topic: str) -> Dict:
        """
        @brief Get all the topic fom the server.
        @return A dictionnary with the requested data.
        """
        param = { }
        header = { }
        if self.token is not None and len(self.token) >15:
            header['Authorization'] = f"zota {self.token}"
        ret = requests.get(f"{self.root_url}/{topic}", headers=header, params=param)
        #print(ret.content.decode('utf-8'))
        if 200 == ret.status_code:
            return json.loads(ret.content.decode('utf-8'))
        raise KarangeSendError(f"Fail get data: {self.root_url}/{topic}", ret.status_code, ret.content.decode("utf-8"))
