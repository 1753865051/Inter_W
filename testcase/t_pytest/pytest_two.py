import pytest

class TestDemo:
    data_list=[("liyado","123456"),("aqy","123456")]

    @pytest.mark.parametrize(("name","password"),data_list)
    def test_a(self,name,password):
        print("test_a")
        print(name,password)
        assert 1

if __name__ == '__main__':
    pytest.main(["pytest_two.py"])