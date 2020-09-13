import time


def test_guest_should_see_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert browser.find_element_by_css_selector(
        "button.btn-add-to-basket"), "The \"Add to the basket\" button isn't on this page"
    browser.find_element_by_css_selector("button.btn-add-to-basket").click()
    time.sleep(3)
