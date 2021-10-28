import base64
import requests
import json

URL_DNAC=str(input("Please enter the URL of your DNA Center: "))#"sandboxdnac.cisco.com"
username=str(input("Username: "))
password=str(input("Password: "))

sample_string = username+":"+password
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

headers = {
    'content-type': "application/json",
    'authorization': "Basic "+ base64_string
    }

request=requests.post("https://"+URL_DNAC+"/dna/system/api/v1/auth/token", headers=headers)
print(request.text)
data=json.loads(request.content)
token=data["Token"]
token_file="DNAC_Token.txt"
file=open(token_file,"w")
file.write(token)
print("The Token will be stored in "+token_file)