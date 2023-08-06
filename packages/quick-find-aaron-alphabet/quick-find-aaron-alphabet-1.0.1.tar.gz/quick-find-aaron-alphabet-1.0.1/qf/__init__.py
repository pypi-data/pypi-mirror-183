import subprocess
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(fromfile_prefix_chars="@", add_help=False,) # prefix_chars="",)
    parser.add_argument('searchterm')
    parser.add_argument('auxarg', nargs='*')
    ns, args = parser.parse_known_args()
    subprocess.run(["find", "-name", f"*{ns.searchterm}*"] + args, check=True)


if __name__ == '__main__':
    main()






