import pyia2
from pyia2.constants import CHILDID_SELF, \
    UNLOCALIZED_ROLE_NAMES, \
    UNLOCALIZED_STATE_NAMES

def event_cb(event):
    print(event)
    ao = pyia2.accessibleObjectFromEvent(event)
    print("ROLE: " + ao.accRoleName())

    try:
        print("NAME: " + ao.accName(CHILDID_SELF))
    except:
        print("NAME: undefined")    

    try:
        print("VALUE: " + ao.accValue(CHILDID_SELF))
    except:
        print("VALUE: undefined")    


print("CHILDID_SELF: " + str(CHILDID_SELF))

event_id = pyia2.IA2_EVENT_DOCUMENT_LOAD_COMPLETE
pyia2.Registry.registerEventListener(event_cb, event_id )

event_id = pyia2.EVENT_OBJECT_FOCUS
pyia2.Registry.registerEventListener(event_cb, event_id )

pyia2.Registry.start()