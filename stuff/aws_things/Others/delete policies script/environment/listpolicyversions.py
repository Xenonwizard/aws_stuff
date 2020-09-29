
import json,boto3
 
client = boto3.client('iam')
# while True:
data=client.list_policies(Scope='Local')

for x in data['Policies']:
    
  data1=client.list_policy_versions(PolicyArn=x['Arn'])
  
  for y in data1['Versions']:
      print(y)