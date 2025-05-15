
import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import PageNumberPaginator
from itertools import islice
import os

os.environ['EXTRACT__WORKERS'] = '7'
os.environ['NORMALIZE__WORKERS'] = '10'
os.environ['LOAD__WORKERS'] = '8'
os.environ['NORMALIZE__DATA_WRITER__BUFFER_MAX_ITEMS'] = '10000'

client = RESTClient(
  base_url="https://jaffle-shop.scalevector.ai/api/v1",
  paginator=PageNumberPaginator(
      base_page=1,                 # NewsAPI starts paging from 1
      page_param="page",           # Matches the API spec
      total_path=None,             # Set it to None explicitly
      stop_after_empty_page=True,  # Stop if no articles returned
      maximum_page=50          # Optional limit for dev/testing
  ),
)

def yield_chunks(iterable, chunk_size=1500):
    iterator = iter(iterable)
    while chunk := list(islice(iterator, chunk_size)):  # <--- we slice data into chunks
        yield chunk

@dlt.resource(write_disposition="replace", name="orders" , primary_key="id" ,parallelized=True)
def orders(client=client):

    for page in client.paginate("orders", json={"page_size":100}):
      yield from yield_chunks(page)

@dlt.resource(write_disposition="replace", name="customers" , primary_key="id" , parallelized=True)
def customers(client=client):

    for page in client.paginate("customers", json={"page_size":100}):
      yield from yield_chunks(page)


@dlt.source
def jaffleshop():
    return orders ,customers

pipeline = dlt.pipeline(
pipeline_name="orders_pipeline",
destination=dlt.destinations.duckdb("/Users/affanzafar/Desktop/datawarehouse/data-warehouse/data.duckdb"),
dataset_name="jaffleshop",
dev_mode=True,
)

if __name__ == "__main__":


    pipeline.run(jaffleshop())

