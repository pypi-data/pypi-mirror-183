# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reddit_comment_scrapper']

package_data = \
{'': ['*']}

install_requires = \
['praw>=7.6.1,<8.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['reddit-comment-scrapper = '
                     'reddit_comment_scrapper.main:app']}

setup_kwargs = {
    'name': 'reddit-comment-scrapper',
    'version': '0.2.0',
    'description': 'Scrape Reddit Comments as a graph structure',
    'long_description': '# Usage\n\nRun \n```\npip install reddit-comment-scrapper\n```\n\nProvide the details\n```\nreddit-comment-scrapper Reddit_ID Reddit_Secret name_subreddit post_category , number_of_posts\n\n## Structure of JSON File\n\n- Each Submission has two entries\n    - Submission Body\n    - List of Dictionary of top level Replies \n- Each reply has 3 enteries\n    - id of reply\n    - Body of Reply\n    - List of Dictionary of second level Replies\n\nAnd this goes on Recursively in a depth first search manner till a reply with no further reply is found\n\nJSON File always stored in a comments.json',
    'author': 'Prarabdha',
    'author_email': 'prabodhkumarsrivastav70@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
