class JobCardPage:
    def __init__(self, page):
        self.page = page
        self.new_jobcard_button = "text='New Job Card'"
        self.customer_input = "input[name='customer']"
        self.vehicle_input = "input[name='vehicle']"
        self.service_input = "input[name='service']"
        self.submit_button = "button[type='submit']"
        self.success_message = "text='Job Card Created Successfully'"

    def go_to_new_jobcard(self):
        self.page.click(self.new_jobcard_button)

    def fill_jobcard(self, customer, vehicle, service):
        self.page.fill(self.customer_input, customer)
        self.page.fill(self.vehicle_input, vehicle)
        self.page.fill(self.service_input, service)

    def submit_jobcard(self):
        self.page.click(self.submit_button)

    def wait_for_success(self):
        self.page.wait_for_selector(self.success_message, timeout=10000)
