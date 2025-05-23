﻿# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import random

# ---------------------------------------------------------------------------
#                       이미지 및 캐릭터 정의 (User provided)
# ---------------------------------------------------------------------------

# 이미지 정의
image I_1 = "/Illust/I_1.png" #테스트 일러스트
image 1room = "/Place/P_0.png" # 자취방
image lecture = "/Place/P_1.png" # 강의실
image stranger = "낮선사람.jpg" # 낯선 사람 이미지 (SCG 또는 일러스트)
image s_in = "/Charactor/Rem_cs.png" # 인하 웃는 표정
image m_in = "/Charactor/Rem_ls.png" # 인하 약간 화남 (여기서는 약간 당황/삐침/슬픔 등 다양하게 활용)
image a_in = "/Charactor/Rem_ls.png" # 인하 어쩔줄 몰라하는 표정 (우물쭈물)
image fad = "/Effect/Fad.png" # 선택지 등에서 쓸 불투명 레이어

# TODO: 추가 이미지 필요 - 학교 카페, 파스타 레스토랑, 여름 느낌 일러스트 등
# image school_cafe = "place/school_cafe.jpg"
# image pasta_restaurant = "place/pasta_restaurant.jpg"
# image summer_bg = "place/summer_day.jpg" # 여름 풍경 배경 - 엔딩 등에서 사용

# 캐릭터 정의
define na = Character('나', color="#000000") # 주인공 (초반 나레이션용)
define s = Character('???', color="#2e2e2e") # 낮선사람
define si = Character('??? | {size=-20}{size=-3}♥{/size}[affection_i]{/size}', color="#ff8b8b") #인하 알기 전
define p = Character('교수님', color="#2e2e2e") #교수
define i = Character('인하 | {size=-20}{size=-3}♥{/size}[affection_i]{/size}', color="#aa3a97") #인하
define cn = Character(None, what_xalign=0.5,what_yalign=0.45) # 가운데 정렬 나레이션 (대사 없음)

# TODO: 플레이어 이름 캐릭터는 입력 후에 정의됨

# 기타 정의 (캐릭터 위치 등)
define Pright = Position(xalign = 0.8, yalign = 0.5)
define Pleft = Position(xalign = 0.2, yalign = 0.5)
define Pcenter = Position(xalign = 0.5, yalign = 0.5) # 중앙 위치 추가 (필요 시 사용)

# 변수 초기화
default player_name = "최민호" # 기본 플레이어 이름

# ---------------------------------------------------------------------------
#                       게임 시작 (User provided starting point)
# ---------------------------------------------------------------------------

label start:
    $ complete_achievement("f2") # 업적 (사용자 코드)
    # 초기 애정도 설정 (사용자 코드 참고)
    default affection_i = random.randint(40,60)
    if affection_i >=51:
        $ complete_achievement("f1") # 업적 (사용자 코드)

    # 플레이어 이름 입력받기
    $ player_name = renpy.input("내 이름은?:")
    if player_name == "":
        $ player_name = "최민호"

    # 플레이어 이름 캐릭터 정의
    define m = Character(na, color="#000000")
    $ complete_achievement("f3") # 업적 (사용자 코드)

    jump scene_1_room_morning # 첫 장면으로 이동

# ---------------------------------------------------------------------------
#                       시나리오 스크립트 시작 (아리마 작성)
# ---------------------------------------------------------------------------

# 씬 1. 주인공 자취방 - 아침
label scene_1_room_morning:
    scene 1room # 자취방 배경
    cn "(뜨거운 햇살이 창문을 통해 쏟아져 들어온다. 선풍기가 윙윙 돌아가는 소리)"

    na "(하아...)"
    na "아... 덥다 더워..."
    na "벌써부터 이렇게 푹푹 찌는데..."
    na "이 여름에 학교를 가야 한다니... 진짜 실화냐?"

    cn "(몸을 일으킨다. 땀이 등줄기를 타고 흐르는 느낌이다.)"

    na "원래 같으면 종강하고 에어컨 빵빵 틀어놓고 집에서 뒹굴거릴 텐데..."
    na "하필 1학년 때 출석을 제대로 안 해서..."
    na "이 뜨거운 여름에 계절학기 재수강이라니... 내 인생 왜 이러냐..."

    cn "(간단하게 옷을 주워 입고 나갈 준비를 한다.)"

    na "젠장... 나가기 싫다..."
    na "벌써부터 아스팔트 열기 느껴지는 것 같네..."

    cn "(주인공, 땀을 뻘뻘 흘리며 방을 나선다.)"
    with dissolve # 장면 전환 효과

# 씬 2. 대학교 강의실 - 오전
label scene_2_lecture_morning:
    scene lecture # 강의실 배경
    cn "(강의실 안은 바깥보다는 시원하지만, 여전히 꿉꿉한 기운이 돈다. 에어컨 바람이 시원찮은 것 같다. 드문드문 학생들이 앉아있고, 약간 웅성대는 소리가 들린다. 창밖에서는 매미 소리가 요란하게 들려온다.)"

    show stranger at Pright # 낯선 사람 등장 (오른쪽 구석)

    s "크읏...! 이 찜통더위에 학교라니...! 정말... 오장육부가 뒤틀리는 기분이군...!"
    s "큿소...! 필수교양이 왜 대학영어인 것이지? 대학일어였으면 이런 일 따윈 없었을 텐데...!"

    hide stranger with dissolve # 낯선 사람 퇴장

    na "(...?)"
    na "(뭐야... 저 사람은? 아침부터 이상하네... 더위 먹었나?)"
    cn "(눈을 피한다. 매미 소리만 더 크게 들리는 것 같다.)"

    na "(근데... 오늘 재수강하는 강의가 뭐였지?)"

    cn "(주인공, 책상에 앉아 스마트폰을 꺼낸다. 화면이 밝은 빛 때문에 잘 안 보인다.)"

    show m_in at Pright with moveinright # 인하 등장 (오른쪽 - 주인공 옆자리 느낌)

    si "대학영어를 재수강하시다니... 1학년 때 조금... 노셨나 봐요?"

    na "???"
    na "(누... 누구지? 저 얼굴... 어디서 본 것 같기도 하고... 아닌 것 같기도 하고... 근데 왜 이렇게 싱그러워? 여름 햇살 같네...)"

    cn "(인하의 얼굴을 빤히 쳐다본다. 매미 소리가 순간 잦아드는 것 같다.)"

    show fad # 선택지 불투명 레이어

    menu:
        # "선택지 1"
        "누구세요?":
            hide fad # 선택지 레이어 숨김
            $ affection_i += random.randint(1, 5) # 애정도 상승 (사용자 코드 참고)
            # "누구세요?" 선택 시 반응
            na "누구... 세요?"
            show a_in at Pright # 인하 당황한 표정
            i "아... 네? 저... 모르세요...?"
            cn "(괜히 머리카락을 만지작거린다. 얼굴에 살짝 홍조가 돈다.)"
            jump choice_1_result # 선택지 처리 라벨로 이동

        "(아무 말 없이 그녀를 쳐다본다)":
            hide fad # 선택지 레이어 숨김
            $ affection_i -= random.randint(1, 5) # 애정도 하락 (사용자 코드 참고)
            cn "(아무 말 없이 인하를 빤히 쳐다본다.)"
            cn "(예쁘다...)"
            cn "(근데... 왜 낯설까? 진짜 동기 맞나?)"
            show a_in at Pright # 인하 어쩔 줄 몰라하는 표정
            hide m_in
            i "그렇게 빤히 보시면... 저도 좀 부끄러운데요..."
            cn "(얼굴이 살짝 빨개진다. 부채로 연신 얼굴을 부친다. 덥지도 않나?)"
            cn "(계속 쳐다본다.)"
            cn "(인하, 어쩔 줄 몰라하며 시선을 피한다.)"
            jump choice_1_result # 선택지 처리 라벨로 이동

