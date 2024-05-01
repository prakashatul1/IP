- indexing data
- replication
- partitioning
- node failure
- concurrent writes
----------------

Indexing data
----------------------
LSM Tree
--------------
very quick writes like cassandra

writes batched in memory (memtable) -> flushed to disk when memory full (sstable)
sstable - key identifies data - sorted string table = binary search
lots of sstable to scale

memtable -> transaction log

update a value
- read the value (that will be problem)

- write new value
- old value still remains
- mark deleted (tombstone) dont return to client

- sstable is immutable

- cleanup can be done. deleted and duplicated value can be deleted

replication (CAP)
--------------------

- problem data consistency
- if one replica is not updated

this node should not do any read requests - available for reads after 50 ms - until latest data updated
- consistency

allow this node to respond stale data (eventual consistency)
- latency

- all nodes will be able to handle write
- read after write

read quorum
- min no of nodes agree to read value transaction (high value low availability)
- 

write quorum
- min no of nodes agree to write transaction (lower value lower consistency)


partitioning
------------------


consistent hashing
---------------
- data nodes lying on ring
- hash value between 0 - 360
- able to choose partition

- if one partition is down
- repartitioning
- data on partition becomes higher

virtual nodes in between actual nodes
- represents actual node
- now if one node is down virtual nodes data spead out equally

node failure
-----------------
use external service
zookeeper key value store
every node sends heartbeat
control plane redirects traffic to another node

gossip protocol
-------------------
every node is control plane
every node knows info about all others 

more than one node heartbeat verify if a node has gone down

if node goes down all writes and go to different node until it comes up

concurrent writes
--------------
last write wins






