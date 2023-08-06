from selenium import webdriver
import time
import lxml
from bs4 import BeautifulSoup
from .scrapper import *
import csv 
import pandas as pd
from tqdm import tqdm
import _csv
import os
import threading
from selenium.webdriver.edge.options import Options
from typing import Union, Iterator 

columns = ['title', 'publication', 'link',  'author', 'followers', 
            'reading_time', 'n_words', 'pure_text', 'date', 
            'responses', 'n_code_chunks', 'bold_text_count', 
            'italic_text_count', 'mean_image_width', 'mean_image_height', 
            'n_images', 'n_lists', 'n_vids', 'n_links', 'claps']

def scrape_page(link: str, options: webdriver.edge.options, 
                csv_writer: '_csv.writer'=None, 
                compare: bool=False, idle_row: pd.Series=None) -> tuple[dict[str, Union[str, int, list[str]]], BeautifulSoup]:
    """
    The function that creates a webdriver, sends a request and scrapes per one link.

    ## Inputs: 
    - link: str. Link to the medium article.
    - options: webdriver.edge.options. Options for selenium webdriver.
    - csv_writer: '_csv.writer'. If not ``None``, then it will write the result explicitely in csv file.
    - compare: bool. If ``True``, then it will take ``idle_row`` 
            as an initial data and fill the impossible to scrap data as it was in initial data.
    - idle_row: pd.Series. Initial data. It works only in case if ``compare`` is ``True``

    ## Returns:
    - tuple[dict[str, Union[str, int, list[str]]], BeautifulSoup]. 
    
    ### The result of scrapping contains: 

    - title: ``str``,
    - publication: ``str``,
    - link: ``str``,
    - author: ``str``,
    - followers: ``int``,
    - reading_time: ``int``,
    - n_words: ``int``,
    - pure_text: ``str``,
    - blockquotes: ``list[str]``,
    - date: ``datetime.datetime``,
    - responses: ``int``,
    - n_code_chunks: ``int``,
    - bold_text_count: ``int``,
    - italic_text_count: ``int``,
    - mean_image_width: ``float``,
    - mean_image_height: ``float``,
    - n_images: ``int``,
    - n_lists: ``int``,
    - n_gists: ``int``,
    - n_vids: ``int``,
    - n_links: ``int``,
    - claps: ``int``


    ## Example of async using:

    ```py
    import csv
    import threading
    from medium_scrapper import *
    with open(path, "w", encoding="utf-8", newline="") as file:
    csv_writer = csv.writer(file)
    for chunk in tqdm(chunker(df, pools), total=df.shape[0] // pools):
        tasks = []
        for _, row in chunk.iterrows():
            tasks.append(threading.Thread(
                target=scrape_page, args=(
                    row["link"], options,
                    csv_writer, True, row, )))
            
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
    ```
    """
    
    page_url = link

    driver = webdriver.Edge(options=options)
    try:
        driver.get(page_url)
    except:
        print('Time out')
        res = {
            "title": None,
            "publication": None,
            "link": link,
            "author": None,
            "followers": None,
            "reading_time": None,
            "n_words": None,
            "pure_text": None,
            #"blockquotes": self.get_blockquotes(soup),
            "date": None,
            "responses": None,
            "n_code_chunks": None,
            "bold_text_count": None,
            "italic_text_count": None,
            "mean_image_width": None,
            "mean_image_height": None,
            "n_images": None,
            "n_lists": None,
            #"n_gists": self.count_gists(soup),
            "n_vids": None,
            "n_links": None,
            "claps": None
        }, 0
        if csv_writer:
            if compare:
                for col in idle_row.keys():
                    if res[col] == None:
                        res[col] = idle_row[col]
                        print(col, "filled by initial data")
            csv_writer.writerow(res.values())
        return res, 0
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    article_scrapper = ArticleScraper()
    res = article_scrapper.scrape(soup=soup, link=link)
    if csv_writer:
        if compare:
            for col in idle_row.keys():
                if res[col] == None:
                    res[col] = idle_row[col]
                    print(col, "filled by initial data")
        csv_writer.writerow(res.values())
    return res, soup


