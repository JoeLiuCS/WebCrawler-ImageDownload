from bs4 import BeautifulSoup
import urllib.request


# The head of Image link
base_url = "https://www.ukhairdressers.com/style/"
key_url = "https://www.ukhairdressers.com/style/index2.asp"
key_button1= 'next'
key_ID1 = 'Mainimage'

download_pages = []
download_pages.append("https://www.ukhairdressers.com/Latest-Hairstyles-Gallery/Hairstyles/1107")
download_pages.append("https://www.ukhairdressers.com/Long-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Medium-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Short-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Blonde-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Brown-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Black-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Red-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Mens-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Straight-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Wavy-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Curly-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Bob-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Choppy-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Layered-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Haircut-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Spikey-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Avant-Garde-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Updo-Hairstyles-17")
download_pages.append("https://www.ukhairdressers.com/Wedding-Hairstyles-17")

#Get the image url by page
def get_image_url(page_url):
    response = urllib.request.urlopen(page_url)
    html = response.read()
    # soup = BeautifulSoup(html, 'html.parser')
    soup = BeautifulSoup(html,'html.parser',from_encoding='iso-8859-1')
    image_url = base_url + soup.find(id=key_ID1)["src"]
    return image_url


def get_image_page_urls(show_page_url):
    response = urllib.request.urlopen(show_page_url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser',from_encoding='iso-8859-1')
    links = soup.select("a")
    hairstyle_links = []
    for link in links:
        if str(link).find("href") != -1:
            temp = str(link['href'])
            if temp.find(key_url) != -1:
                # print temp        #print image url
                hairstyle_links.append(link["href"])
    return hairstyle_links



def get_next_page_urls(start_page):
    page = urllib.request.urlopen(start_page)
    html = page.read()
    soup = BeautifulSoup(html,'html.parser',from_encoding='iso-8859-1')
    single_link = soup.find(rel=key_button1)
    if single_link is None:
        return None
    next_page = single_link["href"]
    #if next page is None return None
    return next_page



def page_running(input_first_page,text_out_put):

    moving_page = input_first_page
    check_back = True

    while check_back:
        link_for_nextPage = get_next_page_urls(moving_page) #get to next page
        print ("Page at : "+moving_page)

        # check next page is not null
        text_out_put.write("Page at : "+moving_page+"\n")
        image_link = get_image_page_urls(moving_page)

        for link in image_link:
            image = get_image_url(link)
            text_out_put.write(image+"\n")
            print (image)

        # one cycle only and next link is not null
        if (link_for_nextPage != input_first_page) and (link_for_nextPage is not None):
            moving_page = link_for_nextPage
        else:
            check_back = False

def main():

    count = 0

    for pages in download_pages:
        text_file = open("Output"+str(count)+".txt", "w")
        page_running(pages, text_file)
        count = count +1
        text_file.close()


if __name__ == "__main__":
    main()
