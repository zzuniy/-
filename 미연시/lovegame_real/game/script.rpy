# # 게임에서 사용할 캐릭터를 정의합니다.
# #요게 실행 파일
# define npc = Character('엔핑', color = "#1abc9c")
# define ex = Character(None, kind=nvl)

# define me = Character('나',color = "#c22626")
# define prof = Character('교수님',color = "#bcae1a")
# define a1 = Character('이하늘',color = "#f0a4ec")


# define rightChar = Position(xalign = 0.8, yalign = 0.35)
# default fairy_clicked = False #사용자가 요정을 클릭했는가?

# image kd1 = "background/왕실1.jpg"
# image kd2 = "background/왕실2.jpg"
# image kd3 = "background/왕실3.jpg"
# image lb1 = "background/연구소.jpeg"

# image prof1 = Transform("character/char1.png", zoom=0.8)
# image ai1 = Transform("character/char2.png", zoom=1.5)
# image ai2 = Transform("character/char3.png", zoom=1.5)
# image ai3 = Transform("character/char4.png", zoom=1.5)

# image np1 = Transform("character/char5.png", zoom=0.3)
# image np2 = Transform("character/char6.png", zoom=0.3)

# screen fairy_info(): #요정 클릭시 보여줄 화면
#     modal True
#     zorder 100
#     frame:
#         align (0.5, 0.5)
       
#         background "#ffffffcc"
#         padding (20, 20)
#         vbox:
#             spacing 20
#             text "✨ 생명과학 지식 ✨" size 40 color "#2c3e50"
#             text "[fairy_text]" size 22 color "#000000"
#             textbutton "닫기" action Hide("fairy_info")

# screen fairy_icon(): #요정 아이콘 이미지 및 위치, 클릭시 변환
#     imagebutton:
#         idle Transform("character/char6.png", zoom=0.1)
#         hover Transform("character/char6.png", zoom=0.105)
#         xpos 0.1
#         ypos 0.01
#         action [SetVariable("fairy_clicked", True), Show("fairy_info")]


# # 카톡 UI 스타일 정의
# # PNG 없이 색깔로 대체
# style kakao_msg_left:
#     background "#ffffff"
#     padding (10, 5)
#     xanchor 0.0
  
# style kakao_msg_right:
#     background "#fee000" 
#     padding (10, 5)
#     xanchor 1.0
#     xpos 575
    
    

# # 카톡 화면
# screen messenger(messages):
#     frame:
#         align (0.5, 0.5)
#         background "#97bedf"
#         xsize 600
#         ysize 800
#         vbox:
#             spacing 10
#             for who, msg in messages:
#                 if who == "me":
#                     frame:
#                         style "kakao_msg_right" 
#                         text msg color "#000000"
#                 else:
#                     frame:
#                         style "kakao_msg_left" 
#                         text msg color "#000000"
                        
 

# # 여기에서부터 게임이 시작합니다.
# label start:
    
    
#     scene lb1

  


    
#     ex "2025년 9월 포항의 한 대학 연구실..엥"
#     ex "교수에게 매일 시달리던 대학원생이 있었으니.."
#     nvl clear

#     me "교수님! 그만 좀 하세요!!" with vpunch
#     me "이젠 곰팡이까지 빵에 발라 먹으라고 하시는건가요?"
#     me "교수님이 저번에 손톱에 곰팡이 발라보라고 하신 뒤로 손톱이 초록색으로 자라거든요!"

#     show prof1 at rightChar with dissolve
#     prof "홀홀 손톱이 초록색으로 변했다는건 자네가 삥뿅빵 나라의 외계인과 DNA과 어느정도 비슷..."

    
#     me "교수님!!" with vpunch
#     me "왜그러시는건가요"

#     show prof1 at rightChar with dissolve
#     prof "아 흠흠 그나저나 자네"
#     prof"내가 최근에 연구한 미생물 나라에 대해서 연구해 봤는가"


#     me"아니요? 솔직히 말이 되는 소리를 하세요.."

#     show prof1 at rightChar with dissolve
#     prof "그럼 지금 말이 되는 소리라고 생각하게 해주지"


#     ex "교수님은 그대로 나를 이상한 포탈로 집어넣으셨다"
#     ex"(이동중........)"

#     scene kd1
#     play music "audio/bgm/piano.mp3" fadein 5.0
#     me "으아아아아악!!!!!!" with vpunch
#     me "여..긴 어디지?"
#     me "교수님....제게 무슨짓을......."
#     me "(주위를 둘러본다)"

#     show np1 at rightChar with dissolve
#     npc "안녕?"
 

#     me "으아아악!!" with vpunch
#     me "ㄴ넌...누구야?"

#     show np1 at rightChar with dissolve
#     npc "나는 삥뿅이야!!"
#     npc "보아하니 네가 여기서 엄청 해맬 것 같아서 도와주러 왔지"
#     npc "여기가 어디냐면 바로 미생물 나라야"


#     me "미생물 나라? 말도안돼"

#     show np1 at rightChar with dissolve
#     npc "하하 처음엔 그럴 수 있지"
   

#     me "일단 알았어. 나는 뭘 하면 되는건데? 여긴 어떻게 나가는거야?"
#     hide np1 with dissolve
#     show np2 at rightChar with dissolve
#     npc "좋은 질문이네!"
#     npc "미생물 나라에는 미생물 소녀 즉, 미소녀들이 살고 있지!"
#     npc "그중 한 명과 러브라인을 만들어 사귀면 돼!"


