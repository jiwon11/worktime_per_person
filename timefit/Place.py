# Place 매소드
# 구글 지도 API를 활용한 지명 주소와 위/경도 주소 변환을 통해 사용자 위치의 위도 경도를 찾는다.
# 1. 사용자의 이름을 생성하고(클래스 생성)
# 2. 정의된 이름에 input()을 통해 지명주소를 추가
# 3. 추가된 지명주소를 위도/경도로 변경
# 4. 변경된 것을 파일에 저장
import requests
key = "AIzaSyCdaar3mN1gVmFUCxq9bPuQ9QsZ8D55DME"
url = 'https://maps.googleapis.com/maps/api/geocode/json'

class Place:
    def __init__(self, place_name, location):
        self.place_name = place_name
        self.location = location

    def print_info(self):
        print("Place_Name : ", self.place_name)
        print("Location : ", self.location)


def geocoder():
	adress = str(input("주소를 입력해주세요 : "))
	params = {'sensor': 'false', 'address': adress}
	r = requests.get(url, params=params)
	results = r.json()['results']
	location = results[0]['geometry']['location']
	print(location['lat'], location['lng'])
	place_name=str(input("지명주소를 입력하세요 : "))
	place = Place(place_name,location)
	print(place.print_info())
#위/경도 객체로 지정
geocoder()