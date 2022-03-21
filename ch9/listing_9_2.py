# After refactor
def test_get_page_hierarchy_as_xml():
	make_pages('PageOne', 'PageOne.ChildOne', 'PageTwo')

	submit_request('root', 'type:pages')

    assert_response_is_xml()
    assert_response_contains(
        '<name>PageOne</name>', '<name>PageTwo</name>', '<name>ChildOne</name>'
    )

def test_symbolic_links_are_not_in_xml_page_hierarchy():
    wiki_page = make_page('PageOne')
    make_pages('PageOne.ChildOne', 'PageTwo')

    add_link_to(wiki_page, 'pageTwo', 'SymPage')

    submit_request('root', 'type:pages')

    assert_response_is_xml()
    assert_response_contains(
        '<name>PageOne</name>', '<name>PageTwo</name>', '<name>ChildOne</name>'
    )
    assert_response_does_not_contains('SymPage')

def test_get_data_as_xml():
    make_page_with_content('TestPageOne', 'test page')

    submit_request('root', 'type:pages')

    assert_response_is_xml()
    assert_response_contains('test page', '<Test')