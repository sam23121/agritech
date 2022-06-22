import os
import sys

import boto3
import botocore

client = boto3.client('s3',  # region_name='us-east-1',
                      config=botocore.client.Config(signature_version=botocore.UNSIGNED))
result = client.list_objects(Bucket='usgs-lidar-public',
                             Prefix='',
                             Delimiter='/'
                             )
obj = list()
for o in result.get('CommonPrefixes'):
    # print(o) 
    obj.append(o.get('Prefix'))

with open("data/REGIONS.txt", "w") as output:
    sys.path.append(os.path.abspath(os.path.join('../data')))
    output.write(str(obj))                  