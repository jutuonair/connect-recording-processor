#check status of a job
import boto3

#module: get status of transcription job in amazon transcribe
def getjobstatus(transcribe_job_name):

    #creates transcribe resource with debug credentials
    debug_session = boto3.Session(profile_name='crp_debug_usr')
    transcribe_client = debug_session.client('transcribe')
    ##OR
    ##creates transcribe client with machine credentials
    #transcribe_client = boto3.client('transcribe')
    print("transcriber.checkjobstatus: transcribe client created")

    #get transcribe job response from client
    transcribe_job_response = transcribe_client.get_transcription_job(TranscriptionJobName=transcribe_job_name)
    print("transcriber.checkjobstatus: transcribe job response queried")

    #return transcribe job status
    return str(transcribe_job_response['TranscriptionJob']['TranscriptionJobStatus'])

#makes current module executable
if __name__ == "__main__":
    import sys
    result = getjobstatus(str(sys.argv[1]))
    print(str(result))
