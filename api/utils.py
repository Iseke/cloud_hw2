from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def azure_connect_sas_token(token, account_url, source_container_name):
    try:
        blob_source_service_client = BlobServiceClient(account_url = account_url, credential = token)
        source_container_client = blob_source_service_client.get_container_client(source_container_name)
        return source_container_client

    except Exception as ex:
        print ("Error: " + str(ex))


def container_content_list(connection_instance):
    try:
        blob_name_list = []
        source_blob_list = connection_instance.list_blobs()

        for blob in source_blob_list:
            blob_name = blob.name.rsplit('/',1)[0]
            blob_name_list.append(blob_name)

        return blob_name_list

    except Exception as ex:
        print ("Error: " + str(ex))

def generate_proper_sas_url_list(image_list):
    generated_image_list = []

    for image in image_list:
        generated_image_list.append(sas_url(image))

    return generated_image_list


def sas_url(image_name):
    return f'https://islamhw4.blob.core.windows.net/publicfiles/{image_name}?sp=rl&st=2021-03-07T08:32:46Z&se=2021-03-21T16:32:46Z&sv=2020-02-10&sr=c&sig=b9r0p3bDwaUXjqBkmoWd7InEeSpEr9EbfFQIXT0V71U%3D'


def main():
    try:
        azure_sas_token = 'sp=rl&st=2021-03-07T08:32:46Z&se=2021-03-21T16:32:46Z&sv=2020-02-10&sr=c&sig=b9r0p3bDwaUXjqBkmoWd7InEeSpEr9EbfFQIXT0V71U%3D'
        azure_acc_url = 'https://islamhw4.blob.core.windows.net'
        container_name = 'publicfiles'

        ## SAS Token
        connection_instance = azure_connect_sas_token(azure_sas_token, azure_acc_url, container_name)
        content_list = container_content_list(connection_instance)
        return generate_proper_sas_url_list(content_list)

    except Exception as ex:
        print('main | Error: ', ex)
