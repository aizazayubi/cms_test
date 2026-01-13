def test_create_jobcard(login_page, dashboard_page, credentials, page):
    from pages.jobcard_page import JobCardPage

    # Login
    login_page.open(credentials["baseUrl"])
    login_page.login(credentials["username"], credentials["password"])
    dashboard_page.wait_loaded()

    # Go to Job Cards
    jobcard_page = JobCardPage(page)
    jobcard_page.go_to_new_jobcard()

    # Fill job card details
    jobcard_page.fill_jobcard(
        customer="Ali Khan",
        vehicle="Toyota Corolla",
        service="Full Service"
    )
    jobcard_page.submit_jobcard()
    jobcard_page.wait_for_success()

    print("Job Card creation test passed!")
