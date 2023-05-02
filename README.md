Certainly, here's a README markdown file explaining the code I provided:

# Using Biopython to Get PubMed ID and Create NLP Summaries for PubMed Articles

This code utilizes Biopython and spaCy to extract PubMed ID and create NLP summaries for PubMed articles. The pipeline is divided into the following steps:

1. Use Biopython's Entrez API to search for and retrieve PubMed IDs for a given search query.
2. Download the PubMed article XML files corresponding to each retrieved PubMed ID from an Amazon S3 bucket.
3. Parse the article XML files using Biopython's `Medline` module to extract the article text.
4. Process the article text using spaCy's NLP pipeline to generate a summary of the article.
5. Save the summary in a CSV file named after the original article file.

## Getting Started

To get started, you'll need to have the following prerequisites installed:

1. Python 3
2. Biopython
3. spaCy
4. An AWS account with access to an S3 bucket containing PubMed article XML files.

You can install the necessary Python packages using pip by running the following command:

```bash
pip install biopython spacy
```

You'll also need to download the spaCy English language model by running the following command:

```bash
python -m spacy download en_core_web_sm
```

## Usage

Once you have the prerequisites installed, you can run the code by running the `main.py` script in the project directory. Before running the script, you'll need to modify the following variables in the `main.py` file to match your AWS S3 bucket and PubMed search query:

```python
S3_BUCKET = "your-s3-bucket-name"
SEARCH_QUERY = "your-pubmed-search-query"
```

After setting these variables, you can run the script by navigating to the project directory in your terminal and running:

```bash
python main.py --> rename later!
```

This will search PubMed for articles matching your search query, download the corresponding article XML files from your S3 bucket, process the article text using spaCy, and generate a summary CSV file for each article in the `text` directory.
