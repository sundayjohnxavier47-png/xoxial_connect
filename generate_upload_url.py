import os
import boto3
from dotenv import load_dotenv

# for reading the .env file
load_dotenv()

# for getting each key
access_key = os.getenv("R2_ACCESS_KEY_ID")
secret_key = os.getenv("R2_SECRET_ACCESS_KEY")
endpoint_url = os.getenv("R2_ENDPOINT_URL")
bucket_name = os.getenv("R2_BUCKET_NAME")

# creating client: what can talk to R2
s3 = boto3.client(
    service_name="s3",
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name="auto",
)

def generate_upload_url(file_name):
    # asking boto3 to build a signed link that allows one action
    url = s3.generate_presigned_url(
        "put_object",
        Params={"Bucket": bucket_name, "Key": file_name},
        ExpiresIn=600,  # link stops working after 600 seconds (10 minutes)
    )
    return url

print(generate_upload_url("test.txt"))