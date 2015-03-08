import sys
sys.path.append("gen-py") 

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from maths import Operation

socket = TSocket.TSocket("localhost",8585)
socket.open()
protocol = TBinaryProtocol.TBinaryProtocol(socket)

client = Operation.Client(protocol)
msg = client.multiply(int(sys.argv[1]), int(sys.argv[2]))
print("[Client] the answer is : %s" % msg) 
