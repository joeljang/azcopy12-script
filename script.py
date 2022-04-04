import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import argparse
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--connect_str', default='', type=str)
parser.add_argument('--container_name', default='', type=str)
parser.add_argument('--source', default='', type=str)
parser.add_argument('--target', default='', type=str)
parser.add_argument('--is_directory', default=False, action='store_true')
parser.add_argument('--download', default=False, action='store_true')
parser.add_argument('--upload', default=False, action='store_true')
arg = parser.parse_args()

connect_str = arg.connect_str #Enter your connection string here! Refer to https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=environment-variable-windows for more info
container_name = arg.container_name #Enter your continaer name from azure blob storage here!
blob_service_client = BlobServiceClient.from_connection_string(connect_str) # Create the BlobServiceClient object which will be used to create a container client

def upload_file_to_blob(upload_file_path, target): #file path - >file path
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=target)
    print("\nUploading to Azure Storage as blob:\n\t" + upload_file_path)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

def upload_directory_to_blob(upload_file_path, target): #directory name -> directory name
    print("\nUploading directory to Azure Storage as blob:\n\t" + upload_file_path)
    files = os.listdir(upload_file_path)
    for dir in files:
        file_name = upload_file_path + '/' + dir
        target_ = target+ '/' + dir
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=target_)
        with open(file_name, "rb") as data:
            blob_client.upload_blob(data)

def download_file_from_blob(source, download_file_path):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=source)
    print("\nDownloading blob to \n\t from container" + download_file_path)

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

def download_directory_from_blob(source, download_directory_path):
    container_client = ContainerClient.from_connection_string(conn_str=connect_str, container_name=container_name)
    print(f"\nDownloading all blobs from the following directory {source} in container {container_name}")
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        if source in blob.name:
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
            os.makedirs(os.path.dirname(blob.name), exist_ok=True)
            with open(blob.name, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())


if not arg.download and not arg.upload:
    raise Exception('Specificy either --upload or --download. Specify only one.')

if arg.download: #downloading from source to target
    if not arg.is_directory:
        download_file_from_blob(arg.source, arg.target)
    else:
        download_directory_from_blob(arg.source, arg.target)
else: #Uploading source to target
    if not arg.is_directory:
        upload_file_to_blob(arg.source, arg.target)
    else:
        upload_directory_to_blob(arg.source, arg.target)