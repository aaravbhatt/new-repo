import requests
import json
import numpy as np
class Test:
    def __init__(self):
        self.api_url = "https://api.thecatapi.com/v1"
        self.headers = {"x-api-key": "23c2d002-3387-4b9c-a164-2a07e5d7120d"}
        pass
    
    
    
    # def upload_image(self, image_path, sub_id):
    #     url = self.api_url + "/images/upload"
    #     payload = {
    #     }
    #     response = requests.request(
    #         "POST", url, headers=self.headers, data=payload
    #     )
    #     if response.status_code >= 200 and response.status_code < 300:
    #         return json.loads(response.text)
    #     else:
    #         raise Exception(json.loads(response.text))
    
    # def create_vote(self, image_id, vote_value, sub_id=None):
    #     url = self.api_url + "/votes"
    #     payload = {
    #         "image_id": image_id,
    #         "sub_id": sub_id,
    #         "value": vote_value
    #     }
    #     response = requests.request(
    #         "POST", url, headers=self.headers, data=payload
    #     )
    #     if response.status_code >= 200 and response.status_code < 300:
    #         return json.loads(response.text)
    #     else:
    #         raise Exception(json.loads(response.text))
    
    """
    Only could attempt this GET operation as the other api modules
    required image_id. needs limit and page param to show categories
    """
    def get_categories(self, limit, page):
        limit = str(limit)
        page = str(page)
        url = self.api_url + "/categories?limit=" + limit + "&page=" + page
        print("limit:" + limit)
        print("page:" + page)
        print(url)
        payload = {}
        response = requests.request(
            "GET", url, headers=self.headers, data=payload
        )
        if response.status_code >= 200 and response.status_code < 300:
            return json.loads(response.text)
        else:
             raise Exception(json.loads(response.text))


             
mycat_class = Test()
#breed_name = mycat_class.get_breeds_siberian("sib")
#print(breed_name)


"""
attempted to print the array but was having difficulties- 
kept showing [None] even though the length was 1 but limit is 3
"""
categories = mycat_class.get_categories(3,1)
cat_len = len(categories)
print(cat_len)
print(categories)




#images = mycat_class.get_images()
#print(images)
#votes = mycat_class.create_vote("asf2", 1)
#votes = mycat_class.get_votes()
#print(votes)