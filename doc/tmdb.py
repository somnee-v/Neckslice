import requests
import json

# 22.11.06 최신욱 추가.
# TMDB API 영화 데이터를 json 파일로 변환.

TMDB_API_KEY = 'API KEY'

tmdb_data = []

for number in range(1, 500):
    request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={number}"
    res = requests.get(request_url)
    movie_list = res.json()
    for movie in movie_list['results']:
        if movie.get('release_date', ''):
            movie_id = movie['id']
            url =f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR"
            movie_detail = requests.get(url).json()
            fields = {
                'title': movie['title'],
                'release_date': movie['release_date'],
                'vote_count': movie['vote_count'],
                'vote_average': movie['vote_average'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'genres': movie['genre_ids'],
                'runtime': movie_detail['runtime'],
                'original_title': movie['original_title'],
                'popularity':movie['popularity'],
                'adult':movie['adult'],
                'backdrop_path':movie['backdrop_path']
            }
            data = {
                "model": "movies.movie",
                "pk": movie['id'],
                "fields": fields
            }
            tmdb_data.append(data)


        break
with open("./movies/fixtures/movies.json", "w", encoding="utf-8") as w:
    json.dump(tmdb_data, w, ensure_ascii=False, indent=4)
