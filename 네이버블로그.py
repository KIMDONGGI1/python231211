import requests 
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    # 검색어로 블로그 검색 페이지 URL 생성
    base_url = 'https://search.naver.com/search.naver'
    params = {'where': 'view', 'sm': 'tab_jum', 'query': search_keyword}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 블로그 검색 결과에서 각 블로그의 정보 추출
        blog_posts = soup.select('.sh_blog_title')

        for post in blog_posts:
            # 블로그명과 블로그 주소 추출
            blog_name = post.select_one('.txt84').get_text(strip=True)
            blog_url = post['href']

            # 포스트 제목 추출
            post_title = post['title']

            # 포스트 날짜 추출
            post_date = post.select_one('.txt_date').get_text(strip=True)

            # 결과 출력
            print(f'블로그명: {blog_name}')
            print(f'블로그주소: {blog_url}')
            print(f'제목: {post_title}')
            print(f'포스팅날짜: {post_date}')
            print('-' * 50)

    else:
        print(f'Error {response.status_code}')

# 검색어 입력
search_keyword = input('검색어를 입력하세요: ')

# 크롤링 실행
naver_blog_crawler(search_keyword)
