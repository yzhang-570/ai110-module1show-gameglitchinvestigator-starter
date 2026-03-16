from logic_utils import check_guess, get_range_for_difficulty, parse_guess

# --- parse_guess range validation ---

"""
Easy: 1-20
Normal: 1-100
Hard: 1-50

if out of range - returns false, None, and "out of range..."
"""

def test_parse_guess_valid_easy():
    ok, value, err = parse_guess("10", "Easy")
    assert ok and value == 10 and err is None

def test_parse_guess_valid_normal():
    ok, value, err = parse_guess("50", "Normal")
    assert ok and value == 50 and err is None

def test_parse_guess_valid_hard():
    ok, value, err = parse_guess("25", "Hard")
    assert ok and value == 25 and err is None

def test_parse_guess_below_range():
    ok, _, err = parse_guess("0", "Easy")
    assert not ok and err is not None

def test_parse_guess_above_range_easy():
    ok, _, err = parse_guess("21", "Easy")
    assert not ok and err is not None

def test_parse_guess_above_range_hard():
    ok, _, err = parse_guess("51", "Hard")
    assert not ok and err is not None

def test_parse_guess_at_lower_bound():
    ok, value, err = parse_guess("1", "Normal")
    assert ok and value == 1

def test_parse_guess_at_upper_bound_easy():
    ok, value, err = parse_guess("20", "Easy")
    assert ok and value == 20

def test_parse_guess_not_a_number():
    ok, _, err = parse_guess("abc", "Normal")
    assert not ok and err is not None

def test_parse_guess_empty():
    ok, _, err = parse_guess("", "Normal")
    assert not ok and err is not None


# --- check_guess tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"