 File "C:\Users\adity\Desktop\12-01-2025\practice.py", line 244, in <module>
    app = SmartUniversity()
  File "C:\Users\adity\Desktop\12-01-2025\practice.py", line 110, in __init__
    self.load_data()
    ~~~~~~~~~~~~~~^^
  File "C:\Users\adity\Desktop\12-01-2025\practice.py", line 114, in load_data
    self._load_json("students.json", "student")
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\adity\Desktop\12-01-2025\practice.py", line 127, in _load_json
    item["id"], item["name"],
    ~~~~^^^^^^
KeyError: 'id'
