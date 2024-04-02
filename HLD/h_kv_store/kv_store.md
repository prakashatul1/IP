Functional Requirement
-----------------------
- get
- put
- delete

NFR
-----------------
- durable
- dont need acid
- scalable

solution
------------------
- indexing data -> lsm tree good for quick writes
- replication
- partitioning
- node failure
- concurrent writes

partitioning
----------------
- lsm tree -> log structured merge tree
- writes are batched in memory
- write written to memory memtable
- eventually it would be flushed to sstable -> sorted string table
- when memory is filled we flush that to sstable (100 MB)
- writing to memory is fast
- while reading we can do binary search
- in case of system faliure memory will be gone
- when we write to memtable we also write transaction logs
- when update we will create new copy of data
- old value is still stored in ss table and eventually removed
- ss table is immutable
- old value is marked for deletion

replication
----------------------
- if suppose data is written to one node and not synced to other
- it read will stop to that node until data is synced (15 ms) favoring conistency
- or we can allow ro respond with old data -> lowering latency
- CAP threorem
- eventual consistency
- leader - follower
- leader - leader replication (allowing writes to all node)
- quorum w=1 if one node data is written 
- quorum w=3 if 3 node data is written -> increase latency 
- tunable consistency
- quorum r=1 one node can agree on value that is read
- quorum r=3 3 node have to agree on value that is read
- tunable

scaling
----------------
- allow users to specify shard key
- automatic shard key
- horizontal scaling
- consistent hashing -> increase and decrease nodes will adjust partitioned data
- if one node goes down it will go to virtual node
- create virtual node and distribute them evenly
- node can send heartbeat to neighbours
- if node is down haven't sent heartbeat in 1 min
- multiple nodes can verify that