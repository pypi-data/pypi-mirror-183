import pandas as pd
import getpass
import os
import zipfile


class Zipndel:
    def __init__(self, file_name: str = 'df', file_format: str = 'csv'):
        """
        Initialize Zipndel object.

        Parameters:
        file_name (str): the name of the file to be written, default is 'df'
        file_format (str): the file format of the file to be written, default is 'csv'
        """
        self.file_name = file_name
        self.file_format = file_format

    def zipit(self, df: pd.DataFrame) -> None:
        """
        Write the input dataframe to a file, create a zip file with the written file, set a password for the zip file, and delete the written file.

        Parameters:
        df (pd.DataFrame): the input dataframe to be written to file and zipped

        Example:
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        >>> Zipndel().zipit(df)
        """
        # write dataframe to a pandas supported file
        write_func = getattr(df, f'to_{self.file_format}')
        write_func(self.file_name, index=False)

        # create zip file and add the written file to it
        df_zip = f"{self.file_name}.zip"
        zf = zipfile.ZipFile(df_zip, mode='w')
        try:
            zf.write(self.file_name, compress_type=zipfile.ZIP_DEFLATED)
        finally:
            zf.close()

        # set password for zip file
        passwd = getpass.getpass('Password:')
        os.system(f'zip --password {passwd} {df_zip} {self.file_name}')

        # delete written file
        os.remove(self.file_name)


class Unzipndel:
    def __init__(self, file_name: str = 'df', file_format: str = 'csv'):
        """
        Initialize Unzipndel object.

        Parameters:
        file_name (str): the name of the file to be extracted, default is 'df'
        file_format (str): the file format of the file to be extracted, default is 'csv'
        """
        self.file_name = file_name
        self.file_format = file_format

    def unzipit(self) -> pd.DataFrame:
        """
        Unzip the zip file, extract the written file, read the extracted file into a DataFrame, and delete the extracted file.

        Returns:
        df (pd.DataFrame): the dataframe extracted from the zip file

        Example:
        >>> df = Unzipndel().unzipit()
        """
        # prompt user for password
        passwd = getpass.getpass('Password:')

        # unzip zip file and extract written file
        df_zip = f"{self.file_name}.zip"
        zf = zipfile.ZipFile(df_zip, mode='r')
        zf.extractall(pwd=passwd.encode())

        # read extracted file into a DataFrame
        read_func = getattr(pd, f'read_{self.file_format}')
        df = read_func(self.file_name)

        # delete extracted file
        os.remove(self.file_name)

        return df
