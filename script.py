import boto3

def update_all_items(table_name, property_name, new_value):
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')
    
    # Scan all items in the table
    response = dynamodb.scan(
        TableName=table_name
    )
    
    # Iterate through each item and update the property
    for item in response['Items']:
        key = {key_name: item[key_name]['S'] for key_name in item.keys()}
        
        # Update the item
        dynamodb.update_item(
            TableName=table_name,
            Key=key,
            UpdateExpression="SET #prop = :val",
            ExpressionAttributeNames={"#prop": property_name},
            ExpressionAttributeValues={":val": {"S": new_value}}
        )
        print(f"Updated item with key: {key}")

if __name__ == "__main__":
    table_name = input("Enter the DynamoDB table name: ")
    property_name = input("Enter the property name to update: ")
    new_value = input("Enter the new value for the property: ")

    update_all_items(table_name, property_name, new_value)
