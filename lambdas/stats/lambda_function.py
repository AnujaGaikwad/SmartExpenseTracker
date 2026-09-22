import json
import boto3
from decimal import Decimal
from datetime import datetime
from zoneinfo import ZoneInfo

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SmartExpenseTracker")


def lambda_handler(event, context):
    try:
        # Get all expenses
        response = table.scan()
        expenses = response.get("Items", [])

        # Initialize statistics
        total_spent = Decimal("0")
        today_spent = Decimal("0")
        highest_expense = Decimal("0")

        # Get current date in India
        india_time = datetime.now(
            ZoneInfo("Asia/Kolkata")
        )

        today = india_time.strftime("%Y-%m-%d")

        # Calculate statistics
        for expense in expenses:

            amount = Decimal(
                str(expense.get("amount", 0))
            )

            total_spent += amount

            if expense.get("date") == today:
                today_spent += amount

            if amount > highest_expense:
                highest_expense = amount

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Statistics calculated successfully",
                "total_spent": float(total_spent),
                "today_spent": float(today_spent),
                "highest_expense": float(highest_expense),
                "expense_count": len(expenses)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Error calculating statistics",
                "error": str(e)
            })
        }
