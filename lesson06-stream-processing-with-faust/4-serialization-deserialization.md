## Serialization and Deserialization
Deserializing and serializing data into native Python objects can make working with streaming data simpler and easier to test. In the following section you will see how to map your internal Python data structures to incoming and outgoing data with Faust.

## Python Dataclasses
- A dataclass is a special type of Class in which instances are meant to represent data, but not contain mutating functions.
- Python dataclass objects can be marked as [frozen](https://docs.python.org/3/library/dataclasses.html#frozen-instances), which makes them immutable
Nothing in Python is truly immutable, but this attribute gets you about as close as you can get
- dataclass objects require type annotations on fields and will enforce those constraints on creation. This helps ensure you’re always working with data in the expected format, reducing and preventing errors.
- Can be paired with the [asdict](https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict) function to quickly transform dataclasses into dictionaries
- [New in Python 3.7](https://docs.python.org/3/whatsnew/3.7.html)
- Default to using dataclass to work with data coming into and out of your Faust applications unless you have a good reason not to