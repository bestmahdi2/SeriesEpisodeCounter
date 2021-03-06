from os import walk

class seasonable:
    def __init__(self,dir):
        types = [".mp4", ".mkv", ".avi", ".mpeg", ".mpg"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        movies = [["S1"], ["S2"], ["S3"], ["S4"], ["S5"], ["S6"], ["S7"], ["S8"], ["S9"], ["S10"],
                  ["S11"], ["S12"], ["S13"], ["S14"], ["S15"], ["S16"], ["S17"], ["S18"], ["S19"], ["S20"],
                  ["S21"], ["S22"], ["S23"], ["S24"], ["S25"], ["S26"], ["S27"], ["S28"], ["S29"], ["S30"]]

        for (dirpath, dirname, filenames) in walk(dir):
            for filename in filenames:
                for type in types:
                    if type in filename:
                        filename = filename.replace(" ", "").lower().replace("season", "s").replace("فصل", "s").replace(
                            "ف", "s").replace("s0", "s").replace("قسمت", "e").replace("ق", "e").replace("episode","e").replace(
                            "e0", "e").replace("10bit", "").replace("1080p", "").replace("1080", "").replace("720p","").replace(
                            "720", "").replace("x265", "").replace("x264", "").replace("480p", "").replace("480","").replace(
                            "4k", "")

                        filename = filename.replace("s1", "S1").replace("s2", "S2").replace("s3", "S3").replace("s4","S4").replace(
                            "s5", "S5").replace("s6", "S6").replace("s7", "S7").replace("s8", "S8").replace("s9", "S9")

                        filename = filename.replace("e1", "E1").replace("e2", "E2").replace("e3", "E3").replace("e4","E4").replace(
                            "e5", "E5").replace("e6", "E6").replace("e7", "E7").replace("e8", "E8").replace("e9", "E9")

                        season_num = filename[filename.rfind("S"):filename.rfind("E")]

                        episode_num = filename[filename.rfind("E"):filename.rfind("E") + 3].replace("E", "")
                        for letter in episode_num:
                            if letter not in numbers:
                                episode_num = episode_num.replace(letter, "")

                        for S in movies:
                            if S[0] == season_num:
                                S.append(episode_num)

        self.movies = []
        for movie in movies:
            if len(movie) > 1:
                self.movies.append(movie)
        # print(self.movies)

    def Ecounter(self):
        self.seasons = []
        self.missEpisode = []
        x = 0
        for movie_Str in self.movies:
            if len(movie_Str) != 1:
                season = movie_Str[0]
                self.seasons.append(int(season.replace("S", "")))
                movie_Str.remove(movie_Str[0])

                movie = []
                x = 0
                while x < len(movie_Str):
                    movie.append(int(movie_Str[x]))
                    x += 1

                movie = list(filter(None, movie))
                movie = sorted(movie)

                d = []
                count = 0
                while count < max(movie):
                    count += 1
                    d.append(str(count))

                toPrint = []
                for du in d:
                    if du not in movie_Str:
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
    def __init__(self,dir):
        self.missEpisode = []
        types = [".mp4", ".mkv", ".avi", ".mpeg", ".mpg"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        Episodes = []
        Episodes_Str = []
    
        for (dirpath, dirname, filenames) in walk(dir):
            for filename in filenames:
                for type in types:
                    if type in filename:
                        filename = filename.replace(" ", "").lower().replace("قسمت", "e").replace("ق", "e").replace(
                            "episode", "e").replace("e0", "e").replace("10bit", "").replace("1080p", "").replace("1080","").replace(
                            "720p", "").replace("720", "").replace("x265", "").replace("x264", "").replace("480p","").replace(
                            "480", "").replace("4k", "")

                        filename = filename.replace("e1", "E1").replace("e2", "E2").replace("e3", "E3").replace("e4","E4").replace(
                            "e5", "E5").replace("e6", "E6").replace("e7", "E7").replace("e8", "E8").replace("e9", "E9")

                        episode_num = filename[filename.rfind("E"):filename.rfind("E") + 4].replace("E", "")
                        for letter in episode_num:
                            if letter not in numbers:
                                episode_num = episode_num.replace(letter, "")

                        for num in numbers:
                            if num in episode_num:
                                Episodes_Str.append(episode_num)
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
            if du not in Episodes_Str:
                toPrint.append(du)
        self.missEpisode = toPrint

if __name__ == "__main__":
    pass