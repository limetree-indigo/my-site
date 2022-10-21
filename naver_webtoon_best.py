import requests
from bs4 import BeautifulSoup


def get_best_challenge50(_url: str) -> list:
    top50 = []
    for page in range(1, 4):
        url = _url + "&page=" + str(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        webtoons = soup.select(".challengeList td>.challengeInfo")
        titles = [w.select_one(".challengeTitle") for w in webtoons]
        titles = [t.text.replace('\n', '') for t in titles]
        titles = [t.strip() for t in titles]

        scores = [w.select_one('.rating_type>strong') for w in webtoons]
        scores = [float(s.text) for s in scores]

        images = soup.select(".challengeList td>.fl img")
        images = [img['src'] for img in images]

        info = list(zip(images, titles, scores))
        top50 += info

    return top50[:50]


if __name__ == "__main__":
    view_count_url = "https://comic.naver.com/genre/bestChallenge?m=main&order=ViewCount"
    star_score_url = "https://comic.naver.com/genre/bestChallenge?m=main&order=StarScore"

    view_count50 = get_best_challenge50(view_count_url)
    star_score50 = get_best_challenge50(star_score_url)

    view_count50_order_score = sorted(view_count50, key=lambda x: x[1], reverse=True)
    print('-도전베스트 조회순50')
    print(view_count50)

    print('-도전베스트 조회순50 별점순 정렬')
    print(view_count50_order_score)

    print('-도전베스트 별점순50')
    print(star_score50)

    view_score_50 = set(view_count50) & set(star_score50)
    print('-조회순50, 별점순50 모두 포함')
    print(view_score_50)

    view_score_50 = [(w, view_count50.index(w)+1, star_score50.index(w)+1) for w in view_score_50]
    view_score_50.sort(key=lambda x: x[1])
    print('-조회순50, 별점순 50 모두 포함, 조회순 정렬')
    print(view_score_50)

    view_score_title = ['웹툰', '조회순위', '별점순위']
    view_score_50 = [{k: v for k, v in zip(view_score_title, w)} for w in view_score_50]
    print('-조회순50, 별점순 50 모두 포함, 조회순 정렬, 딕셔너리')
    print(view_score_50)