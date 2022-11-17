import datetime


class ScoreCenter:
    def __init__(self):
        self.lis_of_score = []
        with open("data/scores.txt", "r", encoding="utf-8") as file:
            for i in file.readlines():
                self.lis_of_score.append(self.ParseString(i))
        self.sort_lis_of_score()

    def sort_lis_of_score(self):
        self.lis_of_score.sort(key=lambda x: (-x[1], x[2], x[0]))

    def ParseString(self, now_string):
        result = now_string.strip().split(";")
        result[1] = int(result[1])
        return result

    def GetHighScore(self):
        if len(self.lis_of_score) == 0:
            return 0
        return self.lis_of_score[0][1]

    def UpdateScore(self, name, score):
        with open("data/scores.txt", "a", encoding="utf-8") as file:
            file.seek(0, 2)
            file.write(str(f"{name};{score};{datetime.datetime.now()}\n"))
        self.lis_of_score.append([name, score, str(datetime.datetime.now())])
        self.sort_lis_of_score()




