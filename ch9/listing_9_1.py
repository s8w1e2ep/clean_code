def test_get_page_hieratchy_as_xml():
	crawler.add_page(root, path_parser.parse('PageOne'))
	crawler.add_page(root, path_parser.parse('PageOne.ChildOne'))
	crawler.add_page(root, path_parser.parse('PageTwo'))

	request.set_resource('root')
	request.add_input('type', 'pages')
	responder = SerializedPageResponder()
	response = responder.make_response(FitNesseContext(root), request)
	xml = response.get_content()

	assert 'text/xml' == response.get_content_type()
	assert '<name>PageOne</name>' in xml
	assert '<name>PageTwo</name>' in xml
	assert '<name>ChildOne</name>' in xml

def test_get_page_hieratchy_as_xml_does_not_contain_symbolic_links():
	wiki_page_one = crawler.add_page(root, path_parser.parse('PageOne'))
	crawler.add_page(root, path_parser.parse('PageOne.ChildOne'))
	crawler.add_page(root, path_parser.parse('PageTwo'))
	
	page_data = wiki_page_one.get_data()
	properties = data.get_properties()
	sym_links = properties.set(SymbolicPage.PROPERTY_NAME)
	sym_links.set('SymPage', 'PageTwo')
	wiki_page_one.commit(data)

	request.set_resource('root')
	request.add_input('type', 'pages')
	responder = SerializedPageResponder()
	response = responder.make_response(FitNesseContext(root), request)
	xml = response.get_content()

	assert 'text/xml' == response.get_content_type()
	assert '<name>PageOne</name>' in xml
	assert '<name>PageTwo</name>' in xml
	assert '<name>ChildOne</name>' in xml
	assert 'SymPage' not in xml

def test_get_data_as_html():
	crawler.add_page(root, path_parser.parse('TestPageOne'), 'test page')

	request.set_resource('TestPageOne')
	request.add_input('type', 'pages')
	responder = SerializedPageResponder()
	response = responder.make_response(FitNesseContext(root), request)
	xml = response.get_content()

	assert 'text/xml' == response.get_content_type()
	assert 'test page' in xml
	assert '<Test' in xml