# Command Pattern

## Remote Controller Example
- [third party vendors](vendor.py) provided classes implementation (APIs) to communicate with their devices 
- remote controller contains buttons with [defined keys `RemoteControllerButtons`](remote_controller.py)
- decoupling remote controller with vendor execution 
    + remote controller only responsible for sending button request and should not know any result to vendor devices after button was pressed
    + vendor device only operated after receiving its command (it has no knowledge about remote controller)
