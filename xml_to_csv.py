"""
XML to CSV Converter

This script converts .xml label files to a single .csv file.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file contains the following functions:

    * xml_to_csv - downloads google images
    * main - the main function of the script
"""

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse


def xml_to_csv(path):
    """
    Parses xml label files found in given directory and returns a pandas.DataFrame containing all xml values.

    :param path: Path to directory containing target xml files
    :return: A pandas.DataFrame containing parsed xml values
    """
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            bndbox = member.find('bndbox')
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member.find('name').text,
                     int(bndbox.find('xmin').text),
                     int(bndbox.find('ymin').text),
                     int(bndbox.find('xmax').text),
                     int(bndbox.find('ymax').text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    parser = argparse.ArgumentParser(description='Convert xml label files to csv')
    parser.add_argument('--in_dir', help='Directory to read', default='./downloads',
                        type=str, required=False)
    parser.add_argument('--out_dir', help='Directory to write', default='./downloads',
                        type=str, required=False)
    parser.add_argument('--out_fname', help='Output file name', default='some_name.csv',
                        type=str, required=False)
    args = vars(parser.parse_args())

    in_dir = args['in_dir']
    out_dir = args['out_dir']
    out_fname = args['out_fname']

    image_path = os.path.join(os.getcwd(), in_dir)
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv(out_dir + '/' + out_fname, index=None)
    print('Successfully converted xml to csv.')


if __name__ == "__main__":
    main()
