class Oracle:
    class __Oracle:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not Oracle.instance:
            Oracle.instance = Oracle.__Oracle(arg)
        else:
            Oracle.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def prt(self, s):
        print(s)

ORACLE = Oracle('shelley')