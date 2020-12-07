from dataclasses import asdict, dataclass
import json

import faust


#
# TODO: Define a ClickEvent Record Class
#
@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int

app = faust.App("sample2", broker="kafka://localhost:9092")
'''
https://faust.readthedocs.io/en/latest/reference/faust.app.html
https://faust.readthedocs.io/en/latest/userguide/application.html#application-configuration
class faust.app.App(id: str, *, 
    monitor: faust.sensors.monitor.Monitor = None, 
    config_source: Any = None, 
    loop: asyncio.events.AbstractEventLoop = None, 
    beacon: mode.utils.types.trees.NodeT = None, **options: Any) → None
'''

#
# TODO: Provide the key and value type to the clickevent
#
clickevents_topic = app.topic(
    "com.udacity.streams.clickevents",
    key_type=str,
    value_type=ClickEvent,
)

@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for ce in clickevents:
        print(json.dumps(asdict(ce), indent=2))


if __name__ == "__main__":
    app.main()
