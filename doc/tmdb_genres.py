import requests
import json

# 22.11.06 최신욱 추가.
# TMDB API 장르 데이터를 json 형태로 변환.

TMDB_API_KEY = 'API KEY'
new_list = []
request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-kr"
res = requests.get(request_url)
genres = res.json()

for genre in genres['genres']:
    fields = {
        'name' : genre['name'],

    }
    data = {
        'model' : 'movies.genre',
        'pk' : genre['id'],
        'fields': fields
            }

    new_list.append(data)

with open('./movies/fixtures/genre.json', 'w' , encoding="utf-8")as w:
    json.dump(new_list, w , ensure_ascii=False , indent=4)


