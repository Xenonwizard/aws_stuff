
import json,boto3
 
client = boto3.client('iam')
# while True:
data=client.list_policies(Scope='Local')

for x in data['Policies']:
    
    print(x)
    