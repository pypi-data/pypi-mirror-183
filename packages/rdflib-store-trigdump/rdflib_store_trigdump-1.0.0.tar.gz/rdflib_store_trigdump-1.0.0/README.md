# rdflib-store-trigdump

This is a thin wrapper around [RDFLib](https://github.com/RDFLib/rdflib)'s
[Memory store](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.plugins.stores.html#rdflib.plugins.stores.memory.Memory)
adding (unsafe) persistence:

 * When opening the store, data is read from a TriG file
 * When closing the store, data is serialized to the TriG file

## Usage

```python
from rdflib import Graph

graph = Graph("TriGDump")
graph.open("/path/to/my/file.trig", create=True)

# do something

graph.close()
```
