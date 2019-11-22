# 파일처리 프로그램

class FestList: # 파일 처리를 해 주는 클래스
    def __init__(self, name): # 파일 처리 함수
        self.name = name # 사용자로부터 이름을 받아 저장하고 불러온다.

    def listMake(self, mylist): # 리스트(자신이 관심있는 축제 리스트) 생성하는 함수
        makefile = open("C:\\Users\\GRAM\\Desktop\\내리스트.txt", 'w') # 어디에 리스트를 생성할 지 경로 설정
        makefile.write("======"+self.name +"의 꽃축제 리스트~!======\n") # 리스트 생성 시 제목
        cnt = 1
        for i in mylist: # 리스트 카운트
            makefile.write(str(cnt)+"번째 축제 : "+i)
            makefile.write("\n")
            cnt += 1
        makefile.close()