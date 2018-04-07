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

print('### End of Transcribe Job ###')
