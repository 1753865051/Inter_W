import pytest

class TestDemo:
    data_list=["liyado","aqy"]

    @pytest.mark.parametrize("name",data_list)
    def test_a(self,name):
        print("test_a")
        print(name)
        assert 1

if __name__ == '__main__':
    pytest.main(["pytest_one.py"])