#start a transcribe job
from __future__ import print_function
from time import gmtime, strftime
import time
import boto3

#sets transcribe job prefix
transcribe_job_prefix = 'transcribe-wav-crp'

#module: start transcription job in amazon transcribe]
def startjob(audio_file_url):

    #creates transcribe resource with debug credentials
    debug_session = boto3.Session(profile_name='crp_debug_usr')
    transcribe_client = debug_session.client('transcribe')
    ##OR
    ##creates transcribe client with machine credentials
    #transcribe_client = boto3.client('transcribe')
    print("transcriber.startjob: transcribe client created")

    #defines relevant job name based on current time
    transcribe_job_suffix = strftime("%Y%m%d-%H%M%S-", gmtime()) + str(int(round(time() * 1000))%1000)
    transcribe_job_name = transcribe_job_prefix + transcribe_job_suffix
    print("transcriber.startjob: job name defined > " + str(transcribe_job_name))

    #define audio file url
    transcribe_job_uri = audio_file_url
    print("transcriber.startjob: job uri defined > " + str(audio_file_url));

    #starts transcribe job
    transcribe_client.start_transcription_job(
        TranscriptionJobName=transcribe_job_name
        ,Media={'MediaFileUri':transcribe_job_uri}
        ,Settings={'ShowSpeakerLabels':True}
        ,MediaFormat='wav'
        ,LanguageCode='en-US'
    )
    print("transcriber.startjob: transcribe job started")

    #returns name of the transcribe job started
    return str(transcribe_job_name)

#makes current module executable
if __name__ == "__main__":
    import sys
    result = startjob(str(sys.argv[1]))
    print(result)
