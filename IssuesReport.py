import requests
import json
#from datetime import datetime
import pandas as pd

#timestamp = 1545730073
#dt_object = datetime.fromtimestamp(timestamp)

#URL_DNAC=str(input("Please enter the URL of your DNA Center: "))#"sandboxdnac.cisco.com"
URL_DNAC="sandboxdnac.cisco.com"
temp=open("DNAC_Token.txt",'r')
DNAC_TOKEN=temp.read()
temp.close()

h_dnac = {
  'content-type': 'application/json',
  'x-auth-token': DNAC_TOKEN
}

audit_logs=requests.get("https://"+URL_DNAC+"/dna/data/api/v1/event/event-series/audit-logs", headers=h_dnac)
print(audit_logs)
audit_logs_data=json.loads(audit_logs.text)
print((audit_logs_data[0]))
audit_logs_df=pd.DataFrame.from_records(audit_logs_data)
audit_logs_df["timestamp"]=pd.to_datetime(audit_logs_df["timestamp"],unit='ms')
df=audit_logs_df.set_index("timestamp")
msg=audit_logs_df[['timestamp','eventId','name','description']].to_string()

url_webex = "https://webexapis.com/v1/messages"
temp=open("Bot access token.txt",'r')
WEBEX_ACCESS_TOKEN=temp.read()
temp.close()
h_webex = {
  'Content-Type': 'application/json',
  "Authorization": "Bearer " + WEBEX_ACCESS_TOKEN
}
#roomId="Y2lzY29zcGFyazovL3VzL1JPT00vNGZmMGQwMDAtZWJmYy0xMWViLWI0OWUtOGRhMjlkNWZiNDJi"#Group Space
roomId="Y2lzY29zcGFyazovL3VzL1JPT00vM2I0ZDU0OTAtMjJjOC0xMWVjLThlNDYtOGI4NGIyMTU4ZGFh"#Direct Space
message={"roomId":roomId,"text":msg}

response_webex = requests.request("POST", url_webex, headers=h_webex, data=json.dumps(message))
print(response_webex)