# Graph CRUD 

High-level API to run CRUD operations on Graph Databases, with JSON inputs.

**UPDATE**. This project is moved to [invanalabs/invana](https://github.com/invanalabs/invana)

**Note** Under Active Development. 

```python
from gremlin_crud.manager import GremlinCRUDManager

manager = GremlinCRUDManager("ws://127.0.0.1:8182/gremlin")
msg = {...}
manager.process(msg)
```
### Add Vertex

```json
{
  "type": "vertex",
  "operation_type": "create",
  "data": {
    "label": "Plant",
    "properties":{
      "common_name": "chrysanths",
      "scientific_name": "Chrysanthemum"
    }
  }
}
manager.process(msg)

```

### Add Edge

```json
{
  "type": "Edge",
  "operation_type": "create",
  "data": {
    "label": "BelongsTo",
    "inV": {
      "query":  {
        "type":  "vertex", 
        "operation_type": "find_one", 
        "filter":  {"label":  "Plant", "properties": {"common_name": "chrysanths"} }
      }
    },
    "outV": {"id":  "123-asdv-asd123"},
    "properties":{
      "first_discovered": 1989
    }    
  }
 
}
```
