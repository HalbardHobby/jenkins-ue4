set "str=%~1"
cd C:\ARCHIVE\DIRECTORY
aws s3 cp PROJECT_NAME_%str%.zip s3://BUCKET_NAME/PROJECT_NAME_%str%.zip