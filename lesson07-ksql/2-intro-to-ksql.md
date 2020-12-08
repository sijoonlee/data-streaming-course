## Stream Processing with KSQL
- In this lesson we’ll review how we can use KSQL to build stream processing applications simply by writing SQL-like statements! In contrast to Faust, we’re not actually going to build an application using a programming language like Python. Instead, KSQL will transform our SQL commands into running stream processing applications for us!

- Throughout this lesson, you’ll see how KSQL can express all the familiar concepts of stream processing applications with the exclusive use of SQL syntax.

## Intro to KSQL
- KSQL provides a SQL-like interface to transform Kafka Topics into streams and tables.

- Joins, aggregates, filtering, and other forms of data manipulation can then be expressed over these streams and tables.

## KSQL Architecture
- KSQL is a Java application built on top of the Kafka Streams Java stream processing library. KSQL is a web-server with a REST API that accepts incoming or preconfigured requests containing SQL-like commands. These commands are translated by the KSQL server into the equivalent Kafka Streams application and then executed.

- Users can interact with KSQL via a REST API, its dedicated CLI, or predefined SQL files.

## KSQL vs. Traditional Frameworks
- Pros
    - It is often simpler to use KSQL and SQL than to build and deploy an entire application
    - KSQL is typically a better fit for rapid experimentation and exploration than a full stream processing application
    - KSQL doesn’t require a particular programming language, like Python for Faust, or Java for Kafka Streams
    - KSQL already comes bundled with standard logs, metrics, and tooling for you to use, so you don’t have to build it yourself
- Cons
    - SQL does not always best capture certain types of data manipulation or remapping scenarios
    - Can’t just use whatever other libraries you want like you can with Faust
    - However, KSQL does allow User Defined Functions (UDFs), written in Java