import random

actions = ["Attack", "Guard", "Double"]

def get_score(p1, p2):
    # Attack vs Guard
    if p1 == "Attack" and p2 == "Guard":
        return (0, 1)
    if p2 == "Attack" and p1 == "Guard":
        return (1, 0)

    # Attack vs Double
    if p1 == "Attack" and p2 == "Double":
        return (2, -1)
    if p2 == "Attack" and p1 == "Double":
        return (-1, 2)

    # Double vs Guard
    if p1 == "Double" and p2 == "Guard":
        return (0, 0)
    if p2 == "Double" and p1 == "Guard":
        return (0, 0)

    # Double vs Double
    if p1 == "Double" and p2 == "Double":
        # 둘 다 성공
        return (2, 2)

    # Attack vs Attack / Guard vs Guard
    return (0, 0)

def play_game():
    p1_score = 0
    p2_score = 0

    print("=== 막고라 심리 대결 시작! ===")
    print("선택지: Attack / Guard / Double\n")

    for round_num in range(1, 6):
        print(f"--- 라운드 {round_num} ---")

        # 플레이어 1 입력
        p1 = input("당신의 선택: ").capitalize()
        while p1 not in actions:
            p1 = input("다시 입력 (Attack / Guard / Double): ").capitalize()

        # 플레이어 2 (컴퓨터) 랜덤 선택 (운빨 요소)
        p2 = random.choice(actions)
        print(f"상대의 선택: {p2}")

        # 점수 계산
        s1, s2 = get_score(p1, p2)
        p1_score += s1
        p2_score += s2

        print(f"라운드 결과 → 당신: {s1}점, 상대: {s2}점")
        print(f"현재 점수 → 당신: {p1_score} / 상대: {p2_score}\n")

    print("=== 최종 결과 ===")
    if p1_score > p2_score:
        print("🎉 당신의 승리! 꿀잼!")
    elif p1_score < p2_score:
        print("💀 상대 승리… 노잼…")
    else:
        print("🤝 무승부!")

play_game()
