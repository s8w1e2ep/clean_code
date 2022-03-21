def test_get_page_hierarchy_as_xml():
    given_pages('PageOne', 'PageOne.ChildOne', 'PageTwo')

    when_request_is_issued('root', 'type:pages')

    then_response_should_be_xml()

def test_get_page_hierarchy_has_right_tags():
    given_pages('PageOne', 'PageOne.ChildOne', 'PageTwo')

    when_request_is_issued('root', 'type:pages')

    then_response_should_be_contain(
        '<name>PageOne</name>', '<name>PageTwo</name>', '<name>ChildOne</name>'
    )