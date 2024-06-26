import os


def main(message, modify_file):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("git add".center(50, "-"))
    os.system("git add " + modify_file)
    print("git commit".center(50, "-"))
    os.system("git commit -m %s" % (message,))
    print("git push".center(50, "-"))
    os.system("git push")
    print("git reflog -n 15".center(50, "-"))
    os.system("git reflog -n 15")
    print("*".center(50, "*"))
    os.system("pause")


if __name__ == '__main__':
    modify_file = input("Enter Modified File Path:\n").strip().strip('"')
    if os.path.isdir(modify_file):
        modify_file = modify_file + r"\*.*"
    mess = input('输入提交信息>>>').strip().replace(' ', '-').replace('|', '-').replace('>', '-')
    decide = input("是否提交(y/n)>>>").strip().lower()
    if decide == 'y':
        main(message=mess, modify_file=modify_file)
    else:
        print("未提交".center(50, "-"))
        os.system('pause')
