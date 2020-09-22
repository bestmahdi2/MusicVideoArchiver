from os import walk,rename,sep
from difflib import ndiff

class mains:
    def __init__(self):

        self.dirs = "" #sep + "testing"


    def bads(self):
    # region bads
        self.bads_twoSpace = [" musicvideo " , " music video " , " youtube " , " you tube "
            , " .135 " , " official " , " video "  ," () " , " ( ) " , " 135 ", " .137 " , " .136 " , " 1080p " , " 1080 " , " 720p " , " 720 " , " 480p "  , " 480 ",
            " hd " ," full hd "  , " [] " , " [ ] ", " {} " , " { } " , " .271 " , " .244 " , " .248 " , " 4k " ,]

        self.bads_leftSpace = [" musicvideo" , " music video" , " youtube" , " you tube"
            , " .135" , " official" , " video" , " ()" , " ( )" , " 135", " .137" , " .136" , " 1080p" , " 1080" , " 720p" , " 720" , " 480p"  , " 480",
            " hd" ," full hd"  , " []" , " [ ]", " {}" , " { }" , " .271" , " .244" , " .248",  " 4k" , ]

        self.bads_rightSpace = ["musicvideo " , "music video " , "youtube " , "you tube "
            , ".135 " , "official " , "video " , "() " , "( ) " , "135 ", ".137 " , ".136 " , "1080p " , "1080 " , "720p " , "720 " , "480p "  , "480 ",
            "hd " ,"full hd "  , "[] " , "[ ] ", "{} " , "{ } " , ".271 " , ".244 ",".248 " , "4k " , ]

        self.bads_noSpace = ["musicvideo" , "music video" , "youtube" , "you tube"
            , ".135" , "official" , "video" , "()" , "( )" , "135", ".137" , ".136" , "1080p" , "1080" , "720p" , "720" , "480p"  , "480",
            "hd" ,"full hd"  , "[]" , "[ ]", "{}" , "{ }" , ".271" , ".244", ".248" , "4k" ,]
        #endregion

    def add2bad(self,name):
        self.bads_noSpace.append(name)
        self.bads_rightSpace.append(name)
        self.bads_leftSpace.append(name)
        self.bads_twoSpace.append(name)

    def renamer(self,time):

        for (dirpath, dirname, filenames) in walk('.'+self.dirs):
            num = 1
            for name in filenames:
                dest = name
                # print(name)
                for bad in self.bads_twoSpace:
                    if bad in name.lower():
                        if dest == "":
                            dest = name.lower().replace("_"," ").replace(bad, "").replace("  ", " ")
                        else:
                            dest = dest.lower().replace("_"," ").replace(bad, "").replace("  ", " ")
                for bad in self.bads_leftSpace:
                    if bad in name.lower():
                        if dest == "":
                            dest = name.lower().replace("_"," ").replace(bad, "").replace("  ", " ")
                        else:
                            dest = dest.lower().replace("_"," ").replace(bad, "").replace("  ", " ")

                for bad in self.bads_rightSpace:
                    if bad in name.lower():
                        if dest == "":
                            dest = name.lower().replace("_"," ").replace(bad, "").replace("  ", " ")
                        else:
                            dest = dest.lower().replace("_"," ").replace(bad, "").replace("  ", " ")
                for bad in self.bads_noSpace:
                    if bad in name.lower():
                        if dest == "":
                            dest = name.lower().replace("_"," ").replace(bad, "").replace("  ", " ")
                        else:
                            dest = dest.lower().replace("_"," ").replace(bad, "").replace("  ", " ")



                if dest == name :
                    dest = name.replace("-.", ".").replace(" . ",".").replace(" .", ".").replace(". ", ".").replace("_"," ").replace("ft.","ft. ").replace("feat.","feat. ").replace("( ","(").replace(" )",")").replace("..",".").replace(" - ","-").replace(" -","-").replace("- ","-").replace("--","-").replace("---","-").replace("-"," - ").replace(" - .",".")
                if dest != name:                                                                                                                                                                                                                                                                                                                               # remove junk " - "
                    dest = dest.replace("-.", ".").replace(" . ",".").replace(" .", ".").replace(". ", ".").replace("_"," ").replace("ft.","ft. ").replace("feat.","feat. ").replace("( ","(").replace(" )",")").replace("..",".").replace(" - ","-").replace(" -","-").replace("- ","-").replace("--","-").replace("---","-").replace("-"," - ").replace(" - .",".")

                    lister = []
                    for i, s in enumerate(ndiff(name.lower(),dest )):
                        if s[0] == "-" : #and s[-1] != " ":
                            lister.append(s[-1])

                    print(name + "\n    ==> " + dest + "\n > (Removed: {} )".format("".join(lister))+"\n")

                    try:
                        rename(dirpath+sep+name,dirpath+sep+dest)
                    except FileExistsError:
                        try:
                            type = name[name.rfind("."):]
                            print(dest +" is already there. so changed to " +dest.replace(name[name.rfind("."):],"")+ "("+str(num)+")"+type)
                            rename(dirpath+sep+name,dirpath+sep+dest.replace(dest[dest.rfind("."):],"")+ "("+str(num)+")"+type)
                            num += 1
                        except FileExistsError:
                            type = name[name.rfind("."):]
                            rename(dirpath+sep+name,dirpath+sep+dest.replace(dest[dest.rfind("."):],"")+ "("+str(num+1)+")"+type)
                            num += 1
                    except PermissionError:
                        print(name + " is being used by another program there, close the program and try again")
        print(time + " Check Completed.")
if __name__ == "__main__":
    M = mains()
    M.bads()
    print("=====Junk-word-remover=====\n")
    # M.add2bad("sth")
    print("------------First Check------------\n")
    M.renamer("First")
    print("------------Second Check------------\n")
    M.renamer("Second")
    input("\n***Everything is fine, click enter to exit.***")
    # Captial first letter ==> title