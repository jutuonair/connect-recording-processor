#check status of a job
import boto3

#module: get transcribe result uri from amazon transcribe
def getresponseuri(transcribe_job_name):

    #creates transcribe resource with debug credentials
    debug_session = boto3.Session(profile_name='crp_debug_usr')
    transcribe_client = debug_session.client('transcribe')
    ##OR
    ##creates transcribe client with machine credentials
    #transcribe_client = boto3.client('transcribe')
    print("transcriber.getresponseuri: transcribe client created")

    #get transcribe job response from client
    transcribe_job_response = transcribe_client.get_transcription_job(TranscriptionJobName=transcribe_job_name)
    print("transcriber.getresponseuri: transcribe job response queried")

    #return transcribe job response uri
    return str(transcribe_job_response['Transcript']['TranscriptFileUri'])

#makes current module executable
if __name__ == "__main__":
    import sys
    result = getresponseuri(str(sys.argv[1]))
    print(str(result))
