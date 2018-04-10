#transcribe one wav file
from __future__ import print_function
import time
import boto3

#creates s3 resource with debug credentials
debug_session = boto3.Session(profile_name='crp_debug_usr')
s3_resource = debug_session.resource('s3')

#creates s3 resource with machine credentials
# s3_resource = boto3.resource('s3')

#creates s3 bucket from resource
wav_bucket = s3_resource.Bucket('testing-crp')

#creates object iterator
object_summary_list = wav_bucket.objects.filter(Prefix='sample-wav/O')

#iterates over the listing
count = 0
for wav_object in object_summary_list:
    count += 1
    print(wav_object.key)

print('### End of List ### Total Objects = ' + str(count))