def scrap_articles_csv(df: pd.DataFrame,  
                columns: list=columns, options: webdriver.edge.options =None, rows: int=50,
                path: str="./scrapped_data/scrapped_data.csv") -> pd.DataFrame:
    """
    The function that takes links from an existing dataframe and scrapes everything into a separate dataframe

    ## Inputs: 
    - df: pd.DataFrame. DataFrame with links.
    - columns: list. Now it is merely columns to add to the csv, it can be upgraded into the columns to scrap.
    - options: webdriver.edge.options. Options for selenium webdriver.
    - rows: int. Frequency to save dataframe.
    - path: str. Path for csv file with desired articles. 


    ## Returns:
    - tuple[dict[str, Union[str, int, list[str]]], BeautifulSoup].  Scrapped information.
    """
    if os.path.exists(path):
        df_scrapped = pd.read_csv(path)
    else:
        df_scrapped = pd.DataFrame(columns=columns).to_csv()
    count = 0
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        res, _ = scrape_page(row['link'], options)
        print(count, df.shape[0])
        for col in df.columns:
            if res[col] == None:
                res[col] = row[col]
        df_scrapped.loc[df_scrapped.shape[0], :] = res   
        if (count % rows == 0 or count == df.shape[0] - 1):
            print("Saving to" + path)
            df_scrapped.to_csv(path, index=False)
        count += 1
    return df_scrapped

def chunker(seq, size) -> Iterator[pd.DataFrame]:
    for pos in range(0, len(seq), size):
        yield seq.iloc[pos:pos + size] 

def chunker_list(seq, size) -> Iterator[list[str]]:
    for pos in range(0, len(seq), size):
        yield seq[pos:pos + size] 


def scrap_articles_async(df:pd.DataFrame, 
                        options=None, columns:list=columns, pools:int=5,
                        path:str="./scrapped_data/scrapped_async_data_part3.csv") \
                            -> None:
    """
    The function that asynchronously takes links from an existing dataframe and scrapes everything into a separate dataframe

    ## Inputs: 
    - df: pd.DataFrame. DataFrame with links.
    - columns: list. Now it is merely columns to add to the csv, it can be upgraded into the columns to scrap.
    - options: webdriver.edge.options. Options for selenium webdriver.
    - pools: int. The number of the threads to use while algorithm working.
    - path: str. Path for csv file with desired articles. 


    ## Returns:
    - save data using csv.writer in the given path.
    """
    links = df["link"].values
    if not os.path.exists(path):
        pd.DataFrame(columns=columns).to_csv(path)
    with open(path, "w", encoding="utf-8", newline="") as file:
        csv_writer = csv.writer(file)
        for chunk in tqdm(chunker(df, pools), total=df.shape[0] // pools):
            tasks = []
            for _, row in chunk.iterrows():
                tasks.append(threading.Thread(target=scrape_page, args=(row["link"], options, csv_writer, True, row, )))
                
            for task in tasks:
                task.start()
            for task in tasks:
                task.join()

def scrap_articles_async_list(links:list, options=None, columns:list=columns, pools:int=5,
                              path:str="./scrapped_data/scrapped_async_data_part7.csv"):
    """
    The function that asynchronously takes links from an given lists and scrapes everything into a separate dataframe

    ## Inputs: 
    - links: list. list with links.
    - columns: list. Now it is merely columns to add to the csv, it can be upgraded into the columns to scrap.
    - options: webdriver.edge.options. Options for selenium webdriver.
    - pools: int. The number of the threads to use while algorithm working.
    - path: str. Path for csv file with desired articles. 


    ## Returns:
    - save data using csv.writer in the given path.
    """
    
    if not os.path.exists(path):
        pd.DataFrame(columns=columns).to_csv(path)
    with open(path, "w", encoding="utf-8", newline="") as file:
        csv_writer = csv.writer(file)
        for chunk in tqdm(chunker_list(links, pools), total=len(links) // pools):
            tasks = []
            for link in chunk:
                tasks.append(threading.Thread(target=scrape_page, args=(link, options, csv_writer, )))
                
            for task in tasks:
                task.start()
            for task in tasks:
                task.join()


def get_desired_options() -> webdriver.edge.options:
    """
    The function that returns desired options for scrap by selenium webdriver


    ## Returns:
    - options: webdriver.edge.options. Options for selenium webdriver
    """
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-insecure-localhost")
    options.add_argument("allow-running-insecure-content")
    options.add_argument("unsafely-treat-insecure-origin-as-secure")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return options

def get_columns():
    """
    Merely return standard columns 
    """
    return columns