"""
Asymptotic complexity in terms of the length of `intervals` `n`:
* Time: O(n * log(n)).
* Auxiliary space: O(1).
* Total space: O(n).
"""


def can_attend_all_meetings(intervals):
    # Sorting in ascending order of start time of an interval.
    # If start time is same for two intervals then sort in ascending order of end time of intervals.
    intervals.sort()
    count = 0
    min_end_time = None
    for i in range(len(intervals) - 1):
        end_time_current_interval = intervals[i][1]
        start_time_next_interval = intervals[i + 1][0]
        min_end_time = min(end_time_current_interval, min_end_time) if min_end_time else end_time_current_interval

        if end_time_current_interval > start_time_next_interval:
            count += 1

    return count


print(can_attend_all_meetings([
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 5]
]))
