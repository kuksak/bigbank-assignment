from framework.webapp import webapp


def before_all(context):
    context.driver = webapp.get_driver()
    context.driver.set_page_load_timeout(10)
    context.driver.maximize_window()


def after_all(context):
    context.driver.quit()
