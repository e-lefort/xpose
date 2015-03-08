import sys
sys.path.append("gen-py")
from maths import Operation

from thrift.transport import TSocket
from thrift.server import TServer

class OperationHandler:
	def multiply(self, val1, val2):
		print "[Server] request :", val1, "*" , val2
		return val1 * val2

handler = OperationHandler()
processor = Operation.Processor(handler)

listening_socket = TSocket.TServerSocket(port=8585)
server = TServer.TSimpleServer(processor,listening_socket)
server.serve()
