# Useful Azcopy v12 Script
Simple scripts for downloading/uploading files &amp; directories from azure blob storage using Azcopy v12

First install azure-storage-blob:
```
pip install azure-storage-blob
```

To upload a file to blob storage
```
python script.py --connect_str [CONNECTION_STRING] --container_name [CONTAINER_NAME] --source [LOCAL_FILE_NAME] --target [BLOB_FILE_NAME] --upload
```

To upload a directory to blob stroage
```
python script.py --connect_str [CONNECTION_STRING] --container_name [CONTAINER_NAME] --source [LOCAL_DIRECTORY_NAME] --target [BLOB_DIRECTORY_NAME] --is_directory --upload
```

To download a file to blob storage
```
python script.py --connect_str [CONNECTION_STRING] --container_name [CONTAINER_NAME] --source [BLOB_FILE_NAME] --target [LOCAL_FILE_NAME] --is_directory --download
```

To downlaod a directory to blob storage
```
python script.py --connect_str [CONNECTION_STRING] --container_name [CONTAINER_NAME] --source [BLOB_DIRECTORY_NAME] --target [LOCAL_DIRECTORY_NAME] --is_directory --download
```
