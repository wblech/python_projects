class ft_map(object):

    def __init__(self, func, itens):
        self.func = func
        self.itens = itens
        self.ret = (self.func(item) for item in self.itens)

    def __iter__(self):
        return self.ret

    def __next__(self):
        return next(self.ret)

