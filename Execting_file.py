# from bs4 import BeautifulSoup
#
# # Reading the data inside the xml
# # file to a variable under the name
# # data
# with open('G:/Scandat/sacndat_studio/BotBees/xml files/ashok.xml', 'r') as f:
#     data = f.read()
#
# # Passing the stored data inside
# # the beautifulsoup parser, storing
# # the returned object
# Bs_data = BeautifulSoup(data, "xml")
#
#
#
# for tag in Bs_data.find_all('path'):
#     tag['path'] = "G:/labelimg/gowtham stores/hrinka.jpg"
#
# print(Bs_data.prettify())
# Finding all instances of tag
# `unique`
# b_unique = Bs_data.find_all('path')
#
# print(b_unique)

# Using find() to extract attributes
# of the first instance of the tag
# b_name = Bs_data.find('child', {'name': 'Frank'})
#
# print(b_name)
#
# # Extracting the data stored in a
# # specific attribute of the
# # `child` tag
# value = b_name.get('test')
#
# print(value)

import xml.etree.ElementTree as ET

tree = ET.parse('G:/Scandat/sacndat_studio/BotBees/xml files/ashok.xml')
root = tree.getroot()

# changing a field text
for elem in root.iter('path'):
    elem.text = 'G:/Scandat/sacndat_studio/BotBees/xml files/ashok'

# # modifying an attribute
# for elem in root.iter('item'):
#     elem.set('path', 'newitem')
#
# # adding an attribute
# for elem in root.iter('item'):
#     elem.set('path2', 'newitem2')

tree.write('G:/Scandat/sacndat_studio/BotBees/xml files/ashok.xml')