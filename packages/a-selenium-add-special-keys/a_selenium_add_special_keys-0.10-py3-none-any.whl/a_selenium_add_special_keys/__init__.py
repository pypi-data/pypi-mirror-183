import json
from functools import partial
from useful_functions_easier_life import NamedFunction


def send_cmd(driver, cmd, params):
    # https://stackoverflow.com/a/47068019/15096247
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({"cmd": cmd, "params": params})
    response = driver.command_executor._request("POST", url, body)
    return response.get("value")

def _send_Backspace_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Backspace",
            "isKeypad": True,
            "key": "Backspace",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 8,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Backspace",
            "key": "Backspace",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 8,
        },
    )


def _create_send_Backspace_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Backspace_key, driver_),
        name_function=lambda: "send_Backspace_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Tab_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Tab",
            "isKeypad": True,
            "key": "Tab",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 9,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Tab",
            "key": "Tab",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 9,
        },
    )


def _create_send_Tab_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Tab_key, driver_),
        name_function=lambda: "send_Tab_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Enter_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Enter",
            "isKeypad": True,
            "key": "Enter",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 13,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Enter",
            "key": "Enter",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 13,
        },
    )


def _create_send_Enter_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Enter_key, driver_),
        name_function=lambda: "send_Enter_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Shift_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Shift",
            "isKeypad": True,
            "key": "Shift",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 16,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Shift",
            "key": "Shift",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 16,
        },
    )


def _create_send_Shift_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Shift_key, driver_),
        name_function=lambda: "send_Shift_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Control_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Control",
            "isKeypad": True,
            "key": "Control",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 17,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Control",
            "key": "Control",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 17,
        },
    )


def _create_send_Control_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Control_key, driver_),
        name_function=lambda: "send_Control_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Alt_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Alt",
            "isKeypad": True,
            "key": "Alt",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 18,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Alt",
            "key": "Alt",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 18,
        },
    )


def _create_send_Alt_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Alt_key, driver_),
        name_function=lambda: "send_Alt_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_CapsLock_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "CapsLock",
            "isKeypad": True,
            "key": "CapsLock",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 20,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "CapsLock",
            "key": "CapsLock",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 20,
        },
    )


def _create_send_CapsLock_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_CapsLock_key, driver_),
        name_function=lambda: "send_CapsLock_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Escape_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Escape",
            "isKeypad": True,
            "key": "Escape",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 27,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Escape",
            "key": "Escape",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 27,
        },
    )


def _create_send_Escape_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Escape_key, driver_),
        name_function=lambda: "send_Escape_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Space_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Space",
            "isKeypad": True,
            "key": "Space",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 32,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Space",
            "key": "Space",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 32,
        },
    )


def _create_send_Space_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Space_key, driver_),
        name_function=lambda: "send_Space_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_PageUp_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "PageUp",
            "isKeypad": True,
            "key": "PageUp",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 33,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "PageUp",
            "key": "PageUp",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 33,
        },
    )


def _create_send_PageUp_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_PageUp_key, driver_),
        name_function=lambda: "send_PageUp_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_PageDown_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "PageDown",
            "isKeypad": True,
            "key": "PageDown",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 34,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "PageDown",
            "key": "PageDown",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 34,
        },
    )


def _create_send_PageDown_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_PageDown_key, driver_),
        name_function=lambda: "send_PageDown_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_End_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "End",
            "isKeypad": True,
            "key": "End",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 35,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "End",
            "key": "End",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 35,
        },
    )


def _create_send_End_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_End_key, driver_),
        name_function=lambda: "send_End_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Home_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Home",
            "isKeypad": True,
            "key": "Home",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 36,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Home",
            "key": "Home",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 36,
        },
    )


def _create_send_Home_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Home_key, driver_),
        name_function=lambda: "send_Home_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_ArrowLeft_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "ArrowLeft",
            "isKeypad": True,
            "key": "ArrowLeft",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 37,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "ArrowLeft",
            "key": "ArrowLeft",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 37,
        },
    )


def _create_send_ArrowLeft_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_ArrowLeft_key, driver_),
        name_function=lambda: "send_ArrowLeft_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_ArrowUp_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "ArrowUp",
            "isKeypad": True,
            "key": "ArrowUp",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 38,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "ArrowUp",
            "key": "ArrowUp",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 38,
        },
    )


def _create_send_ArrowUp_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_ArrowUp_key, driver_),
        name_function=lambda: "send_ArrowUp_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_ArrowRight_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "ArrowRight",
            "isKeypad": True,
            "key": "ArrowRight",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 39,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "ArrowRight",
            "key": "ArrowRight",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 39,
        },
    )


def _create_send_ArrowRight_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_ArrowRight_key, driver_),
        name_function=lambda: "send_ArrowRight_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_ArrowDown_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "ArrowDown",
            "isKeypad": True,
            "key": "ArrowDown",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 40,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "ArrowDown",
            "key": "ArrowDown",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 40,
        },
    )


def _create_send_ArrowDown_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_ArrowDown_key, driver_),
        name_function=lambda: "send_ArrowDown_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def _send_Delete_key(driver):
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "autoRepeat": False,
            "code": "Delete",
            "isKeypad": True,
            "key": "Delete",
            "location": 0,
            "modifiers": 0,
            "text": "",
            "type": "rawKeyDown",
            "unmodifiedText": "",
            "windowsVirtualKeyCode": 46,
        },
    )
    send_cmd(
        driver,
        "Input.dispatchKeyEvent",
        {
            "code": "Delete",
            "key": "Delete",
            "location": 0,
            "modifiers": 0,
            "type": "keyUp",
            "windowsVirtualKeyCode": 46,
        },
    )


def _create_send_Delete_key(driver_):

    return NamedFunction(
        name="",
        execute_function=partial(_send_Delete_key, driver_),
        name_function=lambda: "send_Delete_key()",
        str_prefix="",
        print_before_execution="",
        str_suffix="",
        ljust_prefix=0,
        rjust_prefix=0,
        ljust_suffix=0,
        rjust_suffix=0,
    )


def add_special_keys(driver_):
    driver_.send_Backspace_key = _create_send_Backspace_key(driver_)
    driver_.send_Tab_key = _create_send_Tab_key(driver_)
    driver_.send_Enter_key = _create_send_Enter_key(driver_)
    driver_.send_Shift_key = _create_send_Shift_key(driver_)
    driver_.send_Control_key = _create_send_Control_key(driver_)
    driver_.send_Alt_key = _create_send_Alt_key(driver_)
    driver_.send_CapsLock_key = _create_send_CapsLock_key(driver_)
    driver_.send_Escape_key = _create_send_Escape_key(driver_)
    driver_.send_Space_key = _create_send_Space_key(driver_)
    driver_.send_PageUp_key = _create_send_PageUp_key(driver_)
    driver_.send_PageDown_key = _create_send_PageDown_key(driver_)
    driver_.send_End_key = _create_send_End_key(driver_)
    driver_.send_Home_key = _create_send_Home_key(driver_)
    driver_.send_ArrowLeft_key = _create_send_ArrowLeft_key(driver_)
    driver_.send_ArrowUp_key = _create_send_ArrowUp_key(driver_)
    driver_.send_ArrowRight_key = _create_send_ArrowRight_key(driver_)
    driver_.send_ArrowDown_key = _create_send_ArrowDown_key(driver_)
    driver_.send_Delete_key = _create_send_Delete_key(driver_)
    return driver_