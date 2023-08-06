""" Model for BACnet add-on data"""
from dataclasses import dataclass
from typing import Any, Union

@dataclass
class Object:
    """Represent a BACnet object"""
    objectIdentifier: str
    objectType: str
    objectName: str
    description: str
    presentValue: Union[int, float, str, bool]
    statusFlags: str
    units: str
    outOfService: bool
    eventState: str
    reliability: str
    covIncrement: Union[int, float]

@dataclass
class Device:
    """Represent a BACnet Device"""
    objects: dict[str, Object]

    @staticmethod
    def update_device(device_data: dict[str, Any]):
        """Update the device from device data"""
        objects = {}
        for object_name, object_data in device_data.items():
            object = Object(
                object_data.get("objectIdentifier"), 
                object_data.get("objectType"), 
                object_data.get("objectName"), 
                object_data.get("description"), 
                object_data.get("presentValue"), 
                object_data.get("statusFlags"), 
                object_data.get("units"), 
                object_data.get("outOfService"), 
                object_data.get("eventState"), 
                object_data.get("reliability"),
                object_data.get("covIncrement"),
                )
            objects.update({object_name: object})
        return Device(objects)

class DeviceDict:
    """Represent a dictionary of all BACnet devices on the network"""
    devices: dict[str, Device] = {}

    def __init__(self, data: dict[str, Any]):
        self.update_from_data(data)


    def update_from_data(self, data: dict[str, Device]):    
        """Update the device dictionary from received data"""
        for device_name, device_data in data.items():
            device = Device.update_device(device_data)
            self.devices.update({device_name: device})
        return self