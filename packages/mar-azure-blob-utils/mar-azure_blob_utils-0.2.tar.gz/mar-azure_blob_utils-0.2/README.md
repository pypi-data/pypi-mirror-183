# mar-db_utils

## Description
This package contains a set of utilities for interacting with Azure Blob Storage.
To use, instantiate the AzureBlobUtils class (usually as 'abu') with the SAS connection string as an argument.

The following methods are available:
- list_blobs_in_container
    - Returns a list of all blobs in a container.
- check_blob_exists
    - Returns True if a blob exists, False if it does not.
- check_for_new_blobs
    - Returns a true if there are blobs in a container (slight misnomer, but it's what I'm using it for).
    - This may be renamed to 'check_for_blobs' in the future.
- download_blob
    - Downloads a blob to a specified location.
- upload_blob
    - Uploads a blob to a specified location.
- delete_blob
    - Deletes a blob.
- copy_blob
    - Copies a blob from one container to another.
