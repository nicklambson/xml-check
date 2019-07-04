from pathlib import Path
import datetime
import utils
import sys


class File:
    def __init__(self, source_path, translated_files_path):
        self.source_path = source_path
        self.source_name = self.source_path.name
        self.translated_files_path = translated_files_path
        self.target_path = self.get_target_path()

        self.source_content = utils.get_content(self.source_path)
        self.target_content = utils.get_content(self.target_path)

        self.source_placeholders = utils.get_placeholders(self.source_content)
        self.target_placeholders = utils.get_placeholders(self.target_content)

    def get_target_path(self):
        for path in self.translated_files_path.rglob("*.*"):
            if path.name == self.source_name:
                return path
        else:
            print(f"Could not find a corresponding file for {self.source_name}")
            return None

    def check_placeholders(self):
        if self.target_path:
            if self.source_placeholders != self.target_placeholders:
                for idx, sph in enumerate(self.source_placeholders):
                    tph = self.target_placeholders[idx]
                    if sph != tph:
                        print(sph, tph)
                utils.print_error(name=self.source_name,
                                  error_type="Placeholder Mismatch",
                                  source_placeholders=self.source_placeholders,
                                  target_placeholders=self.target_placeholders)
        else:
            print(f"Cannot check file {self.source_name}")


class Environment:
    def __init__(self, source_files_path, translated_files_path):
        self.source_files_path = Path(source_files_path)
        self.translated_files_path = Path(translated_files_path)

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d")

        parent_path = self.translated_files_path.parent
        result_folder = 'result_' + timestamp
        self.result_path = parent_path / result_folder

    def execute(self):
        print(f"Processing source path: {self.source_files_path}")
        print(f"Processing target path: {self.translated_files_path}")
        for path in self.source_files_path.glob(r"*.*"):
            f = File(path, self.translated_files_path)
            f.check_placeholders()


if __name__ == "__main__":
    env = Environment(sys.argv[-2], sys.argv[-1])
    env.execute()
