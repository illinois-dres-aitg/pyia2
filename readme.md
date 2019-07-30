# Python Interface to MSAA+IAccessible2

This project builds on top of the work of Eitan Isaacson [pyia](https://github.com/eeejay/pyia) project to build a python library to expose Microsoft Active Accessibility (MSAA) and IAccessible2 interfaces for Windows Operating system.
This project extends the pyia project to support the IAccessible2 interfaces. 
The purpose of the project is to support ARIA and HTML5 implementation of the accessibility mapping specifictions as part of the activities of the W3C WAI ARIA and HTML5 working groups.

## Installation Requirements

* Install python 2.7 and pip for Windows 
* Clone this repository
* Install using pip
  
```
pip install -e C:\path\to\repository
```

* The `setup.py` file will try to register IAccessible2Proxy.dll with Windows. If it fails, then you need to register it manually with administration privileges:

```
regsvr32 IAccessible2Proxy.dll
```

## Examples
* test.py will display a list of information on the currenly open windows
* test-callback.py will list events related to document loads and focus changes

## Chrome Browser Configuration
* Chrome has an accessibility configutation options avaialble through typing in the following URL: chrome://accessibility/
* Use this configuration option to configure chrome to expose accessibility information

## References
* [pyia project](https://github.com/eeejay/pyia)
* [W3C Accessible Technology Test Adapter (ATTA) API Specification](https://spec-ops.github.io/atta-api/)
* [Spec-Ops: ATTA tools](https://github.com/Spec-Ops/web-platform-tests/tree/atk-atspi-atta/wai-aria/tools)
* [Microsoft Active Accessibility: Architecture](https://msdn.microsoft.com/en-us/library/ms971310.aspx?f=255&MSPPError=-2147217396)
* [The Linux Foundation: IAccessible2](https://wiki.linuxfoundation.org/accessibility/iaccessible2/start)
* [IAccessible2 COM proxy stub DLL](https://wiki.linuxfoundation.org/accessibility/iaccessible2/comproxydll)
