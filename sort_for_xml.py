import io
from xml.etree import ElementTree as ET
from xml.dom import minidom
from xml.dom.minidom import parseString

xml = open('files/newsafr.xml', 'r', encoding='utf-8-sig') 
xml_data = xml.read()
xml.close()
dom = parseString(xml_data)
channel_description = dom.getElementsByTagName('description')
length = len(dom.getElementsByTagName('description')) # получение количества вхождений

with io.open('files/newsafr.xml', 'r', encoding='utf-8-sig') as xml:
    xml_content = minidom.parse(xml)
xml_content.normalize()

i = 1
content_list = list()
while i < length:
    description_content = str()
    channel_description = xml_content.getElementsByTagName('description')[i]
    splitted_content = channel_description.childNodes[0].nodeValue.split(' ')
    content_list.append(splitted_content)
    i += 1

k = 1
while k < len(content_list):
    content_list[0] += content_list[k]  
    k += 1
content_list_1 = content_list[0]


k = 0
list_4 = list()

while k < len(content_list_1): #отбор слов длиной от 6-и символов
    if len(content_list_1[k]) >= 6:
        list_4.append(content_list_1[k].replace("'", "").lower())
    k += 1

list_4.sort()

k = 1
words_dict = {}
while k < len(list_4): #подсчет кол-ва вхождений слов
    words_dict.update({list_4[k]: ''})
    count = 1
    while k < len(list_4):
        if list_4[k - 1] == list_4[k]:
            count += 1
            words_dict.update({list_4[k]: count})
        else:
            count = 1
            words_dict.update({list_4[k]: count})
        k += 1

smth = list(words_dict.items())
smth_1 = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))

i = 0
while i <= 9:
    print('На {} месте - слово \'{}\', оно встречается {} раз(а)'.format(i+1, smth_1[i][0], smth_1[i][1]))
    i += 1