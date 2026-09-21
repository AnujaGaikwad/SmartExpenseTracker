import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SmartExpenseTracker")


def lambda_handler(event, context):
    try:
        # Get expense_id from API Gateway path parameter
        path_parameters = event.get("pathParameters") or {}
        expense_id = path_parameters.get("expense_id")

        # Validate expense_id
        if not expense_id:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "message": "expense_id is required"
                })
            }

        # Delete expense
        table.delete_item(
            Key={
                "expense_id": expense_id
            }
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Expense deleted successfully",
                "expense_id": expense_id
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Error deleting expense",
                "error": str(e)
            })
        }
