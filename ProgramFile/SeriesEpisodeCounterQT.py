from os import walk

class seasonable:
    def __init__(self):
        types = [".mp4", ".mkv", ".avi", ".mpeg", ".mpg"]
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        movies = [["S1"], ["S2"], ["S3"], ["S4"], ["S5"], ["S6"], ["S7"], ["S8"], ["S9"], ["S10"],
                  ["S11"], ["S12"], ["S13"], ["S14"], ["S15"], ["S16"], ["S17"], ["S18"], ["S19"], ["S20"],
                  ["S21"], ["S22"], ["S23"], ["S24"], ["S25"], ["S26"], ["S27"], ["S28"], ["S29"], ["S30"]]

        for (dirpath, dirname, filenames) in walk('.'):
            for filename in filenames:
                for type in types:
                    if type in filename:
                        filename = filename.replace(" ", "").lower().replace("season", "S").replace("فصل", "S").replace(
                            "ف", "S").replace("s0", "S").replace("قسمت", "E").replace("ق", "E").replace("episode",
                                                                                                        "E").replace(
                            "e0", "E").replace("10bit", "").replace("1080p", "").replace("1080", "").replace("720p",
                                                                                                             "").replace(
                            "720", "").replace("x265", "").replace("x264", "").replace("480p", "").replace("480",
                                                                                                           "").replace(
                            "4k", "")
                        filename = filename.replace("s1", "S1").replace("s2", "S2").replace("e3", "E3").replace("e4",
                                                                                                                "E4").replace(
                            "e5", "E5").replace("e6", "E6").replace("e7", "E7").replace("e8", "E8").replace("e9", "E9")
                        filename = filename.replace("e1", "E1").replace("e2", "E2").replace("e3", "E3").replace("e4",
                                                                                                                "E4").replace(
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
        for movie in self.movies:
            if len(movie) != 1:
                season = movie[0]
                self.seasons.append(int(season.replace("S","")))
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
                        filename = filename.replace(" ", "").lower().replace("قسمت", "E").replace("ق", "E").replace(
                            "episode", "E").replace("e0", "E").replace("10bit", "").replace("1080p", "").replace("1080",
                                                                                                                 "").replace(
                            "720p", "").replace("720", "").replace("x265", "").replace("x264", "").replace("480p",
                                                                                                           "").replace(
                            "480", "").replace("4k", "")
                        filename = filename.replace("e1", "E1").replace("e2", "E2").replace("e3", "E3").replace("e4",
                                                                                                                "E4").replace(
                            "e5", "E5").replace("e6", "E6").replace("e7", "E7").replace("e8", "E8").replace("e9", "E9")

                        episode_num = filename[filename.rfind("E"):filename.rfind("E") + 4].replace("E", "")
                        for letter in episode_num:
                            if letter not in numbers:
                                episode_num = episode_num.replace(letter, "")

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