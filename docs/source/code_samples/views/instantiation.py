from citrination_client import CitrinationClient
from os import environ

client = CitrinationClient(environ["CITRINATION_API_KEY"], environ["CITRINATION_SITE"])
data_views_client = client.data_views