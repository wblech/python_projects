def ft_reduce(function_to_apply, list_of_inputs):
    lst = iter(list_of_inputs)
    value = next(lst)
    for i in lst:
        value = function_to_apply(value, i)
    return value

