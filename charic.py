#캐릭터 클래스 생성
class Ark():

    damage = []
    try:
        with open('Ark_damage.ini', 'r', encoding='utf-8') as f: #아크 데미지 설정 파일 열기
            for line in f:
                line = line.strip() # 공백 제거 strip()함수로 line 변수에 들어가는 값 '1차 스킬 = 300'
                if '=' in line: #만약에 불러온 파일 문자열에 '='이 있으면 해당 조건문 실행
                    # line = '1차 스킬 = 500'
                    num = line.split('=') #split 함수는 안에 인자를 기준으로 나눠서 리스트을 만듦
                    #num = 리스트다 num = ['1차스킬 ', ' 500']
                    num2 = num[1].strip() #공백 제거 strip()함수로 num2 = '300'
                    if num2.isdigit(): #isdigit 숫자만 고르는 함수
                        damage.append(int(num2)) #damage에 num2가 정수형으로 형변환 되어 추가

    except: #만약에 파일이 없어서 실행이 안될 때 예외처리
        skill = [('1차 스킬', 300), ('2차 스킬', 400), ('3차 스킬', 500)] # 디폴트로 들어가는 데미지 값
        with open('Ark_damage.ini','w', encoding='utf-8') as f: #해당 설정 파일 만드는 코드
            for skill, damage in skill: # skill = '1차스킬' , damage = 300 파이썬 고급 문법 
                f.write(f'{skill} = {damage}\n') #'Ark_damage.ini'에 1차 스킬 = 300 저장
            
        damage = [300, 400, 500]
        


    def _1st_skill(self):
        print('1차스킬')
        for _ in range(2):
            print(f'데미지 : {self.damage[0]}')
            print(f'{_ + 1}타')

    def _2nd_skill(self): #인터페이스 동일하게
        print('2차스킬')
        for _ in range(3):
            print(f'데미지 : {self.damage[1]}')
            print(f'{_ + 1}타')

    def _3rd_skill(self):
        print('3차스킬')
        for _ in range(4):
            print(f'데미지 : {self.damage[2]}')
            print(f'{_ + 1}타')

class PastFinder():

    damage = []
    try:
        with open('PastFinder_damage.ini', 'r', encoding='utf-8') as f: #아크 데미지 설정 파일 열기
            for line in f:
                line = line.strip() # 공백 제거 strip()함수로 line 변수에 들어가는 값 '1차 스킬 = 300'
                if '=' in line:
                    num = line.split('=') #split 함수는 안에 인자를 기준으로 나눠서 리스트을 만듦
                    #num = 리스트다 num = ['1차스킬 ', ' 300']
                    num2 = num[1].strip() #공백 제거 strip()함수로 num2 = '300'
                    if num2.isdigit(): #isdigit 숫자만 고르는 함수
                        damage.append(int(num2)) #damage에 num2가 정수형으로 형변환 되어 추가

    except: #만약에 파일이 없어서 실행이 안될 때 예외처리
        skill = [('1차 스킬', 300), ('2차 스킬', 400), ('3차 스킬', 500)] # 디폴트로 들어가는 데미지 값
        with open('PastFinder_damage.ini','w', encoding='utf-8') as f: #해당 설정 파일 만드는 코드
            for skill, damage in skill: # skill = '1차스킬' , damage = 300 파이썬 고급 문법 
                f.write(f'{skill} = {damage}\n') #'Ark_damage.ini'에 1차 스킬 = 300 저장
            
        damage = [300, 400, 500]

    def _1st_skill(self):
        print('1차스킬')
        for _ in range(2):
            print(f'데미지 : {self.damage[0]}')
            print(f'{_ + 1}타')

    def _2nd_skill(self):
        print('2차스킬')
        for _ in range(3):
            print(f'데미지 : {self.damage[1]}')
            print(f'{_ + 1}타')

    def _3rd_skill(self):
        print('3차스킬')
        for _ in range(4):
            print(f'데미지 : {self.damage[2]}')
            print(f'{_ + 1}타')
            
class DemonAvender():

    damage = []
    try:
        with open('DemonAvender_damage.ini', 'r', encoding='utf-8') as f: #아크 데미지 설정 파일 열기
            for line in f:
                line = line.strip() # 공백 제거 strip()함수로 line 변수에 들어가는 값 '1차 스킬 = 300'
                if '=' in line:
                    num = line.split('=') #split 함수는 안에 인자를 기준으로 나눠서 리스트을 만듦
                    #num = 리스트다 num = ['1차스킬 ', ' 300']
                    num2 = num[1].strip() #공백 제거 strip()함수로 num2 = '300'
                    if num2.isdigit(): #isdigit 숫자만 고르는 함수
                        damage.append(int(num2)) #damage에 num2가 정수형으로 형변환 되어 추가

    except: #만약에 파일이 없어서 실행이 안될 때 예외처리
        skill = [('1차 스킬', 300), ('2차 스킬', 400), ('3차 스킬', 500)] # 디폴트로 들어가는 데미지 값
        with open('DemonAvender_damage.ini','w', encoding='utf-8') as f: #해당 설정 파일 만드는 코드
            for skill, damage in skill: # skill = '1차스킬' , damage = 300 파이썬 고급 문법 
                f.write(f'{skill} = {damage}\n') #'Ark_damage.ini'에 1차 스킬 = 300 저장
            
        damage = [300, 400, 500]

    def _1st_skill(self):
        print('1차스킬')
        for _ in range(2):
            print(f'데미지 : {self.damage[0]}')
            print(f'{_ + 1}타')

    def _2nd_skill(self):
        print('2차스킬')
        for _ in range(3):
            print(f'데미지 : {self.damage[1]}')
            print(f'{_ + 1}타')

    def _3rd_skill(self):
        print('3차스킬')
        for _ in range(4):
            print(f'데미지 : {self.damage[2]}')
            print(f'{_ + 1}타')


