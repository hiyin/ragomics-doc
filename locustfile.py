from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Set wait time between requests
    wait_time = between(1, 3)  # Random wait between 1 to 3 seconds

    # Define the host (base URL)
    host = "https://alpha.raganetwork.com"

    @task(1)  # Task with weight 1
    def load_home_page(self):
        """
        Simulates a user visiting the homepage
        """
        self.client.get("/")  # Requests the homepage
