class Page:
    def __init__(self, response):
        self.status = response.status_code
        self.url = response.url
        self.content = response.text
