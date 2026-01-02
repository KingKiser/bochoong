import pymysql


class maso():

    def maso_load():
    # 1. MySQL 데이터베이스에 연결하기
        db = pymysql.connect(
            host="localhost",   # MySQL 서버 호스트
            user="root",         # MySQL 사용자명
            password="your_password",  # MySQL 비밀번호각각 고유 패스워드로 할 것
            database="maple",    # 사용할 데이터베이스 이름
            charset="utf8mb4",   # 문자 인코딩 설정 (필요시)
            cursorclass=pymysql.cursors.DictCursor  # 결과를 딕셔너리 형태로 반환
        )

        # 2. 커서 객체 생성
        cursor = db.cursor() #여기에 쿼리 입력하면 디비로 쿼리 입력 여기서 디비 통제

        # 3. 특정 유저명의 메소를 가져오는 쿼리
        user_name = 'player1'  # 조회할 유저명
        query = "SELECT 메소 FROM users WHERE 유저명 = %s" #%s 자리에 user_name 이 들어감 
        #SELECT 메소 FROM users WHERE 유저명 = player1

        # 4. 쿼리 실행 및 데이터 가져오기
        cursor.execute(query, (user_name,))
        #cursor.execute('SELECT 메소 FROM users WHERE 유저명 = player1') 쿼리는 문자형 이렇게도 쓸 수 있음
        result = cursor.fetchone()  # 한 개의 결과만 가져옴 result 딕셔너리 result = {'메소': 10000}

        # 6. 연결 종료
        cursor.close()
        db.close()

        return result  #{'메소': 10000} 이걸 반환
    
    def maso_save(a): #변수 a에 새로 저장할 메소값 넣음
# 1. MySQL 데이터베이스에 연결하기
        db = pymysql.connect(
            host="localhost",   # MySQL 서버 호스트
            user="root",         # MySQL 사용자명
            password="your_password",  # MySQL 비밀번호
            database="maple",    # 사용할 데이터베이스 이름
            charset="utf8mb4",   # 문자 인코딩 설정
            cursorclass=pymysql.cursors.DictCursor  # 결과를 딕셔너리 형태로 반환
        )

        # 2. 커서 객체 생성
        cursor = db.cursor()

        # 3. 메소 업데이트 쿼리
        user_name = 'player1'   # 메소를 수정할 유저명
        new_mesos = a       # 새롭게 저장할 메소 값

        query = "UPDATE users SET 메소 = %s WHERE 유저명 = %s" 
        # query = "UPDATE users SET 메소 = 수정된 메소 WHERE 유저명 = %player1" 

        try:
            # 4. 쿼리 실행
            cursor.execute(query, (new_mesos, user_name))
           # cursor.execute("UPDATE users SET 메소 = 수정된 메소 WHERE 유저명 = %player1")
            # 5. 변경 사항 저장 (Commit)
            db.commit()

        except Exception as e:
            # 오류 발생 시 롤백
            db.rollback()

        # 6. 연결 종료
        cursor.close()
        db.close()