# ---------------------------------------------------------------------------
#                       선택지 1 처리 라벨 및 공통 부분
# ---------------------------------------------------------------------------

label choice_1_result:
    # 선택지 1 결과에 따른 대화 (스크립트 내용 반영)
    #if renpy.get_version() >= (7, 0, 0): # Ren'Py 7 이상에서 이전 선택지 확인하는 방법

    # 선택지 공통 부분 (스크립트 내용 반영)
    i "혹시... 글로벌 경영 2○학번 아니세요?"

    na "어? 맞는데? 어떻게 아셨어요?"

    i "맞다! 역시! 저 글로벌 경영학과 동기에요! MT에서 한번 뵀던 거 같아서요!"

    na "동기라고? 반갑다 동기야!"
    na "근데 아직도 학교를 다니네? 다들 졸업하지 않았나? 너도 군대 갔다 왔어?"

    hide a_in
    show m_in at Pright # 인하 약간 삐친 표정
    i "아니거든~!"
    i "개인 사정 때문에 1학년 때 휴학했다가 이번에 복학했거든~"

    na "(내 이름을 모른다고? 아까 MT에서 봤다며...)"
    na "(잠시 생각한다. 왠지 낯설지 않은 얼굴인데... 정말 모르겠다.)"

    # 일러스트 등장 전 UI 숨기기 (사용자 코드 참고)
    window hide dissolve

    # -----------------------------------------------------------------------
    #                       일러스트 등장 (User provided)
    # -----------------------------------------------------------------------
    # 일러스트 등장 및 애니메이션 (사용자 코드 그대로 사용)
    show I_1
    show I_1:
        subpixel True
        parallel:
            xpos 0.5
            linear 0.40 xpos 0.5
            linear 0.60 xpos 0.56
            linear 3.00 xpos 0.5
        parallel:
            ypos 1.0
            linear 0.40 ypos 1.0
            linear 0.60 ypos 2.32
            linear 1.00 ypos 1.45
            linear 0.50 ypos 2.32
            linear 0.50 ypos 2.32
            linear 1.00 ypos 1.0
        parallel:
            zoom 1.0
            linear 0.40 zoom 1.0
            linear 0.60 zoom 2.46
            linear 2.00 zoom 2.46
            linear 1.00 zoom 1.0
    with Pause(4.10) # 사용자 코드 그대로 사용

    # 애니메이션 끝난 후 기본 포지션으로 다시 보여주기 (사용자 코드 그대로 사용)
    show I_1:
        pos (0.5, 1.0) zoom 1.0
    with Pause(0) # 애니메이션 끝나고 바로 다음으로 넘어가기 위해 Pause(0) 추가

    with Pause(3) # 사용자 코드 그대로 사용
    window show # UI 다시 나타남 (사용자 코드)
    hide I_1 # 일러스트 숨기기 (사용자 코드)

    # -----------------------------------------------------------------------
    #                       일러스트 이후 대화 계속
    # -----------------------------------------------------------------------

    # 플레이어 이름 입력은 start 라벨로 옮김. 여기서는 바로 사용.
    # $ player_name = renpy.input("내 이름은?:")
    # if player_name == "":
    #     $ player_name = "최민호"
    # define m = Character(player_name, color="#000000") # start에서 정의
    hide m_in
    show s_in at Pright # 인하 웃는 표정 다시 등장

    cn "(아무리 생각해봐도 누군지 모르겠다)" # 이 대사는 사실 선택지 후 바로 나와야 함. 위로 올리는게 좋음. 여기서는 그냥 진행.

    i "그렇게 빤히 보시면...\n"
    extend "저도 좀 부끄러운데요..."

    # 이름 물어보는 대사는 이미 위에서 했으므로 이 부분은 삭제 또는 수정
    # si "혹시... 글로벌 경영 2○학번 아니세요?"
    # (중략)
    # si "근데 너 이름이 뭐였지..?"

    # 일러스트 이후는 바로 이름 확인 대화로 연결
    m "아 내 이름은 [player_name](이)야."
    show s_in at Pright # 인하 웃는 표정

    i "아...! 맞다! [player_name]! 기억났어!"
    i "내 이름은 인하야."
    i "성이 인, 이름이 하 외자. 기억나지?!"

    m "(인 하...? )"
    m "(왜 기억이 안 나지? 아오...)" # 여름 더위 + 기억 안 나는 답답함 느낌 살릴 수 있음

    i "ㅎㅎ... 그럴 수 있지~"

    cn "(문이 열리고 교수님이 들어오시는 모습이 보인다.)"

    show s_in at Pright # 인하 표정 유지
    i "저기 교수님 들어오시네! 이따 보자!"
    hide s_in with moveoutright # 인하 퇴장

# 씬 3. 대학교 강의실 - 수업 중
label scene_3_lecture_class:
    scene lecture with dissolve # 강의실 배경 (교수님이 교단에 서있는 장면 연출)

    cn "(교수님이 교단에 서 있다. 에어컨 바람이 여전히 시원찮아 학생들이 부채질을 하거나 연신 땀을 훔친다.)"

    cn "(교수님이 교단에 서 있다.)" # 지문
    cn "(에어컨 바람이 여전히 시원찮아 학생들이 부채질을 하거나 연신 땀을 훔친다.)" # 지문
    na "어우 왜이리 더워... 에어컨좀 빵빵하게 틀어주지..."

    # (교수님 대사 및 주인공 조는 연출 - 사용자 코드 참고)
    # 교수 캐릭터 재정의 또는 상단에 추가
    p "첫째 주는 원래 OT를 해야 하는데..."
    m "(오? OT?)"
    p "계절학기인 만큼 OT짧게 하고 1주차 강의 나가도록 할게요~"
    m "(뭐? 1주차인데 강의를 한다고? 어차피 1주차니까 중요한건 안하겠지... 그냥 졸아야겠다)"

    with fade # 조는 효과
    p "{cps=*0.2}...그....서 {/cps}{nw}"
    extend "{cps=*0.2}.....주 과....는...\n {/cps}{nw}"
    with fade # 조는 효과
    p "{cps=*0.2}두....씩... 짜.... 어....때 기억.... 남는 ...을...\n {/cps}{nw}"
    with fade # 조는 효과
    p "{cps=*0.2}에......로 작성.... 발.... {/cps}{nw}"
    with fade # 조는 효과
    with vpunch # 깨움
    extend " 해보도록 합시다~{nw}"

    cn "(누군가가 나를 건드린다)"
    show s_in at Pright # 인하 등장

    i "저... [player_name]!"
    # hide s_in # 표정 변경 시 숨김
    # show s_in # 중앙에서 나타난 인하 - 스크립트에서는 중앙 이동 없으므로 오른쪽 유지

    i "교수님이 두 명씩 조를 짜라고 하시는데..."
    i "우리... 같은 조 할래?"

    m "(인하의 얼굴을 본다. 예쁘다... 이렇게 더운 날씨에도 시원해 보인다.)"
    m "(예쁜 여자애랑 팀플? 와... 계절학기 망했다 싶었는데... 갑자기 로또 맞은 느낌?)"
    m "(아... 근데... 원래 같이 하기로 한 사람이 있는데...)"
    m "(어떻게 하지? 약속을 깨?)"

    cn "(잠시 고민한다. 창밖 매미 소리가 더 크게 들리는 것 같다.)"

    window hide # 선택지를 위한 UI 숨김 (사용자 코드)
    show fad # 불투명 레이어 (사용자 코드)

    menu:
        # "선택지 2"
        "원래 같이 하기로 한 형이랑 같이 한다":
            hide fad # 선택지 레이어 숨김
            m "미안... 같이 하기로 한 사람이 있어서 같이 못 할 것 같아..."
            $ affection_i -= random.randint(5, 10) # 애정도 하락 (사용자 코드)
            jump choice_2_decline # 거절 분기 라벨로 이동

        "인하와 함께한다":
            hide fad # 선택지 레이어 숨김
            m "네! 좋아요! 같이 해요!"
            $ affection_i += random.randint(5, 10) # 수락 시 애정도 상승 (사용자 코드)
            jump choice_2_accept # 수락 분기 라벨로 이동

