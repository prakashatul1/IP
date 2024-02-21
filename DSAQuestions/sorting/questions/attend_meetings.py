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
    for i in range(len(intervals) - 1):
        end_time_current_interval = intervals[i][1]
        start_time_next_interval = intervals[i + 1][0]
        # If overlap found, return 0.
        if end_time_current_interval > start_time_next_interval:
            return 0
    return 1


print(can_attend_all_meetings([
    [1, 2],
    [1, 3],
    [3, 5],
    [4, 5]

]))
