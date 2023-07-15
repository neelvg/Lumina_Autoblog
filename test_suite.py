import unittest

from main import research, generateTitles, generateContents, rewrite, publish


class TestResearch(unittest.TestCase):

    def test_research(self):
        highDemandTitles, seo, keywords = research()
        self.assertIsInstance(highDemandTitles, list)
        self.assertIsInstance(seo, list)
        self.assertIsInstance(keywords, list)
        self.assertGreater(len(highDemandTitles), 0)
        self.assertGreater(len(seo), 0)
        self.assertGreater(len(keywords), 0)


class TestGenerateTitles(unittest.TestCase):

    def test_generateTitles(self):
        highDemandTitles, seo, keywords = research()
        titles = generateTitles(highDemandTitles, seo, keywords)
        self.assertIsInstance(titles, list)
        self.assertGreater(len(titles), 0)
        for title in titles:
            self.assertIsInstance(title, str)
            self.assertGreater(len(title), 0)


class TestGenerateContents(unittest.TestCase):

    def test_generateContents(self):
        titles = generateTitles()
        contents = generateContents(titles)
        self.assertIsInstance(contents, list)
        self.assertGreater(len(contents), 0)
        for content in contents:
            self.assertIsInstance(content, str)
            self.assertGreater(len(content), 0)


class TestRewrite(unittest.TestCase):

    def test_rewrite(self):
        contents = generateContents()
        rewrittenContents = rewrite(contents)
        self.assertIsInstance(rewrittenContents, list)
        self.assertGreater(len(rewrittenContents), 0)
        for rewrittenContent in rewrittenContents:
            self.assertIsInstance(rewrittenContent, str)
            self.assertGreater(len(rewrittenContent), 0)


class TestPublish(unittest.TestCase):

    def test_publish(self):
        titles = generateTitles()
        contents = generateContents()
        publish(titles, contents)


if __name__ == "__main__":
    unittest.main()
