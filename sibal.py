class Comic(Fantasy, Sport, Romance, Music):
    _genres =["판타지", "스포츠", "로맨스", "음악"] #0 : 판타지, 1 : 스포츠, 2 : 로맨스, 3 : 음악
    _fantasies = ["슈타인즈 게이트", "종말의 세라프", "이능배틀은 일상계 속에서", "헌터X헌터"]
    _sport = ["츠루네", "용왕이 하는 일!!", "쿠로가네", "치하야후루"]
    _romance = ["너에게 닿기를", "옆자리 괴물군", "마사무네군의 리벤지", "쓰레기의 본망"]
    _music = ["Op8", "온 에어!", "히프노시스 마이크", "B-project"]

    def __init__(self):
        self.genre = genre

    def __str__(self):
        return "장르 목록을 보세요"+self.name

    def set_genre(self):
        self.genre = input("원하는 장르를 선택하세요 (0 : 판타지, 1 : 스포츠, 2 : 로맨스, 3 : 음악")

        if self.genre == 0:
            self.fantasies

        if self.genre == 1:
            self.sport

        if self.genre == 2:
            self.romance

        if self.genre == 3:
            self.music
    
    def set_fantasies(self):
        self.fantasies = input("판타지 장르를 선택하였습니다. 알고 싶은 애니나 만화를 고르세요(0: 슈타인즈 게이트, 1: 종말의 세라프, 2: 이능배틀은 일상계 속에서, 3: 헌터X헌터)")
        
        if self.fantasies == 1:
            self.fantasies
        
        if self.fantasies == 2:

        else:
            self.ice = int(self.ice)

    def 

    def show(self):
        self.set_genre

class Show:
    _genres = [fantasies("판타지"), sport("스포츠"), romance("로맨스"), music("음악")]

    def __init__(self):
        self.show_genre = []
        self.show = None
    
    def show_genre(self):
        print("0 : 판타지, 1 : 스포츠, 2: 로맨스, 3: 음악")