#     me "뭐? 러브라인?" with vpunch
#     hide np2 with dissolve

#     show np1 at rightChar with dissolve
#     npc "뭐 그런 표정이야?"
#     npc "미소녀들 엄청 예쁘거든!" with vpunch
#     npc "축복으로 알아야지"


#     me "하...그거면 돼? 미(생물)소녀와의 연애?"

#     show np1 at rightChar with dissolve
#     npc "정답! 한 명과 연애를 성공하면 넌 자동으로 미생물의 세계를 빠져나올 수 있어"
#     npc "참고로 나는 npc같은 존재라서 미소녀들에겐 보이지 않아"
   
#     $ fairy_text = "곰팡이는 균사로 이루어진 다세포 생물로, 자연에서 유기물을 분해하는 중요한 역할을 합니다."

#     show screen fairy_icon #요정 듀토리얼
#     npc "왼쪽 상단에 요정 아이콘이 보이지?"
#     npc "저걸 클릭해봐!"

#     # 사용자가 클릭할 때까지 기다림
#     while not fairy_clicked:
#         $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

#     npc "좋아! 이제 다음 단계로 가자!"
#     npc "언제든 필요하면 부르라고!"


#     menu:
#         "잠깐!":
#             me "잠깐!"
#             npc "왜 불러?"
#             menu: 
#                 "아 아냐":
#                     npc "싱겁게 뭐야!"
#                 "아 잘못 부름":
#                     npc "뭐야!"
#             jump bye
#         "잘가!":
#             me "잘가!"
#             npc "너무 쉽게 보내주는거 아냐?"
#             jump bye

#     label bye:
#         npc "잠깐! 까먹을뻔 했다, 그 전에 카카오톡 기능을 알려줄게!"
#         $ chat = [("npc", "안녕? 나는 요정이야!"), 
#                 ("me", "반가워! 나는 ooo 이야ㅎㅎ"), 
#                 ("npc", "카카오톡 버전이라고!")]

#         show screen messenger(chat) #카카오톡 듀토리얼

#         "카카오톡으로 대화해봐!"

#         menu:
#             "답장하기":
#                 $ chat.append(("me", "우와 신기하네ㅎㅎ"))
#                 show screen messenger(chat)
#                 $ chat.append(("me", "여기로 대화하면 되는거지?"))
#                 show screen messenger(chat)
#                 $ chat.append(("npc", "응 맞아"))
#                 show screen messenger(chat)
#                 $ chat.append(("npc", "이제 어떻게 하는지 알겠지?"))
#                 show screen messenger(chat)
                
#                 "내가 메시지를 보냄!"
#             "무시하기":
#                 $ chat.append(("me", "읽씹 ㄱㄱ"))
#                 show screen messenger(chat)
#                 "메시지를 씹음 ㅋㅋ"

#         $ chat.append(("npc", "나중에 봐!"))
#         show screen messenger(chat)
#         pause 2.0 
#         hide screen messenger
#         npc "참 저기좀 봐~ 미소녀들 중 한 명이 지나가고 있어"
#         me "어디?"
#         npc "저기~"

#     hide np1 with dissolve
#     show ai1 at rightChar with dissolve
#     a1 "마라탕 먹고싶당"
#     me "여기까지가 베터버전의 끝입니다"
#     me "끝!"
    

#     returndefine npc = Character('요정', color = "#1abc9c")

define softfade = Fade(1.0, 0.5, 1.0)

define npc = Character('요정', color = "#1abc9c",window_xalign=0.5, what_xalign=0.5)
define ex = Character(None, window_xalign=0.5, what_xalign=0.5)

define diff = Character('미분이', color="#4da6ff",window_xalign=0.5, what_xalign=0.5)
define me = Character('나',color = "#c22626",window_xalign=0.5, what_xalign=0.5)
define prof = Character('교수님',color = "#bcae1a",window_xalign=0.5, what_xalign=0.5)
define rai = Character('라이', color="#7fbfff",window_xalign=0.5, what_xalign=0.5)
define student_a = Character('학생 A', color="#3498db",window_xalign=0.5, what_xalign=0.5)
define char2 = Character('하늘이', color="#ffffff",window_xalign=0.5, what_xalign=0.5)
define rona = Character('로나', color="#a569bd",window_xalign=0.5, what_xalign=0.5)
default fairy_clicked = False #사용자가 요정을 클릭했는가?

# 화면 해상도 고정
define config.screen_width = 1280
define config.screen_height = 720

# 캐릭터 포지션 
define rightChar = Position(xalign = 0.8, yalign = 0.01)

# --- 배경 이미지 (자동 스케일) ---
image lab      = im.Scale("background/연구소.jpeg", 1280, 720)
image bus1     = im.Scale("background/버스1.jpg", 1280, 720)
image bus2     = im.Scale("background/버스2.jpg", 1280, 720)
image bus3     = im.Scale("background/버스3.jpg", 1280, 720)
image class1   = im.Scale("background/교실1.jpg", 1280, 720)
image class2   = im.Scale("background/교실2.jpg", 1280, 720)
image hall1    = im.Scale("background/복도1.jpg", 1280, 720)
image hall2    = im.Scale("background/복도2.jpg", 1280, 720)
image hall3    = im.Scale("background/복도3.jpg", 1280, 720)
image cafeteria1 = im.Scale("background/식당1.jpg", 1280, 720)
image cafeteria2 = im.Scale("background/식당2.jpg", 1280, 720)
image rooftop1 = im.Scale("background/옥상1.jpg", 1280, 720)
image rooftop2 = im.Scale("background/옥상2.jpg", 1280, 720)
image royal1   = im.Scale("background/왕실1.jpg", 1280, 720)
image royal2   = im.Scale("background/왕실2.jpg", 1280, 720)
image royal3   = im.Scale("background/왕실3.jpg", 1280, 720)
image exterior1 = im.Scale("background/외관1.jpg", 1280, 720)
image space1    = im.Scale("background/우주1.jpg", 1280, 720)
image garden1   = im.Scale("background/화원1.jpg", 1280, 720)
image garden2   = im.Scale("background/화원2.jpg", 1280, 720)

