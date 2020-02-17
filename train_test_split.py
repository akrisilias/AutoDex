"""
Train Test Splitter

This script splits the data to a train and a test directory.

This file contains the following functions:

    * train_test_split - moves files in two directories (train and test)
    * main - the main function of the script
"""

import argparse
import os
import random
from shutil import move


def train_test_split(image_dir, train_percentage):
    """
    Moves a percentage of files in a directory to a train subdirectory and the rest to a test subdirectory.

    :param image_dir: The directory that contains the files to be moved
    :param train_percentage: The percentage of files that will be moved to the train directory
    :return: None
    """
    if image_dir[-1] != '/':
        image_dir += '/'

    train_dir = image_dir + 'train'
    test_dir = image_dir + 'test'
    dirs = [train_dir, test_dir]

    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)

    files = [os.path.join(image_dir, file).rsplit('.', 1)[0] for file in os.listdir(image_dir)]
    files = list(set(files))

    n_train = int(len(files) * train_percentage)
    indices = random.sample(range(len(files)), n_train)
    train_list = [files[i] for i in indices]
    test_list = [f for f in files if f not in train_list]

    all_files = [os.path.join(image_dir, file) for file in os.listdir(image_dir)]
    all_files.remove(train_dir)
    all_files.remove(test_dir)
    for file in all_files:
        if file.rsplit('.', 1)[0] in test_list:
            move(file, test_dir)
        else:
            move(file, train_dir)


def main():

    parser = argparse.ArgumentParser(description='Split files into train and test directories')
    parser.add_argument('--image_dir', help='The directory that contains the files to be moved',
                        default='./downloads', type=str, required=False)
    parser.add_argument('--train_percentage', help='The percentage of files that will be moved to the train directory',
                        default=0.95, type=float, required=False)
    args = vars(parser.parse_args())

    image_dir = args['image_dir']
    train_percentage = args['train_percentage']

    train_test_split(image_dir, train_percentage)


if __name__ == "__main__":
    main()
