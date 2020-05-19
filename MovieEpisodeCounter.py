from os import sep, listdir, getcwd, chdir, path, walk


# import os.path


class seasonable:
    def __init__(self):
        # numbers = ["0","1","2","3","4","5","6","7","8","9"]
        types = [".mp4",".mkv",".avi",".mpeg",".mpg"]

        movies = [["s1"],["s2"],["s3"],["s4"],["s5"],["s6"],["s7"],["s8"],["s9"],["s10"],
                       ["s11"],["s12"],["s13"],["s14"],["s15"],["s16"],["s17"],["s18"],["s19"],["s20"]]

        for (dirpath, dirname, filenames) in walk('.'):
            for filename in filenames:
                for type in types:
                    if type in filename:
                        filename = filename.replace(" ", "").lower().replace("season", "s").replace("فصل", "s").replace("ف","s").replace("s0", "s").replace("قسمت", "e").replace("ق", "e").replace("episode","e").replace("e0", "e")
                        # print(filename)

                        season_num = filename[filename.rfind("s"):filename.rfind("e")]
                        # print(season_num)
                        episode_num = filename[filename.rfind("e"):filename.rfind(".")].replace("e", "")
                        for S in movies :
                            if S[0] == season_num:
                                S.append(episode_num)
        # print(len(self.movies[2]))
        self.movies = []
        for movie in movies:
            if len(movie) > 1:
                self.movies.append(movie)

        # print(self.movies)

    def Ecounter(self):
        self.seasons = []
        for movie in self.movies:
            if len(movie) != 1:
                season = movie[0]
                self.seasons.append(int(season.replace("s","")))
                movie.remove(movie[0])

                x = 0
                while x < len(movie):
                    movie[x] = int(movie[x])
                    x +=1

                movie = list(filter(None, movie))
                movie = sorted(movie)

                d = []
                count = 0
                while count < max(movie):
                    count += 1
                    d.append(str(count))

                toPrint = []
                for du in d:
                    if du not in str(movie):
                        toPrint.append(du)
                if len(toPrint) > 1 :
                    print(str(len(toPrint)) + " Episodes are missing "+ "in " + season.replace("s","Season *") + "* :    ",str(toPrint).replace("[","").replace("]","").replace("\'",""))
                else:
                    print("1 Episode is missing " + "in " + season.replace("s", "Season *") + "* :    ",str(toPrint).replace("[", "").replace("]", "").replace("\'",""))

    def Scounter(self):
        d = []
        count = 0
        while count < max(self.seasons):
                count += 1
                d.append(str(count))
        toPrint = []
        for du in d:
                if du not in str(self.seasons):
                    toPrint.append(du)

        if len(toPrint) > 1:
            print("Missing Seasons are :    ", str(toPrint).replace("[", "").replace("]", "").replace("\'",""))
        else:
            print("Missing Season is :    ", str(toPrint).replace("[", "").replace("]", "")).replace("\'","")

        # print(self.movies)

class noseason:
    def __init__(self):
        types = [".mp4", ".mkv", ".avi", ".mpeg", ".mpg"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Episodes = []
    
        for (dirpath, dirname, filenames) in walk('.'):
            for filename in filenames:
                for type in types:
                    if type in filename:
                        filename = filename.replace(" ", "").lower().replace("قسمت", "e").replace("ق", "e").replace(
                            "episode", "e").replace("e0", "e")
                        episode_num = filename[filename.rfind("e"):filename.rfind(".")].replace("e", "")
                        for num in numbers:
                            if num in episode_num:
                                Episodes.append(int(episode_num))
    
        Episodes = list(filter(None, Episodes))
        Episodes = sorted(Episodes)
    
        d = []
        count = 0
        while count < max(Episodes):
            count += 1
            d.append(str(count))
    
        toPrint = []
        for du in d:
            if du not in str(Episodes):
                toPrint.append(du)
        print("\n========Episodes========\n")
        if len(toPrint) > 1:
            print("All missing Episodes are : " + str(toPrint).replace("\'", "").replace("[","").replace("]",""))
        else:
            print("The missing Episode is :    "+ str(toPrint).replace("\'", "").replace("[","").replace("]",""))




if __name__ == "__main__":
    print("========Series-Counter========\n")
    ans = input("Does the series specified with seasons?(yes,no)\n> ").lower()
    if ans == "yes":
        try:
            S = seasonable()
            print("\n========Episodes========\n")
            S.Ecounter()
            print("\n========Seasons========\n")
            S.Scounter()
        except :
            print("Error accrued !!! , be sure about season choice.")
        input()
    elif ans == "no":
        try:
            N = noseason()
        except :
            print("Error accrued !!! , be sure about season choice.")
        input()
    else:
        print("Wrong entrance!!!")
        input()