# ---------------------------------------------------------------------------
#                       선택지 2 - 거절 루트
# ---------------------------------------------------------------------------

label choice_2_decline: # "원래 같이 하기로 한 형이랑 같이 한다" 선택 시
    hide s_in with dissolve # 인하 퇴장

    if affection_i >= 41: # 애정도 높음 시 (사용자 코드 참고 - 41 기준)
        i "그래...? 아쉽네... 그럼... 다음에 보자~!"
        cn "(인하가 아쉽다는 표정으로 손을 흔들고 자리로 돌아간다.)" # 지문 추가
        # jump date5 # 이전 스크립트 라벨 (아래에서 통합 처리)
    else: # 애정도 낮음 시 (사용자 코드 참고)
        i "아... 그렇구나. 알겠어."
        cn "(인하가 담담하게 고개를 살짝 숙이고 자리로 돌아간다.)" # 지문 추가
        # jump over0 # 이전 스크립트 라벨 (아래에서 통합 처리)

    m "(왠지 모르게... 조금 아쉬운 기분이다.)"
    m "(아냐, 약속은 약속이니까.)"
    m "(이 찜통더위에 약속 지키는 게 더 중요하지!)"

    scene lecture with dissolve # 강의실 풍경으로 돌아옴

    cn "(교수님이 다시 교단으로 올라서며 수업을 시작하신다.)"
    # 교수 캐릭터 다시 정의
    p "자, 그럼 조는 다 정해진 것 같으니..."
    p "1주차 강의 시작할게요."

    cn "(교수님 목소리가 멀게 들린다...)"
    m "(자꾸 아까 인하 얼굴이 떠오르네. 매미 소리만 귀에 거슬린다.)" # 여름 느낌 추가
    m "(진짜 MT 때 봤다고? 왜 이렇게 기억에 없지...)"

    # 시간이 흐르는 연출
    with fade # 조는 효과 또는 시간 경과
    p "...오늘 강의는 여기까지입니다."
    p "조별 과제는 다음 주까지 주제 정해서 알려주시고, 팀원 정보는 강의 끝나고 저한테 제출해주세요."
    with fade # 깨어나는 효과 또는 시간 경과 종료

    m "(겨우 끝났다...)"
    m "(팀플 형한테 연락해서 조 이름이랑 내 학번 보내줘야겠다.)"
    m "(아... 뭔가 오늘은 좀 피곤하네... 더위 먹었나...)" # 여름 느낌

    scene lecture # 강의실에 앉아있는 장면 유지

    cn "(가방을 챙겨 강의실을 나선다. 바깥은 여전히 숨 막히는 더위다.)"

    m "(집에 가서 찬물 샤워나 해야겠다.)"
    m "(근데 인하... 진짜 동기 맞나? 왜 기억이 안 나지?)"

    cn "(더위 속에서 인하에 대한 생각을 애써 지우며 집으로 향한다.)"
    scene 1room with dissolve # 자취방으로 이동

    # 애정도에 따른 하루 마무리 및 다음 날 연출 분기
    if affection_i >= 61: # 애정도 높을 때 거절 -> 찜찜함 + 타임슬립 복선
        m "집에 도착해서 바로 침대에 누웠다."
        m "강의 내용도 제대로 못 들었고... 그냥 다 귀찮다."
        m "..."
        m "(아까 인하... 진짜 동기 맞는 건가?)"
        m "(왜 자꾸 신경 쓰이지? 왠지... 오늘 뭔가 중요한 걸 놓친 기분이야.)" # 복선 강화
        m "(...피곤해서 그런가보다.)"
        m "그냥 자자."
        cn "(잠이 든다.)"
        jump next_day_after_decline_high_aff # 다음 날 아침 - 복선 있는 시작

    else: # 애정도 낮을 때 거절 -> 평범한 일상
        m "집에 와서 형에게 연락해서 조별 과제 관련 정보를 보냈다."
        cn "(...6시간 후 [player_name]은/는 휴대폰을 확인 했지만, 조별과제를 같이 하기로 한 형이 아직 안읽었다는 것을 확인한다)"
        m "무슨일 생겼나...?"
        cn "(......3일 후에도 휴대폰을 확인 하였지만 휴대폰의 읽음표시는 확인 되지 않는다)"
        m "뭐지...? 이형이 설마 잠수를 타겠어?"
        $ complete_ending("e6")
        m "이번에도 혼자 해야겠네, 조별과제"
        m "씻고 과제나 해야겠다"
        cn "(결국 [player_name]은/는 조별과제를 혼자 마무리 지었다)"
        jump next_day_after_decline_low_aff # 다음 날 아침 - 평범한 시작

# 다음 날 아침, 이상한 기시감이나 타임슬립 징조 (애정도 높을 때 거절)
label next_day_after_decline_high_aff:
    scene 1room # 방 안
    cn "(뜨거운 햇살이 창문을 통해 쏟아져 들어온다. 선풍기가 윙윙 돌아가는 소리)" # 루프 시작 연출
    m "으음... 아침이다."
    m "뭔가 꿈을 꾼 것 같은데... 내용이 잘 기억나지 않는다."
    m "(이상하다... 어제 분명...)"
    m "..."
    m "어제 있었던 일이... 뭔가 희미하다."
    m "마치... 어제 하루가 통째로 삭제된 기분...?"
    m "(이게 뭐지...? 피곤해서 헛소리를 다 하네. 아니... 진짜 이상해...)" # 복선 강화

    # 앞으로 전개될 타임슬립 이벤트의 복선
    # 이 루트는 인하와의 접점이 줄어들면서 다른 방향의 스토리가 전개될 수 있음
    # 예를 들어, 시간이 뒤틀리는 현상을 먼저 겪거나, 다른 인물과의 관계가 부각되거나...

    jump scene_2_lecture_morning # 루프 발생 - 다시 강의실 오전으로 (타임슬립 자각은 나중에 발생)
    # TODO: 이 루트는 인하와 덜 엮이지만 타임슬립은 여전히 일어나는 분기로 만들 수 있음.
    # 일단은 임시로 루프 시작점으로 보내지만, 나중에 별도 루트로 분기 필요.

