from django.test import TestCase


# from django_selenium_clean import selenium, SeleniumTestCase, PageElement

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(name='first todo', completed=False)
    
    def test_name_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.name}'
        self.assertEquals(expected_object_name, 'first todo')
    
    def test_completed_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_completed= todo.completed
        self.assertEquals(expected_object_completed, False)

class TestUI(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.headless = True 
        cls.selenium = WebDriver(options=options,executable_path=r'./geckodriver.exe')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_crud(self):
        self.selenium.get("http://127.0.0.1:8000/")
        # self.selenium.set_window_size(915, 472)
        # self.selenium.find_element(By.ID, "__BVID__7").click()
        # self.selenium.find_element(By.ID, "__BVID__7").send_keys("Teste")
        # self.selenium.find_element(By.CSS_SELECTOR, "form").click()
        # self.selenium.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # self.selenium.find_element(By.CSS_SELECTOR, ".list-group:nth-child(3) input").click()
        # self.selenium.find_element(By.CSS_SELECTOR, ".list-group:nth-child(3) > .list-group-item").click()
        # self.selenium.find_element(By.CSS_SELECTOR, ".list-group:nth-child(3) input").click()
        # self.selenium.find_element(By.CSS_SELECTOR, ".list-group:nth-child(3) .btn").click()