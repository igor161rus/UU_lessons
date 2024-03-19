import xml.etree.ElementTree as ET

developers_cv = ET.parse('demo.xml')
root_of_cv = developers_cv.getroot()
print(root_of_cv.tag, root_of_cv.text)
print(root_of_cv[0].tag, root_of_cv[0].text)

skills = []
for skill in root_of_cv[3]:
    skills.append(skill.attrib['name'])
print(skills)
