import json

from utils.LogUtil import my_log

class AssertUtil:
    def __init__(self):
        self.log=my_log("AssertUtil")

    def assert_code(self,code,exprcted_code):
        try:
            assert int(code) ==int(exprcted_code)
            return True
        except:
            self.log.error("code error,code is %s,expected_code is %s"%(code,exprcted_code))
            raise
    def assert_body(self,body,exprcted_body):
        try:
            assert body == exprcted_body
            return True
        except:
            self.log.error("body error,body is %s,expected_body is %s" %(body, exprcted_body))
        raise
    def assert_in_body(self,body,exprcted_body):
        try:
            body=json.dumps(body)
            assert exprcted_body in body
            return True
        except:
            self.log.error("不包含或者body是错误,body is %s,expected_body is %s" %(body,exprcted_body))
        raise

