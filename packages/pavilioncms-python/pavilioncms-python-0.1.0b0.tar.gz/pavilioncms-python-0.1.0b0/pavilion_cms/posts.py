from pavilion_cms.client import Client

class Posts(Client):
    def __init__(self, read_token):
        super().__init__(read_token)
    

    def all(self, params:dict = None) -> dict:
        url_path = f"{self.post_url}/all/"
        return self.make_list_request(url_path=url_path, params=params)

    def get(self, slug) -> dict:
        url_path = f"{self.post_url}/{slug}/"
        return self.make_single_request(url_path=url_path)