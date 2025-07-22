from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given("the user is logged in")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://todo.qacart.com/login")
    context.driver.find_element(By.ID, "email").send_keys("starlink@example.com")
    context.driver.find_element(By.ID, "password").send_keys("ana01220@STAR")
    context.driver.find_element(By.ID, "submit").click()
    time.sleep(2)

@when('the user adds a to-do item "{task}"')
def step_impl(context, task):
    context.task = task
    context.driver.find_element(By.CSS_SELECTOR, "svg[data-testid='add']").click()
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "input[data-testid='new-todo']").send_keys(task)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-newTask']").click()
    time.sleep(2)

@when('marks the item "{task}" as completed')
def step_impl(context, task):
    checkbox = context.driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox.click()
    time.sleep(1)

@when('deletes the item "{task}"')
def step_impl(context, task):
    delete_btn = context.driver.find_element(By.CSS_SELECTOR, "button[data-testid='delete']")
    delete_btn.click()
    time.sleep(2)

@then('the item "{task}" should no longer appear in the list')
def step_impl(context, task):
    elements = context.driver.find_elements(By.XPATH, f"//*[text()='{task}']")
    assert len(elements) == 0, f"Task '{task}' still appears in the list!"
    context.driver.quit()
