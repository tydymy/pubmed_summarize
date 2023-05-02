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
