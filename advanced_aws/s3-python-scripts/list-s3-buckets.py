import boto3

s3_client = boto3.client('s3')

try:
  response = s3_client.list_buckets()
  print("S3 Buckets:")
  for bucket in response['Buckets']:
    print(bucket['Name'])
except ClientError as e:
  print(f"Error listing S3 buckets: {e}")
