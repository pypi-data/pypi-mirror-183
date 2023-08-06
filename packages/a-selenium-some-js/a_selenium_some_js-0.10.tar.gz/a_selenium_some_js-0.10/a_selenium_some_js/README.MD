# A couple of useful JS scripts for Selenium


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10

$pip install a-selenium-some-js

from a_selenium_some_js import *

execute_scripts_with_timeout(
        driver, script=f"window.scrollBy(0,{200})", script_timeout=3
    )
js_scrollby(driver, y=40, script_timeout=0)	
go_to_top_of_page(driver, script_timeout=1)
get_navigator_infos(driver)
zoom_website(driver, scaleFactor=2, x=0, y=0, relativeSpeed=800)

maximize_window(driver) # window is not maximized, but its size is like maximized

send_cmd(driver,'Input.synthesizePinchGesture', {
                        'x': 0,
                        'y': 0,
                        'scaleFactor': 2,
                        'relativeSpeed': 800, # optional
                        'gestureSourceType': 'default' # optional
                    }) # https://chromedevtools.github.io/devtools-protocol/
    
	
```




