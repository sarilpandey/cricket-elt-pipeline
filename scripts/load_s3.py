import boto3
import json
from datetime import datetime

s3 = boto3.client("s3")

BUCKET_NAME = "your-bucket-name"

def upload_to_s3(data):
    file_name = f"cricket_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(data)
    )

    print("Uploaded to S3:", file_name)