# 다음 날 아침, 일상적인 하루 시작 (애정도 낮을 때 거절)
label next_day_after_decline_low_aff:
    scene 1room # 방 안
    cn "(익숙한 자취방 천장이다. 창밖 매미 소리가 시끄럽다.)" # 여름 느낌
    m "으음... 아침이다."
    m "오늘은 뭐 할까."
    m "강의 발표 준비 해야하는구나...."

    # 이 루트는 인하와의 접점이 거의 없이 흘러가거나,
    # 타임슬립 이벤트가 발생하더라도 인하와 직접적인 연결고리가 약할 수 있음.
    # 순애보다는 타임슬립 미스터리 쪽에 치중되거나,
    # 인하는 그냥 지나가는 조연으로 남을 가능성이 높음.
    return # 일단 여기서는 엔딩 처리 (거절 엔딩)
    # TODO: 이 루트도 루프 발생 시키고 배드 엔딩으로 연결 가능

# ---------------------------------------------------------------------------
#                       선택지 2 - 수락 루트
# ---------------------------------------------------------------------------

label choice_2_accept: # "인하와 함께한다" 선택 시
    show s_in at Pleft with moveinleft # 인하가 주인공 쪽으로 다가옴 (왼쪽으로 이동)

    i "진짜?! 얏호! 완전 좋다!"
    i "[player_name]이랑 같은 조라니! 여름 방학 계절학기가 즐거워질 것 같아!" # 여름 느낌 추가

    m "(이렇게 좋아할 줄이야... ㅋㅋㅋ 귀엽네...)" # 스크립트 내용
    m "(근데... 진짜 예쁘다... 웃는 거 진짜...)" # 스크립트 내용
    m "(아니, 잠깐만... 진짜 기억이 안 난다고? MT 때 나랑 얘기했다고...? 왜 이렇게 낯설지? 마치... 처음 보는 사람 같은데?)" # 타임슬립 복선 강화

    show s_in at Pleft # 표정 유지
    i "[player_name]! 그럼 우리 번호 교환할까? 조별 과제 때문에 연락해야 하잖아!"

    # 주인공 번호 설정은 생략하고 대화만
    m "[player_name] : 아, 응! 당연하지." # 번호 언급은 생략
    cn "(인하와 번호를 교환했다.)" # 지문으로 처리

    hide s_in
    show a_in at Pleft # 인하가 휴대폰에 저장하는 듯한 표정
    i "오키오키! 나도 저장해놨다! 인하! 잘 부탁해!" # 인하 이름 말해줌
    hide a_in
    show s_in at Pleft # 다시 밝은 표정
    i "인하야! 잘 부탁해 [player_name]!" # 인하 대사 변경 (스크립트 기반)

    m "(인 하...? )" # 스크립트 내용
    m "(왜 자꾸 낯설지...? 인하라는 이름... 분명 처음 듣는 것 같은데... 근데 왜 이렇게 익숙하지?)" # 타임슬립 복선 강화

    cn "(그때, 교수님이 기침하며 우리 쪽을 보셨다.)"
    # 교수 캐릭터 재정의
    p "(큼큼)"

    show s_in at Pleft # 인하 표정 유지
    i "앗! 교수님 보신다!"
    show s_in at Pleft with moveoutleft # 인하가 자기 자리로 돌아가는 듯
    hide s_in

    scene lecture with dissolve # 다시 강의에 집중하는 분위기

    p "자, 그럼 조는 다 정해진 것 같으니..."
    p "1주차 강의 시작할게요."

    m "(휴... 인하랑 같은 조가 되었다.)"
    m "(예쁜 여자애랑 팀플이라니... 이 더위에 이게 무슨 횡재냐 ㅋㅋㅋ)" # 여름 느낌
    m "(근데 진짜... 왜 기억이 안 나지...? 인하가 MT 때 봤다고 했는데... 너무 이상해.)" # 타임슬립 복선
    m "(마치... 원래 인하를 몰랐던 것 같은 기분이야. 이 느낌... 전에 한 번 느껴본 적 있는 것 같은데...?)" # 강한 기시감 표현

    # 강의 시간 동안 생각 (스크립트 내용 반영)
    # p "...오늘 배울 내용은..." # 교수님 대사는 생략하고 생각만
    m "(인하는 지금 뭘 하고 있을까?)"
    m "(조별 과제 주제는 뭐로 정하지...)"
    m "(...근데 진짜 왜 기억이 안 나는 거지?)"
    m "(내가 인하를 처음 보는 게 아닌 것 같은 느낌인데...)" # 강한 기시감 표현

    # 강의 끝나는 연출
    with fade # 시간 경과
    p "...자, 오늘 강의는 여기까지입니다."
    p "조별 과제는 다음 주까지 주제 정해서 알려주시고, 팀원 정보는 강의 끝나고 저한테 제출해주세요."
    with fade # 시간 경과 종료

    m "(강의 끝!)"
    m "(이제 인하랑 조별 과제 얘기를 좀 해야겠다.)"

    scene lecture # 강의실에 앉아있는 장면 유지
    show s_in at Pleft with moveinleft # 인하가 다시 다가옴 (왼쪽에서 등장)

    i "[player_name]! 조별 과제 때문에 언제 만날까?"
    i "아니면 일단 카톡으로 먼저 얘기해볼까?"

    # 여기서 또 새로운 선택지로 연결됨 (카톡 vs 직접 만남)
    window hide # 선택지를 위한 UI 숨김 (사용자 코드)
    show fad # 불투명 레이어 (사용자 코드)

    menu:
        # "선택지 3"
        "카톡으로 얘기하자":
            hide fad # 선택지 레이어 숨김
            $ affection_i += random.randint(1, 3) # 소소한 애정도 상승 (사용자 코드)
            jump choice_3_chat # 카톡 분기 라벨로 이동

        "언제 만날지 정하자":
            hide fad # 선택지 레이어 숨김
            $ affection_i += random.randint(2, 5) # 직접 만남 제안 시 애정도 상승 (사용자 코드)
            jump choice_3_meet # 직접 만남 분기 라벨로 이동

# ---------------------------------------------------------------------------
#                       선택지 3 - 분기 처리
# ---------------------------------------------------------------------------

label choice_3_chat: # "카톡으로 얘기하자" 선택 시
    hide s_in # 인하 퇴장
    i "좋아! 그럼 나중에 카톡할게!"
    m "(인하랑 카톡이라... 벌써부터 좀 설레는데? ㅋㅋ)"
    m "(빨리 집에 가서 폰만 봐야겠다.)"
    cn "(여름의 뜨거운 오후, 서둘러 집으로 향했다.)" # 여름 느낌 추가
    jump project_chat # 카톡으로 프로젝트 얘기하는 루트 라벨로 이동

label choice_3_meet: # "언제 만날지 정하자" 선택 시
    hide s_in # 인하 퇴장
    i "음... 다음 주에 강의 오기 전에 만나서 같이 점심 먹으면서 얘기할래?"
    i "시원한 데서!" # 여름 느낌 추가
    m "오! 그거 좋다!"
    i "그럼 다음 주 수업 전에 학교 근처에서 보자!"
    m "(인하랑 단둘이 점심...? 와... 이 더운 여름에 완전 설레는데? ㅋㅋ)" # 여름 느낌
    m "(벌써부터 긴장된다... 뭘 입고 나가지? ㅋㅋㅋ)"
    cn "(인하가 밝게 웃으며 손을 흔들고 강의실을 나선다. 나도 서둘러 집으로 향했다.)" # 지문 추가
    jump project_meet # 직접 만나서 프로젝트 얘기하는 루트 라벨로 이동

