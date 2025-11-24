import mastermind

def test_generate_secret_length():
    secret = mastermind.generate_secret()
    assert len(secret) == 4
    assert len(set(secret)) == 4  # all digits different

def test_check_guess_perfect_match():
    assert mastermind.check_guess("1234", "1234") == "****"

def test_check_guess_partial():
    # 1 correct place, 2 correct but wrong place
    assert mastermind.check_guess("2153", "2715") == "*++"

def test_check_guess_none():
    assert mastermind.check_guess("1234", "5678") == ""
