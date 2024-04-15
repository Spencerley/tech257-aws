import boto3

s3_client = boto3.client('s3')

bucket_name = 'tech257-spencer-bucket'

# specify region to create bucket in
region = 'eu-west-1'

try:
    response = s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': region
        }
    )
    print(f"Bucket {bucket_name} created in {region}")
except ClientError as e:
    print(f"Error creating bucket: {e}")