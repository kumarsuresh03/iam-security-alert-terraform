import json
import urllib3
import os

http = urllib3.PoolManager()

def lambda_handler(event, context):
    webhook = os.environ.get('SLACK_WEBHOOK')
    detail = event.get('detail', {})
    user_identity = detail.get('userIdentity', {})
    request_params = detail.get('requestParameters', {})
    creator = user_identity.get('userName') or user_identity.get('principalId', 'Unknown')
    creator_arn = user_identity.get('arn', 'Unknown')
    account_id = user_identity.get('accountId', 'Unknown')
    access_key = user_identity.get('accessKeyId', 'Unknown')
    new_user = request_params.get('userName', 'Unknown')
    region = event.get('region', 'Unknown')
    event_time = detail.get('eventTime', 'Unknown')
    msg = f"""IAM User Created Alert
New User: {new_user}
Created By: {creator}
ARN: {creator_arn}
Account: {account_id}
Access Key: {access_key}
Region: {region}
Time: {event_time}
"""
    http.request("POST", webhook, body=json.dumps({"text": msg}), headers={"Content-Type": "application/json"})
    return {'statusCode': 200}
