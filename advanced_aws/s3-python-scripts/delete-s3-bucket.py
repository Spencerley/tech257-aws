import boto3

s3_client = boto3.client('s3')

bucket_name = 'tech257-spencer-bucket'

try:
    response = s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted")
except ClientError as e:
    print(f"Error deleting bucket: {e}")