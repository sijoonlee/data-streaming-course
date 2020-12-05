## Data Storage
Table operations are stateful, meaning we must store the intermediate results of combining multiple events to represent the latest point-in-time value for a given key. Therefore, table operations require some form of storage. Options range from using in-memory storage, to dedicated databases such as RocksDB. In this section, we’ll review the options that are available.

- All stream processing frameworks require a changelog
- Kafka changelog topic tracks all changes in stream
- Changelog topics are log compacted
- Changelog topic aids in failure tolerance and recovery

## RocksDB
- in-memory storage is default for local state
- in-memory storage is not appropriate for Production
- Always use RocksDB as your local state store
- Always use RocksDB in Production
- RocksDB dramatically speeds reboot/recovery times
- RocksDB is used by all major streaming frameworks


## Further Optional Reading - Data Storage
[RocksDB](https://rocksdb.org/)
[Kafka Streams State](https://docs.confluent.io/current/streams/architecture.html?&_ga=2.265603023.1364268795.1565759077-2091975159.1565759077#state)