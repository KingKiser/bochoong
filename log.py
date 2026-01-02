from datetime import datetime, date #002

#001 
class log_record(): #로그를 저장하는 함수를 모은 클래스

    def log_record(i): #함수에서 변수를 받을 수 있게 지정
        today = date.today()
        current_time = datetime.now().strftime("%H:%m:%S") #002 current_time 변수는 현재 시간을 저장하는 변수
        with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
            f.write(f'\n {today}:{current_time}') #002 이터레이터
            f.write(f'\n 입력값 {i}')  #이터레이터


    def log_record_where(x, y):
        today = date.today()
        current_time = datetime.now().strftime("%H:%m:%S") #002
        with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
            f.write(f'\n {today}:{current_time}') #002
            f.write(f'\n 좌표x {x}, y좌표{y}')

    def log_maso(a): #인자를 받음  a변수에
        today = date.today()
        current_time = datetime.now().strftime("%H:%m:%S") #현재 시간 변수에 저장
        with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
            f.write(f'\n {today}:{current_time}') #002 
            f.write(f'\n 메소값 : {a}')
#001