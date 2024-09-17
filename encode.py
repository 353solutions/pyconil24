import unter_pb2 as pb
import json
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime


msg = pb.StartRideRequest(
    id='r1',
    kind=pb.Kind.KIND_SHARED,
    driver_id='007',
)
msg.time.GetCurrentTime()
# print(msg)

# Serialization
data = msg.SerializeToString()
print('proto size:', len(data))

# De-serialization
msg2 = pb.StartRideRequest.FromString(data)
print(msg2.id)


# JSON
d = {f.name: getattr(msg, f.name) for f in msg.DESCRIPTOR.fields}
d['time'] = d['time'].ToJsonString()
json_data = json.dumps(d)
print('json size:', len(json_data))

# End
end = pb.EndRideRequest(
    id='r1',
    distance=1.7,
)
end.time.FromDatetime(datetime(2024, 9, 17, 14, 30))
print(end)
data = end.SerializeToString()
print('end:', data)