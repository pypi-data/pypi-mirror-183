from pavilion_cms.client import Client

class Tags(Client):
    def __init__(self, read_token):
        super().__init__(read_token)
    

    def all(self, params: dict = None) -> dict:
        url_path = f"{self.tag_url}/all/"
        return self.make_list_request(url_path, params)
    

    def get(self, tag_id) -> dict:
        url_path = f"{self.tag_url}/{tag_id}/view/"
        return self.make_single_request(url_path)