# ---------------------------------------------------------------------------
#                       수락 루트 - 다음 단계들
# ---------------------------------------------------------------------------

# project_chat 루트 (현재는 간단히 처리)
label project_chat:
    scene 1room with dissolve # 방 안에서 폰 보는 장면
    cn "(집에 오니 인하에게 카톡이 와 있었다.)"
    # cn "(카톡 화면 효과음)" # 효과음 필요 시 추가
    # 카톡 대화 내용 (스크립트 미작성 - Placeholder)
    # i "집에 잘 들어갔어?"
    # m "응! 인하도 잘 들어갔어?"
    # ... (조별 과제 주제, 역할 분담 얘기 등)
    # 대화 중에 타임슬립 관련 복선이나 인하의 다른 모습 발견 등 추가 가능

    cn "(인하와 카톡으로 조별 과제에 대한 대화를 나눴다.)"
    cn "(화면 너머 인하의 목소리가 들리는 것만 같다.)" # 순애 느낌 추가
    cn "(대화는... 왠지 모르게 평범하지만...) "
    cn "(문득... 우리가 나눴던 대화가... 처음이 아닌 것 같은 기분이 든다.)" # 타임슬립 복선
    m "(...이상한 기분이야.)"

    # 카톡 대화 끝내고 다음 스토리로 넘어감 (여기서는 타임슬립 전조로 바로 이동)
    jump scene_6_timeslip_prelude

# project_meet 루트 (직접 만남)
label project_meet:
    # 다음 강의 날, 인하와 만나서 점심 먹으며 프로젝트 얘기
    scene lecture # 강의실 배경에서 시작 (약속 장소 이동 전)
    m "다음 주 강의가 있는 날."
    m "인하를 만나기로 한 약속 시간까지 조금 남았다."
    m "(두근두근... 인하랑 단둘이 점심이라니...)"
    m "(어제 밤에 옷만 몇 번을 갈아입었는지 몰라 ㅋㅋㅋ)"

    # TODO: 학교 근처 배경 이미지 필요
    # scene school_cafe_outside # 학교 근처 카페/식당 앞 배경
    scene lecture # 임시로 강의실 배경 유지

    cn "(약속 장소인 학교 근처로 향했다.)"
    cn "(쨍쨍한 여름 햇살 아래, 약속 장소에서 인하를 기다린다. 땀이 흐르는 게 느껴진다.)" # 여름 느낌

    m "(으... 덥다... 인하는 언제 오지?)"
    m "(거울 좀 볼 걸 그랬나? 머리 괜찮나?)"

    cn "(멀리서 인하가 걸어오는 모습이 보인다. 여름에 잘 어울리는 밝은 옷차림이다. 걸어오는 모습만 봐도 주변이 시원해지는 것 같다.)" # 여름 느낌 + 순애 느낌

    show s_in at Pright with fade # 인하 등장

    i "얏호! [player_name]! 왔네!"
    i "나 기다렸지? 미안미안~!"
    i "좀 더웠지?" # 여름 느낌 추가

    m "아냐! 나도 방금 왔어! 괜찮아!"

    show s_in at Pright # 표정 유지
    i "다행이다~! 우리 뭐 먹을까?"
    i "카페에서 시원한 거 마시면서 얘기할까? 아니면 밥 먹으면서?"

    show fad # 선택지 레이어
    menu:
        # "선택지 4"
        "카페에서 먹자 (시원한 음료)":
            hide fad # 선택지 레이어 숨김
            $ affection_i += random.randint(1, 3) # 애정도 상승
            jump choice_4_cafe # 카페 분기 라벨

        "밥 먹으면서 얘기하자 (배부터 채우자)":
            hide fad # 선택지 레이어 숨김
            $ affection_i += random.randint(2, 5) # 애정도 상승
            jump choice_4_restaurant # 식당 분기 라벨

# ---------------------------------------------------------------------------
#                       선택지 4 - 분기 처리 (만남 장소)
# ---------------------------------------------------------------------------

label choice_4_cafe: # "카페에서 먹자" 선택 시
    i "오케이! 여기 근처에 분위기 좋고 시원한 카페 알아놨어! 같이 가자!"
    cn "(카페로 향한다. 에어컨 바람이 느껴지자 살 것 같다.)" # 여름 느낌
    # TODO: 카페 내부 배경 이미지 필요
    # scene cafe_inside with dissolve
    scene lecture with dissolve # 임시 배경 유지

    cn "(카페 테이블에 앉아 시원한 음료를 마신다. 잔에 맺힌 물방울이 시원해 보인다.)" # 여름 느낌

    m "(아... 시원하다... 역시 여름엔 카페가 최고야.)" # 여름 느낌
    m "(인하... 이렇게 가까이서 보니까 더 예쁘네...)" # 순애 느낌

    show s_in # 인하 중앙으로 (대화 포지션) - 필요 시 위치 조정

    i "음~ 여기 커피 맛있다! [player_name]은/는 뭐 마실거야?"
    m "나는... 아이스 아메리카노."

    i "역시 아.아! ㅋㅋㅋ 아, 우리 조별 과제 얘기해야지! 교수님이 주제는 자유라고 했잖아?"

    cn "(인하가 들고 온 노트를 펼친다.)" # 지문

    i "우리 뭐 할까? 나는... 뭔가 창의적인 거 해보고 싶은데! 너무 뻔한 거 말고!"

    m "(창의적인 거라... 인하랑 같이 하는 건 뭐든 좋지만... 이 기회에 인하랑 더 가까워질 만한 주제가 없을까?)" # 순애 느낌

    show fad # 선택지 레이어
    menu:
        # "선택지 5" (카페용)
        "우리가 기억하는 '가장 인상 깊은 경험'에 대해 발표하자":
            hide fad
            $ affection_i += random.randint(5, 10) # 타임슬립 복선과 연결될 주제, 애정도 크게 상승
            jump choice_5_topic_personal # 개인 경험 주제 선택 분기

        "수업 시간에 배운 개념 하나를 깊이 파고들자":
            hide fad
            $ affection_i -= random.randint(5, 30) # 평범한 주제, 애정도 소폭 상승
            jump choice_5_topic_normal # 일반 주제 선택 분기

