from pprint import pprint
import requests
from get_time import get_base


def get_info():
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

    serviceKey = "/RiLDbQOrX1DYkcfCT5/LyQYEKJ3G4If9ktXL8/B8o3aCQfi/S6D0g+OFjWQD+dZa2ru1Iwbasb9TV+IlJU0wA=="

    base_date, base_time = get_base()

    # 대구광역시 남구, 중구, 수성구 일대
    params = {
        'serviceKey': serviceKey,
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'JSON',
        'base_date': base_date,
        'base_time': base_time,
        'nx': '89',
        'ny': '90'
    }

    res = requests.get(url=url, params=params)
    res = res.json()
    data = res['response']['body']['items']['item']

    _data = []

    for d in data:
        _data.append((d['category'], d['obsrValue']))

    _data = _data[:4]

    print(_data)

    code = {'PTY': '강수형태', 'REH': '습도', 'RN1': '1시간 강수량', 'T1H': '온도'}
    rain_info = ['없음', '비', '비/눈', '눈', '', '빗방울', '빗방울눈날림', '눈날림']

    weather_info = {}
    for c, v in _data:
        # if c == 'PTY':
        #     v = rain_info[int(v)]
        # else:
        #     v = float(v)
        try:
            v = rain_info[int(v)] if c == 'PTY' else float(v)
        except:
            return "데이터 준비 중입니다. 잠시 후 접속해주세요."

        weather_info[code[c]] = v
    return weather_info


if __name__ == "__main__":
    pprint(get_info())

