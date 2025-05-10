# achievements.rpy

init python:
    # 업적 데이터 구조 정의
    achievements = {
        "f1": {"name": '"시작이 반"', "description": "게임을 시작했습니다.", "completed": False},
        "f2": {"name": '"호감상"', "description": "상대방이 첫 만남부터 호감을 느낍니다.", "completed": False},
        "f3": {"name": '"작명가"', "description": "이름을 지었습니다.", "completed": False},
        "f4": {"name": '"네 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f5": {"name": '"다섯 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f6": {"name": '"여섯 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f7": {"name": '"일곱 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f8": {"name": '"여덟 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f8": {"name": '"아홉 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f9": {"name": '"열 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f10": {"name": '"열한 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f11": {"name": '"열두 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f12": {"name": '"열세 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f13": {"name": '"열네 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
        "f14": {"name": '"열다섯 번째 업적"', "description": "게임을 시작했습니다.", "completed": False},
    }

    endings = {
        "e1": {"name": '"수상한 그녀"', "description": "처음? 본 그녀가 갑자기 말을건다.", "image": "images/ending/test.png", "completed": False},
        "e2": {"name": '"호감상"', "description": "상대방이 첫 만남부터 호감을 느낍니다.",  "image": "images/ending/test.png", "completed": False},
        "e3": {"name": '"작명가"', "description": "자기 이름을 지었습니다.",  "image": "images/ending/test.png", "completed": False},
        "e4": {"name": '"네 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e5": {"name": '"다섯 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e6": {"name": '"잠수함"', "description": "과제를 같이하기로 한 형의 별명이 '잠수함'이었다는 사실을 잊고있었다.",  "image": "images/ending/test.png", "completed": False},
        "e7": {"name": '"일곱 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e8": {"name": '"여덟 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e8": {"name": '"아홉 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e9": {"name": '"열 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e10": {"name": '"열한 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e11": {"name": '"열두 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e12": {"name": '"열세 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e13": {"name": '"열네 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
        "e14": {"name": '"열다섯 번째 업적"', "description": "게임을 시작했습니다.",  "image": "images/ending/test.png", "completed": False},
    }

    # 업적 완료 함수
    def complete_achievement(achievement_id):
        if achievement_id in achievements and not achievements[achievement_id]["completed"]:
            achievements[achievement_id]["completed"] = True
            renpy.notify(f"업적 달성! {achievements[achievement_id]['name']}")

    # 엔딩 함수
    def complete_ending(ending_id):
        if ending_id in endings and not endings[ending_id]["completed"]:
            endings[ending_id]["completed"] = True
            renpy.notify(f"일러스트 해금! {endings[ending_id]['name']}")
