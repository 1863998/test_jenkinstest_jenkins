import allure

class TestJenkins:
    @allure.step("测试步骤")
    def test_001(self):
        allure.attach("名称","附件中内容")
        assert True