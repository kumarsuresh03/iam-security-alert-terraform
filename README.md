# IAM Security Alert System

## What This Does
Automatically sends Slack alerts when someone creates a new IAM user in your AWS account. Helps detect attackers creating unauthorized access.

## Architecture
```
IAM User Created 
    ↓
CloudTrail (records the event)
    ↓
EventBridge (detects CreateUser event)
    ↓
Lambda Function (formats alert)
    ↓
Slack (sends notification)
```

## How It Works
1. Someone creates IAM user in AWS
2. CloudTrail logs this action to S3
3. EventBridge catches the CreateUser event
4. EventBridge triggers Lambda function
5. Lambda reads event details
6. Lambda sends formatted message to Slack
7. You get instant alert with details

## What Alert Shows
- New username created
- Who created it
- Their AWS account
- Which region
- When it happened

## Files
- `main.tf` - Terraform infrastructure code
- `index.py` - Lambda function code

## Deploy Steps
'
terraform init
terraform apply -var="slack_webhook_url=YOUR_WEBHOOK"
```

## Test
```bash
aws iam create-user --user-name test-user
```
Check Slack for alert.

## Cost
~$2-5/month
