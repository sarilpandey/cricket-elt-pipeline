COPY cricket_matches
FROM 's3://your-bucket-name/'
IAM_ROLE 'your-iam-role'
FORMAT AS JSON 'auto';