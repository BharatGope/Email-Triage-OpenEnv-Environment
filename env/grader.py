def grade_easy(action, correct_label):
    return 1.0 if action.category == correct_label else 0.0


def grade_medium(action, correct_priority):
    if action.priority:
        return 1.0 if action.priority == correct_priority else 0.0
    return 0.0


def grade_hard(action, correct_label):
    score = 0.0

    # classification
    if action.category == correct_label:
        score += 0.5

    # response quality
    if action.response and len(action.response) > 10:
        score += 0.3

    # completion
    if action.mark_done:
        score += 0.2

    return round(score, 2)