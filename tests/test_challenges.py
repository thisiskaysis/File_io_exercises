import unittest, csv
from collections import Counter
from html.parser import HTMLParser
from challenges import count_mentions, generate_coloured_text, galactic_speed_percentile

class TestCase(unittest.TestCase):
    def test_count_mentions(self):
        with open("data/colours_20_simple.csv", "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            rgb, hex, colour_names = zip(*reader)
            colour_word_counts = Counter(
                [word.lower() for name in colour_names for word in name.split()]
            )
            for word, count in [("eigengrau", 0), *colour_word_counts.items()]:
                result = count_mentions(word)
                if type(result) != int:
                    self.fail(msg=f"\nYour function was supposed to return an integer, but instead it returned {type(result)}!")
                
                self.assertEqual(
                    count,
                    result,
                    msg=f"\nInput: {word}\nExpected result: {count}\nActual result: {result}"
                )

    def test_generate_coloured_text(self):
        class MyHTMLParser(HTMLParser):
            def __init__(self, *, convert_charrefs: bool = True) -> None:
                self.return_value = list()
                super().__init__(convert_charrefs=convert_charrefs)
            
            def handle_starttag(self, tag, attrs):
                self.return_value.extend([tag, dict(attrs)])
            
            def handle_data(self, data: str):
                self.return_value.append(str(data).strip())
            
            def get_return_value(self):
                to_return = self.return_value
                self.return_value = list()
                return to_return
        
        with open("data/colours_865.csv", "r") as file:
            reader = csv.DictReader(file)
            parser = MyHTMLParser()

            for row in reader:
                actual_result = generate_coloured_text(row["English"])

                if type(actual_result) != str:
                    self.fail(msg=f"\nYour function was supposed to return a string, but instead it returned {type(actual_result)}!")
                
                parser.feed(actual_result)

                tag, attrdict, data = parser.get_return_value()
            
                intended_result = f"""<p style="color:{row['HEX']};">{row['English']}</p>"""

                self.assertTrue(
                    (tag=="p" 
                    and attrdict.get("style", "").strip()==f"color:{row['HEX']};"
                    and data == row['English']),
                    msg=f"""\nInput: {row["English"]}\nExpected result: {intended_result}\nActual result: {actual_result}"""
                )

    def test_galactic_speed_percentile(self):
        with open("data/galaxies.csv", "r") as file:
            reader = csv.reader(file)

            for index, speed in reader:
                input_speed = float(speed)+0.5
                expected_result = 100*(82-float(index))/82
                actual_result = galactic_speed_percentile(input_speed)

                if type(actual_result) != float:
                    self.fail(msg=f"\nYour function was supposed to return a float, but instead it returned {type(actual_result)}!")

                self.assertAlmostEqual(
                    actual_result, 
                    expected_result,
                    places=2,
                    msg=f"\nInput: {input_speed}\nExpected result: {expected_result}\nActual result: {actual_result}"
                )
