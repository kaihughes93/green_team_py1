import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='WNBA_Teams', #enter table name
    KeySchema=[
        {
            'AttributeName': 'Team', #Partition key
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Founded', #Sort key
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Team',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Founded',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print(table)