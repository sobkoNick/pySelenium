import re

from model.user import User


def test_phones_on_home_page(app):
    contactFromHomePage = app.user_helper.get_user_list()[0]  # type: User
    contactFromEditPage = app.user_helper.get_contact_from_edit_page(0)  # type: User
    app.user_helper.go_to_home_page()
    assert contactFromEditPage.name == contactFromHomePage.name
    assert clear(contactFromHomePage.all_phones_from_home_page) == merge_phones_like_on_home_page(contactFromEditPage)


def test_phones_on_view_page(app):
    contactFromViewPage = app.user_helper.get_user_from_view_page(0)  # type: User
    app.user_helper.go_to_home_page()
    contactFromEditPage = app.user_helper.get_contact_from_edit_page(0)  # type: User
    app.user_helper.go_to_home_page()
    assert clear(contactFromEditPage.home_phone) == clear(contactFromViewPage.home_phone)
    assert clear(contactFromEditPage.mobile_phone) == clear(contactFromViewPage.mobile_phone)


def clear(s):
    return re.sub("[() +*/-]", "", s)

def merge_phones_like_on_home_page(contactFromEditPage):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contactFromEditPage.home_phone, contactFromEditPage.mobile_phone,
                                        contactFromEditPage.work_phone]))))
