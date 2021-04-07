from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import json

from .models import Todo


class TodoModelTest(TestCase):
    """
    Testes Unitários: Verificando se o objeto Todo é montado e tem o comportamento esperado
    """
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

class CrudTest(TestCase):
    """
    Teste de Integração: Testando se as funcionalidades do CRUD rodam na imagem do docker
    """
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/api/v1/'

    def test_get_todos(self):
        response = requests.get(self.url)
        self.assertEquals(response.status_code, 200)


    def test_crud_todo(self):
        response_create = requests.post(self.url,data={'name':'teste de criacao'})
        test_todo_id = json.loads(response_create.content)['id']
        test_todo_name = json.loads(response_create.content)['name']
        status_create = response_create.status_code
        status_read = requests.get('{}{}/'.format(self.url,test_todo_id)).status_code
        status_update = requests.put('{}{}/'.format(self.url,test_todo_id),{'name':test_todo_name,'completed':'true'}).status_code
        status_delete = requests.delete('{}{}/'.format(self.url,test_todo_id)).status_code
        self.assertEquals(status_create, 201)
        self.assertEquals(status_read, 200)
        self.assertEquals(status_update, 200)
        self.assertEquals(status_delete, 204)
        


class TestUI(StaticLiveServerTestCase):
    """
        Teste Funcional: Verificando se a interface do usuário é montada e funciona de acordo
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        # options.headless = True 
        options.headless = False
        cls.selenium = WebDriver(options=options,executable_path=r'./geckodriver.exe')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_header(self):
        self.selenium.get("http://127.0.0.1:8000/")
        self.selenium.set_window_size(915, 472)
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item").click()
        self.selenium.find_element(By.CSS_SELECTOR, ".nav-item").click()
        self.selenium.find_element(By.CSS_SELECTOR, ".card-title").click()
        elements = self.selenium.find_elements(By.CSS_SELECTOR, ".nav-item")
        assert len(elements) > 0
        
    
    def test_text_field(self):
        self.selenium.get("http://127.0.0.1:8000/")
        self.selenium.set_window_size(915, 472)
        self.selenium.find_element(By.ID, "__BVID__7").click()
        self.selenium.find_element(By.ID, "__BVID__7").send_keys("Teste")
        value = self.selenium.find_element(By.ID, "__BVID__7").get_attribute("value")
        assert value == "Teste"
        self.selenium.find_element(By.CSS_SELECTOR, "form").click()
        self.selenium.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        self.selenium.find_element(By.ID, "__BVID__7").click()
        self.selenium.find_element(By.ID, "__BVID__7").send_keys("novo teste")
        self.selenium.find_element(By.ID, "app").click()
        value = self.selenium.find_element(By.ID, "__BVID__7").get_attribute("value")
        assert value == "novo teste"