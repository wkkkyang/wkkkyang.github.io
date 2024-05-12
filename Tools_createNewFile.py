import os


def main():
    os.chdir(os.path.dirname(__file__))
    
    file_name = input("Enter file name: ").strip()
    os.system("hexo new " + file_name)
    
    os.system("pause")
    
    curr_path = os.getcwd()
    file_folder_path = fr'{curr_path}\source\_posts'
    file_path = fr'{file_folder_path}\{file_name}.md'
    os.system("start explorer " + file_folder_path)
    os.system("start explorer " + file_path)


if __name__ == '__main__':
    main()
