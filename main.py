from bs4 import BeautifulSoup
import requests
import os

# populates an array with dicts with the imgs source link
def get_images():
    # url for the get request
    url = 'https://api.imgur.com/post/v1/albums/xlcfh?client_id=546c25a59c58ad7&include=media%2Cadconfig%2Caccount'

    # obtains the json data of the request
    data_dict = requests.get(url).json()
    # extracts the object that containts the image sources
    img_array_dict = data_dict['media']

    # initializes an empty array
    img_array = []

    # loops through every dict and stores the source link inro an object then appends it into the img_array list
    for obj in img_array_dict:
        data = {"src":obj['url']}
        img_array.append(data)
    
    # returns the new list with the img sources
    return img_array

def make_dir(data):
    # check if there is a img directory
    # gets full path
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # creates imgs directory path 
    path = dir_path+"/imgs"

    # checks to see if imgs directory exists
    isdir = os.path.isdir(path)

    # if the imgs directory exist commence download
    if isdir:
        download(path,data)

    # if the imgs directory doesn't exist, make it than commence download
    else:
        dirname = 'imgs'
        os.mkdir(dirname)
        download(path,data)
        
# downloads the images
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