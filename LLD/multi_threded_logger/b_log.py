import threading
import multiprocessing
import portalocker
import os

class MultiProcessThreadSafeLogger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock = threading.Lock()

    def log(self, message):
        with self.lock:  # Thread-level locking
            # Open the file in append mode for each log entry
            with open(self.file_name, 'a') as file:
                # Lock the file, wait indefinitely until the lock can be acquired
                portalocker.lock(file, portalocker.LOCK_EX)
                file.write(f'{message}\n')
                # The file is unlocked automatically when closed

def log_worker(process_id, logger):
    """ Function to simulate logging from multiple threads within a process """
    thread_id = threading.current_thread().name
    for i in range(10):
        logger.log(f'Process {process_id}, Thread {thread_id}: Log entry {i+1}')

def process_worker(process_id, log_file):
    logger = MultiProcessThreadSafeLogger(log_file)
    threads = [threading.Thread(target=log_worker, args=(process_id, logger), name=f'Thread-{i}') for i in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    log_file = 'app.log'
    processes = [multiprocessing.Process(target=process_worker, args=(i, log_file)) for i in range(3)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
