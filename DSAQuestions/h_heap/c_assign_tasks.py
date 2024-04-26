import heapq
from collections import deque


def assign_tasks(servers, tasks):
    # Create a min-heap to store servers (weight, index)
    available_servers = [(weight, i) for i, weight in enumerate(servers)]
    heapq.heapify(available_servers)

    # List to keep track when each server will be free
    server_free_time = [0] * len(servers)

    # Queue to hold tasks that are coming in
    task_queue = deque()

    # Array to store the result of which server takes each task
    ans = [-1] * len(tasks)

    # Current time simulation
    current_time = 0
    max_time = len(tasks)

    while current_time < max_time or task_queue:
        # Enqueue the current task if there is one
        if current_time < max_time:
            task_queue.append(current_time)

        # Process available servers
        temp_servers = []
        while available_servers and task_queue:
            weight, server_idx = heapq.heappop(available_servers)
            if server_free_time[server_idx] <= current_time:
                task_idx = task_queue.popleft()
                ans[task_idx] = server_idx
                server_free_time[server_idx] = current_time + tasks[task_idx]
            else:
                temp_servers.append((weight, server_idx))

        # Push back not-yet-available servers to heap
        for server in temp_servers:
            heapq.heappush(available_servers, server)

        # Time only progresses if we can't do anything at the current time
        if not task_queue:
            current_time += 1
        elif available_servers:
            # Move time forward to the next task or server availability
            next_task_time = current_time + 1 if current_time < max_time else float('inf')
            next_server_free_time = min(
                server_free_time[i] for i in range(len(servers)) if server_free_time[i] > current_time)
            current_time = min(next_task_time, next_server_free_time)
        else:
            current_time = min(server_free_time)  # No servers available, jump to when next one is free

    return ans
