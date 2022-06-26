"""
Two-pass algorithm exercise, and practice for
'remote' exam:   Calculate a project score
average in which one project is dropped,
maximizing average = (total score / possible score).
"""
from typing import List
import unittest
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
#Q1 ##### QUESTION 1 (DO NOT REMOVE OR ALTER THIS LINE)
# Brute force approach that I have been using in Excel

def best_drop_one(scores: List[int], avail: List[int]) -> float:
    """Returns the max of actual_sum/avail_sum, where actual_sum
    is the sum of all but one of the 'scores' values,
    and avail_sum is the sum of corresponding values in avail.
    The column dropped from both rows is selected to maximize
    the result.
    Brute force version:  Calculate average for every choice
    of dropped column and return the maximum.
    """
    averages = [ ]
    for to_drop in range(len(avail)):
        ## to_drop is the column that we will *not* include
        sum_actual = 0
        sum_avail = 0
        for col in range(len(avail)):
            if col == to_drop:
                continue  # Skip this column
            sum_avail += avail[col]
            sum_actual += scores[col]
        averages.append(sum_actual / sum_avail)
    log.debug(f"All drop-one averages: {averages}")
    log.debug(f"Will select {max(averages)}")
    return max(averages)

def better_drop_one(scores: List[int], avail: List[int]) -> float:
    """Max average actual/possible, where actual is scores with
    one column dropped and possible is avail with a corresponding
    column dropped.
    Must run in linear time and without creating new lists.
    """
    best_average = 0.0
    lowest_weighted_score = scores[0]/avail[0]
    lowest_weighted_score_pos = 0
    weighted_score = 0
    weighted_avail = 0
    # You might need more code here
    log.debug(f"better_drop_one returning {best_average}")
    for i in range ((len(avail))-1):
        if (int(scores[i+1])/int(avail[i+1])) < (lowest_weighted_score):
            lowest_weighted_score = int(scores[i+1])/int(avail[i+1])
            lowest_weighted_score_pos = (i+1)
        if (int(scores[i+1])/int(avail[i+1])) == (lowest_weighted_score):
            if int(avail[i+1]) > int(avail[lowest_weighted_score_pos]):
                lowest_weighted_score = int(scores[i + 1]) / int(avail[i + 1])
                lowest_weighted_score_pos = (i + 1)
    scores.pop(lowest_weighted_score_pos)
    avail.pop(lowest_weighted_score_pos)
    for i in range (len(avail)):
        weighted_score += scores[i]
        weighted_avail += avail[i]
    best_average = (weighted_score/weighted_avail)
    return best_average

class Test_01_Drop_One(unittest.TestCase):
    def setUp(self) -> None:
        self.max_points = [50, 50, 100, 100, 75, 80, 100, 100, 100]
        self.delta = 0.001
    def test_stu1(self):
        stu1 = [40, 42, 100, 100, 74, 80, 100, 100, 100]
        self.assertAlmostEqual(best_drop_one(stu1, self.max_points),
                               0.9872340425531915, delta=self.delta)
        self.assertAlmostEqual(better_drop_one(stu1, self.max_points),
                               0.9872340425531915, delta=self.delta)
    def test_stu10(self):
        stu10 = [40, 0, 80, 100, 71, 80, 0, 75, 100]
        self.assertAlmostEqual(best_drop_one(stu10, self.max_points),
                               0.833587786259542, delta=self.delta)
        self.assertAlmostEqual(better_drop_one(stu10, self.max_points),
                               0.833587786259542, delta=self.delta)
    def test_stu22(self):
        stu22 = [50, 46, 100, 90, 72, 72, 95, 75, 85]
        self.assertAlmostEqual(best_drop_one(stu22, self.max_points),
                               0.9312977099236641, delta=self.delta)
        self.assertAlmostEqual(better_drop_one(stu22, self.max_points),
                               0.9312977099236641, delta=self.delta)

#Q2 ####### Don't take away this line either
# I don't really have a second problem yet, but I want to test
# turning in multiple files for an exam.

def life_the_universe_and_everything() -> int:
    """Perhaps the spec should be clearer"""
    #BUT WHAT IS THE QUESTION TO LIFE THE UNIVERSE AND EVERYTHING!?
    return 42

class Test_42_Fake(unittest.TestCase):
    """The Hitchhikers' Guide is 42 years old this year.
    I had the original radio show on cassette tapes, perfect
    for a long drive.
    """
    def test_fake(self):
        """I think this test case will pass"""
        self.assertEqual(life_the_universe_and_everything(), 42)
if __name__ == "__main__":
    unittest.main()