from __future__ import print_function

# import logging

import json
import sys
import uuid
from random import randrange # TODO remove this
import requests

# TODO: need to re-enable TLS for the handlers in the fly.toml file. Try these settings: https://community.fly.io/t/urgent-grpc-server-unreachable-via-grpcurl/2694/12 for alpn
# TODO figure out how to configure the settings for fly.toml for grpc!
# TODO also need to make sure different runs don't interfere with each other
# TODO add a parameter for an entry point into the system (currently, assume that using cakework_app.py)
class Client:
    def __init__(self, app, local=False, user_id="shared"): # TODO: infer user id // TODO revert local back to False
        self.app = app.lower().replace('_', '-')
        self.user_id = user_id
        self.local = local

        if local:
            self.frontend_url = "http://localhost:8080"
        else:
            self.frontend_url = "https://cakework-frontend.fly.dev"
 
    def get_status(self, request_id):
        # Q: status 200 vs 201??? what's the diff?
        response = requests.get(f"{self.frontend_url}/get-status", json={"userId": self.user_id, "app": self.app, "requestId": request_id})
        print(response) # TODO get rid of this logging
        response_json = response.json()
        # print(response_json)
        status = response_json["status"] # this may be null?
        return status

    def get_result(self, request_id):
        # Q: status 200 vs 201??? what's the diff?
        response = requests.get(f"{self.frontend_url}/get-result", json={"userId": self.user_id, "app": self.app, "requestId": request_id})
        print(response) # TODO get rid of this logging
        response_json = response.json()
        # print(response_json)
        result = response_json["result"] # this may be null? TODO return None if can't get the status
        return result

    def __getattr__(self, name):
        def method(**args):
            sanitized_name = name.lower()
            sanitized_name = name.replace('_', '-')                
            response = requests.post(f"{self.frontend_url}/submit-task", json={"userId": self.user_id, "app": self.app, "task": sanitized_name, "parameters": json.dumps(args)})
            print(response) # TODO get rid of this logging
            response_json = response.json()
            # print(response_json)
            request_id = response_json["requestId"] # this may be null?
            return request_id

        return method
    
# if __name__ == '__main__':
#     run()