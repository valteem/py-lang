import inspect

def _arg_types(f):
        sig = inspect.signature(f)
        print(sig)
        pos_args = [name for name, p in sig.parameters.items()
                    if p.kind == inspect.Parameter.POSITIONAL_ONLY]
        pos_or_kw_args = [name for name, p in sig.parameters.items()
                                      if p.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD]
        keyword_args = [name for name, p in sig.parameters.items()
                    if p.kind == inspect.Parameter.KEYWORD_ONLY]
        print("positional only:", pos_args)
        print("positional or keyword:", pos_or_kw_args)
        print("keyword only:", keyword_args)
        def func_wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return func_wrapper


@_arg_types
def somefunc(a, b, c = 1, t = "text", **kwargs):
    print("nothing")

@_arg_types
def anotherfunc(a, b, /, c, t = "text", *, arg1 = 1, arg2, arg3 = "message"):
     print("another nothing")

def main():
    somefunc(1, 2, arg1 = 1, arg2 = "another text")
    anotherfunc(1, 2, 3, arg2 = "some stuff")

if __name__ == "__main__":
    main()