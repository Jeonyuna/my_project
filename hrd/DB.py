from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

API_KEY = "OMKNjnjBuscXdXExA0u2qK917H10qAA6"
url = "http://www.hrd.go.kr/jsp/HRDP/HRDPO00/HRDPOA60/HRDPOA60_1.jsp"
for i in range(1, 47):
    params = {
        "authKey": API_KEY,
        "returnType": 'XML',
        "outType": 1,
        "pageNum": 1,
        "pageSize": 100,
        "srchTraGbn": 2
        "srchTraStDt": "20200101",
        "srchTraEndDt": "20200301",
        "sort": "DESC",
        "sortCol": "TOT_FXNUM"
    }
data = requests.get(url, params).text
print(data)
tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
res = root.find('srchList').findall('scn_list')
for course in res:
    title = course.find('title').text
    subtitle = course.find('subTitle').text
    print(title, subtitle, sep='|')
