"""
Return State Target functions
"""
from ..utils import Dispatch, exceptions, FrozenDict
from pysnmp.hlapi import * 

Return_State = Dispatch("return_state")

@Return_State.register
def default(*extra_args, **extra_kwargs):
    return exceptions.target_not_implemented()

@Return_State.register
def return_state(acuator,*extra_args, **extra_kwargs):
    g = sendNotification(SnmpEngine(),
                      CommunityData('public'),
                      UdpTransportTarget(('demo.snmplabs.com', 162)),
                      ContextData(),
                      'trap',
                     NotificationType(ObjectIdentity('IF-MIB', 'linkDown')))
    print(next(g))
    (None, 0, 0, [])
    return dict(status=400,status_text="testing")

Return_State.register(return_state,key="Return_State")
