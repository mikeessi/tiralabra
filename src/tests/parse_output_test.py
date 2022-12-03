import unittest
from algorithms.parse_output import parse_wilson_output, parse_kruskal_output

class TestParseOutput(unittest.TestCase):

    def setUp(self):
        self.wilson_path = [(0,0),[(1,0),(0,0)],[(0,1),(1,1),(1,0)]]
        self.kruskal_path = [((0,0),(0,1)),((1,0),(1,1)),((1,0),(0,0))]

    def test_parse_wilson_output(self):
        parsed_wilson = parse_wilson_output(self.wilson_path)
        expected_output = [(0,0,None),(1,0,None),(0,0,"D"),(0,1,None),(1,1,"U"),(1,0,"R")]
        self.assertEqual(parsed_wilson,expected_output)

    def test_parse_kruskal_output(self):
        parsed_kruskal = parse_kruskal_output(self.kruskal_path)
        expected_output = [(0,0,None), (0,1,"L"),(1,0,None),(1,1,"L"),(0,0,"D")]
        self.assertEqual(parsed_kruskal, expected_output)
