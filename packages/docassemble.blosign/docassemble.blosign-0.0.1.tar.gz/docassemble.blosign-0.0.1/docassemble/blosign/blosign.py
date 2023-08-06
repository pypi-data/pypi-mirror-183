# importing the requests library
import requests
import json
from docassemble.base.util import DAError, log, get_config

# api-endpoint
SBX_URL = "https://sbx-api.blosign.com/v2"
PROD_URL = "https://api.blosign.com/v2"

class Blosign:
  def __init__(self):
    self.get_server_config()
    if self.test_mode:
      self.api_uri = SBX_URL
    else:
      self.api_uri = PROD_URL
  
  def get_server_config(self):
    blosign_configuration = get_config('blosign')
    if not blosign_configuration:
      raise DAError("Attempt to read Blosign configuration failed. Blosign is not configured for the server.")
    if 'test-mode' in blosign_configuration:
      self.test_mode = blosign_configuration['test-mode']
    else:
      raise DAError("Blosign configuration does not include test-mode.")
    if 'token' in blosign_configuration:
      self.token = blosign_configuration['token']
    else:
      raise DAError("Blosign configuration does not include token.")
        
  def __upload_document__(self, document):
    files = {'document': (document[0].filename, open(document[0].path(), 'rb'), 'application/pdf')}
    r = requests.post(url=self.api_uri+"/documents/upload", files=files, headers={'x-api-key': self.token})
    data = r.json()
    log(json.dumps(data,indent=2), "console")
    log("status code: "+str(r.status_code), "console")

    return data, r.status_code
    
  def request_signatures(self, people, document, signInOrder=False, message=None, filename=None, expiryDate=None):
    data, status_code = self.__upload_document__(document)
    
    if status_code != 200:
      return data, status_code
    
    docId = data["documentId"]

    data = {
      "signInOrder":signInOrder,
      "people": people
    }
    if message is not None:
      data["message"] = message
    if filename is not None:
      data["filename"] = filename
    if expiryDate is not None:
      data["expiryDate"] = expiryDate

    r = requests.post(url=self.api_uri+"/documents/"+docId+"/request_signature", json=data, headers={'x-api-key': self.token})

    return json.loads(r.text), r.status_code
