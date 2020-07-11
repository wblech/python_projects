class ft_filter(object):

    def __init__(self, function_to_apply, list_of_inputs):
        self.func = function_to_apply
        self.list = list_of_inputs
        # generator expression
        # generator expressions are surrounded by parenthesis ()
        self.ret = (i for i in self.list if self.func(i))

    def __iter__(self):
        return self.ret

    def __next__(self):
        return next(self.ret)
