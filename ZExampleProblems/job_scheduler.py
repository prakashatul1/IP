import uuid
from enum import Enum


class JobStatus(Enum):
    queued = 1
    running = 2
    completed = 3


class Job:

    def __init__(self, payload: dict):
        self.payload = payload
        self.status = JobStatus.queued
        self.id = uuid.uuid1()
        print(f" job {self.id} is queued")

    def start(self):
        self.status = JobStatus.running
        print(f" job {self.id} is running")

    def complete(self):
        self.status = JobStatus.completed
        print(f" job {self.id} is completed")


class Worker:

    def __init__(self):
        self.job = None
        self.id = uuid.uuid1()
        print(f"Initialed worker {self.id}")

    def completeJob(self):
        if self.job:
            print(f"Worker {self.id} is completing job {self.job.id}")
            self.job.complete()

    def assignJob(self, job: Job):
        self.job = job
        print(f"Worker {self.id} is assigned job {self.job.id}")
        self.job.start()


class JobScheduler:

    def __init__(self):
        self.workers = []
        self.jobs = []

    def addJob(self, job: Job):
        print(f"added job {job.id} to scheduler")
        self.jobs.append(job)

    def addWorker(self, worker: Worker):
        print(f"added worker {worker.id} to scheduler")
        self.workers.append(worker)

    def assignJobs(self):
        for job in self.jobs:
            if job.status == JobStatus.queued:
                available_worker = next((worker for worker in self.workers if worker.job is None), None)
                if available_worker:
                    available_worker.assignJob(job)

    def getQueuedJobs(self):
        return [job for job in self.jobs if job.status == JobStatus.queued]

    def getRunningJobs(self):
        return [job for job in self.jobs if job.state == JobStatus.running]

    def getCompletedJobs(self):
        return [job for job in self.jobs if job.state == JobStatus.completed]


job1 = Job(payload={"type": "data_processing", "file": "data.txt"})
job2 = Job(payload={"type": "report_generation", "format": "pdf"})

worker1 = Worker()
worker2 = Worker()

jobScheduler = JobScheduler()

jobScheduler.addJob(job1)
jobScheduler.addJob(job2)

jobScheduler.addWorker(worker1)
jobScheduler.addWorker(worker2)

jobScheduler.assignJobs()

worker1.completeJob()
