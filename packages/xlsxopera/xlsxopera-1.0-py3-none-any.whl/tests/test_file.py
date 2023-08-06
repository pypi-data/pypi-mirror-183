import os


class TestFile:

    @staticmethod
    def test_xlsx_file(test_file):
        for file_in_dir in os.listdir():
            if file_in_dir.endswith('.xlsx'):
                assert file_in_dir == test_file

    def test_tests_sheet_exist(self, tests_book):
        assert tests_book.headers() == [
            'ID', 'Status', 'Test Name', 'Test Description',
        ]

    def test_rows_and_cols_sheet_exist(self, rows_and_cols_book):
        assert rows_and_cols_book.headers() == [
            'COLUMN A', 'COLUMN B', 'COLUMN C', 'COLUMN D', 'COLUMN E', 'COLUMN F'
        ]
