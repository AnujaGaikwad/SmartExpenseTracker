import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SmartExpenseTracker")


def lambda_handler(event, context):
    try:
        # Get expenses from DynamoDB
        response = table.scan()

        expenses = response.get("Items", [])

        # Convert Decimal values to float
        for expense in expenses:
            if "amount" in expense:
                expense["amount"] = float(expense["amount"])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Expenses fetched successfully",
                "count": len(expenses),
                "expenses": expenses
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Error fetching expenses",
                "error": str(e)
            })
        }
