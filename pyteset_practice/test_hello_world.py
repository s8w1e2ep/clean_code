from hello_world import hello_world

def test_hello_world():
    text = hello_world()

    assert text == 'Hello World'