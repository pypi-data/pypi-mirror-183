import requests
from requests_aws4auth import AWS4Auth

from add_disclaimers.utils.helpers  import get_attr



class AWSRequest:
    def __init__(self, config):

        aws_service = get_attr(config, 'aws_service', 'lambda')
        aws_region = get_attr(config, 'aws_region', 'us-east-1')
        aws_client_id = get_attr(config, 'aws_client_id', '')
        aws_client_secret = get_attr(config, 'aws_client_secret', '')
        endpoint = get_attr(config, 'endpoint', '')

        self.auth = AWS4Auth(aws_client_id, aws_client_secret, aws_region, aws_service)

     

  
    def request(self, endpoint, payload):
        response = requests.post(endpoint, data = payload, auth = self.auth)
        return response


