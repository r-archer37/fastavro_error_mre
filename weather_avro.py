import json

import fastavro
from fastavro.schema import load_schema

INPUT_FILE = 'test_weather_data.json'
OUTPUT_FILE = 'test_weather_data.txt'
SCHEMA_TO_USE = 'Weather.avsc'

schema = load_schema(SCHEMA_TO_USE)


def fastavro_encode(schema, file_name, data):
    with open(file_name, 'w') as out:
        fastavro.json_writer(out, schema, data)


def fastavro_decode(schema, file_name):
    with open(file_name, 'r') as fo:
        my_reader = fastavro.json_reader(fo, schema)
        for record in my_reader:
            print(record)


fastavro_encode(schema,
                OUTPUT_FILE,
                [json.loads(open(INPUT_FILE, 'r').read())])

fastavro_decode(schema, OUTPUT_FILE)
