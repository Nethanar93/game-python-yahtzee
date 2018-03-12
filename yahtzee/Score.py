class Score:
    def __init__(self, bonus_thresh=42):
        self.scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bonus_thresh = bonus_thresh

    def get_single(self, value):
        return self.scores[value - 1]

    def set_single(self, value, count):
        self.scores[value-1] = value * count

    def get_inter_score(self):
        return self.scores[6]

    def set_inter_score(self):
        for i in range(6):
            self.scores[6] += self.get_single(i)

    def get_bonus(self):
        return self.scores[7]

    def set_bonus(self):
        if self.get_inter_score() >= self.bonus_thresh:
            self.scores[7] = 50

    def get_one_pair(self):
        return self.scores[8]

    def set_one_pair(self, value):
        self.scores[8] = value * 2

    def get_two_pairs(self):
        return self.scores[9]

    def set_two_pairs(self, value_1, value_2):
        self.scores[9] = value_1 * 2 + value_2 * 2

    def get_three_same(self):
        return self.scores[10]

    def set_three_same(self, value):
        self.scores[10] = value * 3

    def get_four_same(self):
        return self.scores[11]

    def set_four_same(self, value):
        self.scores[11] = value * 4

    def get_sm_straight(self):
        return self.scores[12]

    def set_sm_straight(self):
        self.scores[12] = 15

    def get_lg_straight(self):
        return self.scores[13]

    def set_lg_straight(self):
        self.scores[13] = 21

    def get_house(self):
        return self.scores[14]

    def set_house(self, over, under):
        self.scores[14] = over * 3 + under * 2

    def get_chance(self):
        return self.scores[15]

    def set_chance(self, val1, val2, val3, val4, val5):
        self.scores[15] = val1 + val2 + val3 + val4 + val5

    def get_yahtzee(self):
        return self.scores[16]

    def set_yahtzee(self):
        self.scores[16] = 100

    def get_tot_score(self):
        return self.scores[17]

    def set_tot_score(self):
        self.scores[17] += self.get_inter_score() + self.get_bonus() + self.get_one_pair() + self.get_two_pairs()
        self.scores[17] += self.get_three_same() + self.get_four_same() + self.get_sm_straight() + self.get_lg_straight()
        self.scores[17] += self.get_house() + self.get_chance() + self.get_yahtzee()

