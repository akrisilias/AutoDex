"""
Google Images Downloader

This script downloads google images.

It is customized so that to download medium sized images of car brand emblems.

This script requires that `google_images_download` be installed within the Python
environment you are running this script in.

This file contains the following functions:

    * download_images - downloads google images
    * main - the main function of the script
"""

import argparse
from google_images_download import google_images_download


def download_images(query, response, directory, n_images, form):
    """
    Downloads images from Google given a search query and additional parameters.

    :param query: The search query
    :param response: Object to execute the query
    :param directory: Directory to save images
    :param n_images: Number of images to be downloaded
    :param form: The image file format
    :return: None
    """
    arguments = {"keywords": query,
                 'format': form,
                 "limit": n_images,
                 "print_urls": True,
                 "size": "medium",
                 "output_directory": directory,
                 "no_directory": "True"
                 }
    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": form,
                     "limit": 2,
                     "print_urls": True,
                     "size": "medium"
                     }
        try:
            response.download(arguments)
        except:
            pass


def main():
    parser = argparse.ArgumentParser(description='Download google images')
    parser.add_argument('--directory', help='Directory to save images', default='./downloads',
                        type=str, required=False)
    parser.add_argument('--query', help='The search query', default='BMW',
                        type=str, required=False)
    parser.add_argument('--n_images', help='Number of images to be downloaded', default=100,
                        type=int, required=False)
    parser.add_argument('--format', help='The image file format', default='png',
                        type=str, required=False)
    args = vars(parser.parse_args())

    directory = args['directory']
    query = args['query'] + ' logo on car'
    n_images = args['n_images']
    form = args['format']

    response = google_images_download.googleimagesdownload()

    search_queries = [query]

    for query in search_queries:
        download_images(query, response, directory, n_images, form)
        print()


if __name__ == "__main__":
    main()
