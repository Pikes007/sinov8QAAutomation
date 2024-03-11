import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    url = "https://redrabbit.rebaseventures.com/qa-automation/maintenance"
    driver.get(url)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
