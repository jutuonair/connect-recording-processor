#transcribe one wav file
from __future__ import print_function
import time
import boto3

#defines transcribe job parameters
transcribe_job_name = 'transcribe-wav-crp'
transcribe_job_uri = 'https://s3.amazonaws.com/testing-crp/sample-wav/OSR_us_000_0061_8k.wav'

#creates transcribe resource with debug credentials
debug_session = boto3.Session(profile_name='crp_debug_usr')
transcribe_client = debug_session.client('transcribe')

#creates transcribe client with machine credentials
#transcribe_client = boto3.client('transcribe')

#starts transcribe Job
transcribe_client.start_transcription_job(
    TranscriptionJobName=transcribe_job_name
    ,Media={'MediaFileUri':transcribe_job_uri}
    ,Settings={'ShowSpeakerLabels':True}
    ,MediaFormat='wav'
    ,LanguageCode='en-US'
)

#waits for transcribe job to finish
while True:
    transcribe_job_status = transcribe_client.get_transcription_job(TranscriptionJobName=transcribe_job_name)
    if transcribe_job_status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print('Not ready yet...')
    time.sleep(5)

print(transcribe_job_status)

#s3 delimiters and prefixes: "object" management
### https://realguess.net/2014/05/24/amazon-s3-delimiter-and-prefix/
#s3 file handling reference documentation
### http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.download_file
# file handling examples:
### https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/s3/s3-python-example-download-file.py
### https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/s3/s3-python-example-upload-file.py

#transcript object reference documentation
### http://boto3.readthedocs.io/en/latest/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job
#sample transcribe code
### https://docs.aws.amazon.com/transcribe/latest/dg/getting-started-python.html

##################################################################################################################
#NEXT STEPS:
#STEP 1: in the transcribe job status, you get a "Transcript" objects
#STEP 2: inside the transcript object, you get a "TranscriptFileUri" like the following:
'''
https://s3.amazonaws.com/aws-transcribe-us-east-1-prod/519902577677/transcribe-wav-crp/asrOutput.json?X-Amz-Security-Token=FQoDYXdzEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDLjfmMds4vrhTaM19yK3AwrIOSKLWoSFS5b4qpPXGuatQqt8f3LlMZLWBiHf9FXzp0PkPcB8NdGZ97hRynUFJUX5QZfEn14Xla3GM8iKObXzdDdd4icz2TGqODXHROr9wRS9zIDw9eROO4io8bmQSL2r3BKO3qRobRXYj3OHqb1B7219GVcJ%2Baw%2FZPKi6%2Bsd7N%2BrLTMwBsZpuA9FBj5DxCxkLBBfBQFHHMlmuFniScWaYX3aW4iiGQd2r3E0HmiCFvuo35N0DcLqvoQPmsotTlQrIpIdxmnWhtwM%2FT6tNEiNYoxzdsT0r%2FCgz11qs%2FzRWnOfc6CeqQCsFRLptTM3evyr61MIZ5GgmjSYe0JsLbnITlZ%2BopQAVq%2BMR9JsZObgGFMEVu%2F64WmNo2jTYjxN3fUC%2BkwvWs1uekdaJsh%2BFfbiYUwZ4Gqk%2Fu9lvQt1HrB1%2B3QrXKOv7fQo4k6IrjOsw%2Fh%2BiUzrS3jDATAY68BWixvpnvRaJkOwFReRG0xzr7hbXp4ukGpV6v1s88pWC6Z2YoumtkDmK%2FWcenvs0oTbBCvX%2Fvop4qOvswdzhc%2Fd6%2FAlq7PSqvtpowpj%2FUTikIZsuYkfoS2cOz0oitmh1gU%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20180407T074532Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=ASIAJH65BEMO6RORWDVQ%2F20180407%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=829109fd1bf4dee50d9dc758085f2f0b7e775e0a4d6a4e52b19b8b6eab665ab9
'''
#STEP 3: donwload file using s3.download_fileobj(Bucket, Key, Fileobj, ExtraArgs=None, Callback=None, Config=None)
### or download_file(Bucket, Key, Filename, ExtraArgs=None, Callback=None, Config=None) can also be used
#STEP 4: ýou would have to review how to send X-Amz-Security-Token, X-Amz-Algorithm, X-Amz-Date, X-Amz-SignedHeaders, X-Amz-Expires, X-Amz-Credential and X-Amz-Signature as parameters

###URL: https://s3.amazonaws.com/aws-transcribe-us-east-1-prod/519902577677/transcribe-wav-crp/asrOutput.json?
###X-Amz-Security-Token=FQoDYXdzEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDLjfmMds4vrhTaM19yK3AwrIOSKLWoSFS5b4qpPXGuatQqt8f3LlMZLWBiHf9FXzp0PkPcB8NdGZ97hRynUFJUX5QZfEn14Xla3GM8iKObXzdDdd4icz2TGqODXHROr9wRS9zIDw9eROO4io8bmQSL2r3BKO3qRobRXYj3OHqb1B7219GVcJ%2Baw%2FZPKi6%2Bsd7N%2BrLTMwBsZpuA9FBj5DxCxkLBBfBQFHHMlmuFniScWaYX3aW4iiGQd2r3E0HmiCFvuo35N0DcLqvoQPmsotTlQrIpIdxmnWhtwM%2FT6tNEiNYoxzdsT0r%2FCgz11qs%2FzRWnOfc6CeqQCsFRLptTM3evyr61MIZ5GgmjSYe0JsLbnITlZ%2BopQAVq%2BMR9JsZObgGFMEVu%2F64WmNo2jTYjxN3fUC%2BkwvWs1uekdaJsh%2BFfbiYUwZ4Gqk%2Fu9lvQt1HrB1%2B3QrXKOv7fQo4k6IrjOsw%2Fh%2BiUzrS3jDATAY68BWixvpnvRaJkOwFReRG0xzr7hbXp4ukGpV6v1s88pWC6Z2YoumtkDmK%2FWcenvs0oTbBCvX%2Fvop4qOvswdzhc%2Fd6%2FAlq7PSqvtpowpj%2FUTikIZsuYkfoS2cOz0oitmh1gU%3D
###X-Amz-Algorithm=AWS4-HMAC-SHA256
###X-Amz-Date=20180407T074532Z
###X-Amz-SignedHeaders=host
###X-Amz-Expires=899
###X-Amz-Credential=ASIAJH65BEMO6RORWDVQ%2F20180407%2Fus-east-1%2Fs3%2Faws4_request
###X-Amz-Signature=829109fd1bf4dee50d9dc758085f2f0b7e775e0a4d6a4e52b19b8b6eab665ab9

#STEP 5: Once file is downloaded to local machine, next step is to upload it to json folder in personal S3 bucket
#STEP 6: Upload file via upload_file(Filename, Bucket, Key, ExtraArgs=None, Callback=None, Config=None)
### or upload_fileobj(Fileobj, Bucket, Key, ExtraArgs=None, Callback=None, Config=None) can also be used

print('### End of Transcribe Job ###')
