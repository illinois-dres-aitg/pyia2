import pyia2
from pyia2.constants import CHILDID_SELF, \
    UNLOCALIZED_ROLE_NAMES, \
    UNLOCALIZED_STATE_NAMES
from pyia2.utils import IA2Lib

def NextAccessible(event_id=pyia2.EVENT_OBJECT_FOCUS, predicate=None):
    shared = {}
    def callback(event):
        accessible = pyia2.accessibleObjectFromEvent(event)
        if not accessible:
            return
        if predicate and not predicate(event, accessible):
            return
        shared["accessible"] = accessible

    pyia2.Registry.registerEventListener(callback, event_id)
    while "accessible" not in shared:
        pyia2.Registry.iter_loop(0.01)
    pyia2.Registry.deregisterEventListener(callback, event_id)
    return shared["accessible"]

def NextAccessible2(event_id=pyia2.EVENT_OBJECT_FOCUS, predicate=None):
    def augmented_predicate(event, accessible):
        accessible2 = pyia2.accessible2FromAccessible(accessible, CHILDID_SELF)
        if not isinstance(accessible2, IA2Lib.IAccessible2):
            return False
        if predicate:
            return predicate(event, accessible2)
        else:
            return True
    
    accessible = NextAccessible(event_id, augmented_predicate)
    return pyia2.accessible2FromAccessible(accessible, CHILDID_SELF)
