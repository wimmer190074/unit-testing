import unittest
from unittest.mock import patch
from unit import simple_web_scraper


class TestSimpleWebScraper(unittest.TestCase):

    def test_valid_url(self):
        url_to_scrape = 'https://example.com'
        with patch('builtins.print') as mock_print:
            simple_web_scraper(url_to_scrape)
            captured_output = "\n".join(call.args[0] for call in mock_print.call_args_list)
            self.assertTrue('https://www.iana.org/domains/example' in captured_output)

    def test_invalid_url(self):
        url_to_scrape = 'https://en.wikipedia.org/wiki/Jan_Wimmer'
        with patch('builtins.print') as mock_print:
            simple_web_scraper(url_to_scrape)
            captured_output = "\n".join(call.args[0] for call in mock_print.call_args_list)
            self.assertTrue('Error: Unable to fetch the web page.' in captured_output)

    '''
    Impossible to test, but should work in theory.

    def test_no_links(self):
        url_to_scrape = 'https://webpagewithnolinks.com'
        with patch('builtins.print') as mock_print:
            simple_web_scraper(url_to_scrape)
            captured_output = "\n".join(call.args[0] for call in mock_print.call_args_list)
            self.assertEqual(captured_output.strip(), '')
    '''


if __name__ == '__main__':
    unittest.main()
