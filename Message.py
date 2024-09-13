


MSG = lambda t, x: print(f"[{t}]: {x}")
INFO = lambda x : MSG("INFO", x)
WARN = lambda x : MSG("WARNING", x)
ERR = lambda x : MSG("ERROR", x)