# --- 등장 캐릭터 스탠딩 (정확한 Transform 문법) ---
image prof1:
    "character/char1.png"
    zoom 0.5

image rai:
    "character/rai.png"
    zoom 0.5
image sky:
    "character/sky.png"
    zoom 0.5
image fairy:
    "character/char6.png"
    zoom 0.30
    

# 요정 클릭 팝업
screen fairy_info():
    modal True
    zorder 100
    frame:
        align (0.5, 0.5)
        background "#ffffffcc"
        padding (20, 20)
        vbox:
            spacing 20
            text "✨ 생명과학 지식 ✨" size 40 color "#2c3e50"
            text "[fairy_text]" size 22 color "#000000"
            textbutton "닫기" action Hide("fairy_info")

screen fairy_icon():
    imagebutton:
        idle Transform("character/char5.png", zoom=0.11)
        hover Transform("character/char5.png", zoom=0.12)
        xpos 0.1
        ypos 0.01
        action [SetVariable("fairy_clicked", True), Show("fairy_info")]


label start:

    # -------------- #0 연구실 – 낮 --------------
    scene lab
    play music "audio/bgm/연구실.mp3" fadein 2.0
  
    ex "(실험 기구들이 늘어선 연구실. 대학원생들이 분주히 움직인다.)"
    show prof1 at rightChar with dissolve
    prof "이번 학회 주제는 ‘미생물의 의인화 가능성’이다."
    prof "각자 관심 있는 균이나 바이러스, 원생생물을 조사해 오도록."
    prof "단순한 논문 요약이 아니라, 네 시선에서 ‘그들이 살아간다면 어떤 존재일까’까지 생각해 보길 바라네."

    me "(속으로) …미생물을 사람처럼 살아가는 존재로? 대체 어떻게 풀어야 하지…"


    me "교수님, 혹시 참고할 만한 자료가 있나요?"

    show prof1 at rightChar
    prof "자료는 직접 찾아야지. 학문은 탐험이니까."

    hide prof1 with dissolve

    me "(하아… 또 막연하게 던져놓으시네. 어떻게 해야 하지…)"
    nvl clear


    # -------------- #1 연구실 – 밤 --------------
    scene lab with Fade(1.5, 1.5, 1.5)

    me "(푸른 곰팡이… 대장균… 코로나 바이러스… 아메바… 이름만 들어도 골치 아픈데.)"
    me "(이걸 어떻게 사람으로 만든다는 거야… 망했네, 진짜.)"

    show prof1 at rightChar with dissolve
    prof "…아직도 있었나? 네가 제일 늦게까지 남아 있군."
    hide prof1

    me "아, 교수님… 어떻게 해야 할지 감이 안 와서요."

    show prof1 at rightChar
    prof "남이 가르쳐주길 기다리지 말고, 직접 찾아가는 게 연구자의 길이지. 하지만…"
    prof "(주머니에서 조그만 사탕을 꺼내 책상 위에 올려놓는다.)"
    prof "힘이 필요할 땐 작은 당분도 도움이 되지."

    me "사탕…이요?"

    prof "(사탕에 붙은 메모지를 가리키며) 여기 적힌 사이트에 들어가 보게. 아마 네가 찾는 길에 단서가 될 걸세."
    hide prof1 with dissolve

    me "(…사이트? 뭔가 이상한데…)"
    me "(사탕을 입에 물며, 메모에 적힌 주소를 노트북에 입력한다.)"

    scene black with slowfade
    me "(모니터 빛 속에서 눈꺼풀이 천천히 무거워진다…)"


    # -------------- #2 버스 & 요정 --------------
    play music "audio/bgm/버스_요정.mp3" fadein 4.0
    scene bus1 with dissolve

    me "(…뭐야, 분명 연구실이었는데… 버스? 게다가 이 교복 뭐야? 나 대학원생이라고…!)"

    show fairy at rightChar with dissolve
    npc "아야야야… 쿠헉, 버스 흔들려서 또 넘어졌네…"

    me "…뭐, 뭐야 이 콩알은!?"

    npc "콩알 아냐! 나 이 세계의 안내자거든!"
    npc "이름은… 어, 뭐였더라… 아무튼 너한테 붙은 가이드 요정!"

    me "가이드 치고는 되게 허접하게 생겼는데…?"

    npc "에이, 말이 너무 심하다! 비주얼은 좀 그래도, 설명은 잘한다고! 자, 잘 들어봐."

    npc "여긴 ‘미생물 학교’야! 세균, 곰팡이, 바이러스, 원생생물 애들이 전부 교복 입고 다니는 곳이지. 너는 오늘부로 전학생!"

    me "잠깐, 그럼 내가 지금 미생물이 된 거야?"

    npc "어… 그건 나도 잘 모르겠네? 사실 설명서 반쯤 읽다 말았거든…"

    me "…진짜 믿음직스럽다."

    npc "중요한 건! 이곳에서 애들의 특징과 내력 같은 걸 익히면, 너 원래 세계로 돌아갈 수 있다! …아마도!"

    me "‘아마도’라고…?"

    npc "에헤헤~ 뭐, 돌아가기 싫으면 여기 눌러앉아도 되고~ 재밌잖아?"


    ex "(버스가 멈추고 문이 열린다. 바깥에는 기묘하게 반짝이는 교문, ‘미생물 학교’라는 현판이 보인다.)"
    

    me "하...그거면 돼? 미(생물)소녀와의 연애?"

    npc "정답! 한 명과 연애를 성공하면 넌 자동으로 미생물의 세계를 빠져나올 수 있어"
    npc "참고로 나는 npc같은 존재라서 미소녀들에겐 보이지 않아"
   
    $ fairy_text = "곰팡이는 균사로 이루어진 다세포 생물로, 자연에서 유기물을 분해하는 중요한 역할을 합니다."

    show screen fairy_icon #요정 듀토리얼
    npc "왼쪽 상단에 요정 아이콘이 보이지?"
    npc "저걸 클릭해봐!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False
    npc "자, 이해했지~? 여기서 내리면 챕터1 시작! …난 오늘은 바빠서 여기까지만!"
    me "…바쁘다고? 네가? 뭘 한다고?"
    npc "어, 낮잠 예약이 있거든. 히히. 그럼 잘해봐, 전학생!"
    hide fairy with dissolve

    me "(…이딴 게 가이드라니. 망했다.)"
    scene bus2 with dissolve
    ex "도착이다."

    # -------------- #3 교무실 --------------
    play music "audio/bgm/라이_전학.mp3" fadein 2.0
    scene class1 with dissolve

    show prof1 at rightChar
    prof "오, 너구나? 오늘 전학 온다는 애."
    me "…교…수님?"
    prof "교수? 무슨 교수. 난 네 담임, 서인호 선생님이야. 아직 긴장되나 보네?"
    me "(속으로) …말투도 다르지만… 얼굴이 너무 닮았잖아. 뭐야 이거…"
    hide prof1 with dissolve

    show prof1 at rightChar
    prof "자자, 간단히 설명할게. 여긴 ‘미생물 학교’야. 곰팡이, 세균, 바이러스, 원생생물까지 다 모여서 공부하는 곳이지."
    prof "다양한 애들이 있으니 당황할 수도 있겠지만, 걱정 마. 규칙은 단 하나, 서로의 차이를 존중할 것."
    hide prof1 with dissolve

    me "…네, 알겠습니다."

    show prof1 at rightChar
    prof "좋아! 그럼 반 애들한테 인사하러 가볼까?"
    hide prof1 with dissolve

    scene class2 with dissolve
    prof "얘들아~! 오늘부터 같이 지낼 친구 한 명 전학 왔어! 다들 박수~"
    me "(…헉, 진짜 고등학교 분위기네…)"
    nvl clear


    # -------------- #4 라이 첫만남 --------------
    show rai at rightChar with dissolve
 
    rai "안녕하세요. 반장 장라이예요. 반갑습니다."
    me "아, 네. 잘 부탁드립니다."

    prof "좋아, 오늘은 여기까지. 전학생, 모르는 거 있으면 반장에게 물어봐."
    hide prof1 with dissolve
    
    $ fairy_text = "라이의 몸 속에는 '세포 골격'이라고 불리는 단단한 구조가 있어. 이건 세포 안에서 형태를 유지하고 힘을 전달하는 일종의 뼈대야. 우리 근육이 수축하는 방식도 세포 골격에서 유래된 거야. 그래서 겉모습은 말랑해 보여도, 라이의 몸은 의외로 굉장히 튼튼해."

    show screen fairy_icon 
    npc "알림! 새로운 지식 해제!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False
    rai "자, 여기가 네 자리야. 첫날이라 낯설지? 내가 학교 구경 좀 시켜줄까?"
    me "정말? 고마워. 사실 아직도 좀 얼떨떨해서…"

    rai "하하, 괜찮아. 누구나 처음엔 그렇지. 이 학교가 좀 특이하기도 하고. 따라와, 내가 가이드 해줄게."

    scene hall1 with dissolve
    show rai at rightChar with dissolve
    rai "여기가 우리 교무실, 저쪽은 도서관. 참고로 난 여기서 시간을 제일 많이 보내. 조용하고 공부하기 좋거든."
    me "역시 반장답네… 공부 잘하나 봐?"
    rai "음… 늘 2등이지 뭐. 1등은 다른 사람이 있어서. 하하."
    $ fairy_text = "라이는 힘도 좋고 센스도 있지만, 끝까지 집중이 오래 가지 않아. 이건 라이 몸 속에 있는 '아드레날린' 때문이야. 아드레날린은 흥분하거나 긴장했을 때 순간적으로 힘과 속도를 올려주는 호르몬이야. 하지만 효과가 짧고 금방 소모돼. 그래서 라이처럼 아드레날린 반응이 강한 성격은 시작은 압도적으로 빠르지만, 마지막에 집중력이 떨어지기 쉬워. 즉, 라이가 항상 1등을 놓치고 2등이 되는 건 실력이 약해서가 아니라, 체내 호르몬 반응 특성이 다른 사람보다 강하게 나타나기 때문이야."
    show screen fairy_icon 
    npc "알림! 새로운 지식 해제!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False
    me "(…속으로) 경쟁심이 있구나."

    rai "아, 그리고 급식실은 저쪽. 메뉴는 은근히 괜찮아. 미생물 학교라곤 해도 다 먹을 수 있는 음식들이 나오거든. 네 체질도 고려해 줄 거야."
    me "와, 신기하다. 인간인 나까지 챙겨준다니."
    rai "당연하지. 앞으로 내가 옆자리니까, 모르는 건 다 나한테 물어봐. …전학생이 곤란해하는 건 좀 보기 싫거든."
    


    rai "앞으로 내가 옆자리니까, 모르는 건 다 나한테 물어봐. …전학생이 곤란해하는 건 좀 보기 싫거든."

    # ---- 선택지 시작 ----
    menu:
        "라이를 믿고 함께 이동한다":
            jump trust_rai

        "요정을 다시 찾아본다":
            jump seek_fairy


