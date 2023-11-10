# GRPC
Sample GRPC program 

This is sample GRPC program that client communicate with server for metadata, and clients itself can act as peer and download the file using python.

commands to run

pip install grpcio-tools

1. compile meta data proto buffer
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. metadata.proto

2. compile data proto buffer
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. data.proto

3. Run server
python server.py

4. Run peer
python peer.py 60000

5. Run peer
python peer.py 60001

6. Run peer
python peer.py 60002

7. Run client
python client.py
