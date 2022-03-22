link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.implicitly_wait(10)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button > 0, '!!!НЕ НАШЕЛ!!!'



 