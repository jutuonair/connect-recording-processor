# non-default package: pip3 install requests
from time import gmtime, strftime, time
import requests
import os

#module: download transcript response file into local file path
def downloadresponsefile(transcript_uri,local_directory = '',local_file_name = 'transcribe-asr-output.json',flag_insert_time_suffix = 'Y'):
    #presets local_file+path to local_directory
    if len(local_directory) == 0:
        part_file_directory = ''
    elif local_directory[-1] == '/':
        part_file_directory = str(local_directory)
    else:
        part_file_directory = str(local_directory) + '/'
    print('transcriber.downloadresponsefile: local file directory set > ' + str(part_file_directory))

    #adds time_suffix if flag = 'Y'
    if flag_insert_time_suffix == 'Y':
        #creates suffix
        part_file_time_suffix = strftime("%Y%m%d-%H%M%S-", gmtime()) + str(int(round(time() * 1000))%1000)
        #separates filename and extension
        part_file_name, part_file_extension = os.path.splitext(local_file_name)
        #creates new file name
        part_file_name = part_file_name + '_' + part_file_time_suffix + part_file_extension
    else: #otherwise, uses input local_file_name parameter
        part_file_name = local_file_name
    print('transcriber.downloadresponsefile: local file name set > ' + str(part_file_name))

    #sets complete file path
    local_file_path = str(part_file_directory) + str(part_file_name)
    print('transcriber.downloadresponsefile: local file path set > ' + str(local_file_path))

    #makes request to download file
    download_request = requests.get(transcript_uri, stream=True)
    print('transcriber.downloadresponsefile: download request.get executed')

    #processes request as data stream
    with open(local_file_path, 'wb') as local_file:
        for data_chunk in download_request.iter_content(chunk_size=1024):
            if data_chunk: # filter out keep-alive new chunks
                local_file.write(data_chunk)
    print('transcriber.downloadresponsefile: data stream processed and local file created > ' + str(local_file_path))

    #returns location of file
    return local_file_path

#makes current module executable
if __name__ == "__main__":
    import sys

    #transcript_uri = 'http://mia.futurehosting.com/test100.zip'
    #local_directory = ''
    #local_file_name = 'test001.zip'
    #flag_insert_time_suffix = 'N'
    #result = downloadresponsefile(transcript_uri,local_directory,local_file_name,flag_insert_time_suffix)

    result = downloadresponsefile(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]))
    print(str(result))
