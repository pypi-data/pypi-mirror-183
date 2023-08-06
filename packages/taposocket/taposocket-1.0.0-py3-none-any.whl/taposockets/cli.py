import argparse
from taposockets import P100


def parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--address", required=True, help="Provide your switch ip. Ex: 192.168.2.2")
    ap.add_argument("-u", "--username", required=True, help="Provide username for your switch")
    ap.add_argument("-p", "--password", required=True, help="Provide password for your switch")
    ap.add_argument("-o", "--operation", required=False, default="info", help="Tapo switch operation")
    args = vars(ap.parse_args())
    return args


def on(p100):
    p100.turn_on()


def off(p100):
    p100.turn_off()


def toggle(p100):
    p100.toggle_state()


def on_with_delay(p100):
    p100.turn_on_with_delay(10)


def off_with_delay(p100):
    p100.turn_off_with_delay(10)


def device_info(p100):
    print(p100.get_device_info())


def device(p100):
    print(p100.get_device_name())


def operate_switch():
    args = parser()
    p100 = P100(args["address"], args["username"], args["password"])
    # Creates the cookies required for further methods
    p100.handshake()
    # Sends credentials to the plug and creates AES Key and IV for further methods
    p100.login()
    operation = args["operation"]
    if operation == "info":
        device_info(p100)
    elif operation == "name":
        device(p100)
    elif operation == "on":
        on(p100)
    elif operation == "off":
        off(p100)
    elif operation == "on-delay":
        on_with_delay(p100)
    elif operation == "off-delay":
        off_with_delay(p100)
    elif operation == "toggle":
        toggle(p100)
    else:
        print(f"Please select valid choise. \nTry\n\t python -m taposockets -h")


if __name__ == "__main__":
    operate_switch()
