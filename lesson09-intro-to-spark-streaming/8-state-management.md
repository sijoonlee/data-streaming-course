## Spark < 2.2.0

- The state management was inefficient
- The state was persisted along with the checkpoint metadata(offset or progress of streaming)
- The step of persistent was done at the end of every micro-batch process even when there's no change
- The snapshot of each state was persisted unnecessarily and saved to the store in a file system
- This means State-to-Store was tightly coupled
- It could have been better if snapshot only contains the changes in state

## Spark >= 2.2.0
- Structured Steaming was introduced
- SQL-based streaming
- State management is now decoupled from metadata checkpointing
- Asynchronous to RDD execution
- Supports incremental state persistence

