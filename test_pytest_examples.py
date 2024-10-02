import pytest

class TestPytestExamples:
    
    # Basic test example
    def test_basic_example(self):
        assert 1 + 1 == 2
    
    # Test using fixture
    @pytest.fixture
    def sample_data(self):
        return {"name": "Jinal", "age": 30}

    def test_with_fixture(self, sample_data):
        assert sample_data["name"] == "Jinal"
        assert sample_data["age"] == 30

    # Test using parametrize
    @pytest.mark.parametrize("input, expected", [
        (1 + 2, 3),
        (2 * 2, 4),
        (5 - 2, 3)
    ])
    def test_parametrize(self, input, expected):
        assert input == expected

    # Test string methods
    def test_string_upper(self):
        assert "jinal".upper() == "JINAL"

    def test_string_isupper(self):
        assert "JINAL".isupper()
        assert not "jinal".isupper()

    # Test splitting a string
    def test_string_split(self):
        assert "hello world".split() == ["hello", "world"]

    # Test skipping a test
    @pytest.mark.skip(reason="Feature not yet implemented")
    def test_skip_example(self):
        assert False

    # Test handling exception
    def test_raises_exception(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0

    # Test with screenshot functionality (mock example)
    def test_screenshot_functionality(self):
        # Imagine this function simulates taking a screenshot
        result = self.screenshot_simulation()
        assert result == "screenshot_taken"

    def screenshot_simulation(self):
        # Mock function to simulate a screenshot
        return "screenshot_taken"
