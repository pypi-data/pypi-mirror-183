from azure.storage.blob import BlobServiceClient

class AzureBlobUtils:
    def __init__(self, connection_string: str):
        self.blob_svc = BlobServiceClient.from_connection_string(connection_string)

    # List the blobs in a container
    def list_blobs_in_container(self, container_name: str) -> list:
        '''
        List the blobs in a container and return a list of blob names with their sizes.
        :param container_name: str
        :return: list
        '''
        blobs = []
        container_client = self.blob_svc.get_container_client(container_name)
        for blob in container_client.list_blobs():
            blobs.append(f"{blob.name},{str(blob.size)}")
        return blobs

    # Check if a blob exists
    def check_blob_exists(self, container_name: str, blob_name: str) -> bool:
        '''
        Check if a blob exists in a container.
        :param container_name: str
        :param blob_name: str
        :return: bool
        '''
        container_client = self.blob_svc.get_container_client(container_name)
        return container_client.get_blob_client(blob_name).exists()
    
    # Check for new blobs (are there blobs in the container?)
    def check_for_new_blobs(self, container_name: str) -> bool:
        '''
        Check if there are new blobs in a container.
        :param blob_svc: BlobServiceClient
        :param container_name: str
        :return: bool
        '''
        try:
            container_client = self.blob_svc.get_container_client(container_name)
            return len(list(container_client.list_blobs())) > 0
        except Exception as e:
            raise e

    
    # Download a blob
    def download_blob(self, container_name: str, input_name: str, dest_dir: str, output_name: str=None) -> str:
        '''
        Download a blob from a container.
        :param container_name: str
        :param input_name: str - This is the name of the blob that will be downloaded.
        :param output_name: str - This is the name of the blob that will be created.
        :param dest_dir: str
        :return: str - This is the name of the blob that was downloaded.
        '''
        blob_client = self.blob_svc.get_blob_client(container=container_name, blob=input_name)
        if output_name is None:
                with open(dest_dir+input_name, "wb") as my_blob:
                    download_stream = blob_client.download_blob()
                    my_blob.write(download_stream.readall())
        else:
            with open(dest_dir+output_name, "wb") as my_blob:
                download_stream = blob_client.download_blob()
                my_blob.write(download_stream.readall())
        return input_name if output_name is None else output_name
    
    # Upload a blob
    def upload_blob(self, container_name: str, output_name: str, src_dir: str) -> str:
        '''
        Upload a blob to a container.
        :param container_name: str
        :param input_name: str - This is the name of the blob that will be uploaded.
        :param output_name: str - This is the name of the blob that will be created.
        :param dest_dir: str
        :return: str - This is the name of the blob that was uploaded.
        '''
        try:
            blob_client = self.blob_svc.get_blob_client(container=container_name, blob=output_name)
            with open(src_dir+output_name, "rb") as data:
                blob_client.upload_blob(data)
            return output_name
        except Exception as e:
            raise e
    
    # Delete a blob
    def delete_blob(self, container_name: str, blob_name: str) -> str:
        '''
        Delete a blob from a container.
        :param blob_svc: BlobServiceClient
        :param container_name: str
        :param blob_name: str
        :return: str - This is the name of the blob that was deleted.
        '''
        blob_client = self.blob_svc.get_blob_client(container=container_name, blob=blob_name)
        blob_client.delete_blob()
        return f"{blob_name} deleted from {container_name}."
    
    # Copy a blob
    def copy_blob(self, account_url: str, sas_token: str, src_container_name: str, dest_container_name: str, input_name: str, output_name: str) -> str:
        '''
        Copy a blob from one container to another.
        Requires SAS token for the source container with Service and Container permissions.
        :param blob_svc: BlobServiceClient
        :param account_url: str
        :param sas_token: str
        :param src_container_name: str
        :param dest_container_name: str
        :param input_name: str
        :param output_name: str
        :return: str - This is the name of the blob that was copied.
        '''
        try:
            pz_blob_client = self.blob_svc.get_blob_client(
                container=dest_container_name, blob=output_name)
            pz_blob_client.start_copy_from_url("/".join([account_url, src_container_name, input_name]) + sas_token)
            return output_name
        except Exception as e:
            raise e

    __version__ = "0.1.0"