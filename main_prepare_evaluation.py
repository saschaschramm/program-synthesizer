import os
import utils
from config import config

if __name__ == "__main__":
    tasks = utils.read_file(config.DATA_DIR, "tasks", "json")
    test_dir = os.path.join(config.DATA_DIR, "tmp")
    utils.make_dir(test_dir)
    for taskname, task in tasks.items():
        taskname = taskname.replace("/", "-")
        try:
            task_dir = os.path.join(config.TMP_DIR, taskname)
            program = utils.read_file(task_dir, "main", "py")
            test = task["test"]
            entry_point = task["entry_point"]
            program = f"""{program}\n{test}\ncheck({entry_point})"""
            utils.write_file(program, test_dir, f"{taskname}", "py")
        except:
            print("Task", taskname, "does not have a main.py file")

