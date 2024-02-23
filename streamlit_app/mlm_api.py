import pychrome

browser = pychrome.Browser(url="http://127.0.0.1:9222")
tab = browser.new_tab()

def request_will_be_sent(**kwargs):
    print("loading: %s" % kwargs.get('request').get('url'))


tab.Network.requestWillBeSent = request_will_be_sent
tab.start()
tab.Network.enable()
tab.Page.navigate(url="https://aitestkitchen.withgoogle.com/tools/music-fx", _timeout=5)
tab.wait(5)

js_code = """
function simulateKeystroke(element, keyCode, key) {
    var events = ['keydown', 'keyup'];
    events.forEach(function(eventName) {
        var event = new KeyboardEvent(eventName, {
            key: key,
            keyCode: keyCode,
            charCode: keyCode,
            which: keyCode,
            shiftKey: false,
            ctrlKey: false,
            metaKey: false
        });
        element.dispatchEvent(event);
    });
}

var textBox = document.querySelector('div[role="textbox"][contenteditable="true"]');
if (textBox) {
    var text = "Example";
    for (var i = 0; i < text.length; i++) {
        simulateKeystroke(textBox, text.charCodeAt(i), text[i]);
    }
}
"""

tab.Runtime.evaluate(expression=js_code)
tab.stop()
