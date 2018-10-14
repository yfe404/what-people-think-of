import json
import os 
import boto3

dynamodb = boto3.client('dynamodb')

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    
    for record in event["Records"]: 
        if record["eventName"] == "INSERT":
            tweet_text = record["dynamodb"]["NewImage"]["text"]["S"]
            response = comprehend.detect_sentiment(Text=tweet_text, LanguageCode="en")
            sentiment = response["Sentiment"]
            
            response = dynamodb.update_item(
                TableName=os.environ["DYNAMODB_TABLE"],
                Key={
                    'sentiment': {'S': sentiment}
                },       
                UpdateExpression= "ADD tweets :val",
                ConditionExpression= "attribute_not_exists(sentiment) OR sentiment = :sentiment",
                ExpressionAttributeValues= {
                    ":val": {'N': '1'},
                    ":sentiment": {'S': sentiment}
                },
                ReturnValues= "UPDATED_NEW"
            )


    
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }
