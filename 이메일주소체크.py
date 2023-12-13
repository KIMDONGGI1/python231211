import re

# 이메일 주소를 체크하는 함수
def check_email(email):
    # 이메일 주소를 검사하기 위한 정규표현식 패턴
    # 1. ^: 문자열의 시작
    # 2. [a-zA-Z0-9_.+-]+: 알파벳 대소문자, 숫자, 특수문자(_ . + -) 중 하나 이상이 연속으로 올 수 있음
    # 3. @: @ 기호
    # 4. [a-zA-Z0-9-]+: 도메인 부분에서 알파벳 대소문자, 숫자, 하이픈(-) 중 하나 이상이 연속으로 올 수 있음
    # 5. \.: 도메인과 탑레벨 도메인(TLD)을 구분하는 점 (.)
    # 6. [a-zA-Z0-9-.]+: TLD 부분에서 알파벳 대소문자, 숫자, 하이픈(-), 점(.) 중 하나 이상이 연속으로 올 수 있음
    # 7. $: 문자열의 끝
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.search() 함수를 사용하여 주어진 패턴에 맞는지 확인
    if re.search(pattern, email):
        # 맞으면 True 반환
        return True
    else:
        # 아니면 False 반환
        return False

# 샘플 이메일 주소 10개
sample_emails = [
    'user@example.com',
    'user123@gmail.com',
    'john_doe123@yahoo.co.kr',
    'jane_doe@company.org',
    'test.email@email.co.uk',
    'invalid_email@missing_tld',
    'no_at_sign.com',
    'user@.invalid_tld',
    '@missing_username.com',
    'user@in.valid@double_at_sign.com'
]

# 샘플 이메일 주소 검사 및 결과 출력
for email in sample_emails:
    if check_email(email):
        # 이메일이 올바른 경우 출력
        print(f'{email}은(는) 올바른 이메일 주소입니다.')
    else:
        # 이메일이 올바르지 않은 경우 출력
        print(f'{email}은(는) 올바르지 않은 이메일 주소입니다.')
