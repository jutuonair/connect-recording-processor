#uploads a file to amazon s3
import boto3
from boto3.s3.transfer import TransferConfig
import ntpath
import os

#module: upload local file to amazon s3 bucket
def uploadfile(local_file_path, s3_bucket_name, s3_folder_name, flag_delete_local_file = 'Y'):

    #creates transcribe resource with debug credentials
    debug_session = boto3.Session(profile_name='crp_debug_usr')
    s3_resource = debug_session.resource('s3')
    ##OR
    ##creates transcribe client with machine credentials
    #s3_resource = boto3.resource('s3')
    print("storagehandler.uploadfile: s3 resource object created")

    #create s3 bucket objects
    s3_bucket = s3_resource.Bucket(s3_bucket_name)
    print("storagehandler.uploadfile: s3 bucket object created for > s3::" + str(s3_bucket_name))


    #defines file name from local_file_path
    local_file_name = ntpath.basename(local_file_path)
    print("storagehandler.uploadfile: local file name set > " + str(local_file_name))

    #defines s3 key for file uploads
    s3_key = (str(s3_folder_name) + '/{}').format(local_file_name)
    print("storagehandler.uploadfile: s3 key set > " + str(s3_key))

    #try file upload
    try:
        with open(local_file_path, 'rb') as local_file_data:
            s3_bucket.upload_fileobj(
            local_file_data
            ,s3_key
            )
    except Exception as ex1:
        # This is a catch all exception
        print("File Upload Exception: ", ex1)
        return ex1
    print("storagehandler.uploadfile: upload completed")

    #if flag = 'Y' then deletes local file
    if flag_delete_local_file == 'Y':
        try:
            os.remove(local_file_path)
        except OSError as ex2:
            print ("OS Error: %s - %s." % (ex2.filename,ex2.strerror))
            return ex2
        print("storagehandler.uploadfile: local file deleted")
    else:
        print("storagehandler.uploadfile: local file maintained")

    return 1

#makes current module executable
if __name__ == "__main__":
    import sys

    #local_file_path = 'test02.zip'
    #s3_bucket_name = 'testing-crp'
    #s3_folder_name = 'transcript-response'
    #flag_delete_local_file = 'N'
    #result = uploadfile(local_file_path,s3_bucket_name,s3_folder_name, flag_delete_local_file)

    result = uploadfile(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]))
    print(result)
