#!/usr/bin/python3
import requests
import random
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from enum import Enum
from urllib.parse import parse_qs
# From this module
from rule34Py.api_urls import API_URLS, __base_url__
from rule34Py.__vars__ import __headers__, __version__
from rule34Py.post import Post
from rule34Py.post_comment import PostComment
from rule34Py.icame import ICame
from rule34Py.stats import Stat
from rule34Py.toptag import TopTag

class Stats:
    def __get_top(self, name):
        """Get Top Taggers
        Args:
            name: Top 10 taggers | Top 10 commenters | Top 10 forum posters
                  Top 10 image posters | Top 10 note editors | Top 10 favoriters
        Returns:
            list: List of Stat Class
        """
        retList = []
        response = requests.get(API_URLS.STATS.value, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_topchart = []

        if res_status != 200 or res_len <= 0:
            return []

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
        tables = bfs_raw.select(".toptencont > table")

        for table in tables:
            title = table.select("thead > tr")[0].get_text(strip=True)

            if title == name:
                trs = table.find("tbody").find_all("tr")

                for tr in trs:
                    tds = tr.find_all("td")
                    # 1 = Place
                    # 2 = Count
                    # 3 = Username
                    retList.append(Stat(tds[0].get_text(strip=True), tds[1].get_text(strip=True), tds[2].get_text(strip=True)))
                    #print(f"{tds[0].get_text(strip=True)} - {tds[1].get_text(strip=True)} - {tds[2].get_text(strip=True)}")
        return retList

    def top_taggers(self):
        """Get the top 10 Taggers of the Day

        Returns:
            list: List of Stat Class
        """
        return self.__get_top("Top 10 taggers")

    def top_commenters(self):
        """Get the top 10 Commenters of the Day

        Returns:
            list: List of Stat Class
        """
        return self.__get_top("Top 10 commenters")

    def top_forum_posters(self):
        """Get the top 10 Forum Posters of the Day

        Returns:
            list: List of Stat Class
        """
        return self.__get_top("Top 10 forum posters")

    def top_image_posters(self):
        """Get the top 10 Image Posters of the Day

        Returns:
            list: List of Stat Class
        """
        return self.__get_top("Top 10 image posters")

    def top_note_editors(self):
        """Get the top 10 Note Editors of the Day

        Returns:
            list: List of Stat Class
        """
        return self.__get_top("Top 10 note editors")

    def top_favorites(self):
        """Get the top 10 Favorites of the Day

        Returns:
            list: List of Stat Class
        """
        return self.__get_top("Top 10 favoriters")

# Main Class
class rule34Py(Exception):
    """rule34.xxx API wraper
    """

    def __init__(self):
        """rule34.xxx API wraper
        """
        self.__isInit__ = False
        self.stats = Stats()

    def search(self, tags: list, page_id: int = None, limit: int = 1000, deleted: bool = False,ignore_max_limit: bool = False) -> list:
        """Search for posts

        Args:
            tags (list[str]): Search tags
            page_num (int, optional): Page ID
            ignore_max_limit (bool, optional): If max value should be ignored
            limit (int, optional): Limit for Posts. Max 1000.

        Returns:
            list: Posts result list [empty if error occurs]

        API Docs: https://rule34.xxx/index.php?page=help&topic=dapi
        Tags Cheatsheet: https://rule34.xxx/index.php?page=tags&s=list
        """

        # Check if "limit" is in between 1 and 1000
        if not ignore_max_limit and limit > 1000 or limit <= 0:
            raise Exception("invalid value for \"limit\"\n  value must be between 1 and 1000\n  see for more info:\n  https://github.com/b3yc0d3/rule34Py/blob/master/DOC/usage.md#search")
            return

        params = [
            ["TAGS", "+".join(tags)],
            ["LIMIT", str(limit)],
        ]
        url = API_URLS.SEARCH.value
        # Add "page_id"
        if page_id != None:
            url += f"&pid={{PAGE_ID}}"
            params.append(["PAGE_ID", str(page_id)])

        
        if deleted:
            raise Exception("To include deleted images is not Implemented yet!")
            #url += "&deleted=show"

        formatted_url = self._parseUrlParams(url, params)
        response = requests.get(formatted_url, headers=__headers__)
        
        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        # checking if status code is not 200
        # (it's useless currently, becouse rule34.xxx returns always 200 OK regardless of an error)
        # and checking if content lenths is 0 or smaller
        # (curetly the only way to check for a error response)
        if res_status != 200 or res_len <= 0:
            return ret_posts

        for post in response.json():
            pFileUrl = post["file_url"]
            pHash = post["hash"]
            pId = post["id"]
            pScore = post["score"]
            pSize = [post["width"], post["height"]]
            pOwner = post["owner"]
            pTags = post["tags"].split(" ")

            ret_posts.append(Post(pId, pHash, pScore, pSize, pFileUrl, pOwner, pTags))

        return ret_posts

    def get_comments(self, post_id: int) -> list:
        """Get comments of given Post

        Args:
            post_id (int): Post id

        Returns:
            list: List of PostComment [empty if error occurs]
        """

        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.COMMENTS, params) # Replaceing placeholders
        response = requests.get(formatted_url, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_comments = []

        if res_status != 200 or res_len <= 0:
            return ret_comments

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="xml")
        res_xml = bfs_raw.comments.findAll('comment')

        # loop through all comments
        for comment in res_xml:
            attrs = dict(comment.attrs)
            ret_comments.append(PostComment(attrs["id"], attrs["creator_id"], attrs["body"], attrs["post_id"], attrs["created_at"]))

        return ret_comments

    # TODO: solve the hcaptcher on login page
    # def get_favorites(self, user_id: int, fast: bool = False):
    #     """Get favorites from users
    #
    #     Args:
    #         user_id (int): Id of user
    #         fast (bool): If set to true, only Ids of the posts are returned
    #
    #     Returns:
    #         list: List of Posts (List of ids if "fast" true)
    #     """
    #
    #     return
    #
    #     params = [
    #         ["USER_ID", str(user_id)],
    #     ]
    #
    #     formatted_url = self._parseUrlParams(API_URLS.USER_PAGE.value, params)
    #     response = requests.get(formatted_url, headers=__headers__) # Sending get request
    #
    #     res_status = response.status_code
    #     res_len = len(response.content)
    #     html_string = response.content.decode("utf-8")
    #     ret_favorites = []
    #
    #     if res_status != 200 or res_len <= 0:
    #         return ret_favorites
    #
    #     soup = BeautifulSoup(html_string, "html.parser")
    #     for span in soup.find_all('span', {'class' : 'thumb'}):
    #         print(span["id"][1:])

    def get_pool(self, pool_id: int, fast: bool = True) -> list:
        """Get Pool by Id
        Be aware that if "fast" is set to False, it takes extreme long.

        Args:
            pool_id (int): Id of pool
            fast (bool, optional): If true, returns only post ids

        Returns:
            list: List of Post Objects/id Strings [empty if error occurs]
        """

        params = [
            ["POOL_ID", str(pool_id)]
        ]
        response = requests.get(self._parseUrlParams(API_URLS.POOL.value, params), headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        if res_status != 200 or res_len <= 0:
            return ret_posts

        soup = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")

        for div in soup.find_all("span", class_="thumb"):
            a = div.find("a")
            id = div["id"][1:]

            if fast == True:
                ret_posts.append(id)
            else:
                ret_posts.append(self.get_post(id))

        return ret_posts

    def get_post(self, post_id: int) -> Post:
        """Get Post by Id

        Args:
            id (int): Id of post

        Returns:
            post: Post Object [empty if error occurs]
        """

        params = [
            ["POST_ID", str(post_id)]
        ]
        formatted_url = self._parseUrlParams(API_URLS.GET_POST.value, params)
        response = requests.get(formatted_url, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_posts = []

        if res_status != 200 or res_len <= 0:
            return ret_posts

        for post in response.json():
            pFileUrl = post["file_url"]
            pHash = post["hash"]
            pId = post["id"]
            pScore = post["score"]
            pSize = [post["width"], post["height"]]
            pOwner = post["owner"]
            pTags = post["tags"].split(" ")

            ret_posts.append(Post(pId, pHash, pScore, pSize, pFileUrl, pOwner, pTags))

        return ret_posts if len(ret_posts) > 1 else (ret_posts[0] if len(ret_posts) == 1 else ret_posts)

    def icame(self, limit: int = 100) -> list:
        """Gets a list of the top 100 "came-on characters"

        Args:
            limit (int): Limit of returned items (default 100)

        Returns:
            list: Returns list of ICame Objects [empty if error occurs]
        """

        response = requests.get(API_URLS.ICAME.value, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_topchart = []

        if res_status != 200 or res_len <= 0:
            return ret_topchart

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
        rows = bfs_raw.find("table", border=1).find("tbody").find_all("tr")

        for row in rows:
            if row == None:
                continue

            character_name = row.select('td > a', href=True)[0].get_text(strip=True)
            count = row.select('td')[1].get_text(strip=True)

            ret_topchart.append(ICame(character_name, count))


        return ret_topchart

    def random_post(self, tags: list = None):
        """Get random Post
        Args:
            tags (list, optional): Tag list

        Returns:
            Post: Post Object [empty if error occurs]
        """

        ## Fixed bug: https://github.com/b3yc0d3/rule34Py/issues/2#issuecomment-902728779
        if tags != None:

            search_raw = self.search(tags, limit=1000)
            if search_raw == []:
                return []

            randnum = random.randint(0, len(search_raw)-1)

            while len(search_raw) <= 0:
                search_raw = self.search(tags)
            else:
                return search_raw[randnum]

        else:
            return self.get_post(self._random_post_id())

    def tagmap(self) -> list:
        """Get TagMap (Top 100 Tags searched)
        Returns:
            list: List of dicts [empty if error occurs]
        """

        response = requests.get(API_URLS.TOPMAP.value, headers=__headers__)

        res_status = response.status_code
        res_len = len(response.content)
        ret_topchart = []

        if res_status != 200 or res_len <= 0:
            return []

        bfs_raw = BeautifulSoup(response.content.decode("utf-8"), features="html.parser")
        rows = bfs_raw.find("table", class_="server-assigns").find_all("tr")

        rows.pop(0)
        rows.pop(0)

        retData = []

        for row in rows:
            tags = row.find_all("td")

            rank = tags[0].string[1:]
            tagname = tags[1].string
            percentage = tags[2].string[:-1]

            retData.append(TopTag(rank=rank, tagname=tagname, percentage=percentage))

            #retData.append({
            #    "rank": int(rank),
            #    "tagname": tagname,
            #    "percentage": float(percentage.strip())
            #})

        return retData


    def _random_post_id(self) -> str:
        res = requests.get(API_URLS.RANDOM_POST.value, headers=__headers__)
        parsed = urlparse.urlparse(res.url)

        return parse_qs(parsed.query)['id'][0]

    def _parseUrlParams(self, url: str, params: list) -> str:
        # Usage: _parseUrlParams("domain.com/index.php?v={{VERSION}}", [["VERSION", "1.10"]])
        retURL = url

        for g in params:
            key = g[0]
            value = g[1]

            retURL = retURL.replace("{" + key + "}", value)

        return retURL

    @property
    def version(self) -> str:
        """Get version of module

        Returns:
            str: Version string (eg. xx.xx.xx)
        """
        return __version__
