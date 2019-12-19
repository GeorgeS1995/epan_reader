from lxml import etree


def request_parser(request):
    root = etree.fromstring(request)
    output_d = {}

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text
            output_d[elem.tag] = text
    return output_d


if __name__ == '__main__':
    with open("parser_test.xml", "rb") as f:
        xml = f.read()

    parse_result = request_parser(xml)

    for kv in parse_result.items():
        print(kv)
