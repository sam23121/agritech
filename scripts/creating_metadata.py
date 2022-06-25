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
        # df['filename'] = line.strip()
        # df['xmin'] = text['bounds'][0]
        # df['ymin'] = text['bounds'][1]
        # df['xmax'] = text['bounds'][3]
        # df['ymax'] = text['bounds'][4]
        # df['points'] = text["points"]
        # df2 = {'filename': line.strip(), 'xmin': text['bounds'][0], 'ymin': text['bounds'][1], 'xmax':text['bounds'][3], 'ymax':text['bounds'][4], 'points':text['points']}
        # df = pd.concat([df, df2], ignore_index = True, axis = 0)
        df.loc[count] = [line.strip(), text['bounds'][0], text['bounds'][1], text['bounds'][3],text['bounds'][4],text["points"]]
        count += 1
    except:
        pass

print(df.to_csv('data/metadata.csv'))


    # obj = s3.Object('usgs-lidar-public', line.rstrip()+'ept.json')
    # data = json.loads(obj.get()['bounds']) 
    # for object_summary in my_bucket.objects.filter(Prefix=line.rstrip()+'ept.json'): 
    #     print(object_summary.key)
    #     # file_content = content_object.get()['Body'].read().decode('utf-8')
    #     # json_content = json.loads(object_summary.key)
    #     # print(json_content['bounds'])
    #     text = object_summary.key.read().decode()
    #     print(text['Details'])
    
# my_bucket=s3.Bucket(s3_bucket_name)
# for line in Lines:
#     for file in my_bucket.objects.filter(Prefix = line):
#         file_name=file.key
#         print(file_name)
    #     if file_name.find("ept.json")!=-1:
    #         bucket_list.append(file.key)
    # length_bucket_list=print(len(bucket_list))
    # print(bucket_list[0:10])

