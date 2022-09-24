import os
from os.path import join
from components.verifier.component import Verifier
from config import config


def main():
    test_dir = join(config.DATA_DIR, "tmp")
    test_filenames = os.listdir(test_dir)
    test_filenames.sort()
    verifier: Verifier = Verifier()

    # Be careful, run this script only in a sandboxed environment
    if os.path.exists("/.dockerenv"):
        num_pass = 0
        for filename in test_filenames:
            path: str = os.path.join(test_dir, filename)
            try:
                verifier.verify(path)
                print(f"{filename} - pass")
                num_pass += 1
            except Exception as e:
                print(f"{filename} - fail – {e}")

        pass_rate = num_pass / len(test_filenames)
        print("num_pass", num_pass)
        print(f"pass_rate {pass_rate*100:.2f}%")


if __name__ == "__main__":
    main()
