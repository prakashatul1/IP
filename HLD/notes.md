# why distributed systems

- scale the db and cache tier
- need scale for higher throughput ( requests/sec )
- response time is high, parallelize computation
- availability, reliability in case of faults

- geolocation : using servers on different locations to minimise network latency
- hotspot : disproportionally high load on a piece of data

# why not vertical scaling

- cost is higher when we scale
- cost(2cpu, 2RAM, 2disks) >  2 * cost(cpu, RAM, disk)
- has a limit ( 96 cores in aws )
- single point of failure

# things to consider for storage
- plan for storage space 3 years in advance. 1000 days
- 100000 - 86400 seconds in a day 
- 1-2 tb of disk space in a machine

- any number upto 1000 takes 10 bit
- 10^3 = 10 bits
- 2^10 ~ 10^3
- 1 billion char
- 2^10^3 = 2^30
- 2^X = X bit
- 2 billion
- 2^31 = 31 bit
- 4 billion
- 2^32 = 32 bit
- 

# things to consider for throughput
- thread in a core * number of core
- 30 - 40 % cpu utilisation in serving requests

- x ms time needed to serve one request
- in one sec =  1000/x req/sec
- 100 threads * 1000/x req/sec = 10^5/x r/s
- 30% of cpu = 3*10^4/x rs/s

# Service level indicators (SLI) for performance measures
- correctness
- availability - fraction of all valid requests that were success 2 9s , 5 9s 
- throughput - 
  - number of req/sec that can be handled
  - if throughput low availability also low
- response time - p95, p95, p85, p50

# service level objective (SLO)
- A target value or range for SLI

# service level Agreement (SLA)
- A contract with your users on what SLOs are and consequence of missing them 

# response time = latency + service time
# bandwidth = max bits that can be transmitted over a network per sec
# throughput = actual measured bits getting transferred over a network per second

