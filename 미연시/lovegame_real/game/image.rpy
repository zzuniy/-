init python:
    # 게임 해상도 (이미지 스케일 기준)
    config.screen_width = 1280
    config.screen_height = 720

# --------------------------
# 배경 이미지 (BG)
# --------------------------
image bg 연구실 = im.Scale("연구소.jpeg", 1280, 720)
image bg 교실1 = im.Scale("교실1.jpg", 1280, 720)
image bg 교실2 = im.Scale("교실2.jpg", 1280, 720)

image bg 버스1 = im.Scale("버스1.jpg", 1280, 720)
image bg 버스2 = im.Scale("버스2.jpg", 1280, 720)
image bg 버스3 = im.Scale("버스3.jpg", 1280, 720)

image bg 복도1 = im.Scale("복도1.jpg", 1280, 720)
image bg 복도2 = im.Scale("복도2.jpg", 1280, 720)
image bg 복도3 = im.Scale("복도3.jpg", 1280, 720)

image bg 식당1 = im.Scale("식당1.jpg", 1280, 720)
image bg 식당2 = im.Scale("식당2.jpg", 1280, 720)

image bg 옥상1 = im.Scale("옥상1.jpg", 1280, 720)
image bg 옥상2 = im.Scale("옥상2.jpg", 1280, 720)

image bg 왕실1 = im.Scale("왕실1.jpg", 1280, 720)
image bg 왕실2 = im.Scale("왕실2.jpg", 1280, 720)
image bg 왕실3 = im.Scale("왕실3.jpg", 1280, 720)

image bg 외관1 = im.Scale("외관1.jpg", 1280, 720)
image bg 우주1 = im.Scale("우주1.jpg", 1280, 720)

image bg 화원1 = im.Scale("화원1.jpg", 1280, 720)
image bg 화원2 = im.Scale("화원2.jpg", 1280, 720)


# --------------------------
# 캐릭터 (스프라이트)
# --------------------------
image char1 = im.Scale("char1.png", 512, 720)
image char2 = im.Scale("char2.png", 512, 720)
image char4 = im.Scale("char4.png", 512, 720)
image char5 = im.Scale("char5.png", 512, 720)
image char6 = im.Scale("char6.png", 512, 720)


# --------------------------
# 전환 효과
# --------------------------
define slowfade = Fade(1.5, 1.0, 1.5)
