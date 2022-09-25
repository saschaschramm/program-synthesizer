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
            task["program_2"] = program
        except:
            print("Task", taskname, "does not have a main.py file")
    utils.write_json_file(tasks, config.TMP_DIR, "tasks-synthesized", "json")