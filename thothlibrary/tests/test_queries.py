"""
Tests for generated GraphQL query field selections.
"""
import unittest
from importlib import import_module


queries = import_module("thothlibrary.thoth-1_0_0.queries")


class QueryFieldTests(unittest.TestCase):
    def test_work_full_fields_use_featured_video(self):
        fields = " ".join(queries.WORK_FULL_FIELDS)

        self.assertIn("featuredVideo { workFeaturedVideoId", fields)
        self.assertNotIn("workFeaturedVideos {", fields)

    def test_work_list_fields_use_featured_video(self):
        fields = " ".join(queries.WORK_LIST_FIELDS)

        self.assertIn("featuredVideo { workFeaturedVideoId", fields)
        self.assertNotIn("workFeaturedVideos {", fields)


if __name__ == "__main__":
    unittest.main()
