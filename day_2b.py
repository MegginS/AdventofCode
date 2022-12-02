def rock_paper_scissors_update(strategy_guide):
    """calculates total score, rock paper scissors"""

    points = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7
    }

    score = 0

    data = open(strategy_guide)
    for line in data:
        game_result = line.replace(" ", "").rstrip()
        add_to_score = points.get(game_result)
        score += add_to_score
    
    print(score)
