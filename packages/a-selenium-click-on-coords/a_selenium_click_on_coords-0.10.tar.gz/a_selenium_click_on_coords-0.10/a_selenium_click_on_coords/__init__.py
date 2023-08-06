def click_on_coordinates(driver, x, y, script_timeout=10):

    oldvalue = driver.__dict__["caps"]["timeouts"]["script"]
    try:
        driver.set_script_timeout(script_timeout)

        elementclicked = driver.execute_script(
            rf"""var simulateMouseEvent = function(element, eventName, coordX, coordY) {{
          element.dispatchEvent(new MouseEvent(eventName, {{
            view: window,
            bubbles: true,
            cancelable: true,
            clientX: coordX,
            clientY: coordY,
            button: 0
          }}));
        }};
        var theButton = document.elementFromPoint({x}, {y});
        coordX = {x},
        coordY = {y};
        simulateMouseEvent (theButton, "mousedown", coordX, coordY);
        simulateMouseEvent (theButton, "mouseup", coordX, coordY);
        simulateMouseEvent (theButton, "click", coordX, coordY);return theButton;"""
        )
    finally:
        driver.set_script_timeout(oldvalue)
    return elementclicked
