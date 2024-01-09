def flatten(arr):
    result = []
    for element in arr:
        if isinstance(element, list):
            # Flatten the sublist and extend the main list
            result.extend(flatten(element))
        else:
            result.append(element)
    return result


# Example usage
multi_dim_array = [2,3,[8], [[[12]]]]
flattened_array = flatten(multi_dim_array)
print(flattened_array)  # Output: [1, 2, 3, 4, 5, 6, 7]
