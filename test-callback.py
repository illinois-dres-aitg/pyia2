import pyia2
from pyia2.constants import CHILDID_SELF, \
    UNLOCALIZED_ROLE_NAMES, \
    UNLOCALIZED_STATE_NAMES
from pyia2.utils import IA2Lib

def event_cb(event):
    print(event)
    ao = pyia2.accessibleObjectFromEvent(event)
    print("\nROLE: " + ao.accRoleName())

    try:
        print("NAME: " + ao.accName(CHILDID_SELF))
    except:
        print("NAME: undefined")

    try:
        print("VALUE: " + ao.accValue(CHILDID_SELF))
    except:
        print("VALUE: undefined")

    if isinstance(ao, IA2Lib.IAccessible2):
        print "IAccessible2 Values: %s"%ao
        try:
            print("RELATIONS: ", ao.relations)
        except:
            print("RELATIONS: IA2 ERROR")

        try:
            print("STATES: ", ao.states)
        except:
            print("STATES: IA2 ERROR")
    else:
        print "Not IA2 Object"


print("CHILDID_SELF: " + str(CHILDID_SELF))
event_id = pyia2.IA2_EVENT_DOCUMENT_LOAD_COMPLETE
pyia2.Registry.registerEventListener(event_cb, event_id )

event_id = pyia2.EVENT_OBJECT_FOCUS
pyia2.Registry.registerEventListener(event_cb, event_id )

pyia2.Registry.start()