label trust_rai:
    me "고마워, 라이. 너 정말 친절하네."
    rai "하하, 그러면 다행이고. 자, 이제 반을 안내해줄게."
    jump story_continue


label seek_fairy:
    me "(…아무리 생각해도 이 상황, 너무 비현실적이야.)"
    me "잠깐만. 아까 그 요정…"
    me "요정! 요정!! 어디 있어!!"

    play music "audio/bgm/배드엔딩.mp3" fadein 2.0
    scene hall1 with slowfade

    ex "(복도의 공기가 갑자기 무겁게 가라앉는다.)"

    show fairy at rightChar with dissolve
    npc "…찾았어?"
    npc "미안하지만, 이미 늦었어."

    me "뭐…?"

    npc "이 세계는 ‘관찰’될 때만 유지돼. 하지만 너는 의심했지."
    npc "이제 균형이 깨져버렸어."

    scene black with dissolve
    stop music fadeout 3.0

    ex "세계가 천천히 무너져내린다."
    ex "빛도, 소리도, 기억도. 전부 가루처럼 흩어진다."

    me "……!"

    centered "{size=50}【 BAD ENDING 】{/size}"
    centered "{size=35}의심은 때로, 되돌릴 수 없는 균열을 만든다.{/size}"

    # 선택지: 처음으로 돌아가기
    menu:
        "다시 시작한다":
            jump start


