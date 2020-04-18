import bs4 as bs
import urllib.request as req
import os

class BandDown:
    def __init__(self):
        self.progress = 1

    def download(self, url: str, folder: str, format_ = 'mp3'):
        fetch = req.urlopen(url)
        if fetch.getcode() == 200:
            html = fetch.read()
            soup = bs.BeautifulSoup(html, 'html.parser')
            divs = soup.find_all('div', class_ = 'contents')
            songtable = divs[2].table.find_all('tr')
            album = soup.div.h2.a.string.strip()
            dir = os.path.join(folder, album)
            if not os.path.exists(dir):
                os.mkdir(dir)

            for i in songtable:
                print(f'Downloading: {i.contents[0].div.string.strip()} [{self.progress}/{len(songtable)}]')
                req.urlretrieve(i.contents[1].a['href'], f'{dir}\{i.contents[0].div.string.strip()}.{format_}')
                self.progress += 1
            self.progress = 1
        else:
            print('Status Code is not OK:', fetch.getcode())


def main():
    downloader = BandDown()
    downloader.download('https://downloadmusicschool.com/bandcamp/thatbandofhers.bandcamp.com/album/songs-of-hers', 'D:\Music')
    # https://downloadmusicschool.com/bandcamp/ + bandcamp link
    # if has free FLAC/MP3 full album download, use that instead
    # may need to click "content server from cache. click to refresh"


if __name__ == '__main__':
    main()