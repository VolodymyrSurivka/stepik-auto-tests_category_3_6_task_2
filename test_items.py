import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element_by_css_selector("button.btn-add-to-basket").click()
    assert len(str(add_to_basket_button)) > 0, "The \"Add to the basket\" button isn't on this page"
    time.sleep(3)
