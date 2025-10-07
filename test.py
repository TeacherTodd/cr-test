import subprocess


def test_hello_world():
    """Test that main.py prints 'Hello World.'"""
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello World."
    assert result.returncode == 0
