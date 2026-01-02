#006
#import json # 파이썬의 자료구조 자료형을 그대로 저장 불러올 수 있다
#처음 배울 때 변수, 자료형을 배운 이유
#형변환 안함
import random #랜덤 숫자 넣는 모듈
from masoload import maso

#maso = {'메소' : 10000 ,  }

#with open('maso.json', 'w', encoding= 'utf-8') as j:
#    json.dump(maso, j, ensure_ascii=False ) #ancii 코드 무력화 추가

class changsub(): #모듈에 포함된 클래스
    def hunt(): 
        maso_dic = maso.maso_load() #{'메소': 10000}
        maso_ = maso_dic['메소'] + 1000 #11000
        maso.maso_save(maso_) 

        #사냥하면 메소가 벌림
 #       with open('maso.json', 'r', encoding= 'utf-8') as file: #메소 불러옴
  #          maso = json.load(file) #maso 변수에 {'메소': 1000}
   #         maso['메소'] += 1000 #메소가 벌림 프로그램을 껐다 켜도 메소가 저장 불러올 수 있음 #maso 변수에 {'메소': 2000}
#
 #       with open('maso.json', 'w', encoding= 'utf-8') as file: #메소 저장
  #          json.dump(maso, file, ensure_ascii=False) #maso.json에 바뀐 maso 변수에 {'메소': 2000}저장




    def starforce(): #아이템 강화 함수
      #  with open('maso.json', 'r', encoding= 'utf-8') as file: #메소 불러옴
       #     maso = json.load(file) #불러온 메소를 변수에 저장 연산을 하기 위해서 #maso 변수에 {'메소': 1000}
        maso_dic = maso.maso_load() #{'메소': 10000}



        if maso_dic['메소'] <3000: #{'메소': 2000}
            print('메소가 부족합니다')

        elif maso_dic['메소'] >=3000:
            maso_dic['메소'] -= 3000
            rs = random.randint(1,101) #rs란 변수에 1부터 100까지 숫자가 랜덤하게 들어감
            if rs <=30:
                print({rs})
                print('강화성공')
            else:
                print({rs})
                print('강화 실패')
                if rs > 95:
                    print('파괴')

        maso.maso_save(maso_dic['메소'])            
        
        #with open('maso.json', 'w', encoding= 'utf-8') as file: #메소 저장
         #   json.dump(maso, file, ensure_ascii=False)