label story_continue:
    # 여기서부터 기존 스토리 이어짐
    scene class1 with dissolve
    prof "좋아, 다음 수업 시작하자."


# --- 미분이릭터 정의 ---


# --- 배경 예시 ---
label first_meeting:

    scene class1 with fade
    play music "audio/bgm/미분_급식.mp3" fadein 2.0

    ex "점심시간. 교실 안은 떠들썩하다. 주인공은 도시락을 들고 복도로 나선다."

    me "흠… 다들 자기 무리랑 먹네. 라이는 교무실에 간다고 했고… 나 혼자 먹어야 하나?"

    ex "그때, 복도 끝에서 한 여학생이 트레이를 들고 서성인다. 점액처럼 투명한 빛깔의 머리카락, 살짝 늘어진 셔츠, 멍하니 메뉴판을 바라본다."
    
    $ fairy_text = "아메바일족은 단세포지만, 감정과 기억이 있어요. 느리지만 세심하죠."


    show screen fairy_icon 
    npc "알림! 새로운 지식 해제!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False

    diff "흐음… 볶음밥이 좋을라나… 아니면 아메리카노랑 같이 샌드위치? …아니야, 탄수화물 과하다. 근데 단백질은 또 부족하단 말이지…"

    ex "그녀는 계속 메뉴를 바꾸며 혼잣말을 한다."

    me "저… 혹시 줄 서는 거 도와드릴까요?"

    diff "어머나… 너, 인간이제?"
    diff "아하하… 반갑다아. 나는 미분이라 해. 아메바일족이지."

    me "안녕하세요, 전 전학생이에요. 아직 여긴 익숙하지 않아서요."

    diff "그라제… 처음엔 다 그런 거라~ 나도 아직 점심 메뉴는 못 정하겠네."
    diff "볶음밥도 먹고 싶고, 샌드위치도 좋고, 아메리카노도 포기 못하겠고~ 에휴…"

    ex "그녀는 메뉴판을 바라보다가, 트레이를 들고 계속 방향을 바꾼다."

    me "괜찮아요. 천천히 골라도 돼요. 제가 기다릴게요."

    diff "어라? 진짜 기다려줄껴? 대부분 귀찮다 하던데… 인간인데 참 다르네, 너."
    ex "살짝 웃는다. 그 웃음은 어딘가 느리지만 따뜻하다."

    me "느릿하고 순박한 느낌이네… 아메바라서 그런가?"

    ex "결국 미분이는 ‘볶음밥+아메리카노 세트’를 고르고 자리에 앉는다."

    # --- 급식실 씬 ---
    scene cafeteria1 with fade

    ex "두 사람은 마주 앉아 식사를 시작한다."

    diff "근데 너, 인간이면 먹는 거 조심해야 되는 거 아이가? 여긴 단세포용 메뉴도 좀 섞여 있거든."

    me "괜찮아요. 학교에서 조정해주신대요. 라이가 알려줬어요."

    diff "라이라… 반장 말이지? 하, 똑 부러지게 생겼더라 그 친구. 난 그런 스타일은 좀 어렵다."
    
    $ fairy_text = "미분이의 감정 변화가 빠른 건 세포 속 물의 이동 때문이야. 세포는 농도 차이에 따라 물이 오고 가는 '삼투압' 원리에 민감해. 물이 들어오면 부풀고, 나가면 쪼그라들지. 그래서 외부 자극이나 분위기 변화에 따라 감정이 즉시 바뀌는 것처럼 보일 수 있어."

    show screen fairy_icon 
    npc "알림! 새로운 지식 해제!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False
    diff "나같이 둔한 아메바는 빠릿한 애 보면 좀 위축된다고 해야 하나…"

    me "저는 미분이 씨가 편한데요. 천천히 말해줘서 좋아요."

    diff "그래? 음… 너 참 이상한 인간이네. 대부분은 우리 일족 보면 좀 꺼리는데…"

    # --- 선택지 ---
    menu:

            "맞다, 아메바일족은 뇌를 먹는다고 들었는데… 너도 그래?":
                jump bad_end
            "아니야, 나는 그런 편견 같은 건 안 믿어.":
                jump good_end

