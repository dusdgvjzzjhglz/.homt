from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 基础配置（需要自行修改）
USERNAME = "your_username"
PASSWORD = "your_password"
LOGIN_URL = "https://your-school-portal/login"
RESOURCE_URL = "https://your-school-portal/resources"

# 初始化浏览器驱动
driver = webdriver.Chrome()  # 需要先安装ChromeDriver
wait = WebDriverWait(driver, 20)

def login():
    driver.get(LOGIN_URL)
    
    # 输入用户名密码（根据实际页面元素修改选择器）
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    
    # 提交登录（可能需要修改选择器）
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    time.sleep(3)  # 等待登录完成

def browse_resources():
    driver.get(RESOURCE_URL)
    
    # 获取资源列表（需要根据实际页面结构修改）
    resources = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, ".resource-item a"))
    )
    
    # 遍历浏览每个资源
    for index, resource in enumerate(resources):
        print(f"正在浏览第 {index+1}/{len(resources)} 个资源")
        resource.click()
        
        # 模拟停留时间（随机防检测）
        time.sleep(abs(5 + (index % 3)))
        
        # 返回资源列表页
        driver.back()
        time.sleep(1)

if __name__ == "__main__":
    try:
        login()
        browse_resources()
    finally:
        driver.quit()