import time


def test_guest_should_see_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    add_to_basket_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert add_to_basket_button, "The \"Add to the basket\" button isn't on this page"
    add_to_basket_button.click()
    time.sleep(3)
