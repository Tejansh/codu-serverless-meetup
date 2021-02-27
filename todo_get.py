import boto3

def lambda_handler(event, context):
    dynamodb=boto3.resource("dynamodb","eu-west-1")
    table=dynamodb.Table("todo-table")

    data=table.scan()
    return {
        'statusCode': 200,
        'body': data["Items"]
    }
