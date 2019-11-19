import sys

import six

import pyia2

if six.PY2:
  reload(sys)
  sys.setdefaultencoding('utf-8')

desktop = pyia2.getDesktop()
print(str(desktop))

for window in desktop:
  if not window.accState(0) & pyia2.STATE_SYSTEM_INVISIBLE:
     print(repr(str(window)))

# Need to get ia2.tlb
# create a module comptypes.client.GetModule(path to ia2.tlb)