label choice_4_restaurant: # "밥 먹으면서 얘기하자" 선택 시
    m "엇! 좋아! 근처에 맛있는 국밥 집 있는데 거기 갈래? 배고플땐 국밥이 최고지!" # 여름 느낌
    i "음........"
    # 우물쭈물한 인하의 표정 이내 밝아진다
    i "그래!"
    cn "(국밥 집으로 향한다. 어휴... 눈치없는 새X)" # 여름 느낌
    # TODO: 파스타집 배경 이미지 필요
    # scene pasta_restaurant with dissolve
    scene lecture with dissolve # 임시 배경 유지

    cn "(테이블에 앉아 시원한 물을 마신다. 메뉴판을 본다.)"

    m "(인하도 좋아 하는거겠...지?)" # 여름 느낌 + 순애 느낌

    show s_in # 인하 중앙으로 (대화 포지션) - 필요 시 위치 조정

    i "뭐... 먹을거야?"
    m "나는 특국밥!"

    i "그래? 나도 그거 먹어야겠다 ㅎㅎ..."
    # 애써 웃는 인하의 표정

    cn "(...메뉴가 나올때 까지 어색한 침묵이 이어진다.)" # 지문

    m "여기 국밥 진짜 맛있어, 먹어봐 깜짝 놀랄걸?"
    # 떨떠름한 인하의 표정
    i "으응..."

    cn "(또 다시 어색한 침묵이 이어진다.)"

    m "(재미있는 거라... 인하랑 같이 하면 다 재미있을 것 같긴 한데...)"
    m "(이 기회에 인하랑 더 개인적인 얘기를 나눌 수 있는 주제가 없을까?)" # 순애 느낌
    m "(타임슬립 떡밥이랑 연결될 만한 걸로...?)" # 타임슬립 복선

    show fad # 선택지 레이어
    menu:
        # "선택지 5" (식당용)
        "서로의 '인생 영화'를 소개하고 분석하자":
            hide fad
            $ affection_i += random.randint(5, 10) # 개인적인 얘기, 애정도 크게 상승
            jump choice_5_topic_personal # 개인 경험 주제 선택 분기

        "최근 IT 트렌드에 대해 조사하고 발표하자":
            hide fad
            $ affection_i += random.randint(1, 3) # 평범한 주제, 애정도 소폭 상승
            jump choice_5_topic_normal # 일반 주제 선택 분기

# ---------------------------------------------------------------------------
#                       선택지 5 - 주제 결정 후 공통 단계
# ---------------------------------------------------------------------------

label choice_5_topic_personal: # 개인적인 주제 선택 시 대화
    # 선택지 내용에 따라 인하 대사 분기 (카페 vs 식당)
    menu: # Ren'Py 7 이상에서 이전 선택지 확인
        "우리가 기억하는 '가장 인상 깊은 경험'에 대해 발표하자":
            i "오!! 그거 완전 좋은데?! 뭔가... 개인적인 이야기라 흥미로울 것 같아!"
            i "근데... [player_name]은 가장 인상 깊은 경험이 뭐야?"
            m "[player_name] : 음... 글쎄..."
            m "(머릿속이 하얘진다... 분명... 뭔가 중요한 일이 있었던 것 같은데...)" # 타임슬립 복선 강화
            m "(아니야, 그런 건 아무것도 없어. 그냥 평범한 나날이었지. 근데 왜 이렇게 낯설지?)" # 자기 부정 + 기시감
            m "[player_name] : 아직 잘 모르겠네... 생각해봐야 할 것 같아."
            i "나도! 뭔가 깊이 생각해볼 주제인 것 같아!"
        "서로의 '인생 영화'를 소개하고 분석하자":
            i "인생 영화? 완전 좋다! 뭔가 서로를 더 잘 알게 될 것 같은 느낌!"
            i "[player_name]의 인생 영화는 뭐야?"
            m "[player_name] : 내 인생 영화는... (문득 잊고 있던 기억 조각이 스친다)"
            m "(어떤 영화를... 누구와 봤더라...?)" # 타임슬립 복선 강화
            m "(인하... 인하랑 관련된 기억... 인가...?)"
            m "[player_name] : 음... 생각해보고 알려줄게!"
            i "나도 내 인생 영화 잘 생각해봐야겠다! 어려운 질문인데?"

    # 주제 결정 후 공통 대화
    jump project_topic_decided # 다음 단계로 이동

label choice_5_topic_normal: # 일반적인 주제 선택 시 대화
    # 선택지 내용에 따라 인하 대사 분기 (카페 vs 식당)
    menu: # Ren'Py 7 이상에서 이전 선택지 확인
        "수업 시간에 배운 개념 하나를 깊이 파고들자":
            i "그것도 좋지! 안정적이고!"
            i "그럼 우리 수업 자료 다시 보면서 어떤 개념이 좋을지 골라볼까?"
            m "그래, 그렇게 하자!"
        "최근 IT 트렌드에 대해 조사하고 발표하자":
            i "오! IT 트렌드? 그거 완전 흥미롭지! 나도 IT 쪽 관심 있는데!"
            i "그럼 우리 최신 트렌드 몇 가지 정해서 나눠서 조사할까?"
            m "그래, 그렇게 하자!"

    # 주제 결정 후 공통 대화
    jump project_topic_decided # 다음 단계로 이동


