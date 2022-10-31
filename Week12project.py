#AWS Service Inventory
#Create a list of services using python.IE: S3, Lambda, EC2, etc.
#The list should be empty initially.
#Populate the list using append or insert.
#Print the list and the length of the list.
#Remove two specific services from the list by name or by index.
#Print the new list and the new length of the list.

aws_items = []

aws_items.append('S3')
aws_items.append('Lambda')
aws_items.append('EC2')
aws_items.append('DynamoDB')
aws_items.append('CloudWatch')
aws_items.append('IAM')

print(aws_items)

print(len(aws_items))

del aws_items[1]
del aws_items[2]

print(aws_items)
print(len(aws_items))