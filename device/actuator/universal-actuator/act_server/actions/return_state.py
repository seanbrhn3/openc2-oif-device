"""
Return State Target functions
"""
from .utils import Dispatch, exceptions

Return_State = Dispatch("return_state")

@Return_State.register
def default(*extra_args, **extra_kwargs):
    return dict(status=400,status_text="looks like we're talking! ;)")
    print("Does it reach theres")
    return dict(status=400,status_text="looks like theres a problem!")