# 주제 결정 후 공통 단계 (타임슬립 전조 발생)
label project_topic_decided:
    show s_in # 인하 스탠딩 CG 유지 또는 다시 보여줌
    i "이제 주제도 정했으니까... 역할 분담도 해야겠지?"
    i "[player_name]은 어떤 부분 맡고 싶어?"

    m "(인하랑 같이 하는 건 뭐든 좋아...)"
    m "(근데... 왜 자꾸 인하가 낯설지? 분명 동기라고 했는데...)" # 타임슬립 복선 반복
    m "(아무리 기억해내려고 해도 MT 때 인하랑 얘기했던 기억이 전혀 없어.)"
    m "(이 기분... 전에 한번 느껴본 적 있는 것 같은데...?)" # 강한 기시감 표현

    # 씬 6. 주제 결정 후 - 타임슬립 전조
    label scene_6_timeslip_prelude:
        cn "(갑자기 머리가 어지러워진다.)"
        cn "(눈 앞이 깜빡거린다.)"
        with vpunch # 시야 흔들리는 효과
        cn "(세상이 일렁이는 느낌... 주변 소리가 멀어지고, 매미 소리가 귀를 찢을 듯 크게 들린다.)" # 여름 느낌 + 효과음 묘사

        m "[player_name] : 으...윽...!"
        hide s_in
        show a_in # 인하 당황한 표정

        i "[player_name]?! 괜찮아?! 갑자기 왜 그래?! 더위 먹었어?!" # 여름 느낌 추가

        m "(인하의 목소리가 멀게 들린다.)"
        m "(마치... 다른 세상에서 들려오는 소리 같아.)"
        m "(그리고...)"
        m "(어제 했던 대화들이... 다시 떠오른다.)"
        m "(1학년 때 출석을 제대로 안 해서 계절학기에 재수강을 한다고...) -- 내가 어제 했던 말"
        m "(낯선 사람이 이상한 소리를 한다고...) -- 어제 강의실에서 본 사람"
        m "(재수강 하는 강의가 뭐였는지 기억이 안 난다고...) -- 어제 상황"
        m "(그리고...)"
        m "(인하가 갑자기 나타나 말을 걸었다...)"
        m "(나는 지방 사립 S대에 재학중인 대학생이다.)" # 맨 처음 시작 문구

        cn "(모든 것이 처음으로 돌아가는 느낌...)"

        # 여기서 타임 슬립 발생
        with fade # 화면이 암전되면서 리셋되는 느낌 연출
        # 오디오 페이드아웃 효과 추가 가능

        # 씬 7. 주인공 자취방 - 아침 (루프 시작)
        label scene_7_room_morning_loop:
            scene 1room with dissolve # 자취방 배경, 부드러운 전환
            cn "(눈을 떴다.)"

            cn "(뜨거운 햇살이 창문을 통해 쏟아져 들어온다. 선풍기가 윙윙 돌아가는 소리)" # 루프 시작 연출 반복
            m "나는 지방 사립 S대에 재학 중인 대학생이다."
            m "원래라면 종강이라 학교에 안가도 되지만"
            m "1학년 때 출석을 제대로 안 해서 계절학기에 재수강을 하게 되었다."

            m "(...어?)"
            m "(방금... 똑같은 생각을 하지 않았나?)"
            m "(마치... 어제 아침으로 돌아온 기분이야...)"
            m "(꿈... 인가? 근데 왜 이렇게 생생하지?)" # 스크립트 내용
            m "(이 햇살... 이 더위... 어제랑 똑같아...)" # 여름 느낌 추가

            cn "(땀을 뻘뻘 흘리며 방을 나선다.)"
            with dissolve # 장면 전환 효과

        # 씬 8. 대학교 강의실 - 오전 (루프 속)
        label scene_8_lecture_morning_loop:
            scene lecture # 강의실 배경
            cn "(강의실 안은 바깥보다는 시원하지만, 여전히 꿉꿉한 기운이 돈다. 에어컨 바람이 시원찮은 것 같다. 드문드문 학생들이 앉아있고, 약간 웅성대는 소리가 들린다. 창밖에서는 매미 소리가 요란하게 들려온다.)" # 여름 느낌

            show stranger at Pright # 낯선 사람 등장

            s "크읏...! 이 찜통더위에 학교라니...! 정말... 오장육부가 뒤틀리는 기분이군...!" # 대사 반복
            s "큿소...! 필수교양이 왜 대학영어인 것이지? 대학일어였으면 이런 일 따윈 없었을 텐데...!" # 대사 반복

            hide stranger with dissolve # 낯선 사람 퇴장

            m "(...데자뷰인가?)"
            m "(어제랑 똑같잖아? 낯선 사람까지...?)"
            m "(근데 오늘 재수강하는 강의가 뭐였지?)" # 어제 했던 생각 반복

            cn "(주인공, 책상에 앉아 스마트폰을 꺼낸다. 화면이 밝은 빛 때문에 잘 안 보인다.)"

            show m_in at Pright with moveinright # 인하 등장

            si "대학영어를 재수강하시다니... 1학년 때 조금... 노셨나 봐요?"

            m "(놀라서 인하를 쳐다본다.)"
            m "(...인하?!)" # 인하임을 바로 알아봄
            m "(어? 어제랑 똑같아...!)"
            m "(분명 어제 인하랑 조별 과제 얘기도 하고... 같이 점심도 먹었는데...)"
            m "(왜 다시 처음으로 돌아온 거지? 이게... 타임슬립?)"
            m "(인하... 인하가 나를 기억 못 해... 어제의 인하가 아니야...)"
            m "(이 반복... 인하 때문에 일어나는 건가?)"

            cn "(인하의 얼굴을 빤히 쳐다본다. 어제와 똑같은 상황. 하지만 주인공의 마음은 어제와 완전히 다르다. 매미 소리가 귀를 찢을 듯 시끄럽다.)" # 여름 느낌 + 변화된 심리 묘사

            show fad # 선택지 레이어

            menu:
                # "선택지 6" (루프 자각 후)
                "인하의 이름을 부른다":
                    hide fad
                    $ affection_i += random.randint(5, 10) # 이름을 기억하고 불러주면 애정도 크게 상승
                    jump choice_6_call_name # 이름 부르는 분기

                "어리둥절한 표정으로 쳐다본다 (어제와 똑같이 행동)":
                    hide fad
                    $ affection_i -= random.randint(1, 5) # 어제와 똑같이 반응하면 애정도 하락 가능
                    jump choice_6_repeat_action # 어제처럼 행동하는 분기

# ---------------------------------------------------------------------------
#                       선택지 6 - 분기 처리 (타임슬립 자각 후 반응)
# ---------------------------------------------------------------------------

label choice_6_call_name: # "인하의 이름을 부른다" 선택 시 (타임슬립 자각 루트)
    m "인하...!"

    show s_in at Pright # 인하 놀란 표정
    i "[player_name]...?"
    i "어? 내 이름... 어떻게 알았어?"
    i "우리가 만난 건... 오늘이 처음 아니야?"

    m "(역시... 어제의 나는 인하에게 기억되지 않은 건가...)"
    m "(타임슬립... 내가 시간을 되돌린 건가...? 아니면... 인하와 관련된 어떤 현상?)"
    m "인하... 네가... 내가 시간을 되돌린 거랑 관련이 있는 건가?"

    show a_in at Pright # 인하 더 당황하거나 슬픈 표정
    i "[player_name]... 무슨 소리야? 시간을 되돌리다니..."
    i "나는... 나는 아무것도 몰라..."
    i "다만... 다만 [player_name]을 볼 때마다... 이상한 기분이 드는 건 사실이야."
    i "마치... 아주 오래전부터 알고 지낸 사람처럼..."

    m "(인하도 뭔가 느끼고 있어... 역시 인하가 열쇠인가?)"
    m "(이 타임슬립... 인하 때문에 일어나는 건가? 아니면... 인하를 구하기 위해 일어나는 건가?)"
    m "(만약... 만약 인하 때문에 타임슬립이 일어나는 거라면...)"
    m "(인하를 포기해야만 이 지긋지긋한 반복에서 벗어날 수 있는 걸까...? 이 더운 여름날처럼 끝없는 반복...)" # 여름 느낌
    m "(아니... 안 돼.)"
    m "(나는 인하가 좋아.)"
    m "(매미 소리가 아무리 시끄러워도, 햇살이 아무리 뜨거워도...)" # 여름 느낌
    m "(어제의 기억이 사라져도... 인하를 볼 때마다 다시 반해버릴 것 같아.)"
    m "(설령 이 시간이 반복된다 해도... 나는 인하를 만나고 싶어.)"

    show s_in at Pright # 인하를 바라보는 주인공
    i "[player_name]...?"

    m "[player_name] : 인하."
    m "[player_name] : 어쩌면... 이게 반복될지도 몰라."
    m "[player_name] : 내일이 오면... 나는 오늘 일을 기억 못 할 수도 있어."
    m "[player_name] : 그래도 괜찮다면..."

    show fad # 선택지 레이어
    menu:
        # "선택지 7" (최종 선택)
        "나는 네가 좋아. 매일 너에게 다시 반할 거야.":
            hide fad
            $ affection_i = 100 # 순애 엔딩! 애정도 MAX!
            jump pure_love_ending # 순애 엔딩 진입

        "어쩌면... 이게 마지막 기회일지도 몰라.":
            hide fad
            $ affection_i -= random.randint(10, 20) # 이별 암시, 애정도 하락
            jump sad_ending_choice # 슬픈 엔딩 선택 분기

