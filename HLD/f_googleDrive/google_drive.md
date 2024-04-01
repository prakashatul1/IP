functional Requirement
-------------------------
- upload  
- download  
- edit  
- share  
- manage permission  
- organise in folders   

NFR
-------------
- 200 Million Users
- 50 million Daily active users
- every user 15GB storage
- premium users

- 3000 petabytes of data
- cant lose data

- replicated

- throughput

- 2 file upload a day  10 mb file each
- read/write = 2:1

- available

- latency not a problem

dataModel
------------
- we will store 

- file -> HDFS(hadoop) -> s3
- metadata -> nosql preferred key value store -> data not massive mysql can be used

- file system can store hierarchy -> editable
- s3 -> scale comes for free

- s3 is preferred for simplicity
- hdfs is recommended

- s3 path is flat data structure
- key and value

- reliability and availability multi region

block level storage
----------------------
- we can store chunks of the file in s3 and store
- while get request we can reassemble and share file

deduplication
-----------------------
- if a file's block is equal to another file block
- we can store only one block
- while reassemble we can use same block
- we can do this at global level
- don't delete blocks on delete operation asit could be used by another 
- or we can store block count and delete once count is zero


how to identify block is duplicate
-------------------------------
- we can create a unique id based on block content
- when same block is uploaded by another user we would get same id

content addressable storage
-----------------------------------
- we use content to create address
- to identify duplicates easier or find a content

metadata schema
-------

folder
- name
- uid

file
- file_id
- folder_id
- uid

fileblock
- file_id
- block_id

blocks
- id
- reference to s3
- count

garbage collector / cleanup service
---------------
- on file deletion we will soft delete the folder till fileblock 
- we will run cleanup service that will run async 
- clean any blocks 

things to note
----------------------
- if file upload fails midway, we would be able to resume with blocks
- folders ?
- we wont store folder in object storage
- we can store folders data in database
- every folder is owned by user, and it will have reference for all its children files
- file will be stored in the database and will have references to data blocks
- every file will also have a pointer to folder
- if load balancer goes does another load balancer will take charge
- heartbeat zookeeper
- how to edit - delete and add new data
