import abc
from os import listdir
from os.path import isfile, join

base_path = '/Users/anurag.sh/workspace/SQLDump/logs/tt'


class ProcessLog(abc.ABC):
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

    @staticmethod
    def post_process_file(file):
        print('-' * 170)

    def process_log_line(self, line):
        if self._is_target_log_line(line):
            self._process_log(line)

    def _is_target_log_line(self, line):
        raise NotImplemented('Method not implemented')

    def _process_log(self, line):
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


class AnnouncementScheduleScraper(ProcessLog):
    def _is_target_log_line(self, line):
        return 'Begin processing announcement name:' in line

    def _process_log(self, line):
        run_at = self.__get_run_at(line)
        announcement_name = self.__get_field(line, "Begin processing announcement name:[", "]")
        announcement_id = self.__get_field(line, "id:[", "]")
        print('| {name:80} | {id:40} | {run_at:40} |'.format(name=announcement_name, id=announcement_id, run_at=run_at))


class UserIdScrapper(ProcessLog):

    def _is_target_log_line(self, line):
        return 'unable to notify cPanel for user domain migration' in line

    def _process_log(self, line):
        user_id = self.__get_field(line, 'userId=', ',')
        print(user_id)


class StartStopTimeForAPIScrapper(ProcessLog):
    reqIdSearcher = '8af90b9f-8986-41d8-b69b-3cef3c25be62'

    def _is_target_log_line(self, line):
        if self.reqIdSearcher is not None:
            return 'received req {reqId=' + self.reqIdSearcher in line \
                   or 'processed req {reqId=' + self.reqIdSearcher in line
        return False

    def _process_log(self, line):
        print(line)


class AllLinesInReq(ProcessLog):
    reqIdSearcher = '2144ba37-6b3a-4b65-8a95-4cf873b4593a'

    def _is_target_log_line(self, line):
        return self.reqIdSearcher in line

    def _process_log(self, line):
        print(line)


class CpanelUserFetcher(ProcessLog):
    def _is_target_log_line(self, line):
        return True

    @staticmethod
    def __get_field(line, start_prefix, end_prefix):
        line = str(line)
        start_index = line.index(start_prefix) + len(start_prefix)
        # print(start_index)
        # print(end_prefix)
        end_index = line.index(end_prefix, start_index)
        # print(end_index)
        if start_index != -1 and end_index != -1 and start_index < end_index:
            return line[start_index:end_index]
        else:
            print("StartIndex is ", start_index, " endIndex is ", end_index)
            raise Exception('Invalid prefix seq {}, {} for line {}'.format(start_prefix, end_prefix, line))

    def _process_log(self, line):
        run_at = self.__get_field(line, ': ', ' [')
        # run_at = line[39:62]
        username = self.__get_field(line, '"user":"', '"')
        server_id = self.__get_field(line, "role:partner id:", "}}{")
        event_name = self.__get_field(line, '"event":"', '"')
        print('| {run_at:40} | {username:30} | {server_id:10} | {event_name:20} |'.format(run_at=run_at,
                                                                                          username=username,
                                                                                          server_id=server_id,
                                                                                          event_name=event_name))


def main():
    processor = CpanelUserFetcher()
    for file in processor.get_all_files():
        print("File is ", file)
        with(open(file, 'r')) as fp:
            processor.pre_process_file(file)
            for line in fp:
                processor.process_log_line(line)
            processor.post_process_file(file)


if __name__ == '__main__':
    main()
