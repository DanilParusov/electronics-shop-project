from src.keyboard import KeyBoard
def test_fifth_homework():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    assert kb.price == 9600
    assert kb.quantity == 5
