import requests
# import xml.etree.ElementTree as ET
import xmltodict
import json


API_KEY = "OMKNjnjBuscXdXExA0u2qK917H10qAA6"
url = "http://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_1.jsp"
# for i in range(1, 47):

params = {
    "authKey": API_KEY,
    "returnType": 'XML',
    "outType": 1,
    "pageNum": 1,
    "pageSize": 100,
    "srchTraGbn": 2,
    "srchTraStDt": "20200101",
    "srchTraEndDt": "20200301",
    "srchTraProcessNm": "(주)휴넷",
    "srchTraOrganNm": "왕초보를 위한 영어회화 황금 레시피 2",
    "sort": "DESC",
    "sortCol": "TOT_FXNUM"
}

xml_data = requests.get(url, params).text
# print(xml_data)
# tree = ET.ElementTree(ET.fromstring(data))
# root = tree.getroot()
# res = root.find('srchList').findall('scn_list')

jsonString = json.dumps(xmltodict.parse(xml_data), indent=2)
# print(jsonString, "HERE!!!!")

json_data = json.loads(jsonString)

print(json_data["HRDNet"]["srchList"]["scn_list"][0])

# for course in res:
#     title = course.find('title').text
#     subtitle = course.find('subTitle').text
#     print(title, subtitle, sep='|')
        #DB 저장?