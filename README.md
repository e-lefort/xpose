# XPOSE

## Run demo

### Generate code

    $> thrift --gen java --gen py hello.thrift

    $> javac -cp /usr/local/lib/libthrift-0.9.2.jar:/usr/local/lib/slf4j-api-1.5.8.jar:/usr/local/lib/slf4j-log4j12-1.5.8.jar:/usr/local/lib/log4j-1.2.14.jar HelloClient.java gen-java/HelloSvc.java

    $> javac -cp /usr/local/lib/libthrift-0.9.2.jar:/usr/local/lib/slf4j-api-1.5.8.jar:/usr/local/lib/slf4j-log4j12-1.5.8.jar:/usr/local/lib/log4j-1.2.14.jar Client.java gen-java/fr/upem/maths/Operation.java

### Execute code

    $> python hello_client.py

    $> java -cp /usr/local/lib/libthrift-0.9.2.jar:/usr/local/lib/slf4j-api-1.5.8.jar:/usr/local/lib/slf4j-log4j12-1.5.8.jar:/usr/local/lib/log4j-1.2.14.jar:./gen-java:. HelloClient

    $> java -cp /usr/local/lib/libthrift-0.9.2.jar:/usr/local/lib/slf4j-api-1.5.8.jar:/usr/local/lib/slf4j-log4j12-1.5.8.jar:/usr/local/lib/log4j-1.2.14.jar:./gen-java:. Client 2 3
