from config import config
import utils
from components.verifier.component import Verifier
import os
from os.path import join

def evaluate(tmp_dir):
    test_filenames = os.listdir(tmp_dir)
    verifier: Verifier = Verifier()

    # Be careful, run this script only in a sandboxed environment
    if os.path.exists("/.dockerenv"):
        num_pass = 0
        for filename in test_filenames:
            path: str = os.path.join(tmp_dir, filename)
            try:
                verifier.verify(path)
                print(f"{filename} - pass")
                num_pass += 1
            except Exception as e:
                print(f"{filename} - fail – {e}")
        pass_rate = num_pass / len(test_filenames)
        print("num_pass", num_pass)
        print(f"pass_rate {pass_rate*100:.2f}%")
    else:
        print("Not in docker environment")
        

def generate_files(tmp_dir):
    tasks = utils.read_file(config.DATA_DIR, "tasks-synthesized", "json")
    utils.make_dir(tmp_dir)
    for taskname, task in tasks.items():
        taskname = taskname.replace("/", "-")
        program = task["program_2"]
        test = task["test"]
        entry_point = task["entry_point"]
        program = f"""{program}\n{test}\ncheck({entry_point})"""
        utils.write_file(program, tmp_dir, taskname, "py")

if __name__ == "__main__":
    tmp_dir: str = "tmp-evaluate"
    generate_files(tmp_dir)
    evaluate(tmp_dir)


     
    