from html_del import html_del


def test_html1():
    assert html_del("<h1>Good</h1>") == "Good"


def test_html2():
    assert html_del("<div><p>Good</p></div>") == "Good"
