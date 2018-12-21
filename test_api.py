def func():
    print("Passed!")
    return "Passed!"


def test_answer():
    assert func() == "Passed!"
