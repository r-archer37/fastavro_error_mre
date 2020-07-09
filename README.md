# fastavro_error_mre

A demonstration of an error I encountered in using the `fastavro` python package.

**Expected Output** of `weather_avro.py`
```python
{'temperature': 99, 'time': 1234567890, 'multibroadcaster': {'broadcaster': {'presenterId': '2468ACE', 'presenterName': 'Pat'}}, 'station': {'stationId': '13579BDF', 'stationName': 'Local'}}
```

**Actual Output** of `weather_avro.py`
```
Traceback (most recent call last):
  File "weather_avro.py", line 27, in <module>
    [json.loads(open(INPUT_FILE, 'r').read())])
  File "weather_avro.py", line 15, in fastavro_encode
    fastavro.json_writer(out, schema, data)
  File "/opt/conda/lib/python3.7/site-packages/fastavro/json_write.py", line 46, in json_writer
    return writer(AvroJSONEncoder(fo), schema, records)
  File "/opt/conda/lib/python3.7/site-packages/fastavro/_write_py.py", line 600, in writer
    output.flush()
  File "/opt/conda/lib/python3.7/site-packages/fastavro/_write_py.py", line 484, in flush
    self.encoder.flush()
  File "/opt/conda/lib/python3.7/site-packages/fastavro/io/json_encoder.py", line 72, in flush
    self._parser.flush()
  File "/opt/conda/lib/python3.7/site-packages/fastavro/io/parser.py", line 140, in flush
    self.action_function(top)
  File "/opt/conda/lib/python3.7/site-packages/fastavro/io/json_encoder.py", line 78, in do_action
    self.write_object_end()
  File "/opt/conda/lib/python3.7/site-packages/fastavro/io/json_encoder.py", line 158, in write_object_end
    self._pop()
  File "/opt/conda/lib/python3.7/site-packages/fastavro/io/json_encoder.py", line 50, in _pop
    prev_current[prev_key] = self._current
TypeError: unhashable type: 'list'
```

**How to get the expected results:**
Change `test.MultiBroadcaster.avsc` and `test.Broadcaster.avsc` so that the `broadcaster` field and at least one field in the `Broadcaster` type are non-nullable:
`test.MultiBroadcaster.avsc`:
```json
{
    "namespace": "test",
    "type": "record",
    "name": "MultiBroadcaster",
    "fields": [
        {"name": "broadcaster", "type": "test.Broadcaster"}
    ]
}
```

`test.Broadcaster.avsc`:
```json
{
    "namespace": "test",
    "type": "record",
    "name": "Broadcaster",
    "fields": [
        {"name": "presenterId", "type": ["null", "string"], "default": null},
        {"name": "presenterName", "type": "string"}
    ]
}
```
