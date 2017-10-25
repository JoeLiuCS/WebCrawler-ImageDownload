import urllib.request
import urllib.error
import os
from yelp_uri.encoding import recode_uri


files = []


def read_text(file):
    url_array = []
    with open(file) as f:
        for line in f:
            #remove new line using rstrip
            #replace the space using %20
            if(line[:1] != 'P'):
                url_array.append(line.rstrip().replace(" ","%20"))
    return url_array

def download_image(url_array,folder_dir):
    count = 1;
    for web_link in url_array:
        try:
             web = recode_uri(web_link)
             urllib.request.urlopen(web)
        except urllib.error.HTTPError:
            print ("####### URL 404 ERROR, Link does not exsist!! #########")
        else:
            image_name = web_link.rsplit('/', 1)[1]
            name = str(count) + str(image_name)
            fullfilename = os.path.join(folder_dir, name)
            urllib.request.urlretrieve(web, fullfilename)
            print ("download number: " , count)
            print ("Where I at: " + web_link)
            count=count+1

def get_txts():
    for file in os.listdir("./"):
        if file.endswith(".txt"):
            files.append(str(os.path.join(file)))

def main():

    get_txts()
    for name in files:
        # Create a folder
        folder_Name = str(name).split('.')[0]
        path = str(folder_Name)
        if not os.path.exists(path):
            os.makedirs(path)
            print ("Create a folder, Name : " + str(folder_Name))

        print ("downloading this text file: " + name)
        #read the text file and store the htmls to the array
        url = read_text(name)
        #get all image using array
        download_image(url,path)


    print ("Finished !!")

if __name__== "__main__":
    main()