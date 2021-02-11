from src.basic import Basic

obj = Basic()
class TestBasic:
    def test_basic_op1(self):
        assert obj.op1() == "ok"
    def test_basic_op2(self):
        assert obj.op2() == 3
          
