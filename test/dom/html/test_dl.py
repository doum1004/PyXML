from util import testAttribute
from util import testIntAttribute

def test():
    print 'testing source code syntax'
    from xml.dom.html import HTMLDListElement
    from xml.dom import implementation
    doc = implementation.createHTMLDocument('Title')
    d = doc.createElement('DL')

    print 'testing get and set'
    testIntAttribute(d,'compact')
    print 'get/set works'


if __name__ == '__main__':

    test();
