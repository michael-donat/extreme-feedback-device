import usb.core
import usb.util
import sys

def getInterface():
    # find our device
    dev = usb.core.find(idProduct=0x0250)

    # was it found?
    if dev is None:
        raise ValueError('Device not found')




    # set the active configuration. With no arguments, the first
    # configuration will be the active one
    dev.set_configuration()

    # get an endpoint instance
    cfg = dev.get_active_configuration()
    interface_number = cfg[(0,0)].bInterfaceNumber
    alternate_setting = usb.control.get_interface(dev, interface_number)
    intf = usb.util.find_descriptor(
        cfg, bInterfaceNumber = interface_number,
        bAlternateSetting = alternate_setting
    )

    ep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match = \
        lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == \
            usb.util.ENDPOINT_OUT
    )

    assert ep is not None

class Relay:
    __config=None
    def __init__(self, config):
        self.__config=config
        pass

    def device(self, **kwargs):
        return usb.core.find(**kwargs)

    def interface(self, dev):

        if dev is None:
            sys.exit("No Panic button found in the system");

        try:
            if dev.is_kernel_driver_active(0) is True:
                dev.detach_kernel_driver(0)
        except usb.core.USBError as e:
            sys.exit("Kernel driver won't give up control over device: %s" % str(e))

        try:
            dev.set_configuration()
            dev.reset()
        except usb.core.USBError as e:
            sys.exit("Cannot set configuration the device: %s" % str(e))

        endpoint = dev[0][(0,0)][0]

        return endpoint

    def r1(self, isOn):
        pass

    def r2(self, isOn):
        pass

