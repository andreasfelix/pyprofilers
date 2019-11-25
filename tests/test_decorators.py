def func():
    pass

def test_simple_timer():
    from pyprofilers import simple_timer
    simple_timer(func)()

def test_cprofile():
    from pyprofilers import profile
    profile(func)()

