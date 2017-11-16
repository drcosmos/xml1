from lxml import etree

# Create the root element
page = etree.Element('results')

# Make a new document tree
doc = etree.ElementTree(page)

# Add the subelements
pageElement = etree.SubElement(page, 'Country', 
                                      name='Germany',
                                      Code='DE',
                                      Storage='Basic')
# For multiple multiple attributes, use as shown above

# Save to XML file
outFile = open('output.xml', 'wb')
doc.write(outFile, xml_declaration=True, encoding='utf-8')
