import time
import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver(request):
    # Inicializa el webdriver
    chrome_driver_path = './Driver/chromedriver.exe'
    # Crea un servicio 
    chrome_service = ChromeService(chrome_driver_path)
    # Inicializa y maximiza el webdriver
    driver = webdriver.Chrome(service=chrome_service)    
    driver.maximize_window()

    def teardown():
        # Cierra el driver
        driver.quit()

    request.addfinalizer(teardown)
    return driver


@pytest.mark.usefixtures("driver")
class TestE2EOrdenDeCompra:
    
    @pytest.mark.order1
    def test_login(self, driver):
        driver.get('https://www.demoblaze.com/index.html')
        time.sleep(1)
        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
        login.click()  
        
        try:
            with open('data.json', 'r') as json_file:
                datoslogin = json.load(json_file)
            
        except Exception as e:
            pytest.fail(f"Error reading JSON file: {e}")
        
        
        username = datoslogin['username']
        password = datoslogin['password']
        
        userlogin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'loginusername')))
        userlogin.send_keys(username)
        driver.find_element(By.ID, 'loginpassword').send_keys(password)
        driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
        time.sleep(2)
        assert "Welcome " + username in driver.page_source


    @pytest.mark.order2
    def test_add_to_cart(self, driver):
        #Localiza y accede a la seccion Telefonos
        telefonos = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-3']//a[2]")))
        telefonos.click()
    
        # Localiza y clickea en un Telefono
        galaxy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Samsung galaxy s6']")))
        galaxy.click()
        
        # Agrega el telefono al carrito
        agregar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Add to cart")]')))
        agregar.click()
        
        # Verifica y acepta el mensaje de confirmación
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert 'Product added' in alert.text
        alert.accept()

        # Regresa a la pagina de inicio
        driver.get('https://www.demoblaze.com/index.html')

        # Localiza y accede a la seccion Laptops
        laptops = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-3']//a[3]")))
        laptops.click()
            
        # Localiza y clickea en una computadora
        time.sleep(1) #algo raro ocurre en este wait, necesito decifrar porque falla el wait.

        vaio = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sony vaio i5']")))
        vaio.click()
        
        # Agrega la computadora al carrito
        agregar = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Add to cart")]')))
        agregar.click()
        

        # Verifica y acepta el mensaje de confirmación
        alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert 'Product added' in alert.text
        alerta.accept()    

        # Regresa a la pagina de inicio
        driver.get('https://www.demoblaze.com/index.html')

        # Localizar y acceder a la seccion Monitores
        monitores = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-3']//a[4]")))
        monitores.click()

        # Localiza y clickea un Monitor
        Apple = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Apple monitor 24']")))
        Apple.click()

        # Agrega un monitor al carrito
        agregar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Add to cart")]')))
        agregar.click()

        # Verifica y acepta el mensaje de confirmación
        alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
        assert 'Product added' in alert.text
        alerta.accept()

        # Accede al carrito
        carrito = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'cartur')))
        carrito.click()

        # Verifica que el carrito contenga tres items
        time.sleep(1)
        items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr')))
        assert len(items) == 3

        # Lista los nombres de los articulos previamente seleccionados
        items_agregados = ["Samsung galaxy s6", "Sony vaio i5", "Apple monitor 24"]

        # Extrae los nombres de los items en el carrito y los normaliza para agregarlos a una lista de comparacion
        items_carrito = []

        for item in items:
            nombre_item = item.find_element(By.XPATH, './td[2]')  
            nombre = nombre_item.text
            nombre_normalizado = nombre.strip() 
            items_carrito.append(nombre_normalizado)

        # Verifica que los items en el carrito sean los deseados
        assert all(item in items_carrito for item in items_agregados)

    @pytest.mark.order3
    def test_checkout(self, driver):
        # Localiza y clickea el boton de Checkout
        checkout= driver.find_element(By.XPATH, '//button[normalize-space()="Place Order"]')
        checkout.click()
        try:
            with open('data.json', 'r') as json_file:
                datos = json.load(json_file)
        
        except Exception as e:
            raise Exception(f"Error reading JSON file: {e}")
        
        # Fill out the checkout form (assuming form fields by ID, please adjust as needed)
        time.sleep (1)
        name_input = driver.find_element(By.ID, 'name')
        name_input.send_keys(datos['Nombre'])

        country_input = driver.find_element(By.ID, 'country')
        country_input.send_keys(datos['Pais'])

        city_input = driver.find_element(By.ID, 'city')
        city_input.send_keys(datos['Ciudad'])

        card_input = driver.find_element(By.ID, 'card')
        card_input.send_keys(datos['Tarjeta'])

        month_input = driver.find_element(By.ID, 'month')
        month_input.send_keys(datos['Mes'])

        year_input = driver.find_element(By.ID, 'year')
        year_input.send_keys(datos['Ao'])

        # Completa la orden
        purchase_button = driver.find_element(By.XPATH, '//button[normalize-space()="Purchase"]')
        purchase_button.click()

        # Espera al mensaje de confirmacion
        time.sleep(1)
        botonOK = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))

        # Verifica que se despliege el numero de tarjeta de credito correcto
        alert= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='lead text-muted ']")))
        alert_text = alert.text
        print (alert_text)
        assert datos['Tarjeta'] in alert_text, f"Expected text '{datos['Tarjeta']}' not found in paragraph: '{alert_text}'"

        # Cierra el pop-up
        botonOK.click()

        time.sleep(5)


