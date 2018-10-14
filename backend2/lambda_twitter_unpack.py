import json
import base64
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("rawTweets") 

s3 = boto3.resource("s3")



def base64_to_dict(data):
    return json.loads(base64.urlsafe_b64decode(data.encode()).decode())
    
    
def lambda_handler(event, context):
    
    for record in event['Records']: 
        bucket_name = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"] 
        
        object = s3.Object(bucket_name, key)

        for code in [x.strip() for x in object.get()['Body'].read().decode('utf-8').split('|')]:
            if code:
                data = base64_to_dict(code)
                data["id"] = int(data["id"]) 
                table.put_item(Item=data)
                    

    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }
