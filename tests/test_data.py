import unittest

from tennis_analysis.data import (
    _normalize_player_name,
    _calculate_age,
    _get_opponent_age,
    _parse_career_js,
)


class TestTennisData(unittest.TestCase):

    def test_player_name(self):
        self.assertEqual(
            _normalize_player_name("Serena Williams"),
            _normalize_player_name("serena williams"),
        )

    def test_calculate_age(self):
        age = _calculate_age("19810926", "19951030")
        self.assertAlmostEqual(age, 14.09, places=2)

    def test_female_opponent_age(self):
        age = _get_opponent_age("19770119", "19951030")
        self.assertAlmostEqual(age, 18.78, places=2)

    def test_male_opponent_age(self):
        age = _get_opponent_age("22.264202601", "20010910")
        self.assertAlmostEqual(age, 22.264202601)

    def test_parse_career_js(self):
        js = 'var morematchmx = [["20200101", "Test Open"]];'
        matches = _parse_career_js(js)
        self.assertEqual(matches[0][1], "Test Open")


if __name__ == "__main__":
    unittest.main()