label choice_6_repeat_action: # "어리둥절한 표정으로 쳐다본다" 선택 시 (하루 반복 루트)
    cn "(어리둥절한 표정으로 인하를 빤히 쳐다본다.)" # 어제와 똑같은 행동 연출

    # 어제와 똑같은 대화 반복
    show a_in at Pright # 인하 어쩔 줄 몰라하는 표정 (어제와 같은 반응)
    si "그렇게 빤히 보시면...\n"
    extend "저도 좀 부끄러운데요..."

    si "혹시... 글로벌 경영 2○학번 아니세요?"
    m "어? 맞는데? 어떻게 아셨어요?"
    # ... (어제와 같은 대화 흐름 반복)
    # 이름 입력받는 부분은 스킵하고 바로 이름 확인으로 넘어갈 수 있음 (이미 알고 있으므로)
    # m "아 제 이름은 [player_name](이)야."
    # si "아...! 맞다! [player_name]! 기억났어!"
    # si "내 이름은 인하야."
    # si "성이 인, 이름이 하 외자. 기억나지?!"
    # m "(인 하...? )"
    # m "(왜 기억이 안 나지? 아오...)"
    # si "ㅎㅎ... 그럴 수 있지~"

    cn "(결국... 어제와 똑같은 하루가 반복되었다.)"
    cn "(나는 인하에게 다시 낯선 사람처럼 대했고...)"
    cn "(인하는 나를 알아보지 못했다.)"
    cn "(마치... 끝없는 악몽처럼... 이 뜨거운 여름이 반복된다.)" # 여름 느낌

    jump looping_nightmare_ending # 반복 엔딩 진입

# ---------------------------------------------------------------------------
#                       엔딩 라벨들
# ---------------------------------------------------------------------------

# 순애 엔딩
label pure_love_ending:
    # TODO: 둘이 함께 있는 아름다운 여름 일러스트 필요 (I_1 재활용 가능)
    scene I_1 with dissolve # 둘이 함께 있는 아름다운 일러스트 (재활용 또는 새 일러스트)
    cn "(푸른 여름 하늘이 눈부시게 펼쳐져 있다. 시원한 바람이 불어온다.)" # 여름 느낌

    cn "(그 후로도... 시간은 가끔 우리를 괴롭혔다.)"
    cn "(아침이 오면... 어제의 내가 인하를 잊어버리는 날도 있었다.)"
    cn "(하지만 인하는 변함없이 내 곁에 있어주었고...)"
    cn "(나는 매일 다시 인하에게 첫눈에 반했다.)"
    cn "(마치 매일매일 새로운 여름을 만나는 것처럼...)" # 여름 느낌

    show i at Pright with fade # 인하 등장 (엔딩 일러스트 위에 보여줄 경우 위치/효과 조정)
    show m at Pleft with fade # 주인공 등장 (엔딩 일러스트 위에 보여줄 경우 위치/효과 조정)
    # 엔딩 대화 (스크립트 내용)
    i "[player_name], 오늘 날씨 진짜 좋다! 우리 저번에 가려다 못 간 카페 갈까?"
    m "좋지! 인하가 가자고 하면 어디든 좋아!"
    i "ㅎㅎ... [player_name]은 맨날 그렇게 나 좋다고 한다니까~"
    m "(바보야... 잊어버려도 다시 좋아지는 걸 어떡하라고...)"
    m "(매일매일 새로운 사랑을 하는 기분이야.)"

    cn "(두 사람의 웃음소리가 여름 하늘에 울려 퍼진다.)" # 여름 느낌

    cn "(시간의 반복 속에서...)"
    cn "(우리의 사랑은 계속해서 다시 피어났다.)"
    cn "(뜨거운 여름처럼... 영원히...)" # 여름 느낌

    $ complete_ending("PureLoveEnding") # 순애 엔딩 달성 업적/플래그
    return # 게임 종료 또는 엔딩 크레딧

# 슬픈 엔딩 선택 분기 -> 새드 엔딩 라벨로 이동
label sad_ending_choice:
    m "[player_name] : 인하... 아마도... 우리가 함께 있으면 이 반복은 끝나지 않을 거야."
    m "[player_name] : 너를 위해서... 그리고 나를 위해서..."
    m "[player_name] : 우리... 여기서 끝내자." # 이별 선언

    hide s_in # 인하 스탠딩 CG 숨김
    show a_in at Pright # 인하 충격받은 표정 (또는 슬픈 표정 SCG 사용)
    i "...[player_name]..."
    i "그게... 무슨 말이야...?"
    i "싫어... [player_name]...! 가지 마...!"

    m "(인하의 눈에서 눈물이 흘러내린다.)"
    m "(가슴이 찢어질 것 같다... 이게 맞는 걸까?)"
    m "(하지만... 이 지긋지긋한 반복을 끝내려면... 이 여름을 끝내려면...)" # 여름 느낌 추가

    cn "(결국... 나는 인하의 곁을 떠나기로 결심했다.)"

    scene lecture with fadeout # 강의실에서 홀로 남는 주인공 (떠나는 연출)
    m "나는 인하에게서 등을 돌렸다."
    m "들려오는 인하의 울음소리를 애써 무시하며..."
    m "나는... 시간을 초월한 사랑 대신... 평범한 일상으로 돌아가기로 선택했다."

    jump sad_ending # 새드 엔딩 라벨로 이동

# 새드 엔딩
label sad_ending:
    scene 1room with dissolve # 자취방으로 돌아옴 배경
    cn "(그리고 다음 날 아침.)"
    cn "(익숙한 천장이다. 창밖 매미 소리가 요란하다.)" # 여름 느낌
    m "익숙한 천장이다."
    m "어제 있었던... 이상한 일들은 모두 꿈이었던 것 같다."
    m "마치... 애초에 그런 일은 없었던 것처럼... 모든 기억이 깨끗하게 사라졌다."
    m "..."
    m "(왠지 모르게... 가슴 한구석이 허전하다.)"
    m "(뭔가... 아주 소중한 것을 잃어버린 기분...)"
    m "(하지만... 그것이 무엇이었는지... 아무리 생각해도 떠오르지 않는다.)"

    cn "(시간의 반복은 멈추었다.)"
    cn "(나는... 평범한 일상으로 돌아왔다.)"
    cn "(하지만... 그 대가로...)"
    cn "(가장 소중했을지도 모를 기억을...)"
    cn "(그리고 인하를... 영원히 잃어버렸다.)"
    cn "(그 여름날의 기억과 함께...)" # 여름 느낌 추가

    $ complete_ending("SadEnding") # 새드 엔딩 달성 업적/플래그
    return # 게임 종료 또는 엔딩 크레딧

# 하루 반복 엔딩 (배드 엔딩)
label looping_nightmare_ending:
    scene lecture # 강의실 배경 유지
    cn "(결국... 어제와 똑같은 하루가 반복되었다.)"
    cn "(나는 인하에게 다시 낯선 사람처럼 대했고...)"
    cn "(인하는 나를 알아보지 못했다.)"
    cn "(마치... 끝없는 악몽처럼... 이 뜨거운 여름이 반복된다.)" # 여름 느낌

    # 계속 반복되는 상황 암시 (간단히 텍스트로)
    cn "(몇 번의 아침이 더 밝아왔다.)"
    cn "(매번 같은 자취방에서 눈을 뜨고, 같은 강의실로 향한다.)"
    cn "(같은 낯선 사람의 혼잣말을 듣고, 같은 인하의 질문에 답한다.)"
    cn "(그리고...)"
    cn "(다시 밤이 되면... 모든 것이 리셋된다.)"
    cn "(이 여름은... 끝나지 않는다.)"
    cn "(영원히...)"

    
    $ complete_ending("LoopingNightmareEnding") # 반복 엔딩 달성 업적/플래그
    return # 게임 종료 또는 엔딩 크레딧

# ---------------------------------------------------------------------------
#                       코드 끝
# ---------------------------------------------------------------------------