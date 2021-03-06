
#basic
import xml.etree.ElementTree as ET
from tqdm import tqdm
from glob import glob
import os

#hotam
from hotam.utils import download, unzip


class BNC:
    """
    Link to coprus http://www.natcorp.ox.ac.uk/

    """

    def __init__(self, save_path:str="/tmp/BNC-Corpus.zip"):
        self.save_path = save_path
        self.data_path = save_path.replace(".zip", "")
        self.url = "https://ota.bodleian.ox.ac.uk/repository/xmlui/bitstream/handle/20.500.12024/2554/2554.zip?sequence=3&isAllowed=y"
        self.__download()
        self.files, self.n, self.max = self.__get_files()

    def __len__(self):
        return self.max


    def __download(self):
        if not os.path.exists(self.save_path):
            download(url=self.url, save_path=self.save_path, desc="Downloading BNC-Corpus")

        if not os.path.exists(self.data_path):
            unzip(self.save_path, self.data_path)


    def __get_files(self):
        path_to_text = os.path.join(self.data_path,"download", "Texts")
        files = glob(path_to_text+"/**/*.xml", recursive=True)
        return files, 0 ,len(files)-1


    def __iter__(self):
        return self


    def __next__(self):
        
        if self.n > self.max:
            raise StopIteration
        
        tree = ET.parse(self.files[self.n])
        root = tree.getroot()

        for child in root:
            if "text" in child.tag:
                xml_doc = child

        doc = " ".join([text.strip() for text in xml_doc.itertext()])
        self.n += 1
        return doc

