import pandas as pd
from Bio import Entrez
import boto3
import os
from tqdm import tqdm
import multiprocessing as mp

### search pubmed for pubmed ids
def search_pubmed(keywords):
    # Set the email for Entrez
    Entrez.email = "your_email@example.com"
    query = ' AND '.join(keywords)
    keywords.extend([query])
    # Initialize an empty list to store the IDs
    id_list = []
    
    # Loop through each keyword and retrieve a list of IDs
    for keyword in keywords:
        # Use the esearch function to retrieve the PubMed IDs
        handle = Entrez.esearch(db="pubmed", term=keyword, retmax=100000)
        record = Entrez.read(handle)
        id_list.extend(record["IdList"])
        
    return id_list

# define a function to download a single file from the S3 bucket
def download_file(file_name):
    # create an S3 client object
    s3 = boto3.client('s3')
    bucket_name = 'pmc-oa-opendata'
    prefix = 'oa_comm/txt/all/'
    
    try:
        # download the file from the S3 bucket
        s3.download_file(bucket_name, prefix + file_name, os.path.join('text', file_name))
        #s3.get_object(Bucket=bucket_name, Key=prefix+file_name)
        #print(f"File {file_name} downloaded from S3 bucket")
        return 1
    except Exception as e:
        # if the file is not available in the S3 bucket, print the error message
        #print(f"File {file_name} not available in S3 bucket. Error message: {e}")
        return 0
