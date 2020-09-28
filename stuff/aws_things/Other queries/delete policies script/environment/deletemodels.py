import json,boto3
 
client = boto3.client('iam')
# while True:
data=client.list_policies(Scope='Local')

#deletes all non-default policy versions

for x in data['Policies']:
    
  data1=client.list_policy_versions(PolicyArn=x['Arn'])
  
  for y in data1['Versions']:
    
    if(y['IsDefaultVersion'] is False):
        print("Deleting all non-default policy versions")
        
        response = client.delete_policy_version(PolicyArn=x['Arn'], VersionId=y['VersionId'])
        
        if response is not None:
        
            break;
            
# #detach all policies
# while True:
    
#     count=1
#     maxcount = len(data['Policies'])
    
#         for z in data['Policies']:
            
#           response1=client.detach_role_policy(RoleName=z['RoleName'], PolicyArn=z['Arn'])
#           count +=1
    
#     if(count==maxcount):
#         break;        
       
                    
# deletes all policies
while True:     
    if(data is not None):
        for x in data['Policies']:
         try:
         
            client.delete_policy(PolicyArn=x['Arn'])
        
    else:
        break
        
    
print("all done")
