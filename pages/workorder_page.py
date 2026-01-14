class WorkOrderPage:
    def __init__(self, page):
        self.page = page
        self.new_workorder_button = "text='New Work Order'"
        self.customer_input = "input[name='customer']"
        self.jobcard_input = "input[name='jobcard']"
        self.task_input = "input[name='task']"
        self.submit_button = "button[type='submit']"
        self.success_message = "text='Work Order Created Successfully'"

    def go_to_new_workorder(self):
        self.page.click(self.new_workorder_button)

    def fill_workorder(self, customer, jobcard, task):
        self.page.fill(self.customer_input, customer)
        self.page.fill(self.jobcard_input, jobcard)
        self.page.fill(self.task_input, task)

    def submit_workorder(self):
        self.page.click(self.submit_button)

    def wait_for_success(self):
        self.page.wait_for_selector(self.success_message, timeout=10000)
