import boto3
import botocore
import pandas as pd
import json

# Using readlines()
file1 = open('data/REGIONS.txt', 'r')
Lines = file1.readlines()

s3_client =boto3.client('s3', config=botocore.client.Config(signature_version=botocore.UNSIGNED))

s3 = boto3.resource('s3',
                   config=botocore.client.Config(signature_version=botocore.UNSIGNED))
my_bucket = s3.Bucket('usgs-lidar-public')
df = pd.DataFrame(columns = ['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'points'])
count = 0
for line in Lines[1:-1]:
    # print(line.rstrip())
    my_file = line.strip()+'ept.json'
    # print(line.strip())
    # print(my_file)
    try:
        result = s3_client.get_object(Bucket='usgs-lidar-public', Key=my_file)
        text = json.load(result["Body"])#.read().decode()
        df.loc[count] = [line.strip(), text['bounds'][0], text['bounds'][1], text['bounds'][3],text['bounds'][4],text["points"]]
        count += 1
    except:
        pass

print(df.to_csv('data/metadata.csv'), index= False)


   
    
