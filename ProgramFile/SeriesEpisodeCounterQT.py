from os import walk

class seasonable:
    def __init__(self):
        types = [".mp4",".mkv",".avi",".mpeg",".mpg"]

        movies = [["s1"],["s2"],["s3"],["s4"],["s5"],["s6"],["s7"],["s8"],["s9"],["s10"],
                       ["s11"],["s12"],["s13"],["s14"],["s15"],["s16"],["s17"],["s18"],["s19"],["s20"],
                     ["21"],["22"],["23"],["24"],["25"],["26"],["27"],["28"],["29"],["30"]]

        for (dirpath, dirname, filenames) in walk('.'):
            for filename in filenames:
                for type in types:
                    if type in filename:
                        filename = filename.replace(" ", "").lower().replace("season", "s").replace("فصل", "s").replace("ف","s").replace("s0", "s").replace("قسمت", "e").replace("ق", "e").replace("episode","e").replace("e0", "e")

                        season_num = filename[filename.rfind("s"):filename.rfind("e")]

                        episode_num = filename[filename.rfind("e"):filename.rfind(".")].replace("e", "")
                        for S in movies :
                            if S[0] == season_num:
                                S.append(episode_num)

        self.movies = []
        for movie in movies:
            if len(movie) > 1:
                self.movies.append(movie)

    def Ecounter(self):
        self.seasons = []
        self.missEpisode = []
        x = 0
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
                toPrint.append(season)
                self.missEpisode.append(toPrint)

    def Scounter(self):
        self.missSeason = []
        d = []
        count = 0
        while count < max(self.seasons):
                count += 1
                d.append(str(count))
        toPrint = []
        for du in d:
                if du not in str(self.seasons):
                    toPrint.append(du)
        self.missSeason.append(toPrint)

class noseason:
    def __init__(self):
        self.missEpisode = []
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
        self.missEpisode = toPrint

if __name__ == "__main__":
    pass