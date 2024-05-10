dvc remote add -d myminio s3://<bucket-name>/path
dvc remote modify myminio endpointurl http://localhost:9000
dvc remote modify myminio access_key 'minio-access-key'
dvc remote modify myminio secret_key 'minio-secret-key'

dvc remote modify myminio access_key_id 'admin'
dvc remote modify myminio secret_access_key 'admin123'
