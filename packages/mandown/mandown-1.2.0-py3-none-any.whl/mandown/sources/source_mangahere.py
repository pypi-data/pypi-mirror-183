"""
Source file for mangahere.cc
"""
# pylint: disable=invalid-name

import re
import string

import requests
from bs4 import BeautifulSoup

from ..base import BaseChapter, BaseMetadata
from .base_source import BaseSource


class MangaHereSource(BaseSource):
    name = "Manga Here"
    domains = ["https://www.mangahere.cc"]
    headers = {"Referer": "https://www.mangahere.cc"}

    def __init__(self, url: str) -> None:
        super().__init__(url)
        self._scripts: str | None = None

    def fetch_metadata(self) -> BaseMetadata:
        soup = BeautifulSoup(self._get_scripts(), "lxml")

        cover_img = soup.select_one("img.detail-info-cover-img")
        cover_art: str = cover_img["src"].replace("&amp;", "&")
        title: str = cover_img["alt"]

        author: str = soup.select_one("p.detail-info-right-say > a").text
        description: str = soup.select_one("p.detail-info-right-content").text
        genres: list[str] = [
            el["href"] for el in soup.select("p.detail-info-right-tag-list > a")
        ]

        return BaseMetadata(title, [author], self.url, genres, "", cover_art)

    def fetch_chapter_list(self) -> list[BaseChapter]:
        soup = BeautifulSoup(self._get_scripts(), "lxml")
        chap_els = soup.select("li > a")

        chapters: list[BaseChapter] = []
        for el in chap_els:
            title = el.select_one(".title3").text.split(" - ")[-1]
            url = self.domains[0] + el["href"]
            chapters.append(BaseChapter(title, url))
        return list(reversed(chapters))

    def fetch_chapter_image_list(self, chapter: BaseChapter) -> list[str]:
        soup = BeautifulSoup(requests.get(chapter.url, timeout=5).text, "lxml")

        num_pages = max(
            int(el["data-page"])
            for el in soup.select("span > a[data-page]")
            if str(el["data-page"]).isdigit()
        )

        id = [s for s in self.metadata.cover_art.split("/") if s.isdigit()][0]
        # TODO: document this magic number bullshittery or use a regex
        # or look at tachiyomi
        chap_num = chapter.url.split("/")[-2][1:]

        chap_id_start = soup.text.index("var chapterid =") + len("var chapterid =")
        chap_id_end = soup.text.index(";", chap_id_start)
        chap_id = soup.text[chap_id_start:chap_id_end].strip()

        # mkey filtering
        mkey_start = soup.text.index("'\\'+\\") + len("'\\'+\\")
        mkey_end = soup.text.index(";", mkey_start)
        mkey = soup.text[mkey_start:mkey_end].strip()
        regex = re.compile(f"[{string.punctuation}]")
        mkey = regex.sub("", mkey)
        mkey = mkey[:-1] + "e"

        # request to get full urls
        str_id = requests.get(
            f"https://www.mangahere.cc/ajax/chapterfun.ashx?cid={chap_id}&page=1&key={mkey}",
            timeout=5,
        ).text

        # not quite done but close
        return [
            f"https://zjcdn.mangahere.org/store/manga/{id}/"
            f"{chap_num}.0/compressed/b{str_id}_{chap_num}_{i:03}.jpg"
            for i in range(1, num_pages + 1)
        ]

    @staticmethod
    def check_url(url: str) -> bool:
        return bool(re.match(r"https://www.mangahere.cc/manga/[^/]+/?$", url))

    def _get_scripts(self) -> str:
        if self._scripts:
            return self._scripts

        self._scripts = requests.get(self.url, timeout=5).text
        return self._scripts


def get_class() -> type[BaseSource]:
    return MangaHereSource
