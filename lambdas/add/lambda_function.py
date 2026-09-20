import json
import boto3
import uuid
from decimal import Decimal
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SmartExpenseTracker")


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    amount = Decimal(str(body.get("amount")))
    category = body.get("category")
    description = body.get("description", "")

    expense_id = str(uuid.uuid4())

    item = {
        "expense_id": expense_id,
        "amount": amount,
        "category": category,
        "description": description,
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Expense added successfully",
            "expense_id": expense_id
        })
    }
