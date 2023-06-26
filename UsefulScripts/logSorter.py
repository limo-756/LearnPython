import abc
from collections import OrderedDict
from os import listdir
from os.path import isfile, join

base_path = '/Users/anurag.sh/workspace/SQLDump/logs/tt'


class LogSorter(abc.ABC):
    sorted_map = OrderedDict()

    @staticmethod
    def get_all_files():
        print("Base path is ", base_path)
        res = []
        for file in listdir(base_path):
            print("Got a file : ", file)
            if isfile(join(base_path, file)) and not file.__contains__("DS_Store"):
                res.append(join(base_path, file))

        return res
        # return (file for file in listdir(base_path) if isfile(join(base_path, file)))

    @staticmethod
    def pre_process_file(file):
        print('Starting file processing for : {}'.format(file))
        print('-' * 170)

    def post_process_file(self):
        value_key_pairs = ((key, value) for (key, value) in self.sorted_map.items())
        sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
        # print(sorted_value_key_pairs)
        for val in sorted_value_key_pairs:
            print(val[1])

    def process_log_line(self, line):
        if self._is_target_log_line(line):
            val = int(self.extract_key(line))
            self.sorted_map[val] = line

    def extract_key(self, line):
        raise NotImplemented('Method not implemented')

    def _is_target_log_line(self, line):
        raise NotImplemented('Method not implemented')

    @staticmethod
    def __get_field(line, start_prefix, end_prefix):
        line = str(line)
        start_index = line.index(start_prefix) + len(start_prefix)
        end_index = line.index(end_prefix, start_index)
        if start_index != -1 and end_index != -1 and start_index < end_index:
            return line[start_index:end_index]
        else:
            print("StartIndex is ", start_index, " endIndex is ", end_index)
            raise Exception('Invalid prefix seq {}, {} for line {}'.format(start_prefix, end_prefix, line))

    @staticmethod
    def __get_run_at(line):
        return line[0:23]


class RespTimeSorter(LogSorter):

    @staticmethod
    def __get_field(line, start_prefix, end_prefix):
        line = str(line)
        start_index = line.index(start_prefix) + len(start_prefix)
        end_index = line.index(end_prefix, start_index)
        if start_index != -1 and end_index != -1 and start_index < end_index:
            return line[start_index:end_index]
        else:
            print("StartIndex is ", start_index, " endIndex is ", end_index)
            raise Exception('Invalid prefix seq {}, {} for line {}'.format(start_prefix, end_prefix, line))

    def extract_key(self, line):
        return self.__get_field(line, 'resp-time:', 'ms').strip()

    def _is_target_log_line(self, line):
        return 'processed req' in line


class MedusaRespTimeSorter(LogSorter):

    @staticmethod
    def __get_field(line, start_prefix, end_prefix):
        line = str(line)
        start_index = line.index(start_prefix) + len(start_prefix)
        end_index = line.index(end_prefix, start_index)
        if start_index != -1 and end_index != -1 and start_index < end_index:
            return line[start_index:end_index]
        else:
            print("StartIndex is ", start_index, " endIndex is ", end_index)
            raise Exception('Invalid prefix seq {}, {} for line {}'.format(start_prefix, end_prefix, line))

    def extract_key(self, line):
        return self.__get_field(line, 'resp time:', 'ms').strip()

    def _is_target_log_line(self, line):
        return 'to medusa, resp time:' in line


def main():
    processor = MedusaRespTimeSorter()
    for file in processor.get_all_files():
        print("File is ", file)
        with(open(file, 'r')) as fp:
            processor.pre_process_file(file)
            for line in fp:
                processor.process_log_line(line)
            processor.post_process_file()


if __name__ == '__main__':
    main()
