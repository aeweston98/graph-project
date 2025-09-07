# Doc intent
The intent of this doc is to capture the major design points of the first iteration of the project.

# Areas of Volatility
* The algorithm we want to run
  * Depending on this, the edge and node properties of the corresponding input graph may also differ. We should isolate that data within the algorithm contract, but have the storage contract have a generic representation of any properties.
* Method and layout of storage
  * Should experiment with different options, different algorithms may benefit from different structure.
* Client
  * This can change over time, will probably just start with CLI but should have a clear data in/out contract and support any auxiliary operations clients may want to do through a contract

# First iteration design
Layer diagram:<br>
![Layer diagram](Layers.jpg)

# Graph contracts
## Graph
### Graph Struct
* Set of nodes
* Set of edges

### Graph constructor
* Some kind of input format?

### Graph interface
* GetRandomNode
* GetNode
* DeleteNode
* UpdateNodeBaggage
* UpdateEdgeBaggage

## Nodes
### Node struct
* ID - read-only
* Baggage
* Adjacent (list of edges)

### Node constructor
* ID

### Node interface
* Get Baggage
* Set Baggage
* Get Adjacent
* AddEdge
* DeleteEdge
* Delete

## Edges
### Edge struct
* ID? - read-only
* Baggage
*  NodeA
*  NodeB

### Edge ctor
* ID
* NodeA
* NodeB
* Baggage

### Edge Interface
* GetID
* GetBaggage
* SetBaggage
* Delete