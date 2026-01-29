def test_hello_prints_expected_text(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, DevOps learner!"

def test_bye_prints_expected_text(capsys):
    bye()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Goodmorning!"

