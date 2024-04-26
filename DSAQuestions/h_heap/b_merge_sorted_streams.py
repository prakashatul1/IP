import heapq


def merge_sorted_streams(*streams):
    # Create a min-heap
    min_heap = []

    # Initialize the heap with the first element of each stream, if available
    # We store a tuple containing the value, the index of the stream, and the index of the element within the stream
    for stream_index, stream in enumerate(streams):
        if stream:  # Check if the stream is not empty
            heapq.heappush(min_heap, (stream[0], stream_index, 0))

    # Create a list to store the merged output
    result = []

    # Continue merging until the heap is empty
    while min_heap:
        value, stream_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # Check if there are more elements in the same stream
        if element_index + 1 < len(streams[stream_index]):
            # Get the next element from the same stream
            next_value = streams[stream_index][element_index + 1]
            # Push it to the heap
            heapq.heappush(min_heap, (next_value, stream_index, element_index + 1))

    return result


# Example usage
stream1 = [1, 2]
stream2 = [1, 1, 3, 4]
merged_stream = merge_sorted_streams(stream1, stream2)
print("Merged Stream:", merged_stream)
