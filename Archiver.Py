from os import sep,rename,listdir,path,getcwd
from shutil import move

class Mains:
    def __init__(self):

        self.exceptExist = []
        self.exceptPermission = []
        self.exceptDir = [".idea","Zzzzz"]
        self.pwd = listdir('.')
        self.baseLoc = str(getcwd())+sep

        self.Capitalize()

        self.files = [i for i in self.pwd if path.isfile(i)]
        self.Directories = [i for i in self.pwd if path.isdir(i) and i not in self.exceptDir]

        self.FileChecker()

    def Capitalize(self):
        for filename in self.pwd:
            try:
                rename(filename, filename.title())
            except PermissionError:
                self.exceptPermission.append(filename)
            except FileExistsError:
                self.exceptExist.append(filename)

    def FileChecker(self):
        singer_name = [singer for singer in self.Directories]
        file_name = [file for file in self.files]

        duplicateFinder = []

        for file in file_name:
            for singer in singer_name:
                if singer.lower() in file.lower() and file not in duplicateFinder:             # try not to move a file twice

                    indexing = file.lower().find(singer.lower())

                    if indexing == 0:
                        start = False
                    else:
                        if file.lower()[indexing - 1].isalpha():
                            start = True
                        else:
                            start = False

                    # To recognize containing names like : "Jessi" and "Essi"
                    if start or file.lower()[indexing+len(singer)].isalpha():
                        pass
                    else:
                        try:
                            self.Replacer(file, singer)
                            print(file.title() + "\nmoved to ==>   " + singer + "\n---------------------------")
                        except PermissionError:
                            self.exceptPermission.append(file)
                        duplicateFinder.append(file)

    def Replacer(self, file, directory):
        move(self.baseLoc+file, self.baseLoc+directory+sep+file)

if __name__ == "__main__":
    print("=====Music-Video-Archiver=====\n")

    m = Mains()

    if len(m.exceptPermission) > 0:
        print("Program couldn't access above file(s) because they're in use by another process or need Admin Permission"
              + ":\n" + str(list(set(m.exceptPermission))).replace("[", "").replace("]", ""))

    if len(m.exceptExist) > 0:
        print("Program can't move above file(s) because they already exist in destination directory:\n"
              + str(list(set(m.exceptExist))).replace("[", "").replace("]", ""))

    input("\n========Done!========")



    # def directory2database(self):
    #     f = open("Database.txt","w")
    #
    #     self.write = []
    #     for i in self.Directories:
    #         self.write.append(i.title() + "\n")
    #     # print(self.write)
    #
    #     self.write = sorted(self.write)
    #     f.writelines(self.write)
    #     f.close()

    # m.directory2database()
