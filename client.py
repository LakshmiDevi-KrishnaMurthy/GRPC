import grpc

# import file meta data
from metadata_pb2_grpc import MetadataStub
from metadata_pb2 import(
    GetFileMetaDataRequest,
    GetFileMetaDataResponse  
)

# import file data 
from data_pb2_grpc import DataStub
from data_pb2 import(
    GetFileDataRequest,
    GetFileDataResponse  
)

# get server channel and and unlimited max message length
mdchannel = grpc.insecure_channel("localhost:60009", options=[
            ('grpc.max_send_message_length', -1),
            ('grpc.max_receive_message_length', -1),
        ])

# get meta data stub using server channel
mdstub = MetadataStub(mdchannel)

# files
files = ['english_song.mp3', 'english_rhyme.mp3', 'hindi_song.mp3', 'telugu_song.mp3', 'tamil_song.mp3']

# get each file from files
for f in files:
    # get file meta data
    mdresponse = mdstub.GetFileMetaData(GetFileMetaDataRequest(file=f))

    # get peer channel and unlimited max message length
    dchannel = grpc.insecure_channel(mdresponse.peer_ip_address + ":" + str(mdresponse.peer_port), options=[
            ('grpc.max_send_message_length', -1),
            ('grpc.max_receive_message_length', -1),
        ])

    # get data stub using peer channel
    dstub = DataStub(dchannel)

    # get file data
    dresponse = dstub.GetFileData(GetFileDataRequest(file=f))
    
    # write file data
    fn = "client_" + f
    fnh = open(fn, "wb")
    fnh.write(dresponse.file_content)
    fnh.close()
    
    # print download file
    print("File {} is downloaded as {}".format(f, fn))