# --- BAD END ---
label bad_end:
    play music "audio/bgm/배드엔딩.mp3" fadein 2.0
    me "맞다, 아메바일족은 뇌를 먹는다고 들었는데… 너도 그래?"

    ex "순간, 미분이의 표정이 굳는다. 눈동자가 흐릿하게 변하고, 목소리가 차갑게 떨린다."

    diff "…그 말, 농담으로 한 거가?"

    me "아, 그게 아니고 그냥 궁금해서—"

    diff "하하… 역시 인간은 다 똑같네. 겉으론 웃으면서 속으론 우리를 괴물로 본다 그치?"

    ex "트레이를 내려놓고 자리에서 일어선다. 그녀의 손끝이 약간 흔들리며 점액질로 퍼져나간다."

    diff "고맙다. 덕분에 다시는 기대 안 하게 됐네."

    ex "그녀는 떠나가고, 남겨진 볶음밥은 천천히 식어간다."

    me "…그냥, 궁금했을 뿐인데."

    scene black with fade
   
    
    centered "{size=50}【 BAD ENDING 】{/size}"
    centered "{size=35}그녀의 심기를 거슬렀다{/size}"

    menu:
        "다시 시작한다":
            jump start

    return

# --- GOOD END ---
label good_end:
    me "아니야, 나는 그런 편견 같은 건 안 믿어. 사람들은 다 다르잖아요."

    ex "미분이가 멈춰서 주인공을 바라본다. 눈동자가 작게 흔들리다, 따뜻한 미소를 짓는다."

    diff "…그래서 말이 좀 통한다 했제."
    diff "사람들은 우리 아메바일족이 다 뇌를 먹는다고 헛소문 퍼트리거든. 근데 그런 건 옛날 얘기야."
    diff "지금은 그냥 커피 마시고 공부하는 게 더 좋다 아이가."

    me "하하, 역시 아메리카노파구나."

    diff "그라제~ 단백질보다 카페인이 낫다니까. …그리고 말이야."
    diff "너, 우리 일족을 나쁘게 보지 않아서 고맙다. 덕분에 오늘 밥 맛있게 먹었어."

    ex "그녀가 아메리카노를 살짝 들어올리며 건배하듯 말한다."

    diff "이건 평화의 카페인이다~ 인간."

    me "받아들이겠습니다, 미분이님."

    ex "둘의 웃음소리가 섞이며 화면이 서서히 페이드아웃된다."

    ex "호감도 상승 ↑ / 관계 발전 루트 개방"
    

    #---------하늘이-------

scene class2 with fade

play music "audio/bgm/하늘_정원.mp3" fadein 2.0

ex "야간 자율학습 시간. 교실에는 연필 긁는 소리와 시계 초침 소리만 가득하다."

me "으으… 이 문제, 아무리 봐도 모르겠는데. 다들 이미 자기 공부하느라 바빠 보이네…"

student_a "그거? 하늘이한테 물어봐. 페니실린 가문이라 그런지 공부는 진짜 잘해."

me "하늘이…? 아, 그 흰 머리 학생?"

show sky at rightChar with dissolve
$ fairy_text = "하늘이는 페니실린 가문 출신이라 항생제와 균 연구에 관심이 많아요."

show screen fairy_icon 
npc "알림! 새로운 지식 해제!"

# 사용자가 클릭할 때까지 기다림
while not fairy_clicked:
    $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

hide screen fairy_icon
$ fairy_clicked = False
ex "창가 구석. 조용히 필기를 하고 있는 학생 — 하늘이. 안경 너머의 눈빛은 잔잔하고 집중되어 있다."

me "저기… 미안한데 이 문제 좀 도와줄 수 있을까?"

char2 "아, 이건… 연립방정식에서 로그 항을 정리해야 해. 여기서 음수를 없애려면…"

ex "하늘이가 펜을 들어 조용히 문제를 풀어준다. 필체가 아주 단정하다."

me "와… 진짜 깔끔하다. 설명도 이해가 잘 돼."
show sky at rightChar with dissolve
$ fairy_text = "하늘이는 늘 노트를 가득 채우며 공부하는데, 그건 그냥 성실해서가 아니야. 자기 자신을 이해하고 싶어서야. DNA는 세포핵 안에 들어 있는 유전 정보로, 우리 몸을 만들고 유지하는 모든 설계도가 들어 있어."

show screen fairy_icon 
npc "알림! 새로운 지식 해제!"

# 사용자가 클릭할 때까지 기다림
while not fairy_clicked:
    $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

hide screen fairy_icon
$ fairy_clicked = False

char2 "다행이다. 사실 나는 누가 이렇게 질문해주면 좋아. 누군가를 도와줄 수 있다는 게, 나한테는… 의미가 있거든."

