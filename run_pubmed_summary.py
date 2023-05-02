import pandas as pd
#from ____ import search_pubmed, download_file


pubmed_ids = search_pubmed(query)

# define the directory name
dir_name = "text"

# create the directory if it doesn't exist
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

# define the list of file names to download
file_list = ['PMC'+pubmed_ids[i]+'.txt' for i in range(len(pubmed_ids))]

# initialize the count of available files to 0
available_count = 0

# create a multiprocessing Pool with 4 worker processes
with mp.Pool(processes=8) as pool:
    # map the download_file function to the file list and get a list of results
    results = list(tqdm(pool.imap(download_file, file_list), total=len(file_list)))

# count the number of available files
available_count = sum(results)
print(f"{available_count} files available for download")
