import re
from selenium import webdriver
from PIL import Image
import requests
import datetime
from bs4 import BeautifulSoup
import time


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except:
            name = ' '.join(func.__name__.split('_'))
            print(f"Can't {name} from article")
            return None
    return inner_function

class ArticleScraper():
    """
    A class that allows you to get the necessary features for articles on the
    medium using the ``requests`` and ``BeautifulSoup`` technologies. 

    ## Problems and motivations:

    - the medium limits the number of articles without a membership;
    - subscription with Russian cards is not possible;
    - scraping requires a full page load, and when scraping > 700 articles, all sites addressed by medium start checking certificates. 
    This saves incognito mode and clearing the cache by ``Selenium``.
    """

    def __init__(self) -> None:
        self.scraper_class = 'ArticleScraper' 


    @exception_handler
    def __get_title(self, soup: BeautifulSoup) -> str:
        """
        The function that collects the title of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - title: str. The title of an article.
        """
        return soup.find('h1').text


    @exception_handler
    def __get_subtitle(self, soup: BeautifulSoup) -> str:
        """
        The function that collects the subtitle of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - subtitle: str. The subtitle of an article.
        """
        return soup.find('section').find('h2').text


    @exception_handler
    def __get_publication(self, soup: BeautifulSoup) -> str:
        """
        The function that collects the publication type of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - publication type: str. The publication type of an article.
        """
        for div in soup.find_all("div"):
            if div.text == 'Published in':
                try:
                    return div.next_element.next_element.next_element.find('p').text
                except:
                    continue


    @exception_handler
    def __get_author(self, soup: BeautifulSoup):
        """
        The function that collects the author of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - author: str. The author of an article.
        """
        return soup.find('h2', class_=r"pw-author-name").text


    @exception_handler
    def __get_reading_time(self, soup: BeautifulSoup):
        """
        The function that collects the reading time required for an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - reading time: str. The reading time required for an article.
        """
        return int(soup.find('div', class_=r"pw-reading-time").text.split()[0])


    @exception_handler
    def __get_claps(self, soup: BeautifulSoup) -> int:
        """
        The first function that collects the claps count of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - claps count: str. The claps count of an article.
        """
        claps = soup.find_all("div", {"class": "pw-multi-vote-count"})[0].text
        tens = {'K': 10e2, 'M': 10e5, 'B': 10e8, 'k': 10e2, 'm': 10e5, 'b': 10e8}
        if (claps[-1] != 'K' and claps[-1] != 'M' 
                    and claps[-1] != 'k' and claps[-1] != 'm'
                    and claps[-1] != 'b' and claps[-1] != 'B'):
                    return int(claps)
        f = lambda x: int(float(x[:-1])*tens[x[-1]])
        return f(claps)

    @exception_handler
    def __get_claps2(self, link: str) -> int:
        """
        The second type of function that collects the claps count of an article by simple request.

        ## Inputs: 
        - link: str. Link to the medium article.

        ## Returns:
        - claps count: str. The claps count of an article.
        """
        aditionalPage = requests.get(link).content.decode("utf-8")
        claps = aditionalPage.split("clapCount\":")[1]
        endIndex = claps.index(",")
        claps = int(claps[0:endIndex])
        return claps

    @exception_handler
    def __get_responses(self, soup: BeautifulSoup) -> int:
        """
        The function that collects the responses count of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - responses count: str. The responses count of an article.
        """
        responses = [x.text for x in soup.find_all("span") if x.has_attr("class") and 'pw-responses-count' in x['class']][0].split()[0]
        tens = {'K': 10e2, 'M': 10e5, 'B': 10e8, 'k': 10e2, 'm': 10e5, 'b': 10e8}
        if (responses[-1] != 'K' and responses[-1] != 'M' 
                    and responses[-1] != 'k' and responses[-1] != 'm'
                    and responses[-1] != 'b' and responses[-1] != 'B'):
                    return int(responses)
        f = lambda x: int(float(x[:-1])*tens[x[-1]])
        return f(responses)


    @exception_handler
    def __get_date(self, soup: BeautifulSoup) -> datetime.datetime:
        """
        The first function that collects the date an article was published from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - date: str. The date an article was published.
        """
        date_string = soup.find('p', class_=r"pw-published-date").text 
        try:
            date = datetime.datetime.strptime(date_string, '%b %d, %Y').strftime('%d/%m/%Y')
        except:
            date = datetime.datetime.strptime(date_string, '%b %d').strftime(f'%d/%m/{datetime.date.today().year}')
        return date 


    @exception_handler
    def __get_followers(self, soup: BeautifulSoup) -> int:
        """
        The function that collects the number of subscribers per article author from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - followers count: str. Number of subscribers per article author.
        """
        fol_string = [x.text for x in soup.find_all("span") if x.has_attr("class") and 'pw-follower-count' in x['class']][0].split()[0]
        tens = {'K': 10e2, 'M': 10e5, 'B': 10e8, 'k': 10e2, 'm': 10e5, 'b': 10e8}
        if (fol_string[-1] != 'K' and fol_string[-1] != 'M' 
                    and fol_string[-1] != 'k' and fol_string[-1] != 'm'
                    and fol_string[-1] != 'b' and fol_string[-1] != 'B'):
                    return int(fol_string)
        f = lambda x: int(float(x[:-1])*tens[x[-1]])
        return f(fol_string)


    @exception_handler
    def __get_mean_size(self, soup: BeautifulSoup) -> tuple[int, int]:
        """
        The function that calculates the average size of photos of an article html page its ``lxml`` parse.

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - mean: str. The average size of photos of an article.
        """
        pics = soup.find('section').find_all('img')
        sums = (0,0)
        for pic in pics:
            try:
                sums = (int(pic["width"]), int(pic["height"]))
            except:
                url = pic.get('src')
                if url:
                    im = Image.open(requests.get(url, stream=True).raw)
                    sums = tuple(map(sum, zip(sums, im.size)))
        mean = tuple(ti//len(pics) for ti in sums)
        if len(pics) == 0:
            return (0,0)
        return mean
         

    @exception_handler
    def __count_figures(self, soup: BeautifulSoup) -> int:
        """
        The function that counts the number of images on an article page from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - figures count: str. The number of images on an article page.
        """
        return len(soup.find('section').find_all('img'))


    @exception_handler
    def __get_pure_text(self, soup: BeautifulSoup) -> str:
        """
        The first function that collects the full text of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - pure text: str. The full text of an article.
        """
        pure_text = ''
        for unparsed in soup.find('section').find_all('p'):
            pure_text += unparsed.text
        return pure_text
    

    @exception_handler
    def __count_words(self, soup: BeautifulSoup) -> int:
        """
        The function that counts the words and syntax of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - count words: int. The amount of words and syntax.
        """
        pure_text = self.__get_pure_text(soup=soup)
        return len(pure_text.split())

    
    @exception_handler
    def __count_lists(self, soup: BeautifulSoup) -> int:
        """
        The function that counts the markered lists (bullet lists) of an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - lists count: int. The number of bullet lists.
        """
        return len(soup.find('section').find_all('ol')) + len(soup.find('section').find_all('ul'))
    

    @exception_handler
    def __bold_text_count(self, soup: BeautifulSoup) -> int:
        """
        The function that counts the number of blocks of bold text of an article from its ``lxml`` parse

        ## Inputs:
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - bold text count: int. The number of blocks of bold text of an article.
        """
        return len(soup.find('section').find_all('strong'))
    

    @exception_handler
    def __get_blockquotes(self, soup: BeautifulSoup) -> list[str]:
        """
        The function that collects the notes in an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - notes: list. The notes count of an article.
        """
        notes = []
        blockquotes = soup.find_all('blockquote')
        for blockquote in blockquotes:
            notes.append(blockquote.text)
        return notes


    @exception_handler
    def __italic_text_count(self, soup: BeautifulSoup) -> int:
        """
        The function that counts the number of blocks of italic text of an article from its ``lxml`` parse

        ## Inputs:
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - italic text count: int. The number of blocks of italic text of an article.
        """
        return len(soup.find('section').find_all('em'))


    @exception_handler
    def __count_vids(self, soup: BeautifulSoup) -> int:
        """
        The function that counts the number of videos on an article page from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - videos count: int. The number of videos on an article page.
        """
        yt_vids = []
        article_soup = soup.find('article')
        for figure in article_soup.find_all('figure'):
            yt_soup = figure.find('iframe', src=re.compile('.*youtube.*'))
            if yt_soup == None:
                continue
            else:
                yt_vids.append(yt_soup)
                
        return len(yt_vids)


    @exception_handler
    def __count_gists(self, soup: BeautifulSoup) -> int:
        """
        The function that collects the number of code gists in an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - gists: int. The code gists count in an article.
        """
        gists = []
        article_soup = soup.find('article')
        for fig in article_soup.find_all('figure'):
            gist_soup = fig.find('iframe', title=re.compile('.*\.py'))
            if gist_soup == None:
                continue
            else:
                gists.append(gist_soup)
        return len(gists)


    @exception_handler
    def __count_links(self, soup: BeautifulSoup) -> int:
        """
        The function that collects the number of references in an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - links: int. The number of references to other articles in an desired article.
        """
        links = []
        for a in soup.find('section').find_all('a'):
            link = a.get('href')
            if link != None:
                links.append(link)
        return len(links)


    @exception_handler
    def __count_code_chunks(self, soup: BeautifulSoup):
        """
        The function that collects the number of code chunks in an article from its ``lxml`` parse

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.

        ## Returns:
        - code chunks: int. The number of code chunks.
        """
        return len(soup.find_all('pre'))
    

    def scrape(self, soup: BeautifulSoup, link:str):
        """
        The function that calls all other private methods to scrape the following fields:

        - title: ``self.__get_title(soup)``,
        - publication: ``self.__get_publication(soup)``,
        - link: ``link``,
        - author: ``self.__get_author(soup)``,
        - followers: ``self.__get_followers(soup)``,
        - reading_time: ``self.__get_reading_time(soup)``,
        - n_words: ``self.__count_words(soup)``,
        - pure_text: ``self.__get_pure_text(soup)``,
        - blockquotes: ``self.get_blockquotes(soup)``,
        - date: ``self.__get_date(soup)``,
        - responses: ``self.__get_responses(soup)``,
        - n_code_chunks: ``self.__count_code_chunks(soup)``,
        - bold_text_count: ``self.__bold_text_count(soup)``,
        - italic_text_count: ``self.__italic_text_count(soup)``,
        - mean_image_width: ``self.__get_mean_size(soup)``,
        - mean_image_height: ``self.__get_mean_size(soup)``,
        - n_images: ``self.__count_figures(soup)``,
        - n_lists: ``self.__count_lists(soup)``,
        - n_gists: ``self.count_gists(soup)``,
        - n_vids: ``self.__count_vids(soup)``,
        - n_links: ``self.__count_links(soup)``,
        - claps: ``self.__get_claps(soup)``

        ## Inputs: 
        - soup: ``BeautifulSoup``. A data structure representing a parsed HTML or XML document.
        - link: str. Link to the medium article.

        ## Returns:
        - figures count: str. The number of images on an article page.

        ## Example 
        
        ```python
        page_url = link

        driver = webdriver.Edge(options=options)
        driver.get(page_url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        article_scrapper = ArticleScraper()
        res = article_scrapper.scrape(soup=soup, link=link)
        ```

        """
        im_size = self.__get_mean_size(soup)
        im_size = (None, None) if im_size == None else im_size
        claps = self.__get_claps2(link)
        claps = claps if claps else self.__get_claps(soup)
        article_data = {
            "title": self.__get_title(soup),
            "publication": self.__get_publication(soup),
            "link": link,
            "author": self.__get_author(soup),
            "followers": self.__get_followers(soup),
            "reading_time": self.__get_reading_time(soup),
            "n_words": self.__count_words(soup),
            "pure_text": self.__get_pure_text(soup),
            #"blockquotes": self.get_blockquotes(soup),
            "date": self.__get_date(soup),
            "responses": self.__get_responses(soup),
            "n_code_chunks": self.__count_code_chunks(soup),
            "bold_text_count": self.__bold_text_count(soup),
            "italic_text_count": self.__italic_text_count(soup),
            "mean_image_width": im_size[0],
            "mean_image_height": im_size[1],
            "n_images": self.__count_figures(soup),
            "n_lists": self.__count_lists(soup),
            #"n_gists": self.count_gists(soup),
            "n_vids": self.__count_vids(soup),
            "n_links": self.__count_links(soup),
            "claps": claps
        }
            
        return (article_data)


    @exception_handler
    def get_pure_text_(self, link: str, options: webdriver.edge.options) -> str:
        """
        The separate function to scrape only the full text of the article.

        ## Inputs: 
        - link: str. Link to the medium article.
        - options: webdriver.edge.options. Options for selenium webdriver

        ## Returns:
        - pure text: str. The full text of an article.
        """
        page_url = link

        driver = webdriver.Edge(options=options)
        driver.get(page_url)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'lxml')

        return self.__get_pure_text(soup=soup)


    @exception_handler
    def get_date_current_year_(self, link, options):
        page_url = link

        driver = webdriver.Edge(options=options)
        driver.get(page_url)
        time.sleep(0.2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        try:
            date_string = soup.find('p', class_=r"pw-published-date").text 
            return datetime.datetime.strptime(date_string, '%b %d').strftime(f'%d/%m/{datetime.date.today().year}')
        except:
            print("Couldn't get date from article.") 


    @exception_handler
    def get_date_(self, link, options):
        page_url = link

        driver = webdriver.Edge(options=options)
        driver.get(page_url)
        time.sleep(0.2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        return self.__get_date(soup=soup)