ex "작게 웃으며 창문 쪽을 바라본다. 바깥은 부슬비가 내리고 있다."

char2 "비 냄새 좋지 않아? 공기 중에 곰팡이 포자들이 살짝 일어나면서… 향이 달라져. 이럴 땐 산책이 최고야. 잠깐 같이 나갈래?"

# --- 씬 전환 ---
scene garden1 with fade
show sky at rightChar with dissolve

ex "하늘이와 주인공이 우산 없이 걸으며 정원을 돈다. 가로등 불빛 아래, 하늘이의 머리칼이 비에 젖어 은은히 빛난다."

char2 "저기 봐, 저건 ‘클라도스포리움’ 꽃이야. 사람들은 그냥 야생화라고 하지만, 내겐 치료의 상징이야. 옛날엔 그 균에서 항생제가 만들어졌거든."

me "역시… 이름처럼, 하늘이답다. 그런 걸 다 알고 있다니."

char2 "그냥 좋아서 외운 거야. …나는 향이 있는 것들이 좋더라. 살아있다는 느낌이 들어서."

ex "하늘이가 살짝 미소 짓는다. 비가 떨어지며 작은 빗방울이 얼굴에 닿는다."

char2 "아, 그거 알아? 내 취미 중 하나가 달고나 만들기야. 요즘 스트레스 받을 때마다 조금씩 만들어."

ex "작은 휴대용 버너를 꺼내고, 두 사람은 급식실 한쪽 구석에서 달고나를 만든다."

char2 "이렇게 설탕을 녹이고… 여기에 소다를 조금만 넣으면—"

ex "치익- 하는 소리. 두 개의 달고나가 완성된다."

char2 "자, 완성! 하나는 내 거, 하나는 네 거~"

ex "그런데 갑자기 하늘이의 달고나가 손에서 떨어져 바닥에 쩍 붙는다."

char2 "앗… 망했다. 바닥에 붙어버렸네."

# --- 선택지 ---
menu:
    "괜찮아요. 제 거 드세요.":
        jump bad_end_h
    "그건 좀… 위험해요. 다시 만들죠.":
        jump good_end_h

# --- BAD END ---
label bad_end_h:
    play music "audio/bgm/배드엔딩.mp3" fadein 2.0
    me "괜찮아요, 제 거 드세요. 저는 괜찮아요."
    char2 "정말? 고마워… 역시 네가 있어서 좋다."
    ex "하늘이가 조심스레 달고나를 한입 깨물자, 갑자기 표정이 일그러진다."
    char2 "읏… 잠깐, 이거… 이거 설마…"
    ex "입술이 푸르게 변하고, 손끝이 떨린다."
    me "하늘이?! 무슨 일이야!"
    char2 "과… 탄산… 소다… 그건… 페니실린류를… 죽여…"
    ex "말이 끝나기도 전에, 하늘이의 몸에서 희미한 푸른 빛이 번진다. 곰팡이 포자가 서서히 흩어지고, 자리에 남은 건 향기만."
    me "...그냥, 나눠주고 싶었을 뿐인데."
    scene black with fade
    centered "{size=50}【 BAD ENDING 】{/size}"
    centered "{size=35}“호의가, 독이 되었다.”{/size}"

    menu:
        "다시 시작한다":
            jump start
    return

# --- GOOD END ---
label good_end_h:
    me "그건 좀… 위험할지도 몰라요. 다시 만들죠. 냄새가 좀 이상한데요?"
    char2 "…잠깐, 냄새?" 
    char2 "이럴수가… 이거, 과탄산 소다잖아! 식용이 아니라 세척용이야!"
    ex "깜짝 놀라며 웃는다."
    char2 "하하… 큰일날 뻔했네. 나, 이거 먹었으면 진짜… 사라질 뻔했을지도 몰라. 운이 좋았네, 덕분에 살아있다."
    me "다행이다… 다음엔 내가 제대로 된 달고나 만들어줄게요."
    char2 "응… 기대할게. …그리고 고마워. 나를 걱정해준 사람, 오랜만이라서 기분이 좋아."
    ex "비가 그치고, 가로등 아래 물방울이 반짝인다."
    char2 "달고나는 못 먹었지만… 오늘, 마음은 꽉 찼다."
    ex "“치유하는 이는, 누군가에게 치유받고 싶었다.”"


