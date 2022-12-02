def rock_paper_scissors(strategy_guide):
    """calculates total score, rock paper scissors"""

    points = {
        "AX": 4,
        "AY": 8,
        "AZ": 3,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 7,
        "CY": 2,
        "CZ": 6,

    }

    score = 0

    data = open(strategy_guide)
    for line in data:
        game_result = line.replace(" ", "").rstrip()
        add_to_score = points.get(game_result)
        score += add_to_score
    
    print(score)
