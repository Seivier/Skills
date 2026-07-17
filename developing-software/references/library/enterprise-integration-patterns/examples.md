# Enterprise Integration Patterns - Code Examples & Case Studies

## Table of Contents

- [The Addison-Wesley Signature Series](#the-addison-wesley-signature-series)
- [Foreword (1)](#foreword-1)
- [Foreword (2)](#foreword-2)
- [Preface](#preface)
- [Acknowledgments](#acknowledgments)
- [Introduction](#introduction)
- [Chapter 1. Solving Integration Problems Using Patterns](#chapter-1-solving-integration-problems-using-patterns)
- [Chapter 2. Integration Styles](#chapter-2-integration-styles)
- [Chapter 3. Messaging Systems](#chapter-3-messaging-systems)
- [Chapter 4. Messaging Channels](#chapter-4-messaging-channels)
- [Chapter 5. Message Construction](#chapter-5-message-construction)
- [Chapter 6. Interlude: Simple Messaging](#chapter-6-interlude-simple-messaging)
- [Chapter 7. Message Routing](#chapter-7-message-routing)
- [Chapter 8. Message Transformation](#chapter-8-message-transformation)
- [Chapter 9. Interlude: Composed Messaging](#chapter-9-interlude-composed-messaging)
- [Chapter 10. Messaging Endpoints](#chapter-10-messaging-endpoints)
- [Chapter 11. System Management](#chapter-11-system-management)
- [Chapter 12. Interlude: System Management Example](#chapter-12-interlude-system-management-example)
- [Chapter 13. Integration Patterns in Practice](#chapter-13-integration-patterns-in-practice)
- [Chapter 14. Concluding Remarks](#chapter-14-concluding-remarks)
- [Bibliography](#bibliography)

---

## The Addison-Wesley Signature Series

There are no code examples or pattern design examples in this chapter. The chapter lists metadata for books in the Addison-Wesley Signature Series, including titles, authors, and ISBNs, which are detailed in the summary.

---

## Foreword (1)

There are no code snippets or specific pattern implementation examples in this foreword.

---

## Foreword (2)

There are no code snippets or specific pattern examples provided in this foreword.

---

## Preface

There are no code snippets or concrete software design examples in the Preface. The text mentions that code examples in subsequent chapters will be implemented using technologies like Java Message Service (JMS), Microsoft Message Queuing (MSMQ), TIBCO, BizTalk, and XSLT. It also includes a reference to Dr. Carl Sagan's Pioneer Plaque as a high-level representation/metaphor of a message sent to extraterrestrial life forms, but contains no technical architectural examples.

---

## Acknowledgments

There are no architectural diagrams, code snippets, pattern descriptions, or technical examples in this introductory acknowledgments chapter.

---

## Introduction

There are no code snippets or concrete examples provided in this introductory chapter of the book. The chapter focus is strictly conceptual, defining basic integration styles, asynchronous messaging terms, pattern architecture, and mapping neutral terminology to various commercial messaging platforms.

---

## Chapter 1. Solving Integration Problems Using Patterns

String hostName = "finance.bank.com";
int port = 80;

IPHostEntry hostInfo = Dns.GetHostByName(hostName);
IPAddress address = hostInfo.AddressList[0];

IPEndPoint endpoint = new IPEndPoint(address, port);

Socket socket = new Socket(address.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
socket.Connect(endpoint);

byte[] amount = BitConverter.GetBytes(1000);
byte[] name   = Encoding.ASCII.GetBytes("Joe");

int bytesSent = socket.Send(amount);
bytesSent    += socket.Send(name);

socket.Close();

Byte Representation Example:
232  3  0  0

---

## Chapter 2. Integration Styles

There are no code snippets in this chapter. However, the chapter provides conceptual pattern descriptions and figures for four integration styles: File Transfer, Shared Database, Remote Procedure Invocation, and Messaging. Below are the pattern descriptions in prose as detailed in the chapter:
- File Transfer: Have each application produce files that contain the information the other applications must consume. Integrators take the responsibility of transforming files into different formats. Produce the files at regular intervals according to the nature of the business.
- Shared Database: Integrate applications by having them store their data in a single Shared Database, and define the schema of the database to handle all the needs of the different applications.
- Remote Procedure Invocation: Develop each application as a large-scale object or component with encapsulated data. Provide an interface to allow other applications to interact with the running application.
- Messaging: Use Messaging to transfer packets of data frequently, immediately, reliably, and asynchronously, using customizable formats.

---

## Chapter 3. Messaging Systems

**EXAMPLE 1: J2EE JMS REFERENCE IMPLEMENTATION**

Creating JMS destinations using the `j2eeadmin` administration tool:

```
j2eeadmin -addJmsDestination jms/mytopic topic
j2eeadmin -addJmsDestination jms/myqueue queue
```

Accessing the administered destinations via Java NNDI lookup:

```java
Context jndiContext = new InitialContext();
Queue myQueue = (Queue) jndiContext.lookup("jms/myqueue");
Topic myTopic = (Topic) jndiContext.lookup("jms/mytopic");
```

**EXAMPLE 2: IBM WEBSPHERE MQ DESCRIPTONS**

Defining a queue via the MQ administration command:

```
DEFINE Q(myQueue)
```

Accessing the queue programmatically using a JMS session in WebSphere MQ:

```java
Session session = // create the session
Queue queue = session.createQueue("myQueue");
```

**EXAMPLE 3: MICROSOFT MSMQ INSTANTIATION**

Creating a message queue programmatically in C#:

```csharp
using System.Messaging;
...
MessageQueue.Create("MyQueue");
```

Accessing the queue using the MessageQueue class instance:

```csharp
MessageQueue mq = new MessageQueue("MyQueue");
```

**EXAMPLE 4: SOAP ENVELOPE STRUCTURING**

An example of a SOAP envelope containing a Header and a Body, representing a message:

```xml
<SOAP-ENV:Envelope
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
   <SOAP-ENV:Header>
       <t:Transaction
           xmlns:t="some-URI"
           SOAP-ENV:mustUnderstand="1">
               5
       </t:Transaction>
   </SOAP-ENV:Header>
   <SOAP-ENV:Body>
       <m:GetLastTradePrice xmlns:m="Some-URI">
           <symbol>DEF</symbol>
       </m:GetLastTradePrice>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

**EXAMPLE 5: SIMPLE FILTER IN C# AND MSMQ**

Below is the complete C# code for a generic base Processor class, representing a filter with one input and one output port:

```csharp
using System;
using System.Messaging;

namespace PipesAndFilters
{
    public class Processor
    {
        protected MessageQueue inputQueue;
        protected MessageQueue outputQueue;

        public Processor (MessageQueue inputQueue, MessageQueue outputQueue)
        {
            this.inputQueue = inputQueue;
            this.outputQueue = outputQueue;
        }

        public void Process()
        {
            inputQueue.ReceiveCompleted += new
 ReceiveCompletedEventHandler(OnReceiveCompleted);
            inputQueue.BeginReceive();
        }

        private void OnReceiveCompleted(Object source, 
 ReceiveCompletedEventArgs asyncResult)
        {
            MessageQueue mq = (MessageQueue)source;

            Message inputMessage = mq.EndReceive(asyncResult.AsyncResult);
            inputMessage.Formatter = new XmlMessageFormatter
                                          (new String[] {"System.String,mscorlib"});

            Message outputMessage = ProcessMessage(inputMessage);

            outputQueue.Send(outputMessage);

            mq.BeginReceive();
        }

        protected virtual Message ProcessMessage(Message m)
        {
            Console.WriteLine("Received Message: " + m.Body);
            return (m);
        }
    }
}
```

**EXAMPLE 6: SIMPLE ROUTER IN C# AND MSMQ**

A simple message router that routes an incoming message to one of two output channels based on an alternating boolean condition:

```csharp
using System;
using System.Messaging;

class SimpleRouter
{
    protected MessageQueue inQueue;
    protected MessageQueue outQueue1;
    protected MessageQueue outQueue2;

    public SimpleRouter(MessageQueue inQueue, MessageQueue outQueue1, MessageQueue outQueue2)
    {
        this.inQueue = inQueue;
        this.outQueue1 = outQueue1;
        this.outQueue2 = outQueue2;

        inQueue.ReceiveCompleted += new
 ReceiveCompletedEventHandler(OnMessage);
        inQueue.BeginReceive();
    }
    
    private void OnMessage(Object source, 
 ReceiveCompletedEventArgs asyncResult)
    {
        MessageQueue mq = (MessageQueue)source;
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        if (IsConditionFulfilled())
            outQueue1.Send(message);
        else
            outQueue2.Send(message);

        mq.BeginReceive();
    }

    protected bool toggle = false;

    protected bool IsConditionFulfilled()
    {
        toggle = !toggle;
        return toggle;
    }
}
```

**EXAMPLE 7: STRUCTURAL TRANSFORMATION WITH XSL**

An incoming XML document representing nested customer data:

```xml
<data>
    <customer>
        <firstname>Joe</firstname>
        <lastname>Doe</lastname>
        <address type="primary">
            <ref id="55355"/>
        </address>
        <address type="secondary">
            <ref id="77889"/>
        </address>
    </customer>
    <address id="55355">
        <street>123 Main</street>
        <city>San Francisco</city>
        <state>CA</state>
        <postalcode>94123</postalcode>
        <country>USA</country>
        <phone type="cell">
            <area>415</area>
            <prefix>555</prefix>
            <number>1234</number>
        </phone>
        <phone type="home">
            <area>415</area>
            <prefix>555</prefix>
            <number>5678</number>
        </phone>
    </address>
    <address id="77889">
        <company>ThoughtWorks</company>
        <street>410 Townsend</street>
        <city>San Francisco</city>
        <state>CA</state>
        <postalcode>94107</postalcode>
        <country>USA</country>
    </address>
</data>
```

Below is the expected output XML structure for the accounting system:

```xml
<Kunde>
    <Name>Joe Doe</Name>
    <Adresse>
        <Strasse>123 Main</Strasse>
        <Ort>San Francisco</Ort>
        <Telefon>415-555-1234</Telefon>
    </Adresse>
</Kunde>
```

And here is the complete XSLT stylesheet that achieves this structural mapping:

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes"/>
    <xsl:key name="addrlookup" match="/data/address" use="@id"/>
    <xsl:template match="data">
        <xsl:apply-templates select="customer"/>
    </xsl:template>
    <xsl:template match="customer">
        <Kunde>
            <Name>
                <xsl:value-of select="concat(firstname, ' ', lastname)"/>
            </Name>
            <Adresse>
                <xsl:variable name="id" select="./address[@type='primary']/ref/@id"/>
                <xsl:call-template name="getaddr">
                    <xsl:with-param name="addr" select="key('addrlookup', $id)"/>
                </xsl:call-template>
            </Adresse>
        </Kunde>
    </xsl:template>
    <xsl:template name="getaddr">
        <xsl:param name="addr"/>
        <Strasse>
            <xsl:value-of select="$addr/street"/>
        </Strasse>
        <Ort>
            <xsl:value-of select="$addr/city"/>
        </Ort>
        <Telefon>
            <xsl:choose>
                <xsl:when test="$addr/phone[@type='cell']">
                    <xsl:apply-templates select="$addr/phone[@type='cell']" mode="getphone"/>
                </xsl:when>
                <xsl:otherwise>
                    <xsl:apply-templates select="$addr/phone[@type='home']" mode="getphone"/>
                </xsl:otherwise>
            </xsl:choose>
        </Telefon>
    </xsl:template>
    <xsl:template match="phone" mode="getphone">
        <xsl:value-of select="concat(area, '-', prefix, '-', number)"/>
    </xsl:template>
    <xsl:template match="*"/>
</xsl:stylesheet>
```

---

## Chapter 4. Messaging Channels

Point-to-Point Channel Code Snippets:

1. Java Message Service (JMS) 1.0/1.1 Queue Sender (Point-to-Point):
Queue queue = // obtain the queue via JNDI
QueueConnectionFactory factory = // obtain the connection factory via JNDI
QueueConnection connection = factory.createQueueConnection();
QueueSession session = connection.createQueueSession(true, Session.AUTO_ACKNOWLEDGE);
QueueSender sender = session.createSender(queue);

Message message = session.createTextMessage("The contents of the message.");

sender.send(message);

2. Java Message Service (JMS) 1.0/1.1 Queue Receiver (Point-to-Point):
Queue queue = // obtain the queue via JNDI
QueueConnectionFactory factory = // obtain the connection factory via JNDI
QueueConnection connection = factory.createQueueConnection();
QueueSession session = connection.createQueueSession(true, Session.AUTO_ACKNOWLEDGE);
QueueReceiver receiver = session.createReceiver(queue);

TextMessage message = (TextMessage) receiver.receive();
String contents = message.getText();

3. .NET MessageQueue Sender (Point-to-Point):
MessageQueue queue = new MessageQueue("MyQueue");
queue.Send("The contents of the message.");

4. .NET MessageQueue Receiver (Point-to-Point):
MessageQueue queue = new MessageQueue("MyQueue");
Message message = queue.Receive();
String contents = (String) message.Body();

Publish-Subscribe Channel Code Snippets:

1. Java Message Service (JMS) Topic Publisher (Publish-Subscribe):
Topic topic = // obtain the topic via JNDI
TopicConnectionFactory factory = // obtain the connection factory via JNDI
TopicConnection connection = factory.createTopicConnection();
TopicSession session = connection.createTopicSession(true, Session.AUTO_ACKNOWLEDGE);
TopicPublisher publisher = session.createPublisher(topic);

Message message = session.createTextMessage("The contents of the message.");

publisher.publish(message);

2. Java Message Service (JMS) Topic Subscriber (Publish-Subscribe):
Topic topic = // obtain the topic via JNDI
TopicConnectionFactory factory = // obtain the connection factory via JNDI
TopicConnection connection = factory.createTopicConnection();
TopicSession session = connection.createTopicSession(true, Session.AUTO_ACKNOWLEDGE);
TopicSubscriber subscriber = session.createSubscriber(topic);

TextMessage message = (TextMessage) subscriber.receive();
String contents = message.getText();

Guaranteed Delivery Code Snippets and Configurations:

1. Setting Per-Message Persistence in JMS:
Session session = // obtain the session
Destination destination = // obtain the destination
Message message = // create the message
MessageProducer producer = session.createProducer(destination);
producer.send(
    message,
    javax.jms.DeliveryMode.PERSISTENT,
    javax.jms.Message.DEFAULT_PRIORITY,
    javax.jms.Message.DEFAULT_TIME_TO_LIVE);

2. Setting Default Persistent Delivery Mode on a JMS Producer:
producer.setDeliveryMode(javax.jms.DeliveryMode.PERSISTENT);
producer.send(message);

3. WebSphere MQ Persistent Queue Configurations:
- Define a queue with persistent messages:
DEFINE Q(myQueue) PER(PERS)

- Define a queue where message persistence is determined by the application:
DEFINE Q(myQueue) PER(APP)

4. .NET Transactional (Persistent) Queue Creation:
MessageQueue.Create("MyQueue", true);

---

## Chapter 5. Message Construction

The chapter provides several concrete examples and code snippets for different patterns:

Command Message Example:
In the SOAP protocol and WSDL service description, an RPC-style SOAP request serves as a Command Message. The XML body contains the method name GetLastTradePrice and the parameter symbol:
```xml
<SOAP-ENV:Envelope
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
   <SOAP-ENV:Body>
       <m:GetLastTradePrice xmlns:m="Some-URI">
           <symbol>DIS</symbol>
       </m:GetLastTradePrice>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

Document Message Example:
A purchase order represented in XML is sent using JMS via a TextMessage:
```java
Session session = // Obtain the session
Destination dest = // Obtain the destination
MessageProducer sender = session.createProducer(dest);
String purchaseOrder =
"    <po id=\"48881\" submitted=\"2002-04-23\">" +
"        <shipTo>" +
"            <company>Chocoholics</company>" +
"            <street>2112 North Street</street>" +
"            <city>Cary</city>" +
"            <state>NC</state>" +
"            <postalCode>27522</postalCode>" +
"        </shipTo>" +
"        <order>" +
"            <item sku=\"22211\" quantity=\"40\">" +
"                <description>Bunny, Dark Chocolate, Large</description>" +
"            </item>" +
"        </order>" +
"    </po>";
TextMessage message = session.createTextMessage();
message.setText(purchaseOrder);
sender.send(message);
```
Additionally, a SOAP response message is a Document Message returning the result of the method call:
```xml
<SOAP-ENV:Envelope
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
   <SOAP-ENV:Body>
       <m:GetLastTradePriceResponse xmlns:m="Some-URI">
           <Price>34.5</Price>
       </m:GetLastTradePriceResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

Request-Reply Example:
A JMS implementation uses QueueRequestor to send requests and block until a reply is received:
```java
QueueConnection connection = // obtain the connection
Queue requestQueue = // obtain the queue
Message request = // create the request message
QueueSession session = connection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
QueueRequestor requestor = new QueueRequestor(session, requestQueue);
Message reply = requestor.request(request);
```

Return Address Example:
A JMS sender sets the JMSReplyTo property on the request message, and the receiver retrieves it to send the reply:
```java
// Sender side
Queue requestQueue = // Specify the request destination
Queue replyQueue = // Specify the reply destination
Message requestMessage = // Create the request message
requestMessage.setJMSReplyTo(replyQueue);
MessageProducer requestSender = session.createProducer(requestQueue);
requestSender.send(requestMessage);

// Receiver side
Queue requestQueue = // Specify the request destination
MessageConsumer requestReceiver = session.createConsumer(requestQueue);
Message requestMessage = requestReceiver.receive();
Message replyMessage = // Create the reply message
Destination replyQueue = requestMessage.getJMSReplyTo();
MessageProducer replySender = session.createProducer(replyQueue);
replySender.send(replyMessage);
```

Correlation Identifier Example:
A JMS reply message copies the request's message ID to its correlation ID property:
```java
Message requestMessage = // Get the request message
Message replyMessage = // Create the reply message
String requestID = requestMessage.getJMSMessageID();
replyMessage.setJMSCorrelationID(requestID);
```
In Web Services, SOAP request and response headers contain MessageId and ResponseTo to correlate asynchronous exchanges:
Request message containing Message Identifier:
```xml
<?xml version="1.0" ?>
<env:Envelope xmlns:env="http://www.w3.org/2002/06/soap-envelope">
  <env:Header>
    <n:MsgHeader xmlns:n="http://example.org/requestresponse">
      <n:MessageId>uuid:09233523-345b-4351-b623-5dsf35sgs5d6</n:MessageId>
    </n:MsgHeader>
  </env:Header>
  <env:Body>
      ........
  </env:Body>
</env:Envelope>
```
Response message containing correlation:
```xml
<?xml version="1.0" ?>
<env:Envelope xmlns:env="http://www.w3.org/2002/06/soap-envelope">
  <env:Header>
    <n:MsgHeader xmlns:n="http://example.org/requestresponse">
      <n:MessageId>uuid:09233523-567b-2891-b623-9dke28yod7m9</n:MessageId>
      <n:ResponseTo>uuid:09233523-345b-4351-b623-5dsf35sgs5d6</n:ResponseTo>
    </n:MsgHeader>
  </env:Header>
  <env:Body>
      ........
  </env:Body>
</env:Envelope>
```

Message Sequence Example:
A Web Services example illustrates response messages containing sequencing and correlation:
First response message:
```xml
<?xml version="1.0" ?>
<env:Envelope xmlns:env="http://www.w3.org/2002/06/soap-envelope">
  <env:Header>
    <n:MsgHeader xmlns:n="http://example.org/requestresponse">
      <n:MessageId>uuid:09233523-567b-2891-b623-9dke28yod7m9</n:MessageId>
      <n:ResponseTo>uuid:09233523-345b-4351-b623-5dsf35sgs5d6</n:ResponseTo>
    </n:MsgHeader>
    <s:Sequence xmlns:s="http://example.org/sequence">
      <s:SequenceNumber>1</s:SequenceNumber>
      <s:TotalInSequence>5</s:TotalInSequence>
    </s:Sequence>
  </env:Header>
  <env:Body>
    ........
  </env:Body>
</env:Envelope>
```
Final response message:
```xml
<?xml version="1.0" ?>
<env:Envelope xmlns:env="http://www.w3.org/2002/06/soap-envelope">
  <env:Header>
    <n:MsgHeader xmlns:n="http://example.org/requestresponse">
      <n:MessageId>uuid:40195729-sj20-pso3-1092-p20dj28rk104</n:MessageId>
      <n:ResponseTo>uuid:09233523-345b-4351-b623-5dsf35sgs5d6</n:ResponseTo>
    </n:MsgHeader>
    <s:Sequence xmlns:s="http://example.org/sequence">
      <s:SequenceNumber>5</s:SequenceNumber>
      <s:TotalInSequence>5</s:TotalInSequence>
    </s:Sequence>
  </env:Header>
  <env:Body>
    ........
  </env:Body>
</env:Envelope>
```

Format Indicator Example:
XML supports three approaches:
Version Number:
```xml
<?xml version="1.0"?>
```
Foreign Key (External DTD System Identifier):
```xml
<!DOCTYPE greeting SYSTEM "hello.dtd">
```
Format Document (Embedded DTD Markup Declaration):
```xml
<!DOCTYPE greeting [
  <!ELEMENT greeting (#PCDATA)>
]>
```

---

## Chapter 6. Interlude: Simple Messaging

**JMS Request-Reply Requestor Class (Java)**
```java
import javax.jms.Connection;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.NamingException;

public class Requestor {

    private Session session;
    private Destination replyQueue;
    private MessageProducer requestProducer;
    private MessageConsumer replyConsumer;
    private MessageProducer invalidProducer;

    protected Requestor() {
        super();
    }

    public static Requestor newRequestor(Connection connection, String requestQueueName,
        String replyQueueName, String invalidQueueName)
        throws JMSException, NamingException {

        Requestor requestor = new Requestor();
        requestor.initialize(connection, requestQueueName, replyQueueName, invalidQueueName);
        return requestor;
    }

    protected void initialize(Connection connection, String requestQueueName,
        String replyQueueName, String invalidQueueName)
        throws NamingException, JMSException {

        session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);

        Destination requestQueue = JndiUtil.getDestination(requestQueueName);
        replyQueue = JndiUtil.getDestination(replyQueueName);
        Destination invalidQueue = JndiUtil.getDestination(invalidQueueName);

        requestProducer = session.createProducer(requestQueue);
        replyConsumer = session.createConsumer(replyQueue);
        invalidProducer = session.createProducer(invalidQueue);
    }

    public void send() throws JMSException {
        TextMessage requestMessage = session.createTextMessage();
        requestMessage.setText("Hello world.");
        requestMessage.setJMSReplyTo(replyQueue);
        requestProducer.send(requestMessage);
        System.out.println("Sent request");
        System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
        System.out.println("\tMessage ID: " + requestMessage.getJMSMessageID());
        System.out.println("\tCorrel. ID: " + requestMessage.getJMSCorrelationID());
        System.out.println("\tReply to:   " + requestMessage.getJMSReplyTo());
        System.out.println("\tContents:   " + requestMessage.getText());
    }

    public void receiveSync() throws JMSException {
        Message msg = replyConsumer.receive();
        if (msg instanceof TextMessage) {
            TextMessage replyMessage = (TextMessage) msg;
            System.out.println("Received reply ");
            System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
            System.out.println("\tMessage ID: " + replyMessage.getJMSMessageID());
            System.out.println("\tCorrel. ID: " + replyMessage.getJMSCorrelationID());
            System.out.println("\tReply to:   " + replyMessage.getJMSReplyTo());
            System.out.println("\tContents:   " + replyMessage.getText());
        } else {
            System.out.println("Invalid message detected");
            System.out.println("\tType:       " + msg.getClass().getName());
            System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
            System.out.println("\tMessage ID: " + msg.getJMSMessageID());
            System.out.println("\tCorrel. ID: " + msg.getJMSCorrelationID());
            System.out.println("\tReply to:   " + msg.getJMSReplyTo());

            msg.setJMSCorrelationID(msg.getJMSMessageID());
            invalidProducer.send(msg);

            System.out.println("Sent to invalid message queue");
            System.out.println("\tType:       " + msg.getClass().getName());
            System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
            System.out.println("\tMessage ID: " + msg.getJMSMessageID());
            System.out.println("\tCorrel. ID: " + msg.getJMSCorrelationID());
            System.out.println("\tReply to:   " + msg.getJMSReplyTo());
        }
    }
}
```

**JMS Request-Reply Replier Class (Java)**
```java
import javax.jms.Connection;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageListener;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.NamingException;

public class Replier implements MessageListener {

    private Session session;
    private MessageProducer invalidProducer;

    protected Replier() {
        super();
    }

    public static Replier newReplier(Connection connection,
      String requestQueueName, String invalidQueueName)
        throws JMSException, NamingException {

        Replier replier = new Replier();
        replier.initialize(connection, requestQueueName, invalidQueueName);
        return replier;
    }

    protected void initialize(Connection connection, String requestQueueName,
    String invalidQueueName)
        throws NamingException, JMSException {

        session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination requestQueue = JndiUtil.getDestination(requestQueueName);
        Destination invalidQueue = JndiUtil.getDestination(invalidQueueName);

        MessageConsumer requestConsumer = session.createConsumer(requestQueue);
        MessageListener listener = this;
        requestConsumer.setMessageListener(listener);

        invalidProducer = session.createProducer(invalidQueue);
    }

    public void onMessage(Message message) {
        try {
            if ((message instanceof TextMessage) && (message.getJMSReplyTo() != null)) {
                TextMessage requestMessage = (TextMessage) message;
                System.out.println("Received request");
                System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
                System.out.println("\tMessage ID: " + requestMessage.getJMSMessageID());
                System.out.println("\tCorrel. ID: " + requestMessage.getJMSCorrelationID());
                System.out.println("\tReply to:   " + requestMessage.getJMSReplyTo());
                System.out.println("\tContents:   " + requestMessage.getText());

                String contents = requestMessage.getText();
                Destination replyDestination = message.getJMSReplyTo();
                MessageProducer replyProducer = session.createProducer(replyDestination);

                TextMessage replyMessage = session.createTextMessage();
                replyMessage.setText(contents);
                replyMessage.setJMSCorrelationID(requestMessage.getJMSMessageID());
                replyProducer.send(replyMessage);

                System.out.println("Sent reply");
                System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
                System.out.println("\tMessage ID: " + replyMessage.getJMSMessageID());
                System.out.println("\tCorrel. ID: " + replyMessage.getJMSCorrelationID());
                System.out.println("\tReply to:   " + replyMessage.getJMSReplyTo());
                System.out.println("\tContents:   " + replyMessage.getText());
            } else {
                System.out.println("Invalid message detected");
                System.out.println("\tType:       " + message.getClass().getName());
                System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
                System.out.println("\tMessage ID: " + message.getJMSMessageID());
                System.out.println("\tCorrel. ID: " + message.getJMSCorrelationID());
                System.out.println("\tReply to:   " + message.getJMSReplyTo());

                message.setJMSCorrelationID(message.getJMSMessageID());
                invalidProducer.send(message);

                System.out.println("Sent to invalid message queue");
                System.out.println("\tType:       " + message.getClass().getName());
                System.out.println("\tTime:       " + System.currentTimeMillis() + " ms");
                System.out.println("\tMessage ID: " + message.getJMSMessageID());
                System.out.println("\tCorrel. ID: " + message.getJMSCorrelationID());
                System.out.println("\tReply to:   " + message.getJMSReplyTo());
            }
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
}
```

**.NET Request-Reply Requestor Class (C#)**
```csharp
using System;
using System.Messaging;

public class Requestor
{
    private MessageQueue requestQueue;
    private MessageQueue replyQueue;

    public Requestor(String requestQueueName, String replyQueueName)
    {
        requestQueue = new MessageQueue(requestQueueName);
        replyQueue = new MessageQueue(replyQueueName);

        replyQueue.MessageReadPropertyFilter.SetAll();
        ((XmlMessageFormatter)replyQueue.Formatter).TargetTypeNames =
          new string[]{"System.String,mscorlib"};
    }

    public void Send()
    {
        Message requestMessage = new Message();
        requestMessage.Body = "Hello world.";
        requestMessage.ResponseQueue = replyQueue;
        requestQueue.Send(requestMessage);

        Console.WriteLine("Sent request");
        Console.WriteLine("\tTime:       {0}", DateTime.Now.ToString("HH:mm:ss.ffffff"));
        Console.WriteLine("\tMessage ID: {0}", requestMessage.Id);
        Console.WriteLine("\tCorrel. ID: {0}", requestMessage.CorrelationId);
        Console.WriteLine("\tReply to:   {0}", requestMessage.ResponseQueue.Path);
        Console.WriteLine("\tContents:   {0}", requestMessage.Body.ToString());
    }

    public void ReceiveSync()
    {
        Message replyMessage = replyQueue.Receive();

        Console.WriteLine("Received reply");
        Console.WriteLine("\tTime:       {0}", DateTime.Now.ToString("HH:mm:ss.ffffff"));
        Console.WriteLine("\tMessage ID: {0}", replyMessage.Id);
        Console.WriteLine("\tCorrel. ID: {0}", replyMessage.CorrelationId);
        Console.WriteLine("\tReply to:   {0}", "<n/a>");
        Console.WriteLine("\tContents:   {0}", replyMessage.Body.ToString());
    }
}
```

**.NET Request-Reply Replier Class (C#)**
```csharp
using System;
using System.Messaging;

class Replier {

    private MessageQueue invalidQueue;

    public Replier(String requestQueueName, String invalidQueueName)
    {
        MessageQueue requestQueue = new MessageQueue(requestQueueName);
        invalidQueue = new MessageQueue(invalidQueueName);

        requestQueue.MessageReadPropertyFilter.SetAll();
        ((XmlMessageFormatter)requestQueue.Formatter).TargetTypeNames =
          new string[]{"System.String,mscorlib"};

        requestQueue.ReceiveCompleted += new ReceiveCompletedEventHandler(OnReceiveCompleted);
        requestQueue.BeginReceive();
    }

    public void OnReceiveCompleted(Object source, ReceiveCompletedEventArgs asyncResult)
    {
        MessageQueue requestQueue = (MessageQueue)source;
        Message requestMessage = requestQueue.EndReceive(asyncResult.AsyncResult);

        try
        {
            Console.WriteLine("Received request");
            Console.WriteLine("\tTime:       {0}", DateTime.Now.ToString("HH:mm:ss.ffffff"));
            Console.WriteLine("\tMessage ID: {0}", requestMessage.Id);
            Console.WriteLine("\tCorrel. ID: {0}", "<n/a>");
            Console.WriteLine("\tReply to:   {0}", requestMessage.ResponseQueue.Path);
            Console.WriteLine("\tContents:   {0}", requestMessage.Body.ToString());

            string contents = requestMessage.Body.ToString();
            MessageQueue replyQueue = requestMessage.ResponseQueue;
            Message replyMessage = new Message();
            replyMessage.Body = contents;
            replyMessage.CorrelationId = requestMessage.Id;
            replyQueue.Send(replyMessage);

            Console.WriteLine("Sent reply");
            Console.WriteLine("\tTime:       {0}", DateTime.Now.ToString("HH:mm:ss.ffffff"));
            Console.WriteLine("\tMessage ID: {0}", replyMessage.Id);
            Console.WriteLine("\tCorrel. ID: {0}", replyMessage.CorrelationId);
            Console.WriteLine("\tReply to:   {0}", "<n/a>");
            Console.WriteLine("\tContents:   {0}", replyMessage.Body.ToString());
        }
        catch ( Exception ) {
            Console.WriteLine("Invalid message detected");
            Console.WriteLine("\tType:       {0}", requestMessage.BodyType);
            Console.WriteLine("\tTime:       {0}", DateTime.Now.ToString("HH:mm:ss.ffffff"));
            Console.WriteLine("\tMessage ID: {0}", requestMessage.Id);
            Console.WriteLine("\tCorrel. ID: {0}", "<n/a>");
            Console.WriteLine("\tReply to:   {0}", "<n/a>");

            requestMessage.CorrelationId = requestMessage.Id;

            invalidQueue.Send(requestMessage);

            Console.WriteLine("Sent to invalid message queue");
            Console.WriteLine("\tType:       {0}", requestMessage.BodyType);
            Console.WriteLine("\tTime:       {0}", DateTime.Now.ToString("HH:mm:ss.ffffff"));
            Console.WriteLine("\tMessage ID: {0}", requestMessage.Id);
            Console.WriteLine("\tCorrel. ID: {0}", requestMessage.CorrelationId);
            Console.WriteLine("\tReply to:   {0}", requestMessage.ResponseQueue.Path);
        }

        requestQueue.BeginReceive();
    }
}
```

**JMS SubjectGateway Class (Java)**
```java
import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.NamingException;

public class SubjectGateway {

    public static final String UPDATE_TOPIC_NAME = "jms/Update";
    private Connection connection;
    private Session session;
    private MessageProducer updateProducer;

    protected SubjectGateway() {
        super();
    }

    public static SubjectGateway newGateway() throws JMSException, NamingException {
        SubjectGateway gateway = new SubjectGateway();
        gateway.initialize();
        return gateway;
    }

    protected void initialize() throws JMSException, NamingException {
        ConnectionFactory connectionFactory = JndiUtil.getQueueConnectionFactory();
        connection = connectionFactory.createConnection();
        session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination updateTopic = JndiUtil.getDestination(UPDATE_TOPIC_NAME);
        updateProducer = session.createProducer(updateTopic);

        connection.start();
    }

    public void notify(String state) throws JMSException {
        TextMessage message = session.createTextMessage(state);
        updateProducer.send(message);
    }

    public void release() throws JMSException {
        if (connection != null) {
            connection.stop();
            connection.close();
        }
    }
}
```

**JMS ObserverGateway Class (Java)**
```java
import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageListener;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.NamingException;

public class ObserverGateway implements MessageListener {

    public static final String UPDATE_TOPIC_NAME = "jms/Update";
    private Observer observer;
    private Connection connection;
    private MessageConsumer updateConsumer;

    protected ObserverGateway() {
        super();
    }

    public static ObserverGateway newGateway(Observer observer)
        throws JMSException, NamingException {
        ObserverGateway gateway = new ObserverGateway();
        gateway.initialize(observer);
        return gateway;
    }

    protected void initialize(Observer observer) throws JMSException, NamingException {
        this.observer = observer;

        ConnectionFactory connectionFactory = JndiUtil.getQueueConnectionFactory();
        connection = connectionFactory.createConnection();
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination updateTopic = JndiUtil.getDestination(UPDATE_TOPIC_NAME);
        updateConsumer = session.createConsumer(updateTopic);
        updateConsumer.setMessageListener(this);
    }

    public void onMessage(Message message) {
        try {
            TextMessage textMsg = (TextMessage) message; // assume cast always works
            String newState = textMsg.getText();
            update(newState);
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }

    public void attach() throws JMSException {
        connection.start();
    }

    public void detach() throws JMSException {
        if (connection != null) {
            connection.stop();
            connection.close();
        }
    }

    private void update(String newState) throws JMSException {
        observer.update(newState);
    }
}
```

**JMS PullSubjectGateway Class (Java)**
```java
import javax.jms.Connection;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageListener;
import javax.jms.MessageProducer;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.NamingException;

public class PullSubjectGateway {

    public static final String UPDATE_TOPIC_NAME = "jms/Update";
    private PullSubject subject;
    private Connection connection;
    private Session session;
    private MessageProducer updateProducer;

    protected PullSubjectGateway() {
        super();
    }

    public static PullSubjectGateway newGateway(PullSubject subject)
        throws JMSException, NamingException {
        PullSubjectGateway gateway = new PullSubjectGateway();
        gateway.initialize(subject);
        return gateway;
    }

    protected void initialize(PullSubject subject) throws JMSException, NamingException {
        this.subject = subject;

        ConnectionFactory connectionFactory = JndiUtil.getQueueConnectionFactory();
        connection = connectionFactory.createConnection();
        session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination updateTopic = JndiUtil.getDestination(UPDATE_TOPIC_NAME);
        updateProducer = session.createProducer(updateTopic);

        new Thread(new GetStateReplier()).start();

        connection.start();
    }

    public void notifyNoState() throws JMSException {
        TextMessage message = session.createTextMessage();
        updateProducer.send(message);
    }

    public void release() throws JMSException {
        if (connection != null) {
            connection.stop();
            connection.close();
        }
    }

    private class GetStateReplier implements Runnable, MessageListener {

        public static final String GET_STATE_QUEUE_NAME = "jms/GetState";
        private Session session;
        private MessageConsumer requestConsumer;

        public void run() {
            try {
                session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
                Destination getStateQueue = JndiUtil.getDestination(GET_STATE_QUEUE_NAME);
                requestConsumer = session.createConsumer(getStateQueue);
                requestConsumer.setMessageListener(this);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        public void onMessage(Message message) {
            try {
                Destination replyQueue = message.getJMSReplyTo();
                MessageProducer replyProducer = session.createProducer(replyQueue);

                Message replyMessage = session.createTextMessage(subject.getState());
                replyProducer.send(replyMessage);
            } catch (JMSException e) {
                e.printStackTrace();
            }
        }
    }
}
```

**JMS PullObserverGateway Class (Java)**
```java
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.MessageListener;
import javax.jms.Queue;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueRequestor;
import javax.jms.QueueSession;
import javax.jms.Session;
import javax.jms.TextMessage;
import javax.naming.NamingException;

public class PullObserverGateway implements MessageListener {

    public static final String UPDATE_TOPIC_NAME = "jms/Update";
    public static final String GET_STATE_QUEUE_NAME = "jms/GetState";
    private PullObserver observer;
    private QueueConnection connection;
    private QueueSession session;
    private MessageConsumer updateConsumer;
    private QueueRequestor getStateRequestor;

    protected PullObserverGateway() {
        super();
    }

    public static PullObserverGateway newGateway(PullObserver observer)
        throws JMSException, NamingException {
        PullObserverGateway gateway = new PullObserverGateway();
        gateway.initialize(observer);
        return gateway;
    }

    protected void initialize(PullObserver observer) throws JMSException, NamingException {
        this.observer = observer;

        QueueConnectionFactory connectionFactory = JndiUtil.getQueueConnectionFactory();
        connection = connectionFactory.createQueueConnection();
        session = connection.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination updateTopic = JndiUtil.getDestination(UPDATE_TOPIC_NAME);
        updateConsumer = session.createConsumer(updateTopic);
        updateConsumer.setMessageListener(this);

        Queue getStateQueue = (Queue) JndiUtil.getDestination(GET_STATE_QUEUE_NAME);
        getStateRequestor = new QueueRequestor(session, getStateQueue);
    }

    public void onMessage(Message message) {
        try {
            // message's contents are empty
            updateNoState();
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }

    public void attach() throws JMSException {
        connection.start();
    }

    public void detach() throws JMSException {
        if (connection != null) {
            connection.stop();
            connection.close();
        }
    }

    private void updateNoState() throws JMSException {
        TextMessage getStateRequestMessage = session.createTextMessage();
        Message getStateReplyMessage = getStateRequestor.request(getStateRequestMessage);
        TextMessage textMsg = (TextMessage) getStateReplyMessage; // assume cast always works
        String newState = textMsg.getText();
        observer.update(newState);
    }
}
```

**XML Message Payload Examples**

*Address Change Message*:
```xml
<AddressChange customer_id="12345">
    <OldAddress>
        <Street>123 Wall Street</Street>
        <City>New York</City>
        <State>NY</State>
        <Zip>10005</Zip>
    </OldAddress>
    <NewAddress>
        <Street>321 Sunset Blvd</Street>
        <City>Los Angeles</City>
        <State>CA</State>
        <Zip>90012</Zip>
    </NewAddress>
</AddressChange>
```

*Out Of Product Message*:
```xml
<OutOfProduct>
    <ProductID>12345</ProductID>
    <StoreID>67890</StoreID>
    <QuantityRequested>100</QuantityRequested>
</OutOfProduct>
```

*Credit Rating Change Message*:
```xml
<CreditRatingChange customer_id="12345">
    <OldRating>AAA</OldRating>
    <NewRating>BBB</NewRating>
</CreditRatingChange>
```

*Unified Customer Change Messages*:
```xml
<CustomerChange customer_id="12345">
    <AddressChange>
        <OldAddress>
            <Street>123 Wall Street</Street>
            <City>New York</City>
            <State>NY</State>
            <Zip>10005</Zip>
        </OldAddress>
        <NewAddress>
            <Street>321 Sunset Blvd</Street>
            <City>Los Angeles</City>
            <State>CA</State>
            <Zip>90012</Zip>
        </NewAddress>
    </AddressChange>
</CustomerChange>

<CustomerChange customer_id="12345">
    <CreditRatingChange>
        <OldRating>AAA</OldRating>
        <NewRating>BBB</NewRating>
    </CreditRatingChange>
</CustomerChange>
```

---

## Chapter 7. Message Routing

CONTENT-BASED ROUTER (C# & MSMQ EXAMPLE)

class ContentBasedRouter
{
    protected MessageQueue inQueue;
    protected MessageQueue widgetQueue;
    protected MessageQueue gadgetQueue;
    protected MessageQueue dunnoQueue;

    public ContentBasedRouter(MessageQueue inQueue, MessageQueue widgetQueue,
                              MessageQueue gadgetQueue, MessageQueue dunnoQueue)
    { 
        this.inQueue = inQueue;
        this.widgetQueue = widgetQueue;
        this.gadgetQueue = gadgetQueue;
        this.dunnoQueue = dunnoQueue;

        inQueue.ReceiveCompleted += new ReceiveCompletedEventHandler(OnMessage);
        inQueue.BeginReceive();
    }

    private void OnMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new System.Messaging.XmlMessageFormatter
                           (new String[] {"System.String,mscorlib"});
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        if (IsWidgetMessage(message))
            widgetQueue.Send(message);
        else if (IsGadgetMessage(message))
            gadgetQueue.Send(message);
        else
            dunnoQueue.Send(message);
        mq.BeginReceive();
    }

    protected bool IsWidgetMessage (Message message)
    { 
        String text = (String)message.Body;
        return (text.StartsWith("W"));
    }

    protected bool IsGadgetMessage (Message message)
    { 
        String text = (String)message.Body;
        return (text.StartsWith("G"));
    }
}


TIBCO MESSAGEBROKER EXPRESSION

concat("router.out.",DGet(map,Upper(Left(OrderItem.ItemNumber,1))))


DYNAMIC ROUTER (C# & MSMQ EXAMPLE)

class DynamicRouter
{
    protected MessageQueue inQueue;
    protected MessageQueue controlQueue;
    protected MessageQueue dunnoQueue;

    protected IDictionary routingTable = (IDictionary)(new Hashtable());

    public DynamicRouter(MessageQueue inQueue, MessageQueue controlQueue,
                         MessageQueue dunnoQueue)
    { 
        this.inQueue = inQueue;
        this.controlQueue = controlQueue;
        this.dunnoQueue = dunnoQueue;

        inQueue.ReceiveCompleted += new ReceiveCompletedEventHandler(OnMessage);
        inQueue.BeginReceive();

        controlQueue.ReceiveCompleted +=
            new ReceiveCompletedEventHandler(OnControlMessage);
        controlQueue.BeginReceive();
    }

    protected void OnMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new System.Messaging.XmlMessageFormatter
                           (new String[] {"System.String,mscorlib"});
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        String key = ((String)message.Body).Substring(0, 1);

        if (routingTable.Contains(key))
        { 
            MessageQueue destination  = (MessageQueue)routingTable[key];
            destination.Send(message);
        }
        else
            dunnoQueue.Send(message);
        mq.BeginReceive();
    }

    protected void OnControlMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new System.Messaging.XmlMessageFormatter
                           (new String[] {"System.String,mscorlib"});
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        String text = ((String)message.Body);
        String [] split = (text.Split(new char[] {':'}, 2));
        if (split.Length == 2)
        { 
            String key = split[0];
            String queueName = split[1];
            MessageQueue queue = FindQueue(queueName);
            routingTable.Add(key, queue);
        }
        else
        { 
            dunnoQueue.Send(message);
        }
        mq.BeginReceive();
    }

    protected MessageQueue FindQueue(string queueName)
    { 
        if (!MessageQueue.Exists(queueName))
        { 
            return MessageQueue.Create(queueName);
        }
        else
            return new MessageQueue(queueName);
    }
}


DYNAMIC RECIPIENT LIST (C# & MSMQ EXAMPLE)

class DynamicRecipientList
{
    protected MessageQueue inQueue;
    protected MessageQueue controlQueue;

    protected IDictionary routingTable = (IDictionary)(new Hashtable());

    public DynamicRecipientList(MessageQueue inQueue, MessageQueue controlQueue)
    { 
        this.inQueue = inQueue;
        this.controlQueue = controlQueue;

        inQueue.ReceiveCompleted += new ReceiveCompletedEventHandler(OnMessage);
        inQueue.BeginReceive();

        controlQueue.ReceiveCompleted +=
            new ReceiveCompletedEventHandler(OnControlMessage);
        controlQueue.BeginReceive();
    }

    protected void OnMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new System.Messaging.XmlMessageFormatter
                           (new String[] {"System.String,mscorlib"});
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        if (((String)message.Body).Length > 0)
        { 
            char key = ((String)message.Body)[0];

            ArrayList destinations  = (ArrayList)routingTable[key];
            foreach (MessageQueue destination in destinations)
            { 
                destination.Send(message);
                Console.WriteLine("sending message " + message.Body +
                                  " to " + destination.Path);
            }
        }
        mq.BeginReceive();
    }

    protected void OnControlMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new System.Messaging.XmlMessageFormatter
                           (new String[] {"System.String,mscorlib"});
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        String text = ((String)message.Body);
        String [] split = (text.Split(new char[] {':'}, 2));
        if (split.Length == 2)
        { 
            char[] keys = split[0].ToCharArray();
            String queueName = split[1];
            MessageQueue queue = FindQueue(queueName);
            foreach (char c in keys)
            { 
                if (!routingTable.Contains(c))
                { 
                    routingTable.Add(c, new ArrayList());
                }
                ((ArrayList)(routingTable[c])).Add(queue);
                Console.WriteLine("Subscribed queue " + queueName
                                  + " for message " + c);
            }
        }
        mq.BeginReceive();
    }

    protected MessageQueue FindQueue(string queueName)
    { 
        if (!MessageQueue.Exists(queueName))
        { 
            return MessageQueue.Create(queueName);
        }
        else
            return new MessageQueue(queueName);
    }
}


XML DOCUMENT SPLITTER EXAMPLES

- Input composite message:

<order>
    <date>7/18/2002</date>
    <ordernumber>3825968</ordernumber>
    <customer>
        <id>12345</id>
        <name>Joe Doe</name>
    </customer>
    <orderitems>
        <item>
            <quantity>3.0</quantity>
            <itemno>W1234</itemno>
            <description>A Widget</description>
        </item>
        <item>
            <quantity>2.0</quantity>
            <itemno>G2345</itemno>
            <description>A Gadget</description>
        </item>
    </orderitems>
</order>

- Output split messages:

<orderitem>
    <date>7/18/2002</date>
    <ordernumber>3825968</ordernumber>
    <customerid>12345</customerid>
    <quantity>3.0</quantity>
    <itemno>W1234</itemno>
    <description>A Widget</description>
</orderitem>

<orderitem>
    <date>7/18/2002</date>
    <ordernumber>3825968</ordernumber>
    <customerid>12345</customerid>
    <quantity>2.0</quantity>
    <itemno>G2345</itemno>
    <description>A Gadget</description>
</orderitem>

- C# XMLSplitter:

class XMLSplitter
{
    protected MessageQueue inQueue;
    protected MessageQueue outQueue;

    public XMLSplitter(MessageQueue inQueue, MessageQueue outQueue)
    { 
        this.inQueue = inQueue;
        this.outQueue = outQueue;

        inQueue.ReceiveCompleted += new ReceiveCompletedEventHandler(OnMessage);
        inQueue.BeginReceive();

        outQueue.Formatter = new ActiveXMessageFormatter();
    }

    protected void OnMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new ActiveXMessageFormatter();
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        XmlDocument doc = new XmlDocument();
        doc.LoadXml((String)message.Body);

        XmlNodeList nodeList;
        XmlElement root = doc.DocumentElement;

        XmlNode date = root.SelectSingleNode("date");
        XmlNode ordernumber = root.SelectSingleNode("ordernumber");
        XmlNode id = root.SelectSingleNode("customer/id");
        XmlElement customerid = doc.CreateElement("customerid");
        customerid.InnerText = id.InnerXml;

        nodeList = root.SelectNodes("/order/orderitems/item");

        foreach (XmlNode item in nodeList)
        { 
            XmlDocument orderItemDoc = new XmlDocument();
            orderItemDoc.LoadXml("<orderitem/>");
            XmlElement orderItem = orderItemDoc.DocumentElement;

            orderItem.AppendChild(orderItemDoc.ImportNode(date, true));
            orderItem.AppendChild(orderItemDoc.ImportNode(ordernumber, true));
            orderItem.AppendChild(orderItemDoc.ImportNode(customerid, true));

            for (int i=0; i < item.ChildNodes.Count; i++)
            { 
                orderItem.AppendChild(orderItemDoc.ImportNode(item.ChildNodes[i], true));
            }

            outQueue.Send(orderItem.OuterXml);
        }

        mq.BeginReceive();
    }
}

- C# XSLSplitter:

class XSLSplitter
{
    protected MessageQueue inQueue;
    protected MessageQueue outQueue;
    protected String styleSheet = "..\\\\..\\\\Order2OrderItem.xsl";
    protected XslTransform xslt;

    public XSLSplitter(MessageQueue inQueue, MessageQueue outQueue)
    { 
        this.inQueue = inQueue;
        this.outQueue = outQueue;

        xslt = new XslTransform();
        xslt.Load(styleSheet, null); 
        outQueue.Formatter = new ActiveXMessageFormatter();

        inQueue.ReceiveCompleted += new ReceiveCompletedEventHandler(OnMessage);
        inQueue.BeginReceive();
    }

    protected void OnMessage(Object source, ReceiveCompletedEventArgs asyncResult)
    { 
        MessageQueue mq = (MessageQueue)source;
        mq.Formatter = new ActiveXMessageFormatter();
        Message message = mq.EndReceive(asyncResult.AsyncResult);

        try
        { 
            XPathDocument doc = new XPathDocument(new StringReader((String)message.Body));
            XmlReader reader = xslt.Transform(doc, null, new XmlUrlResolver());
            XmlDocument allItems = new XmlDocument();
            allItems.Load(reader);
            XmlNodeList nodeList = allItems.DocumentElement.GetElementsByTagName("orderitem");
            foreach (XmlNode orderItem in nodeList)
            { 
                outQueue.Send(orderItem.OuterXml);
            }
        }
        catch (Exception e) { Console.WriteLine(e.ToString()); }
        mq.BeginReceive();
    }
}

- XSL Stylesheet (Order2OrderItem.xsl):

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/order">
        <orderitems>
            <xsl:apply-templates select="orderitems/item"/>
        </orderitems>
    </xsl:template>
    <xsl:template match="item">
        <orderitem>
            <date>
                <xsl:value-of select="parent::node()/parent::node()/date"/>
            </date>
            <ordernumber>
                <xsl:value-of select="parent::node()/parent::node()/ordernumber"/>
            </ordernumber>
            <customerid>
                <xsl:value-of select="parent::node()/parent::node()/customer/id"/>
            </customerid>
            <xsl:apply-templates select="*"/>
        </orderitem>
    </xsl:template>
    <xsl:template match="*">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>


JMS AGGREGATOR EXAMPLE

- Aggregate Interface:

public interface Aggregate { 
    public void addMessage(Message message);
    public boolean isComplete();
    public Message getResultMessage();
}

- Domain Auction Class:

public class Auction
{ 
    ArrayList bids = new ArrayList();
    public void addBid(Bid bid)
    { 
        bids.add(bid);
        System.out.println(bids.size() + " Bids in auction.");
    }
    public boolean isComplete()
    { 
        return (bids.size() >= 3);
    }
    public Bid getBestBid()
    { 
        Bid bestBid = null;
        Iterator iter = bids.iterator();
        if (iter.hasNext())
            bestBid = (Bid) iter.next();
        while (iter.hasNext()) { 
            Bid b = (Bid) iter.next();
            if (b.getPrice() < bestBid.getPrice()) { 
                bestBid = b;
            }
        }
        return bestBid;
    }
}

- JMS Adapter AuctionAggregate Class:

public class AuctionAggregate implements Aggregate { 
    static String PROP_AUCTIONID = "AuctionID";
    static String ITEMID = "ItemID";
    static String VENDOR = "Vendor";
    static String PRICE = "Price";
    private Session session;
    private Auction auction;

    public AuctionAggregate(Session session)
    { 
        this.session = session; 
        auction = new Auction();
    }

    public void addMessage(Message message) { 
        Bid bid = null;
        if (message instanceof MapMessage) { 
            try { 
                MapMessage mapmsg = (MapMessage)message;
                String auctionID = mapmsg.getStringProperty(PROP_AUCTIONID);
                String itemID = mapmsg.getString(ITEMID);
                String vendor = mapmsg.getString(VENDOR);
                double price = mapmsg.getDouble(PRICE);
                bid = new Bid(auctionID, itemID, vendor, price);
                auction.addBid(bid);
            } catch (JMSException e) { 
                System.out.println(e.getMessage());
            }
        }
    }

    public boolean isComplete()
    { 
        return auction.isComplete();
    }

    public Message getResultMessage() { 
        Bid bid = auction.getBestBid();
        try { 
            MapMessage msg = session.createMapMessage();
            msg.setStringProperty(PROP_AUCTIONID, bid.getCorrelationID());
            msg.setString(ITEMID, bid.getItemID());
            msg.setString(VENDOR, bid.getVendorName());
            msg.setDouble(PRICE, bid.getPrice());
            return msg;
        } catch (JMSException e) { 
            System.out.println("Could not create message: " + e.getMessage());
            return null;
        }
     }
}

- JMS Aggregator MessageListener Class:

public class Aggregator implements MessageListener
{ 
    static final String PROP_CORRID = "AuctionID";
    Map activeAggregates = new HashMap();
    Destination inputDest = null;
    Destination outputDest = null;
    Session session = null;
    MessageConsumer in = null;
    MessageProducer out = null;

    public Aggregator (Destination inputDest, Destination outputDest, Session session)
    { 
        this.inputDest = inputDest;
        this.outputDest = outputDest;
        this.session = session;
    }

    public void run()
    { 
        try { 
            in = session.createConsumer(inputDest);
            out = session.createProducer(outputDest);
            in.setMessageListener(this);
        } catch (Exception e) { 
            System.out.println("Exception occurred: " + e.toString());
        }
    }

    public void onMessage(Message msg)
    { 
        try { 
            String correlationID = msg.getStringProperty(PROP_CORRID);
            Aggregate aggregate = (Aggregate)activeAggregates.get(correlationID);
            if (aggregate == null) { 
                aggregate = new AuctionAggregate(session);
                activeAggregates.put(correlationID, aggregate);
            }
            if (!aggregate.isComplete()) { 
                aggregate.addMessage(msg);
                if (aggregate.isComplete()) { 
                    MapMessage result = (MapMessage)aggregate.getResultMessage();
                    out.send(result);
                }
            }
        } catch (JMSException e) { 
            System.out.println("Exception occurred: " + e.toString());
        }
    }
}


RESEQUENCER EXAMPLE

- C# Resequencer Class:

using System;
using System.Messaging;
using System.Collections;
using MsgProcessor;

namespace Resequencer
{
    class Resequencer : Processor
    { 
        private int startIndex = 1;
        private IDictionary buffer = (IDictionary)(new Hashtable());
        private int endIndex = -1;

        public Resequencer(MessageQueue inputQueue, MessageQueue outputQueue)
                          : base (inputQueue, outputQueue) {}

        protected override void ProcessMessage(Message m)
        { 
            AddToBuffer(m);
            SendConsecutiveMessages();
        }

        private void AddToBuffer(Message m)
        { 
            Int32 msgIndex = m.AppSpecific;
            Console.WriteLine("Received message index {0}", msgIndex);
            if (msgIndex < startIndex)
            { 
                Console.WriteLine("Out of range message index! Current start is: {0}",
                                  startIndex);
            }
            else
            { 
                buffer.Add(msgIndex, m);
                if (msgIndex > endIndex)
                    endIndex = msgIndex;
            }
            Console.WriteLine("    Buffer range: {0} - {1}", startIndex, endIndex);
        }

        private void SendConsecutiveMessages()
        { 
            while (buffer.Contains(startIndex))
            { 
                Message m = (Message)(buffer[startIndex]);
                Console.WriteLine("Sending message with index {0}", startIndex);
                outputQueue.Send(m);
                buffer.Remove(startIndex);
                startIndex++;
            }
        }
    }
}

- C# Processor Base Class:

using System;
using System.Messaging;
using System.Threading;

namespace MsgProcessor
{
    public class Processor
    { 
        protected MessageQueue inputQueue;
        protected MessageQueue outputQueue;

        public Processor (MessageQueue inputQueue, MessageQueue outputQueue)
        { 
            this.inputQueue = inputQueue;
            this.outputQueue = outputQueue;
            inputQueue.Formatter = new System.Messaging.XmlMessageFormatter
                                       (new String[] {"System.String,mscorlib"});
            inputQueue.MessageReadPropertyFilter.ClearAll();
            inputQueue.MessageReadPropertyFilter.AppSpecific = true;
            inputQueue.MessageReadPropertyFilter.Body = true;
            inputQueue.MessageReadPropertyFilter.CorrelationId = true;
            inputQueue.MessageReadPropertyFilter.Id = true;
            Console.WriteLine("Processing messages from " + inputQueue.Path +
                              " to " + outputQueue.Path);
        }

        public void Process()
        { 
            inputQueue.ReceiveCompleted += new
                ReceiveCompletedEventHandler(OnReceiveCompleted);
            inputQueue.BeginReceive();
        }

        private void OnReceiveCompleted(Object source,
                                        ReceiveCompletedEventArgs asyncResult)
        { 
            MessageQueue mq = (MessageQueue)source;

            Message m = mq.EndReceive(asyncResult.AsyncResult);
            m.Formatter =  new System.Messaging.XmlMessageFormatter
                               (new String[] {"System.String,mscorlib"});

            ProcessMessage(m);

            mq.BeginReceive();
        }

        protected virtual void ProcessMessage(Message m)
        { 
            string body = (string)m.Body;
            Console.WriteLine("Received Message: " + body);
            outputQueue.Send(m);
        }
    }
}


WS-ROUTING SOAP HEADER EXAMPLE

<SOAP-ENV:Envelope
      xmlns:SOAP-ENV="http://www.w3.org/2001/06/soap-envelope">
   <SOAP-ENV:Header>
      <wsrp:path xmlns:wsrp="http://schemas.xmlsoap.org/rp/">
         <wsrp:action>http://www.im.org/chat</wsrp:action>
         <wsrp:to>soap://D.com/some/endpoint</wsrp:to>
         <wsrp:fwd>
            <wsrp:via>soap://B.com</wsrp:via>
            <wsrp:via>soap://C.com</wsrp:via>
         </wsrp:fwd>
         <wsrp:from>soap://A.com/some/endpoint</wsrp:from>
         <wsrp:id>uuid:84b9f5d0-33fb-4a81-b02b-5b760641c1d6</wsrp:id>
      </wsrp:path>
   </SOAP-ENV:Header>
   <SOAP-ENV:Body>
      ...
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

---

## Chapter 8. Message Transformation

The chapter includes several key pattern descriptions and one explicit SOAP XML envelope format example. Below are the extracted examples and detailed pattern descriptions.

**Example 1: Hierarchical SOAP Envelope Structure**
This code block from the Envelope Wrapper pattern demonstrates a nested SOAP XML format where an outer SOAP envelope wraps another SOAP envelope inside the body section. This is common when crossing trust boundaries to secure the headers from intermediaries.

```xml
<env:Envelope xmlns:env="http://www.w3.org/2001/06/soap-envelope">
    <env:Header env:actor="http://example.org/xmlsec/Bob">
        <n:forward xmlns:n="http://example.org/xmlsec/forwarding">
            <n:window>120</n:window>
        </n:forward>
    </env:Header>
    <env:Body>
        <env:Envelope xmlns:env="http://www.w3.org/2001/06/soap-envelope">
            <env:Header env:actor="http://example.org/xmlsec/Alice"/>
            <env:Body>
                <secret xmlns="http://example.org/xmlsec/message">
      The black squirrel rises at dawn</secret>
            </env:Body>
        </env:Envelope>
    </env:Body>
</env:Envelope>
```

**Example 2: Network Protocol Envelope Wrapping (Prose)**
In networking, application data is wrapped into a TCP transport envelope (adding a TCP header), which is then wrapped into an IP network envelope (adding an IP header), which is then wrapped into an Ethernet link envelope (adding an Ethernet header and trailer). This sequential nesting enables stream-oriented network transport.

**Example 3: Hospital Patient Visit Enrichment (Prose)**
A hospital scheduling system publishes a raw "Doctor Visit" message containing only patient ID, patient first name, and date. The accounting system requires patient full name, SSN, and insurance carrier to submit insurance claims. A Content Enricher resolves this by intercepting the event, querying the Customer Care database synchronously for the missing details, and merging them into the message structure before delivering it to accounting.

**Example 4: Database Adapter Content Filtering (Prose)**
A database adapter publishes a message representing a join across relational tables: ACCOUNT, CONTACT, and ACCOUNT_CONTACT. The published hierarchical structure is complex and contains technical primary and foreign keys. A Content Filter intercepts this message, extracts only five relevant business fields (account name, contact name, contact phone, contact email, contact address), and flattens the hierarchy into a simple flat structure for downstream processors.

**Example 5: Claim Check for Hiding Sensitive B2B Information (Prose)**
Before sending employee details to an external B2B partner, a Check Luggage component extracts the employee's sensitive social security number and payroll info, stores it in an internal database, and inserts a generated abstract key into the message. The external partner receives the message containing only the key and non-sensitive info. When the partner returns the processed result, a Content Enricher uses the key to retrieve the SSN from the internal store and re-enrich the message.

**Example 6: Normalizer for viewer-info Affiliate Data (Prose)**
An information aggregator receives viewer data from over 1,700 affiliates in varying formats, including CSV, Excel, XML, and EDI. A Normalizer routes these messages through datatype channels to a Message Router, which detects the format (e.g., via XPath or file naming conventions) and forwards it to a specific translator (e.g., Translator A, B, or C). All translators produce messages conforming to a single, unified canonical model schema.

---

## Chapter 9. Interlude: Composed Messaging

**1. Java Web Services - Loan Broker Operations (Apache Axis)**

The `getLoanQuote` method in `LoanBrokerWS.jws` accepts customer details and starts the processing:
```java
public String getLoanQuote(int ssn, double loanamount, int loan_duration) {
  String results = "";

  results = results + "Client with ssn= " + ssn + " requests a loan of amount= " +
                      loanamount + " for " + loan_duration + " months" + "\
\
";
  results = results + this.getLoanQuotesWithScores(ssn,loanamount,loan_duration);

  return results;
}
```

The `getLoanQuotesWithScores` method retrieves credit profile data to enrich the request and queries the clearinghouse:
```java
private String getLoanQuotesWithScores(int de_ssn, double de_loanamount, int de_duration) {
  String qws_results = "Additional data for customer: credit score and length of credit history\
";
  int ssn = de_ssn;
  double loanamount = de_loanamount;
  int loan_duration = de_duration;
  int credit_score = 0;
  int credit_history_length = 0;

  CreditProfile creditprofile = CreditAgencyGateway.getCustomerCreditProfile(ssn);

  credit_score = creditprofile.getCreditScore();
  credit_history_length = creditprofile.getCreditHistoryLength();

  qws_results = qws_results + "Credit Score= " + credit_score + " Credit History Length= " + credit_history_length;
  qws_results = qws_results + "\
\
";
  qws_results = qws_results + "The details of the best quote from all banks that responded are shown below: \
\
";

  qws_results = qws_results + getResultsFromLoanClearingHouse(ssn,loanamount,loan_duration,credit_history_length,credit_score);

  qws_results = qws_results + "\
\
";
  return qws_results;
}
```

The `getCustomerCreditProfile` method in `CreditAgencyGateway.java` performs the synchronous web service call to the credit agency:
```java
public static CreditProfile getCustomerCreditProfile(int ssn){
  int credit_score = 0;
  int credit_history_length = 0;
  CreditProfile creditprofile = null; 
  try{
    CreditAgencyGateway.readProps();
    creditprofile = new CreditProfile();
    String creditagency_ep = "http://" + hostname + ":" + portnum + "/axis/CreditAgencyWS.jws";
    Integer i1 = new Integer(ssn);
    Service  service = new Service();
    Call     call    = (Call) service.createCall();
    call.setTargetEndpointAddress( new java.net.URL(creditagency_ep) );
    call.setOperationName("getCreditHistoryLength");
    call.addParameter( "op1", XMLType.XSD_INT, ParameterMode.IN );
    call.setReturnType( XMLType.XSD_INT );
    Integer ret1 = (Integer) call.invoke( new Object [] {i1});
    credit_history_length = ret1.intValue();
    call.setOperationName("getCreditScore");
    Integer ret2 = (Integer) call.invoke( new Object [] {i1});
    credit_score = ret2.intValue();
    creditprofile.setCreditScore(credit_score);
    creditprofile.setCreditHistoryLength(credit_history_length);
    Thread.sleep(credit_score);
  }catch(Exception ex){
    System.out.println("Error accessing the CreditAgency Webservice");
  }
  return creditprofile;
}
```

The `getLenderList` method in `LenderGateway.java` implements the Recipient List pattern to choose bank endpoints based on business rules:
```java
public static ArrayList getLenderList(double loanamount, int credit_history_length, int credit_score){
  ArrayList lenders = new ArrayList();
  LenderGateway.readProps();
  if ((loanamount >= (double)75000) && (credit_score >= 600) && (credit_history_length >= 8)) {
    lenders.add(new Bank1(hostname, portnum));
    lenders.add(new Bank2(hostname, portnum));
  }
  if (((loanamount >= (double)10000) && (loanamount <= (double)74999)) && (credit_score >= 400) && (credit_history_length >= 3)) {
    lenders.add(new Bank3(hostname, portnum));
    lenders.add(new Bank4(hostname, portnum));
  }
  lenders.add(new Bank5(hostname, portnum));
  return lenders;
}
```

**2. Asynchronous MSMQ Implementation - Messaging Gateways and base structures (C#)**

The `IMessageSender` and `IMessageReceiver` interfaces abstract MSMQ messaging from the application:
```csharp
namespace MessageGateway
{
    using System.Messaging;
    public interface IMessageSender
    {
        void Send(Message mess);
    }
}

namespace MessageGateway
{
    using System.Messaging;
    public interface IMessageReceiver
    {
        OnMsgEvent OnMessage { get; get; set; }
        void Begin();
        MessageQueue GetQueue();
    }
}
```

The `SendReply` method in `MQService.cs` encapsulates correlation behavior:
```csharp\public void SendReply(Object outObj, Message inMsg)
{
    Message outMsg = new Message(outObj);
    outMsg.CorrelationId = inMsg.Id;
    outMsg.AppSpecific = inMsg.AppSpecific;

    if (inMsg.ResponseQueue != null)
    {
        IMessageSender replyQueue = new MessageSenderGateway(inMsg.ResponseQueue);
        replyQueue.Send(outMsg);
    }
    else
    {
        invalidQueue.Send(outMsg);
    }
}
```

The `ComputeBankReply` method in `Bank.cs` computes the rate based on loan term and adds a random spread:
```csharp
protected BankQuoteReply ComputeBankReply(BankQuoteRequest requestStruct)
{
    BankQuoteReply replyStruct = new BankQuoteReply();
    if (requestStruct.LoanTerm <= MaxLoanTerm)
    {
        replyStruct.InterestRate = PrimeRate + RatePremium
                                   + (double)(requestStruct.LoanTerm / 12)/10
                                   + (double)random.Next(10) / 10;
        replyStruct.ErrorCode = 0;
    }
    else
    {
        replyStruct.InterestRate = 0.0;
        replyStruct.ErrorCode = 1;
    }
    replyStruct.QuoteID = String.Format("{0}-{1:00000}", BankName, quoteCounter);
    quoteCounter++;
    return replyStruct;
}
```

The `LoanBrokerProcess` class acts as the stateful process object for each client request:
```csharp
internal class LoanBrokerProcess
{
    protected LoanBrokerPM broker;
    protected String processID;
    protected LoanQuoteRequest loanRequest;
    protected Message message;
    protected CreditBureauGateway creditBureauGateway;
    protected BankGateway bankInterface;

    public LoanBrokerProcess(LoanBrokerPM broker, String processID,
                             CreditBureauGateway creditBureauGateway,
                             BankGateway bankGateway,
                             LoanQuoteRequest loanRequest, Message msg)
    {
        this.broker = broker; 
        this.creditBureauGateway = broker.CreditBureauGateway;
        this.bankInterface = broker.BankInterface;
        this.processID = processID;
        this.loanRequest = loanRequest;
        this.message = msg;

        CreditBureauRequest creditRequest = LoanBrokerTranslator.GetCreditBureaurequest(loanRequest);
        creditBureauGateway.GetCreditScore(creditRequest, new OnCreditReplyEvent(OnCreditReply), null);
    }

    private void OnCreditReply(CreditBureauReply creditReply, Object act)
    { 
        Console.WriteLine("Received Credit Score -- SSN {0} Score {1} Length {2}",
            creditReply.SSN, creditReply.CreditScore, creditReply.HistoryLength);
        BankQuoteRequest bankRequest = LoanBrokerTranslator.GetBankQuoteRequest(loanRequest, creditReply);
        bankInterface.GetBestQuote(bankRequest, new OnBestQuoteEvent(OnBestQuote), null);
    }

    private void OnBestQuote(BankQuoteReply bestQuote, Object act)
    {
        LoanQuoteReply quoteReply = LoanBrokerTranslator.GetLoanQuoteReply(loanRequest, bestQuote);
        Console.WriteLine("Best quote {0} {1}", quoteReply.InterestRate, quoteReply.QuoteID);
        broker.SendReply(quoteReply, message);
        broker.OnProcessComplete(processID);
    }
}
```

The `LoanBrokerPM` is a Process Manager that spawns and tracks `LoanBrokerProcess` instances:
```csharp
internal class LoanBrokerPM : AsyncRequestReplyService
{
    protected CreditBureauGateway creditBureauGateway;
    protected BankGateway bankInterface;
    protected IDictionary activeProcesses = (IDictionary)(new Hashtable());

    public LoanBrokerPM(String requestQueueName,
                        String creditRequestQueueName, String creditReplyQueueName,
                        String bankReplyQueueName,
                        BankConnectionManager connectionManager): base(requestQueueName)
    {
        creditBureauGateway = new CreditBureauGateway(creditRequestQueueName, creditReplyQueueName);
        creditBureauGateway.Listen();

        bankInterface = new BankGateway(bankReplyQueueName, connectionManager);
        bankInterface.Listen();
    }

    protected override Type GetRequestBodyType()
    {
        return typeof(LoanQuoteRequest);
    }

    protected override void ProcessMessage(Object o, Message message)
    {
        LoanQuoteRequest quoteRequest = (LoanQuoteRequest)o;
        String processID = message.Id;
        LoanBrokerProcess newProcess = new LoanBrokerProcess(this, processID, creditBureauGateway, bankInterface, quoteRequest, message);
        activeProcesses.Add(processID, newProcess);
    }

    public void OnProcessComplete(String processID)
    {
        activeProcesses.Remove(processID);
    }
}
```

**3. TIBCO ActiveEnterprise - Process Definition and Mapping Scripts**

Mapping fields using ECMAScript to construct a `BankQuoteRequest`:
```javascript
var bank = new ae_class.BankQuoteRequest();
bank.CorrelationID = job.generateGUID();
bank.SSN = job.request.SSN;
bank.CreditScore = job.creditReply.CreditScore;
bank.HistoryLength = job.creditReply.HistoryLength;
bank.LoanAmount = job.request.LoanAmount;
bank.LoanTerm = job.request.LoanTerm;
job.bankRequest = bank;
```

Filtering bank responses dynamically using a Selective Consumer condition:
```javascript
(event.msg.CorrelationID == job.bankRequest.CorrelationID)
```

Aggregating the bids inside TIB/IntegrationManager once the auction times out:
```javascript
var loanReply = new ae_class.LoanQuoteReply();
loanReply.SSN = job.request.SSN;
loanReply.LoanAmount = job.request.LoanAmount;

var bids = job.bids;
for(var i = 0; i < bids.length; i++){
    var item = bids[i];
    if(i == 0 || (item.InterestRate < loanReply.InterestRate)){
        loanReply.InterestRate = item.InterestRate;
        loanReply.QuoteID = item.QuoteID;
    }
}
job.loanReply = loanReply;
```

---

## Chapter 10. Messaging Endpoints

1. Blocking vs Event-Driven Gateway Signatures in C#
Blocking Interface:
int GetCreditScore(string SSN);

Event-Driven Interface:
delegate void OnCreditReplyEvent(int CreditScore);
void RequestCreditScore(string SSN, OnCreditReplyEvent OnCreditResponse);

With Asynchronous Completion Token (ACT):
delegate void OnCreditReplyEvent(int CreditScore, Object ACT);
void RequestCreditScore(string SSN, OnCreditReplyEvent OnCreditResponse, Object ACT);

2. Asynchronous Loan Broker Gateway in MSMQ (C#)
public delegate void OnCreditReplyEvent(CreditBureauReply creditReply, Object ACT);

internal struct CreditRequestProcess
{
    public int CorrelationID;
    public Object ACT;
    public OnCreditReplyEvent callback;
}

internal class CreditBureauGateway
{
    protected IMessageSender creditRequestQueue;
    protected IMessageReceiver creditReplyQueue;
    protected IDictionary activeProcesses = (IDictionary)(new Hashtable());
    protected Random random = new Random();

    public void Listen()
    {
        creditReplyQueue.Begin();
    }

    public void GetCreditScore(CreditBureauRequest quoteRequest,
                               OnCreditReplyEvent OnCreditResponse,
                               Object ACT)
    {
        Message requestMessage = new Message(quoteRequest);
        requestMessage.ResponseQueue = creditReplyQueue.GetQueue();
        requestMessage.AppSpecific = random.Next();

        CreditRequestProcess processInstance = new CreditRequestProcess();
        processInstance.ACT = ACT;
        processInstance.callback = OnCreditResponse;
        processInstance.CorrelationID = requestMessage.AppSpecific;

        creditRequestQueue.Send(requestMessage);
        activeProcesses.Add(processInstance.CorrelationID, processInstance);
    }

    private void OnCreditResponse(Message msg)
    {
        msg.Formatter = GetFormatter();
        CreditBureauReply replyStruct;
        try
        {
            if (msg.Body is CreditBureauReply)
            { 
                replyStruct = (CreditBureauReply)msg.Body;
                int CorrelationID = msg.AppSpecific;
                if (activeProcesses.Contains(CorrelationID))
                {
                    CreditRequestProcess processInstance =
                        (CreditRequestProcess)(activeProcesses[CorrelationID]);
                    processInstance.callback(replyStruct, processInstance.ACT);
                    activeProcesses.Remove(CorrelationID);
                }
                else
                {
                    Console.WriteLine(\"Incoming credit response does not match any request\");
                }
            }
            else
            { Console.WriteLine(\"Illegal reply.\"); }
        }
        catch (Exception e)
        {
            Console.WriteLine(\"Exception: {0}\", e.ToString());
        }
    }
}

3. JMS Transacted Session (Java)
Connection connection = // Get the connection
Session session = connection.createSession(true, Session.AUTO_ACKNOWLEDGE);
Queue queue = // Get the queue
MessageConsumer consumer = session.createConsumer(queue);
Message message = consumer.receive();
session.commit();

4. .NET Transactional Queue (C#)
MessageQueue.Create(\"MyQueue\", true);
MessageQueue queue = new MessageQueue(\"MyQueue\");
MessageQueueTransaction transaction = new MessageQueueTransaction();
transaction.Begin();
Message message = queue.Receive(transaction);
transaction.Commit();

5. Transactional Filter with MSMQ (C#)
public class TransactionalFilter
{
    protected MessageQueue inputQueue;
    protected MessageQueue outputQueue;
    protected Thread receiveThread;
    protected bool stopFlag = false;

    public TransactionalFilter(MessageQueue inputQueue, MessageQueue outputQueue)
    {
        this.inputQueue = inputQueue;
        this.inputQueue.Formatter = new System.Messaging.XmlMessageFormatter
                                      (new String[] {\"System.String,mscorlib\"});
        this.outputQueue = outputQueue;
    }

    public void Process()
    {
        ThreadStart receiveDelegate = new ThreadStart(this.ReceiveMessages);
        receiveThread = new Thread(receiveDelegate);
        receiveThread.Start();
    }

    private void ReceiveMessages()
    {
        MessageQueueTransaction myTransaction = new MessageQueueTransaction();
        while (!stopFlag)
        {
            try
            {
                myTransaction.Begin();
                Message inputMessage = inputQueue.Receive(myTransaction);
                Message outputMessage = ProcessMessage(inputMessage);
                outputQueue.Send(outputMessage, myTransaction);
                myTransaction.Commit();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message + \" - Transaction aborted \");
                myTransaction.Abort();
            }
        }
    }

    protected virtual Message ProcessMessage(Message m)
    {
        Console.WriteLine(\"Received Message: \" + m.Body);
        return m;
    }
}

6. Randomly Failing Filter with MSMQ (C#)
public class RandomlyFailingFilter : TransactionalFilter
{
    Random rand = new Random();

    public RandomlyFailingFilter(MessageQueue inputQueue, MessageQueue outputQueue)
      : base(inputQueue, outputQueue) { }

    protected override Message ProcessMessage(Message m)
    {
        string text = (string)m.Body;
        Console.WriteLine(\"Received Message: \" + text);
        if (rand.Next(10) < 3)
        {
            Console.WriteLine(\"EXCEPTION\");
            throw (new ArgumentNullException());
        }
        if (text == \"end\")
            stopFlag = true;
        return(m);
    }
}

7. MSMQ Transactional Test Harness (C#)
public void RunTests()
{
    MessageQueueTransaction myTransaction = new MessageQueueTransaction();
    for (int i=0; i < messages.Length; i++)
    {
        myTransaction.Begin();
        inQueue.Send(messages[i], myTransaction);
        myTransaction.Commit();
    }
    for (int i=0; i < messages.Length; i++)
    {
        myTransaction.Begin();
        Message message = outQueue.Receive(new TimeSpan(0,0,3), myTransaction);
        myTransaction.Commit();
        String text = (String)message.Body;
        Console.Write(text);
        if (text == messages[i])
            Console.WriteLine(\" OK\");
        else
            Console.WriteLine(\" ERROR\");
    }
    Console.WriteLine(\"Hit enter to exit\");
    Console.ReadLine();
}

8. JMS Polling Consumer Receive (Java)
Destination dest = // Get the destination
Session session = // Create the session
MessageConsumer consumer = session.createConsumer(dest);
Message message = consumer.receive();

9. .NET Polling Consumer Receive (C#)
MessageQueue queue = // Get the queue
Message message = queue.Receive();

10. JMS Event-Driven Consumer (Java)
public class MyEventDrivenConsumer implements MessageListener {
    public void onMessage(Message message) {
        // Process the message
    }
}
// Initialization:
Destination destination = // Get the destination
Session session = // Create the session
MessageConsumer consumer = session.createConsumer(destination);
MessageListener listener = new MyEventDrivenConsumer();
consumer.setMessageListener(listener);

11. .NET Event-Driven Consumer (C#)
public static void MyEventDrivenConsumer(Object source,
    ReceiveCompletedEventArgs asyncResult)
{
    MessageQueue mq = (MessageQueue) source;
    Message m = mq.EndReceive(asyncResult.AsyncResult);
    // Process the message
    mq.BeginReceive();
    return;
}
// Initialization:
MessageQueue queue = // Get the queue
queue.ReceiveCompleted +=
    new ReceiveCompletedEventHandler(MyEventDrivenConsumer);
queue.BeginReceive();

12. JMS Competing Consumer (Java)
import javax.jms.Connection;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.Session;
import javax.naming.NamingException;

public class CompetingConsumer implements Runnable {
    private int performerID;
    private MessageConsumer consumer;
    private boolean isRunning;

    protected CompetingConsumer() {
        super();
    }

    public static CompetingConsumer newConsumer(int id,
                                                Connection connection,
                                                String queueName)
        throws JMSException, NamingException {
        CompetingConsumer consumer = new CompetingConsumer();
        consumer.initialize(id, connection, queueName);
        return consumer;
    }

    protected void initialize(int id, Connection connection,
                             String queueName)
        throws JMSException, NamingException {
        performerID = id;
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination dispatcherQueue = JndiUtil.getDestination(queueName);
        consumer = session.createConsumer(dispatcherQueue);
        isRunning = true;
    }

    public void run() {
        try {
            while (isRunning())
                receiveSync();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private synchronized boolean isRunning() {
        return isRunning;
    }

    public synchronized void stopRunning() {
        isRunning = false;
    }

    private void receiveSync() throws JMSException,
                             InterruptedException {
        Message message = consumer.receive();
        if (message != null)
            processMessage(message);
    }

    private void processMessage(Message message)
      throws JMSException, InterruptedException {
        int id = message.getIntProperty(\"cust_id\");
        System.out.println(System.currentTimeMillis() + \": Performer #\"
          + performerID + \" starting; message ID \" + id);
        Thread.sleep(500);
        System.out.println(System.currentTimeMillis() + \": Performer #\"
          + performerID + \" processing.\");
        Thread.sleep(500);
        System.out.println(System.currentTimeMillis() + \": Performer #\"
          + performerID + \" finished.\");
    }
}

13. Java Message Dispatcher and Performer
import javax.jms.Connection;
import javax.jms.Destination;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageConsumer;
import javax.jms.Session;
import javax.naming.NamingException;

public class MessageDispatcher {
    MessageConsumer consumer;
    int nextID = 1;

    protected MessageDispatcher() {
        super();
    }

    public static MessageDispatcher newDispatcher(Connection connection,
                                                 String queueName)
        throws JMSException, NamingException {
        MessageDispatcher dispatcher = new MessageDispatcher();
        dispatcher.initialize(connection, queueName);
        return dispatcher;
    }

    protected void initialize(Connection connection, String queueName)
        throws JMSException, NamingException {
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Destination dispatcherQueue = JndiUtil.getDestination(queueName);
        consumer = session.createConsumer(dispatcherQueue);
    }

    public void receiveSync() throws JMSException {
        Message message = consumer.receive();
        Performer performer = new Performer(nextID++, message);
        new Thread(performer).start();
    }
}

import javax.jms.JMSException;
import javax.jms.Message;

public class Performer implements Runnable {
    private int performerID;
    private Message message;

    public Performer(int id, Message message) {
        performerID = id;
        this.message = message;
    }

    public void run() {
        try {
            processMessage();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void processMessage() throws JMSException,
                                 InterruptedException {
        int id = message.getIntProperty(\"cust_id\");
        System.out.println(System.currentTimeMillis() + \": Performer #\"
          + performerID + \" starting; message ID \" + id);
        Thread.sleep(500);
        System.out.println(System.currentTimeMillis() + \": Performer #\"
          + performerID + \" processing.\");
        Thread.sleep(500);
        System.out.println(System.currentTimeMillis() + \": Performer #\"
          + performerID + \" finished.\");
    }
}

14. JMS Message Selector (Java)
// Sender:
Session session = // get the session
TextMessage message = session.createTextMessage();
message.setText(\"<quote>SUNW</quote>\");
message.setStringProperty(\"req_type\", \"quote\");
Destination destination = //get the destination
MessageProducer producer = session.createProducer(destination);
producer.send(message);

// Receiver:
Session session = // get the session
Destination destination = //get the destination
String selector = \"req_type = 'quote'\";
MessageConsumer consumer = session.createConsumer(destination, selector);

15. JMS Durable Subscription (Java)
ConnectionFactory factory = // obtain the factory
Connection connection = factory.createConnection();
Topic topic = // obtain the topic
String clientID = connection.getClientID();
String subscriptionName = \"subscriber1\";

Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
TopicSubscriber subscriber = session.createDurableSubscriber(topic, subscriptionName);

// To make it inactive:
subscriber.close();

// To completely remove the subscription:
subscriber.close();
session.unsubscribe(subscriptionName);

16. MIDL Idempotent Attribute (IDL)
interface IFoo;
[
    uuid(5767B67C-3F02-40ba-8B85-D8516F20A83B),
    pointer_default(unique)
]
interface IFoo
{
    [idempotent]
    bool GetCustomerName
    (
        [in] int CustomerID,
        [out] char *Name
    );
}

---

## Chapter 11. System Management

**MSMQ and C# Smart Proxy Example**

```csharp
// 1. MessageConsumer Base Class
// Helper class to encapsulate event-driven MSMQ consumption
public class MessageConsumer
{
    protected MessageQueue inputQueue;

    public MessageConsumer (MessageQueue inputQueue)
    {
        this.inputQueue = inputQueue;
        SetupQueue(this.inputQueue);
        Console.WriteLine(this.GetType().Name + ": Processing messages from " + inputQueue.Path);
    }

    protected void SetupQueue(MessageQueue queue)
    {
        queue.Formatter = new System.Messaging.XmlMessageFormatter
                              (new String[] {"System.String,mscorlib"});
        queue.MessageReadPropertyFilter.ClearAll();
        queue.MessageReadPropertyFilter.AppSpecific = true;
        queue.MessageReadPropertyFilter.Body = true;
        queue.MessageReadPropertyFilter.CorrelationId = true;
        queue.MessageReadPropertyFilter.Id = true;
        queue.MessageReadPropertyFilter.ResponseQueue = true;
    }

    public virtual void Process()
    {
        inputQueue.ReceiveCompleted +=
            new ReceiveCompletedEventHandler(OnReceiveCompleted);
        inputQueue.BeginReceive();
    }

    private void OnReceiveCompleted(Object source,
        ReceiveCompletedEventArgs asyncResult)
    {
        MessageQueue mq = (MessageQueue)source;
        Message m = mq.EndReceive(asyncResult.AsyncResult);
        m.Formatter =  new System.Messaging.XmlMessageFormatter
                           (new String[] {"System.String,mscorlib"});
        ProcessMessage(m);
        mq.BeginReceive();
    }

    protected virtual void ProcessMessage(Message m)
    {
        String text = "";
        try
        { 
            text = (String)m.Body;
        }
        catch (InvalidOperationException) {};
        Console.WriteLine(this.GetType().Name + ": Received Message " + text);
    }
}

// 2. SmartProxyBase Class
// Manages the request and reply consumers and sharing of state
public class SmartProxyBase
{
    protected SmartProxyRequestConsumer requestConsumer;
    protected SmartProxyReplyConsumer replyConsumer;
    protected Hashtable messageData;

    public SmartProxyBase(MessageQueue inputQueue,
                          MessageQueue serviceRequestQueue,
                          MessageQueue serviceReplyQueue)
    {
        messageData = Hashtable.Synchronized(new Hashtable());
        requestConsumer = new SmartProxyRequestConsumer
                              (inputQueue, serviceRequestQueue,
                               serviceReplyQueue, messageData);
        replyConsumer = new SmartProxyReplyConsumer
                            (serviceReplyQueue, messageData);
    }

    public virtual void Process()
    {
        requestConsumer.Process();
        replyConsumer.Process();
    }
}

// 3. SmartProxyRequestConsumer Class
// Intercepts requests, stores return address info, and forwards them
public class SmartProxyRequestConsumer : MessageConsumer
{
    protected Hashtable messageData;
    protected MessageQueue serviceRequestQueue;
    protected MessageQueue serviceReplyQueue;

    public SmartProxyRequestConsumer(MessageQueue requestQueue,
                                     MessageQueue serviceRequestQueue,
                                     MessageQueue serviceReplyQueue,
                                     Hashtable messageData) : base(requestQueue)
    {
        this.messageData = messageData;
        this.serviceRequestQueue = serviceRequestQueue;
        this.serviceReplyQueue = serviceReplyQueue;
    }

    protected override void ProcessMessage(Message requestMsg)
    { 
        base.ProcessMessage(requestMsg);
        MessageData data = new MessageData(requestMsg.Id,
                                           requestMsg.ResponseQueue,
                                           requestMsg.AppSpecific);
        requestMsg.ResponseQueue = serviceReplyQueue;
        serviceRequestQueue.Send(requestMsg);
        messageData.Add(requestMsg.Id, data);
        AnalyzeMessage(requestMsg);
    }

    protected virtual void AnalyzeMessage(Message requestMsg)
    {
    }
}

// 4. SmartProxyReplyConsumer Class
// Listens on the service reply queue and restores the original Return Address
public class SmartProxyReplyConsumer : MessageConsumer
{
    protected Hashtable messageData;

    public SmartProxyReplyConsumer(MessageQueue replyQueue,
                                   Hashtable messageData) : base(replyQueue)
    {
        this.messageData = messageData;
    }

    protected override void ProcessMessage(Message replyMsg)
    { 
        base.ProcessMessage(replyMsg);
        String corr = replyMsg.CorrelationId;
        if (messageData.Contains(corr))
        { 
            MessageData data = (MessageData)(messageData[corr]);
            AnalyzeMessage(data, replyMsg);
            replyMsg.CorrelationId = data.CorrelationID;
            replyMsg.AppSpecific = data.AppSpecific;
            MessageQueue outputQueue = data.ReturnAddress;
            outputQueue.Send(replyMsg);
            messageData.Remove(corr);
        }
        else
        { 
            Console.WriteLine(this.GetType().Name + "Unrecognized Reply Message");
        }
    }

    protected virtual void AnalyzeMessage(MessageData data,
        Message replyMessage)
    {
    }
}

// 5. MetricsSmartProxy Class
// Extends SmartProxyBase to collect performance metrics
public class MetricsSmartProxy : SmartProxyBase
{
    public MetricsSmartProxy(MessageQueue inputQueue,
                             MessageQueue serviceRequestQueue,
                             MessageQueue serviceReplyQueue,
                             MessageQueue controlBus) :
                        base (inputQueue, serviceRequestQueue, serviceReplyQueue)
    { 
        replyConsumer = new SmartProxyReplyConsumerMetrics
                            (serviceReplyQueue, messageData, controlBus);
    }
}

// 6. SmartProxyReplyConsumerMetrics Class
// Calculates processing time and sends statistics to the Control Bus
public class SmartProxyReplyConsumerMetrics : SmartProxyReplyConsumer
{
    MessageQueue controlBus;

    public SmartProxyReplyConsumerMetrics(MessageQueue replyQueue,
                                          Hashtable messageData,
                                          MessageQueue controlBus) :
                                     base(replyQueue, messageData)
    { 
        this.controlBus = controlBus;
    }

    protected override void AnalyzeMessage(MessageData data,
        Message replyMessage)
    {
        TimeSpan duration = DateTime.Now - data.SentTime;
        Console.WriteLine(" processing time: {0:f}", duration.TotalSeconds);
        if (controlBus != null)
        { 
            controlBus.Send(duration.TotalSeconds.ToString() + "," + messageData.Count);
        }
    }
}
```

*Note on dependencies:* The `MessageData` class is a helper class storing Request ID, Return Address, AppSpecific state, and SentTime, which is utilized by the proxy but omitted from the original text's definitions. This C# code assumes usage of the `System.Messaging` namespace for MSMQ queues.

**Java and JMS Channel Purger Example**

```java
import javax.jms.JMSException;
import javax.jms.MessageConsumer;
import javax.jms.Queue;

public class ChannelPurger extends JmsEndpoint
{
    public static void main(String[] args)
    {
        if (args.length != 1) {
            System.out.println("Usage: java ChannelPurger <queue_name>");
            System.exit(1);
        }
        String queueName = new String(args[0]);
        System.out.println("Purging queue " + queueName);
        ChannelPurger purger = new ChannelPurger();
        purger.purgeQueue(queueName);
    }

    private void purgeQueue(String queueName)
    {
        try {
            initialize();
            connection.start();
            Queue queue = (Queue) JndiUtil.getDestination(queueName);
            MessageConsumer consumer = session.createConsumer(queue);
            while (consumer.receiveNoWait() != null)
                System.out.print(".");
            connection.stop();
        } catch (Exception e) {
            System.out.println("Exception occurred: " + e.toString());
        } finally {
            if (connection != null) {
                try {
                    connection.close();
                } catch (JMSException e) {
                    // ignore
                }
            }
        }
    }
}
```

*Note on dependencies:* The Java JMS example inherits from `JmsEndpoint` and references `JndiUtil` helper methods to run, which are external to the code shown in this chapter.

---

## Chapter 12. Interlude: System Management Example

**Example 1: LoanBrokerProxy Class**

```csharp
public class LoanBrokerProxy : SmartProxyBase
{
    protected MessageQueue controlBus;

    protected ArrayList performanceStats;
    protected ArrayList queueStats;

    protected int interval;
    protected Timer timer;

    public LoanBrokerProxy(MessageQueue inputQueue, MessageQueue serviceRequestQueue,
                           MessageQueue serviceReplyQueue, MessageQueue controlBus,
                           int interval) :
        base (inputQueue, serviceRequestQueue, serviceReplyQueue)
    {
        messageData = Hashtable.Synchronized(new Hashtable());
        queueStats = ArrayList.Synchronized(new ArrayList());
        performanceStats = ArrayList.Synchronized(new ArrayList());

        this.controlBus = controlBus;
        this.interval = interval;

        requestConsumer = new LoanBrokerProxyRequestConsumer(inputQueue,
            serviceRequestQueue, serviceReplyQueue, messageData, queueStats);
        replyConsumer = new LoanBrokerProxyReplyConsumer(serviceReplyQueue,
            messageData, queueStats, performanceStats);
    }

    public override void Process()
    {
        base.Process();

        TimerCallback timerDelegate = new TimerCallback(OnTimerEvent);
        timer = new Timer(timerDelegate, null, interval*1000, interval*1000);
    }

    protected void OnTimerEvent(Object state)
    {
        ArrayList currentQueueStats;
        ArrayList currentPerformanceStats;

        lock (queueStats)
        {
            currentQueueStats = (ArrayList)(queueStats.Clone());
            queueStats.Clear();
        }

        lock (performanceStats)
        {
            currentPerformanceStats = (ArrayList)(performanceStats.Clone());
            performanceStats.Clear();
        }

        SummaryStats summary = new SummaryStats(currentQueueStats,
                                                currentPerformanceStats);
        if (controlBus != null)
            controlBus.Send(summary);
    }
}
```

**Example 2: LoanBrokerProxyRequestConsumer Class**

```csharp
public class LoanBrokerProxyRequestConsumer : SmartProxyRequestConsumer
{
    ArrayList queueStats;

    public LoanBrokerProxyRequestConsumer(MessageQueue requestQueue,
                                          MessageQueue serviceRequestQueue,
                                          MessageQueue serviceReplyQueue,
                                          Hashtable messageData,
                                          ArrayList queueStats) :
        base(requestQueue, serviceRequestQueue, serviceReplyQueue, messageData)
    {
        this.queueStats = queueStats;
    }

    protected override void ProcessMessage(Message requestMsg)
    {
        base.ProcessMessage(requestMsg);
        queueStats.Add(messageData.Count);
    }
}
```

**Example 3: LoanBrokerProxyReplyConsumer Class**

```csharp
public class LoanBrokerProxyReplyConsumer : SmartProxyReplyConsumer
{
    ArrayList queueStats;
    ArrayList performanceStats;

    public LoanBrokerProxyReplyConsumer(MessageQueue replyQueue,
                                        Hashtable messageData,
                                        ArrayList queueStats,
                                        ArrayList performanceStats) :
           base(replyQueue, messageData)
    {
        this.queueStats = queueStats;
        this.performanceStats = performanceStats;
    }

    protected override void AnalyzeMessage(MessageData data, Message replyMessage)
    {
        TimeSpan duration = DateTime.Now - data.SentTime;
        performanceStats.Add(duration.TotalSeconds);

        queueStats.Add(messageData.Count);
    }
}
```

**Example 4: Monitor Class - Sending Messages**

```csharp
public override void Process()
{
    base.Process();
    sendTimer = new Timer(new TimerCallback
                         (OnSendTimerEvent), null, interval*1000, Timeout.Infinite);

    MonitorStatus status = new MonitorStatus(
                 MonitorStatus.STATUS_ANNOUNCE, "Monitor On-Line", null, MonitorID);
    Console.WriteLine(status.Description);
    controlQueue.Send(status);
    lastStatus = status.Status;
}

protected void OnSendTimerEvent(Object state)
{
    CreditBureauRequest request = new CreditBureauRequest();
    request.SSN = SSN;

    Message requestMessage = new Message(request);
    requestMessage.Priority = MessagePriority.AboveNormal;
    requestMessage.ResponseQueue = inputQueue;

    Console.WriteLine(DateTime.Now.ToString() + " Sending request message");
    requestQueue.Send(requestMessage);

    correlationID = requestMessage.Id;

    timeoutTimer = new Timer(new TimerCallback(OnTimeoutEvent), null,
                             timeout*1000, Timeout.Infinite);
}
```

**Example 5: Monitor Class - Receiving Messages**

```csharp
protected override void ProcessMessage(Message msg)
{
    Console.WriteLine(DateTime.Now.ToString() + " Received reply message");

    if (timeoutTimer != null)
        timeoutTimer.Dispose();

    msg.Formatter = new XmlMessageFormatter(new Type[] {typeof(CreditBureauReply)});
    CreditBureauReply replyStruct;
    MonitorStatus status = new MonitorStatus();

    status.Status = MonitorStatus.STATUS_OK;
    status.Description = "No Error";
    status.ID = MonitorID;

    try
    {
        if (msg.Body is CreditBureauReply)
        {
            replyStruct = (CreditBureauReply)msg.Body;
            if (msg.CorrelationId != correlationID)
            {
                status.Status = MonitorStatus.STATUS_FAILED_CORRELATION;
                status.Description =
                    "Incoming message correlation ID does not match outgoing message ID";
            }
            else
            {
                if (replyStruct.CreditScore < 300 || replyStruct.CreditScore > 900 ||
                    replyStruct.HistoryLength < 1 || replyStruct.HistoryLength > 24)
                {
                    status.Status = MonitorStatus.STATUS_INVALID_DATA;
                    status.Description = "Credit score values out of range";
                }
            }

        }
        else
        {
            status.Status = MonitorStatus.STATUS_INVALID_FORMAT;
            status.Description = "Invalid message format";        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception: {0}", e.ToString());
        status.Status = MonitorStatus.STATUS_INVALID_FORMAT;
        status.Description = "Could not deserialize message body";
    }

    StreamReader reader = new StreamReader (msg.BodyStream);
    status.MessageBody =  reader.ReadToEnd();

    Console.WriteLine(status.Description);

    if (status.Status != MonitorStatus.STATUS_OK ||
        (status.Status == MonitorStatus.STATUS_OK &&
         lastStatus != MonitorStatus.STATUS_OK))
    {
        controlQueue.Send(status);
    }

    lastStatus = status.Status;
    sendTimer.Dispose();
    sendTimer = new Timer(new TimerCallback(OnSendTimerEvent), null,
                          interval*1000, Timeout.Infinite);
}
```

**Example 6: Monitor Class - Timeout**

```csharp
protected void OnTimeoutEvent(Object state)
{
    MonitorStatus status = new MonitorStatus(
                           MonitorStatus.STATUS_TIMEOUT, "Timeout", null, MonitorID);
    Console.WriteLine(status.Description);
    controlQueue.Send(status);
    lastStatus = status.Status;

    timeoutTimer.Dispose();
    sendTimer = new Timer(new TimerCallback(OnSendTimerEvent), null,
                          interval*1000, Timeout.Infinite);
}
```

**Example 7: ContextBasedRouter Class**

```csharp
delegate void ControlEvent(int control);

class ContextBasedRouter : MessageConsumer
{
    protected override void ProcessMessage(Message msg)
    {
        if (control == 0)
        {
            primaryOutputQueue.Send(msg);
        }
        else
        {
            secondaryOutputQueue.Send(msg);
        }
    }

    protected void OnControlEvent(int control)
    {
        this.control = control;
        Console.WriteLine("Control = " + control);
    }
}
```

**Example 8: ControlReceiver Class**

```csharp
class ControlReceiver : MessageConsumer
{
    protected ControlEvent controlEvent;

    public ControlReceiver(MessageQueue inputQueue,
                           ControlEvent controlEvent) : base (inputQueue)
    {
        this.controlEvent = controlEvent;
    }

    protected override void ProcessMessage(Message msg)
    {
        String text = (string)msg.Body;
        Double resNum;

        if (Double.TryParse(text, NumberStyles.Integer,
                            NumberFormatInfo.InvariantInfo, out resNum))
        {
            int control = int.Parse(text);
            controlEvent(control);
        }
    }
}
```

**Example 9: ManagementConsole - ProcessMessage**

```csharp
public delegate void ControlMessageReceived(String body);

public class ManagementConsole : MessageConsumer
{
    protected Logger logger;
    public MonitorStatusHandler monitorStatusHandler;

    public ControlMessageReceived updateEvent;

    public ManagementConsole(MessageQueue inputQueue, string pathName) : base(inputQueue)
    {
        logger = new Logger(pathName);
        monitorStatusHandler = new MonitorStatusHandler();

        updateEvent += new ControlMessageReceived(logger.Log);
        updateEvent += new ControlMessageReceived(monitorStatusHandler.OnControlMessage);
    }

    protected override void ProcessMessage(Message m)
    {
        Stream stm = m.BodyStream;
        StreamReader reader = new StreamReader (stm);
        String body =  reader.ReadToEnd();

        updateEvent(body);
    }
}
```

**Example 10: MonitorStatusHandler Class**

```csharp
public delegate void MonitorStatusUpdate(String ID, int Status);

public class MonitorStatusHandler
{
    public  MonitorStatusUpdate updateEvent;

    public void OnControlMessage(String body)
    {
        XmlDocument doc = new XmlDocument();
        doc.LoadXml(body);

        XmlElement root = doc.DocumentElement;
        if (root.Name == "MonitorStatus")
        {
            XmlNode statusNode = root.SelectSingleNode("Status");
            XmlNode idNode = root.SelectSingleNode("ID");

            if (idNode!= null && statusNode != null)
            {
                String msgID = idNode.InnerText;
                String msgStatus = statusNode.InnerText;
                Double resNum;
                int status = 99;

                if (Double.TryParse(msgStatus, NumberStyles.Integer,
                                    NumberFormatInfo.InvariantInfo, out resNum))
                {
                    status = (int)resNum;
                }
                updateEvent(msgID, status);
            }
        }
    }
}
```

**Example 11: Console Form Initialization (Component Status Controls)**

```csharp
console = new ManagementConsole(controlBusQueue, logFileName);

primaryCreditBureauControl =
    new ComponentStatusControl("Primary Credit Bureau", "PrimaryCreditService");
primaryCreditBureauControl.Bounds =
    new Rectangle(300, 30, COMPONENT_WIDTH, COMPONENT_HEIGHT);

secondaryCreditBureauControl =
    new ComponentStatusControl("Secondary Credit Bureau", "SecondaryCreditService");
secondaryCreditBureauControl.Bounds =
    new Rectangle(300, 130, COMPONENT_WIDTH, COMPONENT_HEIGHT);

console.monitorStatusHandler.updateEvent += new
     MonitorStatusUpdate(primaryCreditBureauControl.OnMonitorStatusUpdate);
console.monitorStatusHandler.updateEvent += new
     MonitorStatusUpdate(secondaryCreditBureauControl.OnMonitorStatusUpdate);
```

**Example 12: FailOverHandler Class**

```csharp
public delegate void FailOverStatusUpdate(String ID, string Command);

public class FailOverHandler
{
    public void OnMonitorStatusUpdate(String ID, int status)
    {
        if (componentID == ID)
        {
            if (IsOK(status) ^ IsOK(currentStatus))
            {
                String command = IsOK(status) ? "0" : "1";
                commandQueue.Send(command);
                currentStatus = status;
                updateEvent(ID, command);
            }
        }
    }

    protected bool IsOK(int status)
    {
        return (status == 0 || status >= 99);
    }
}
```

**Example 13: Console Form Initialization (FailOver Controls)**

```csharp
failOverControl = new FailOverControl("Credit Bureau Failover", "PrimaryCreditService");
failOverControl.Bounds = new Rectangle(100, 80, ROUTER_WIDTH, COMPONENT_HEIGHT);

FailOverHandler failOverHandler =
     new FailOverHandler(commandQueue, "PrimaryCreditService");
console.monitorStatusHandler.updateEvent +=
     new MonitorStatusUpdate(failOverHandler.OnMonitorStatusUpdate);

failOverHandler.updateEvent += new
    FailOverStatusUpdate(failOverControl.OnMonitorStatusUpdate);
```"

---

## Chapter 13. Integration Patterns in Practice

There are no code snippets provided in this chapter. However, the chapter provides detailed architectural pattern descriptions and data flows in prose. These implementations are documented below:

1. The Message Dispatcher Implementation Details:
- Class structure: A single message listener class called Dispatcher implementing the JMS MessageListener interface.
- The Dispatcher class maintains a collection of helper MessageListener objects referred to as Performers.
- Threading model: The Dispatcher's onMessage(Message message) method is invoked by the JMS provider. Instead of executing the business logic in the listener thread, it retrieves a free Performer from its pool, schedules or passes the message to it, and immediately returns. This keeps the provider's delivery thread free and prevents queue backups.

2. The Messaging Bridge using Channel Adapters:
- Integration of legacy C++ TIBCO and Java MQSeries JMS.
- A C++ Channel Adapter is created that communicates natively with TIBCO.
- A Java Channel Adapter is created that communicates natively with JMS.
- These two adapters act as Message Endpoints and communicate with each other via CORBA to bridge the two messaging architectures.

3. Pricing Gateway as a Content-Based Router:
- Translates fine-grained bond channels on the TIBCO side into coarse-grained, trader-specific topics on the JMS side.
- Pricing Gateway subscribes to the C++ Channel Adapter's output for all bonds corresponding to active traders, receives updates, and routes them to the appropriate JMS topic.

---

## Chapter 14. Concluding Remarks

There is only one code snippet in this chapter, which demonstrates a coordination context header for SOAP transactions using WS-Transaction:

```xml
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2001/12/soap-envelope">

  <SOAP-ENV:Header>

    <wscoor:CoordinationContext
            xmlns:wscoor="http://schemas.xmlsoap.org/ws/2002/08/wscoor"
            xmlns:wsu="http://schemas.xmlsoap.org/ws/2002/07/utility"
            xmlns:myTransactableApp="http://foo.com/baz">

      <wsu:Identifier>http://foo.com/baz/bar</wsu:Identifier>
      <wsu:Expires>2004-12-31T18:00:00-08:00</wsu:Expires>

      <wscoor:CoordinationType>
        http://schemas.xmlsoap.org/ws/2002/08/wstx
      </wscoor:CoordinationType>

      <wscoor:RegistrationService>
        <wsu:Address>
          http://foo.com/coordinationservice/registration
        </wsu:Address>
      </wscoor:RegistrationService>

      <myTransactableApp:IsolationLevel>
        RepeatableRead
      </myTransactableApp:IsolationLevel>

    </wscoor:CoordinationContext>

  </SOAP-ENV:Header>

  <!-- SOAP BODY (snipped) -->

</SOAP-ENV:Envelope>
```

---

## Bibliography

There are no code examples or code snippets in this bibliography chapter.

---

