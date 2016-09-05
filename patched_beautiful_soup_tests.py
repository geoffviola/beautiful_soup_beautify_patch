#!/usr/bin/env python

import unittest
from bs4 import BeautifulSoup
import patched_beautiful_soup


class TestStringMethods(unittest.TestCase):
    maxDiff = None

    def assert_pretty_print(self, filename_base):
        default_extension = '.html'
        html_unformatted_string = ''
        with open(filename_base + '_unformatted' + default_extension, 'r') as unformatted_file:
            html_unformatted_string = unformatted_file.read()
        html_formatted_string = ''
        with open(filename_base + '_formatted' + default_extension, 'r') as formatted_file:
            html_formatted_string = formatted_file.read()
        bs_html = BeautifulSoup(html_unformatted_string, "lxml")
        pretty_html = bs_html.prettify(formatter="html")
        self.assertEqual(pretty_html, html_formatted_string)

    def test_p_multiline(self):
        self.assert_pretty_print('p_multiline')

    def test_3_a_inline(self):
        self.assert_pretty_print('3_a_inline')

    def test_3_a_multiline(self):
        self.assert_pretty_print('3_a_multiline')

    def test_p_with_a_inline(self):
        self.assert_pretty_print('p_with_a_inline')

    def test_p_with_a_multiline(self):
        self.assert_pretty_print('p_with_a_multiline')

    def test_p_inline(self):
        self.assert_pretty_print('p_inline')

    def test_title(self):
        self.assert_pretty_print('title')


if __name__ == '__main__':
    unittest.main()
