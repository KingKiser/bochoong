from masoload import maso
from charic import * #모듈 클래스 주입
from log import log_record #001 모듈 주입
from changsub import changsub
# import json


#코드가 넘 길어 모듈을 쓴다

#함수화
#함수를 실행할 때마다 게임 실행

#로그를 남기는 함수를 만든다


######001
#def log_record(i): #함수에서 변수를 받을 수 있게 지정
 #   with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
  #      f.write(f'\n 입력값 {i}')


#def log_record_where(x, y):
 #   with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
  #      f.write(f'\n 좌표x {x}, y좌표{y}') 
######001 해당 코드 모듈 분기

def choice(): 
    chric_tuple = ('아크', '패스파인더', '데몬어밴져', '라라', '호영', '히어로')  #튜플 자료구조 캐릭터 목록
    print(chric_tuple) #캐릭터 목록 출력
    print('캐릭터를 선택해주세요')
    t = input()
    if t == chric_tuple[0]: #if t == '아크':
        log_record.log_record(t) #004
        #with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
         #   f.write(f'\n 입력값 {t}')
        return Ark() #클래스 반환
    elif t == chric_tuple[1]:
        log_record.log_record(t) #004
        #with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
         #   f.write(f'\n 입력값 {t}')
        return  PastFinder()
    elif t == chric_tuple[2]:
        log_record.log_record(t) #004
        #with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
         #   f.write(f'\n 입력값 {t}')
        return DemonAvender()
    elif t == chric_tuple[3]:
        log_record.log_record(t) #004
        #with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
         #   f.write(f'\n 입력값 {t}')
        return Lala()
    elif t == chric_tuple[4]:
        log_record.log_record(t) #004
        #with open('log.txt', 'a', encoding = 'utf-8') as f: #로그 파일 생성 코드 인코딩 옵션 한글 안깨지게 설정
         #   f.write(f'\n 입력값 {t}')
        return Hoyoung()

    elif t == chric_tuple[5]: #005 히어로 추가
        log_record.log_record(t)
        return Hero() 
    else:
        print('잘못 입력했습니다')
        print('다시 입력해주세요')
        return None #잘못 입력시 아래 반복문 계속 반복하게 하기 위해서

#def maso_load(maso): #이 함수 재활용 할거임 메소json파일에 있는 메소값을 불러오는 함수
 #   try:
  #      with open('maso.json', 'r', encoding= 'utf-8') as file: #메소 불러옴
   #         maso = json.load(file)
    #    return maso
    #except : #메소 파일이 없을 경우 새로 생성하고 메소는 0으로 리셋한다 #예외처리 수정
     #   maso_dic = {'메소' : 0}
      #  with open('maso.json', 'w', encoding= 'utf-8') as file:
        #    json.dump(maso_dic, file, ensure_ascii=False)
       # return maso_dic

def game(a):
    #maso_ =  #메소 디폴트 0
    #maso_load(maso) #함수 삽입 이유는 maso.json 파일이 없을 때 미리 파일을 만들어야 아래있는 함수가 정상적으로 구동되어서 007
    if a == 1234: #패스워드 개념으로 실행 
        print('게임실행')
    else:
        print('비밀번호 틀림')
        return
    charic = None #변수는 선언되었지만 값은 없는 상태 0하고 스페이스랑 다름 캐릭터 지정하는 변수
    
    #charic = choice() 제대로 입력할 때 까지 반복
    
    #charic 모듈에 있는 거 가져와서 사용 가능

    while charic == None: #캐릭이 논이면 계속 반복
        charic = choice() #코루틴 캐릭터 고르는 함수 사용 잘못 입력시 논 


    x, y  = 0, 0   #지역변수 설정 게임이 실행되면 생기고 게임이 종료되면 없어지게
    while True: #while 문 안에 조건이 True이면 무한 반복
        i =input() #input  함수는 문자열입니다
    
        if i == '1' : #조건문도 문자열이어야 명령 대로 수행
            log_record.log_record(i) #001
            if x < 10:
                print('전진')
                x += 1  #증감 연산
            elif x == 10:
                print('더이상 앞으로 갈수 없습니다')
            log_record.log_record_where(x, y) #001
            
        elif i == '2'  :
            log_record.log_record(i) #001
            if x > 0:
                print('후진')
                x -= 1
            elif x == 0:
                print('더이상 뒤로 갈 수 없습니다')
            log_record.log_record_where(x, y) #001
        
        elif i == '3'  :
            log_record.log_record(i) #001
            if y < 10:
                print('점프')
                y += 1
            elif y == 10:
                print('더이상 점프 할 수 없습니다')
            log_record.log_record_where(x, y) #001
                
        elif i == '4' :
            log_record.log_record(i) #001
            if y > 0:
                print('하단점프')
                y -= 1
            elif y == 0:
                print('더이상 점프 할 수 없습니다')
            log_record.log_record_where(x, y) #001
          
        elif i == '5':
            log_record.log_record(i) #001
            print('공격')
            log_record.log_record_where(x, y) #001

        elif i == 'q':
            log_record.log_record(i) #001
            charic._1st_skill() #인터페이스 통일
            changsub.hunt()
            maso_dic = maso.maso_load() #딕션너리
            log_record.log_maso(maso_dic['메소'])
            print(maso_dic)
            #이쪽에 헌트 넣음
        elif i == 'w':
            log_record.log_record(i) #001
            charic._2nd_skill()
            changsub.hunt()
            maso_dic = maso.maso_load() #딕션너리
            log_record.log_maso(maso_dic['메소'])
            print(maso_dic)
            #이쪽에 헌트 넣음

        elif i == 'e':
            log_record.log_record(i) #001
            charic._3rd_skill() #인터페이스 동일하게
            changsub.hunt()
            maso_dic = maso.maso_load() #딕션너리
            log_record.log_maso(maso_dic['메소'])
            print(maso_dic)
            #이쪽에 헌트 넣음
        
        elif i == '0':
            log_record.log_record(i) #001
            print('게임종료')
            break
        elif i == 'r': #006 r을 입력하면 강화 실행
            #스타포스 돌림 
            log_record.log_record(i)  #입력키 로그 찍음
            changsub.starforce() # changsub 모듈의 changsub 클래스의 starforce 함수 실행
            maso_dic = maso.maso_load() #딕션너리  maso = {'메소': 99853000} 위에 정의해놓음
            log_record.log_maso(maso_dic['메소']) #유저가 메소를 얼마나 가지고 있는지 확인하는 로그
            print(maso_dic)
        else:
            log_record.log_record(i) #003 로그 추가 잘못 누른 키도 확인
            print('잘못 입력했습니다') #예외처리 try except을 안쓰고도 예외처리가 가능한 경우
    print('박승휘가 만듦')

game(1234) #메인으로 실행