class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.dashboard = "#dashboard"

    def wait_loaded(self):
        self.page.wait_for_selector(self.dashboard, timeout=10000)
