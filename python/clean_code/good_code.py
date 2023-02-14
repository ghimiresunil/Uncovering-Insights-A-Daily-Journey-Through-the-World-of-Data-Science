import gdown
import zipfile
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
from typing import List, Tuple


def main():
    """
    Downloads Twitter data from a Google Drive URL and saves it as a zip file at `output_path`.
    The training and testing data are retrieved from the downloaded data using the `DataGetter` class,
    with the training data stored at `path_train` and the testing data at `path_test`.

    Returns:
    tuple: A tuple of two lists containing the training and testing Twitter data, respectively.
    """
    url = "Data from google drive"
    output_path = "Twitter.zip"
    path_train = "Data/train/en"
    path_test = "Data/test/en"

    data_getter = DataGetter(url, output_path, path_train, path_test)

    tweet_train, tweet_test = data_getter.get_train_test_docs()

    return tweet_train, tweet_test


class DataGetter:
    """
    A class for downloading, unzipping, and extracting text from a set of files.
    """

    def __init__(self, url: str, output_path: str, path_train: str, path_test: str):
        """
        Initialize a DataGetter object.

        Args:
        url (str): URL of zip file to download.
        output_path (str): Path to save the downloaded zip file.
        path_train (str): Path to training data.
        path_test (str): Path to testing data.
        """
        self.url = url
        self.output_path = output_path
        self.path_train = path_train
        self.path_test = path_test
        self.download_zip_data_from_google_drive()
        self.unzip_data()

    def download_zip_data_from_google_drive(self):
        """
        Download a zip file from Google Drive.
        """
        gdown.download(self.url, self.output_path, quiet=False)

    def unzip_data(self):
        """
        Unzip the downloaded zip file.
        """
        with zipfile.ZipFile(self.output_path, "r") as zip_ref:
            zip_ref.extractall(".")

    def get_train_test_docs(self) -> Tuple[list, list]:
        """
        Extract text from training and testing data.

        Returns:
        Tuple[list, list]: A tuple containing two lists of text documents (training and testing).
        """
        tweets_train_files = self.get_files(self.path_train)
        tweets_test_files = self.get_files(self.path_test)

        t_train = self.extract_texts_from_multiple_files(
            self.path_train, tweets_train_files
        )
        t_test = self.extract_texts_from_multiple_files(
            self.path_test, tweets_test_files
        )
        return t_train, t_test

    @staticmethod
    def get_files(path: str) -> List[str]:
        """
        Get a list of files in a directory.

        Args:
        path (str): Path to the directory.

        Returns:
        List[str]: A list of file names.
        """
        return [
            file
            for file in listdir(path)
            if isfile(join(path, file)) and file != "truth.txt"
        ]

    @classmethod
    def extract_texts_from_multiple_files(
        cls, path_to_file: str, files: list
    ) -> List[str]:
        """
        Extract text from multiple files.

        Args:
        path_to_file (str): Path to the directory containing the files.
        files (list): A list of file names.

        Returns:
        List[str]: A list of text documents.
        """
        all_docs = []
        for file in files:
            text_in_one_file = cls.extract_texts_from_each_file(path_to_file, file)
            all_docs.append(text_in_one_file)

        return all_docs

    @staticmethod
    def extract_texts_from_each_file(path_to_file: str, file_name: list) -> str:
        """
        Extract text from a single file.

        Args:
        path_to_file (str): Path to the directory containing the file.
        file_name (list): Name of the file.

        Returns:
        str: The text from the file.
        """
        list_of_text_in_one_file = [
            r.text for r in ET.parse(join(path_to_file, file_name)).getroot()[0]
        ]
        text_in_one_file_as_string = " ".join(t for t in list_of_text_in_one_file)

        return text_in_one_file_as_string

""" Execute the main function"""
if __name__ == "__main__":
    main()
