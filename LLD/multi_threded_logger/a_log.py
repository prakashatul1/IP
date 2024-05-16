import threading


class ThreadSafeLogger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock = threading.Lock()

    def log(self, message):
        with self.lock:
            with open(self.file_name, 'a') as file:
                file.write(f'{message}\n')


# Usage:
logger = ThreadSafeLogger('app.log')


def worker_thread(id):
    for _ in range(10):
        logger.log(f'Log entry from Thread {id}')


# Example of spawning multiple threads
threads = [threading.Thread(target=worker_thread, args=(i,)) for i in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
