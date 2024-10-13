import xml.dom.minidom

def main():
    path = "E:\python nang cao\Chuong 2\employee.xml"
    doc=xml.dom.minidom.parse("employee.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
if __name__=="__main":
    main() 