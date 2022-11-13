import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('WNBA_Teams')


with table.batch_writer() as batch:
 batch.put_item(Item={'Team': "Las Vegas Aces", "Founded":"1997"})
 batch.put_item(Item={'Team': "Chicago Sky", "Founded":"2006"})
 batch.put_item(Item={'Team': "Los Angeles Sparks", "Founded":"1997"})
 batch.put_item(Item={'Team': "Seattle Storm", "Founded":"2000"})
 batch.put_item(Item={'Team': "Dallas Wings", "Founded":"1998"})
 batch.put_item(Item={'Team': "Connecticut Sun", "Founded":"1999"})
 batch.put_item(Item={'Team': "Indiana Fever", "Founded":"2000"})
 batch.put_item(Item={'Team': "Phoenix Mercury", "Founded":"1997"})
 batch.put_item(Item={'Team': "Minnesota Lynx", "Founded":"1999"})
 batch.put_item(Item={'Team': "Atlanta Dream", "Founded":"2008"})
    
print(batch)
