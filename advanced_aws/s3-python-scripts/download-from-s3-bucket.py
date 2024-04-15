import boto3

s3_client = boto3.client('s3')

bucket_name = 'tech257-spencer-bucket'

region = 'eu-west-1'

# download to downloads folder
file_name = 'test.txt'

try:
    response = s3_client.download_file(bucket_name, file_name, f"downloads/{file_name}")
    print(f"File downloaded to downloads/{file_name}")
except ClientError as e:
    print(f"Error downloading file: {e}")