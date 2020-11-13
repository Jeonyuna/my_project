import requests
# import xml.etree.ElementTree as ET
import xmltodict
import json


API_KEY = "OMKNjnjBuscXdXExA0u2qK917H10qAA6"

url_dict = {
    'gubun1': 'http://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_1.jsp',
    'gubun2': 'http://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA61/HRDPOA61_1.jsp',
    'gubun3': 'http://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA62/HRDPOA62_1.jsp'
}

# course & academy & classify are optional
def get_data_from_api(target, start_date, end_date, course=None, classify=None, academy=None):
    params = {
        "authKey": API_KEY,
        "returnType": 'XML',
        "outType": 1,
        "pageNum": 1,
        "pageSize": 100,
        "srchTraGbn": classify,
        "srchTraStDt": start_date,
        "srchTraEndDt": end_date,
        "srchTraProcessNm": course,
        "srchTraOrganNm": academy,
        "sort": "DESC",
        "sortCol": "TOT_FXNUM"
    }

    xml_data = requests.get(url_dict[target], params).text

    jsonString = json.dumps(xmltodict.parse(xml_data), indent=2)

    json_data = json.loads(jsonString)
    print(json_data)
    return json_data["HRDNet"]["srchList"]["scn_list"]


# result = get_data_from_api('20201101', '20201109')
# for course in result:
#
#     sub_title = course['subTitle']#학원이름
#     title = course['title']#수업이름
#     man_count = int(course['regCourseMan'])#수강인원
#     fee = course['realMan']#수강비
#
#     if fee is None:
#         fee = 0
#     else:
#         fee = int(fee)
#
#     sales = man_count * fee
#
#     print(title, sub_title, man_count, fee, sales)

# for course in res:
#     title = course.find('title').text
#     subtitle = course.find('subTitle').text
#     print(title, subtitle, sep='|')
        #DB 저장?