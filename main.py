from bs4 import BeautifulSoup
import requests
import os


def get_images():
    url = 'https://api.imgur.com/post/v1/albums/xlcfh?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount'

    data_dict = requests.get(url).json()
    img_array_dict = data_dict['media']
    img_array = []

    for obj in img_array_dict:
        data = {"src":obj['url']}
        img_array.append(data)
    
    return img_array

def make_dir(data):
    # check if there is a img directory

    # gets full path
    dir_path = os.path.dirname(os.path.realpath(__file__))

    path = dir_path+"/imgs"
    isdir = os.path.isdir(path)

    # if the imgs directory exist commence download
    if isdir:
        download(path,data)

    # if the imgs directory doesn't exist, make it than commence download
    else:
        dirname = 'imgs'
        os.mkdir(dirname)
        download(path,data)
        

def download(path,data):
    os.chdir(path)
    # download img part
    for index, obj in enumerate(data):
        # print(index, obj['src'])
        # gets img from url
        response = requests.get(obj['src'])
        # write img into a file
        with open('img{}.png'.format(index),'wb') as f:
            f.write(response.content)
            f.close()
    print('Download Complete!')
   
def main():
    data = get_images()
    make_dir(data)

main()