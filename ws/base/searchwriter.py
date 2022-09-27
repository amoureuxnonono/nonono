class SearchWriter:
    def __init__(self):
        self._data_path = ''
        self._data_file_name = 0
        self._data_prefix = ''

    def _write_results(self, results: []):
        if(len(results) > 0):
            file_path = self._data_path + self._data_prefix + '-' + str(self._data_file_name) + '.txt'
            self._data_file_name = self._data_file_name + 1
            with open(file_path, 'w') as writeFile:
                for item in results:
                    writeFile.writelines(item + '\n') 