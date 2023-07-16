import unittest

from main import research, generate_titles, generate_contents, rewrite, publish


class TestResearch(unittest.TestCase):

    def test_research(self):
        high_demand_titles, seo, keywords = research()
        self.assertIsInstance(high_demand_titles, list)
        self.assertIsInstance(seo, list)
        self.assertIsInstance(keywords, list)


class TestGenerateTitles(unittest.TestCase):

    def test_generate_titles(self):
        titles = generate_titles()
        self.assertIsInstance(titles, list)
        self.assertGreater(len(titles), 0)


class TestGenerateContents(unittest.TestCase):

    def test_generate_contents(self):
        contents = generate_contents()
        self.assertIsInstance(contents, list)
        self.assertGreater(len(contents), 0)


class TestRewrite(unittest.TestCase):

    def test_rewrite(self):
        contents = generate_contents()
        rewritten_contents = rewrite(contents)
        self.assertIsInstance(rewritten_contents, list)
        self.assertGreater(len(rewritten_contents), 0)


class TestPublish(unittest.TestCase):

    def test_publish(self):
        titles = generate_titles()
        contents = generate_contents()
        publish(titles, contents)


if __name__ == "__main__":
    unittest.main()
