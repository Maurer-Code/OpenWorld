from webapp import db
from webapp.database.base import Base

import hashlib
from json import dumps, loads


# Encoding for the json / dictionary string
ENCODING = 'UTF-8'


def generate_hash_from_dictionary(dictionary: dict) -> str:
    """
    This function generates a md5 hash key from a dictionary.
    """
    hash_data = hashlib.md5(dumps(dictionary).encode(ENCODING))
    return hash_data.hexdigest()


def generate_hash_from_string(string: str) -> str:
    """
    This function generates a md5 hash key from a string.
    """
    hash_data = hashlib.md5(string.encode(ENCODING))
    return hash_data.hexdigest()


def check_hash_from_dictionary(source: str, target: dict) -> bool:
    """
    This function returns True, if the string and the dictionary are identical.
    """
    source_hash = generate_hash_from_string(source)
    target_hash = generate_hash_from_dictionary(target)
    return source_hash == target_hash


class Hash(Base):
    """
    An abstract class to store data in kind of dictionaries which allows independence of database columns.

    Attributes
    ----------
    id : int
        identifier of the database entry
    hash : str
        hash key generated from the dictionary string
    dictionary : str
        Stored data as dictionary string (for example settings)
    created_on : datetime
        creation timestamp of the database entry
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(150), unique=True)
    dictionary = db.Column(db.String(2000))

    def __init__(self, dictionary: dict):
        json_string = dumps(dictionary)
        self.hash = generate_hash_from_string(json_string)
        self.dictionary = json_string

    def generate_hash(self, dictionary: dict):
        """
        This method generates a hash key and the dictionary string for the database.
        """
        json_string = dumps(dictionary)
        self.hash = generate_hash_from_string(json_string)
        self.dictionary = json_string

    def check_hash(self, dictionary: dict) -> bool:
        """
        This method check if the dictionary is identical to the database entry.
        """
        return check_hash_from_dictionary(self.dictionary, dictionary)

    def get_dict(self):
        """
        This method returns the stored data als dictionary.
        """
        return loads(self.dictionary)

    @classmethod
    def get_entry(cls, dataset: dict, key_words: list = None):
        """
        This class method returns existing entries from the database or creates new entries dependent on the dataset.
        """

        # Remove dynamic and ignorable keys from project dataset
        filtered_dataset = {key: dataset[key] for key in key_words if key in dataset} if key_words else dataset

        if bool(filtered_dataset):

            entry = cls(dictionary=filtered_dataset)

            existing_entry = cls.query.filter_by(hash=entry.hash).first()

            if existing_entry is None:
                db.session.add(entry)
            else:
                entry = existing_entry
        else:
            entry = None

        return entry