label rooftop_scene:

    scene rooftop1
    play music "audio/bgm/로나옥상_슬픔.mp3" fadein 2.0
    with fade

    ex "미생물학교 옥상, 오후 5시 42분."
    ex "주인공은 머리를 식히기 위해 옥상 문을 밀어 올린다."
    ex "문이 삐걱 소리를 내며 열리고, 붉게 물든 노을빛이 쏟아져 들어온다."

    me "(조용하다… 모두가 내려간 시간인데, 누가 있을 리가 없겠지.)"
    
    ex "하지만 난간 쪽, 바람이 스치듯 흩날리는 머리카락 사이로 한 사람이 서 있었다."
    ex "회색 교복 재킷을 느슨하게 입고, 단추는 거의 잠그지 않은 채."
    ex "짙은 눈매, 사탕을 굴리는 듯한 입놀림 — 한로나."

    $ fairy_text = "로나는 바이러스 특성상 고립을 선호하지만, 관찰자의 친절에 반응할 수 있어요."
    show screen fairy_icon 
    npc "알림! 새로운 지식 해제!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False

    me "여기 있었구나… 몰랐네. 미안, 방해했지?"
    rona "아냐. 어차피 여긴 아무도 안 올라오거든. 지금은 너만 예외네."

    me "바람 좋다. 하루 종일 실험실에 있어서 그런가, 숨 막히더라."
    rona "...그럴 만하지. 너희 세균 애들은 통풍이 안 되면 금방 질식하잖아."

    me "그럼 넌? 넌 왜 여기 있어?"
    rona "...그냥, 잠깐 숨 쉬러."

    ex "그녀는 한동안 말을 멈추더니, 노을빛이 얼굴에 닿을 때쯤 작게 속삭인다."
    rona "바이러스를 죽었다고 말하는 사람도 있고, 우리가문을 싫어하는 사람도 많아."
    rona "사실 내가 ‘미생물학교’에 다닌다는 게 말이 안 된다고 하는 사람도 있지."
    rona "여긴... 내가 있을 곳이 아닌 것 같아."

    $ fairy_text = "라이는 사람 많은 곳에 가면 괜히 긴장해. 코로나 때, 모두가 서로를 조심해야 했던 기억이 아직 마음에 남아 있어. '바이러스는 아주 작은데… 사람 사이를 오가며 전염될 수 있어.' 라이는 말해. 바이러스는 세포보다 훨씬 작은 감염성 입자로, 숙주의 세포 안에서만 증식할 수 있어. 그래서 한 번 퍼지기 시작하면 정말 빠르게 번져."

    show screen fairy_icon 
    npc "알림! 새로운 지식 해제!"

    # 사용자가 클릭할 때까지 기다림
    while not fairy_clicked:
        $ renpy.pause(0.1, hard=True)  # 0.1초마다 체크

    hide screen fairy_icon
    $ fairy_clicked = False

    ex "그녀의 목소리는 처음으로, 강함이 아닌 ‘피로’로 젖어 있었다."

    # --- 선택지 ---
    menu:
       
            "로나, 여긴 네가 있어야 할 곳이야. 네가 없으면 이 학교도, 나도 좀 텅 비어버릴 것 같아.":
                jump rona_good
            "...로나, 네가 말한 게 맞는지도 몰라. 여긴 원래... 너 같은 애들이 있을 곳이 아니야.":
                jump rona_bad

# --- GOOD END ---


# --- BAD END ---
label rona_bad:
    play music "audio/bgm/배드엔딩.mp3" fadein 2.0
    ex "로나의 표정이 서서히 굳는다. 노을빛이 사라지고, 그림자가 얼굴을 덮는다."
    rona "...그래. 역시 그렇지."
    rona "결국, 너희도 우리를 연구 대상으로만 보잖아. 같이 있는 게 불편하지?"
    me "그게 아니라—"
    rona "됐어. 변명 안 해도 돼. 감염되면, 다치니까. 멀리 있는 게 나을 거야."
    ex "그녀는 그대로 문을 열고 나간다. 옥상에는 바람소리만 남는다."
    ex "주인공의 손끝엔 아직도, 그녀가 남긴 공기의 온기가 희미하게 남아 있었다."
    scene black with fade
    centered "{size=50}【 BAD ENDING 】{/size}"
    centered "{size=35}“그녀의 트라우마를 건드렸다.”{/size}"

    menu:
        "다시 시작한다":
            jump start
    label rona_good:
    play music "audio/bgm/로나옥상_전환.mp3" fadein 2.0
    rona "...뭐라고?"
    me "너무 다르다고 해서, 같이 있으면 안 되는 건 아니잖아. 로나 네가 있어서... 이 학교가 조금 더 진짜같아."
    rona "...너, 미쳤구나. 나한테 감염되면 진짜 위험할 수도 있는데."
    me "그럼 감염되면 되지. 난 네가 전염시키는 게 싫지 않아."
    ex "로나는 입을 다문다. 잠시 바람만 불고, 붉은 하늘이 그녀의 얼굴을 비춘다."
    rona "...하, 이상한 애네. 이상하게 따뜻해서... 짜증나."
    rona "받아. 이건 내가 준 첫 감염이야."
    ex "주인공은 사탕을 손에 쥐며 웃는다. 바람에 둘의 머리카락이 엇갈린다."
    ex "노을빛이 점점 옅어지고, 화면엔 부드러운 빛만 남는다."
    

    label ending_common:
    play music "audio/bgm/버스_신비.mp3" fadein 2.0

    scene black with dissolve
    pause 1.0
    show fairy at rightChar with dissolve
    ex "…………"

    scene bus2 with slowfade

    me "…어?"

    ex "주변이 갑자기 일그러진다. 색이 번지고, 소리가 멀어지더니—"

    ex "{b}ERROR: 생명체 분류 불가{/b}"
    ex "{b}ERROR: 상호 연결 상태 파손{/b}"
    ex "{b}REBOOTING…{/b}"

    scene lab with slowfade       # ← 연구실 배경


    ex "눈을 뜨자, 익숙한 형광등 불빛이 머리 위에 있었다."
    ex "차가운 바람도, 붉은 노을도, 따뜻했던 목소리도 없다."

    me "…다시 연구실로 돌아온 거야?"

    pause 1.0

    ex "분명히 함께 있었는데."
    ex "웃고, 이야기하고, 손을 뻗으면 닿을 것 같았는데…"

    pause 1.0

    ex "그 세계는 마치 꿈처럼, 손가락 사이로 스르르 빠져나가 있었다."

    me "……그래. 다시 시작하면 돼."

    scene black with dissolve
    pause 1.2

    centered "{size=45}END{/size}"

    return

  