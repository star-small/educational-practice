import json
import sqlite3
from datetime import datetime

json_file = 'file.json'
with open(json_file, 'r') as f:
    data = json.load(f)

conn = sqlite3.connect('annotations.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS annotations (
        id INT PRIMARY KEY,
        x FLOAT,
        y FLOAT,
        width FLOAT,
        height FLOAT,
        rectanglelabels TEXT,
        image TEXT,
        created_at TIMESTAMP
    )
''')

for item in data:
    if item['annotations']:  
    annotation = item['annotations'][0]['result']
        if annotation:  
        value = annotation[0]['value']
            x, y, width, height = value['x'], value['y'], value['width'], value['height']
            rectanglelabels = value['rectanglelabels'][0]
            image = item['data']['image']
            created_at = datetime.now()

            c.execute('''
                INSERT INTO annotations (id, x, y, width, height, rectanglelabels, image, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (item['id'], x, y, width, height, rectanglelabels, image, created_at))

conn.commit()
conn.close()



