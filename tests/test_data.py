import unittest

from tennis_analysis.data import (
    _build_match_dataframe,
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

    def test_female_match_dataframe(self):
        match = [""] * 27
        match[0] = "19951030"
        match[1] = "Canadian Open"
        match[2] = "Carpet"
        match[4] = "L"
        match[11] = "Anne Miller"
        match[16] = "19770119"

        df = _build_match_dataframe([match], "19810926")

        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["result"], "loss")
        self.assertAlmostEqual(df.iloc[0]["opponent_age"], 18.78, places = 2)

    def test_male_match_dataframe(self):
        match = [""] * 49
        match[0] = "20010910"
        match[1] = "Spain F10"
        match[2] = "Hard"
        match[4] = "L"
        match[11] = "Guillermo Platel"
        match[16] = "22.264202601"

        df = _build_match_dataframe([match], "19860603")

        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["result"], "loss")
        self.assertAlmostEqual(df.iloc[0]["opponent_age"], 22.26, places = 2)

if __name__ == "__main__":
    unittest.main()