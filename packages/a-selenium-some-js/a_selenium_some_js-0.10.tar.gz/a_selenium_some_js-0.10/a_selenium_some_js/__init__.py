import json
import ctypes


def execute_scripts_with_timeout(driver, script, script_timeout=1):
    execu = None
    oldvalue = driver.__dict__["caps"]["timeouts"]["script"]
    driver.set_script_timeout(script_timeout)
    try:

        execu = driver.execute_async_script(script)
    except Exception as fe:
        print(fe)
    finally:
        driver.set_script_timeout(oldvalue)

    return execu


def js_scrollby(driver, y, script_timeout=1):
    execute_scripts_with_timeout(
        driver, script=f"window.scrollBy(0,{y})", script_timeout=script_timeout
    )


def go_to_top_of_page(driver, script_timeout=1):
    execute_scripts_with_timeout(
        driver, script=f"window.scrollTo(0, 0);", script_timeout=script_timeout
    )


def get_navigator_infos(driver):
    navigator = {
        "userAgent": driver.execute_script("return window.navigator.userAgent"),
        "appVersion": driver.execute_script("return window.navigator.appVersion"),
        "platform": driver.execute_script("return window.navigator.platform"),
        "vendor": driver.execute_script("return window.navigator.vendor"),
        "language": driver.execute_script("return window.navigator.language"),
        "languages": driver.execute_script("return window.navigator.languages"),
        "cookieEnabled": driver.execute_script("return window.navigator.cookieEnabled"),
        "doNotTrack": driver.execute_script("return window.navigator.doNotTrack"),
        "oscpu": driver.execute_script("return window.navigator.oscpu"),
        "plugins": driver.execute_script(
            "return Array.from(navigator.plugins).map(({filename,name,description}) => ({filename,name,description}));"
        ),
        "mimeTypes": driver.execute_script(
            "return Array.from(navigator.mimeTypes).map(a => ({'type':a.type, 'description':a.description, 'suffixes':a.suffixes, 'enabledPlugin':a.enabledPlugin.name}));"
        ),
    }
    return navigator


def zoom_website(driver, scaleFactor=2, x=0, y=0, relativeSpeed=800):
    send_cmd(
        driver,
        "Input.synthesizePinchGesture",
        {
            "x": x,
            "y": y,
            "scaleFactor": scaleFactor,
            "relativeSpeed": relativeSpeed,  # optional
            "gestureSourceType": "default",  # optional
        },
    )


def maximize_window(driver__):
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screenr = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    driver__.set_window_position(0, 0, windowHandle="current")
    driver__.set_window_size(*screenr)


def send_cmd(driver, cmd, params):
    # https://stackoverflow.com/a/47068019/15096247
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({"cmd": cmd, "params": params})
    response = driver.command_executor._request("POST", url, body)
    return response.get("value")
