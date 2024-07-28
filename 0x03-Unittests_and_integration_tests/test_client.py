#!/usr/bin/env python3
"""Module to test GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"key": "value"})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test the public repos URL"""
        mock_org.return_value = {"repos_url": "http://test_url.com"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "http://test_url.com")

    @patch('client.get_json', return_value=[{"name": "repo1"}, {"name": "repo2"}])
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public repos"""
        mock_public_repos_url.return_value = "http://test_url.com"
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://test_url.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)


if __name__ == "__main__":
    unittest.main()