class Lala():

    damage = []
    try:
        with open('Lala_damage.ini', 'r', encoding='utf-8') as f: #아크 데미지 설정 파일 열기
            for line in f:
                line = line.strip() # 공백 제거 strip()함수로 line 변수에 들어가는 값 '1차 스킬 = 300'
                if '=' in line:
                    num = line.split('=') #split 함수는 안에 인자를 기준으로 나눠서 리스트을 만듦
                    #num = 리스트다 num = ['1차스킬 ', ' 300']
                    num2 = num[1].strip() #공백 제거 strip()함수로 num2 = '300'
                    if num2.isdigit(): #isdigit 숫자만 고르는 함수
                        damage.append(int(num2)) #damage에 num2가 정수형으로 형변환 되어 추가

    except: #만약에 파일이 없어서 실행이 안될 때 예외처리
        skill = [('1차 스킬', 300), ('2차 스킬', 400), ('3차 스킬', 500)] # 디폴트로 들어가는 데미지 값
        with open('Lala_damage.ini','w', encoding='utf-8') as f: #해당 설정 파일 만드는 코드
            for skill, damage in skill: # skill = '1차스킬' , damage = 300 파이썬 고급 문법 
                f.write(f'{skill} = {damage}\n') #'Ark_damage.ini'에 1차 스킬 = 300 저장
            
        damage = [300, 400, 500]

    def _1st_skill(self):
        print('1차스킬')
        for _ in range(2):
            print(f'데미지 : {self.damage[0]}')
            print(f'{_ + 1}타')

    def _2nd_skill(self):
        print('2차스킬')
        for _ in range(3):
            print(f'데미지 : {self.damage[1]}')
            print(f'{_ + 1}타')

    def _3rd_skill(self):
        print('3차스킬')
        for _ in range(4):
            print(f'데미지 : {self.damage[2]}')
            print(f'{_ + 1}타')


class Hoyoung():

    damage = []
    try:
        with open('Hoyoung_damage.ini', 'r', encoding='utf-8') as f: #아크 데미지 설정 파일 열기
            for line in f:
                line = line.strip() # 공백 제거 strip()함수로 line 변수에 들어가는 값 '1차스킬=300'
                if '=' in line:#
                    num = line.split('=') #split 함수는 안에 인자를 기준으로 나눠서 리스트을 만듦
                    #num = 리스트다 num = ['1차스킬 ', ' 300']
                    num2 = num[1].strip() #공백 제거 strip()함수로 num2 = '300'
                    if num2.isdigit(): #isdigit 숫자만 고르는 함수
                        damage.append(int(num2)) #damage에 num2가 정수형으로 형변환 되어 추가

    except: #만약에 파일이 없어서 실행이 안될 때 예외처리
        skill = [('1차 스킬', 300), ('2차 스킬', 400), ('3차 스킬', 500)] # 디폴트로 들어가는 데미지 값
        with open('Hoyoung_damage.ini','w', encoding='utf-8') as f: #해당 설정 파일 만드는 코드
            for skill, damage in skill: # skill = '1차스킬' , damage = 300 파이썬 고급 문법 
                f.write(f'{skill} = {damage}\n') #'Ark_damage.ini'에 1차 스킬 = 300 저장
            
        damage = [300, 400, 500]

    def _1st_skill(self):
        print('1차스킬')
        for _ in range(2):
            print(f'데미지 : {self.damage[0]}')
            print(f'{_ + 1}타')

    def _2nd_skill(self):
        print('2차스킬')
        for _ in range(3):
            print(f'데미지 : {self.damage[1]}')
            print(f'{_ + 1}타')

    def _3rd_skill(self):
        print('3차스킬')
        for _ in range(4):
            print(f'데미지 : {self.damage[2]}')
            print(f'{_ + 1}타')


class Hero(): #005

    damage = []
    try:
        with open('Hero_damage.ini', 'r', encoding='utf-8') as f: #아크 데미지 설정 파일 열기
            for line in f:
                line = line.strip() # 공백 제거 strip()함수로 line 변수에 들어가는 값 '1차 스킬 = 300'
                if '=' in line:
                    num = line.split('=') #split 함수는 안에 인자를 기준으로 나눠서 리스트을 만듦
                    #num = 리스트다 num = ['1차스킬 ', ' 300']
                    num2 = num[1].strip() #공백 제거 strip()함수로 num2 = '300'
                    if num2.isdigit(): #isdigit 숫자만 고르는 함수
                        damage.append(int(num2)) #damage에 num2가 정수형으로 형변환 되어 추가

    except: #만약에 파일이 없어서 실행이 안될 때 예외처리
        skill = [('1차 스킬', 300), ('2차 스킬', 400), ('3차 스킬', 500)] # 디폴트로 들어가는 데미지 값
        with open('Hero_damage.ini','w', encoding='utf-8') as f: #해당 설정 파일 만드는 코드
            for skill, damage in skill: # skill = '1차스킬' , damage = 300 파이썬 고급 문법 
                f.write(f'{skill} = {damage}\n') #'Ark_damage.ini'에 1차 스킬 = 300 저장
            
        damage = [300, 400, 500]
        


    def _1st_skill(self):
        print('1차스킬')
        for _ in range(2):
            print(f'데미지 : {self.damage[0]}')
            print(f'{_ + 1}타')

    def _2nd_skill(self):
        print('2차스킬')
        for _ in range(3):
            print(f'데미지 : {self.damage[1]}')
            print(f'{_ + 1}타')

    def _3rd_skill(self):
        print('3차스킬')
        for _ in range(4):
            print(f'데미지 : {self.damage[2]}')
            print(f'{_ + 1}타')