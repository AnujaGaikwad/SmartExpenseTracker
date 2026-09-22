import json
import boto3
import uuid
from decimal import Decimal
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SmartExpenseTracker")


def lambda_handler(event, context):
    try:
        # Get request body
        if "body" in event:
            body = event["body"]

            if isinstance(body, str):
                body = json.loads(body)
        else:
            body = event

        # Get values from request
        amount = body.get("amount")
        category = body.get("category")
        description = body.get("description")
        date = body.get("date")

        # Validate required fields
        if amount is None or not category or not description or not date:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "message": "All fields are required"
                })
            }

        # Generate unique ID
        expense_id = str(uuid.uuid4())

        # Create DynamoDB item
        item = {
            "expense_id": expense_id,
            "amount": Decimal(str(amount)),
            "category": category,
            "description": description,
            "date": date,
            "created_at": datetime.now(timezone.utc).isoformat()
        }

        # Save to DynamoDB
        table.put_item(Item=item)

        # Return response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Expense added successfully",
                "expense": {
                    "expense_id": expense_id,
                    "amount": float(item["amount"]),
                    "category": category,
                    "description": description,
                    "date": date,
                    "created_at": item["created_at"]
                }
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Error adding expense",
                "error": str(e)
            })
        }
