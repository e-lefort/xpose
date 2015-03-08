import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.TException;

import fr.upem.maths.Operation;

public class Client{

	public static void main(String[] args) throws TException {
		TSocket socket = new TSocket("localhost",8585);
		socket.open();

		TBinaryProtocol protocol = new TBinaryProtocol(socket);
		Operation.Client client = new Operation.Client(protocol);

		int res = client.multiply(Integer.parseInt(args[0]), Integer.parseInt(args[1]));

		System.out.println("[Client] the answer is: " + res);

		socket.close();
	}
}
