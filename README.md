[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://phydev.github.io/PyBlog)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# PyBlog
Serverless blog system powered by python and GitHub Actions.


| Files |  Description  |
| ------------------- | ------------------- |
|  [deploy.py](https://github.com/phydev/PyBlog/blob/main/deploy.py) |  the blog system's heart|
| [posts.html](https://github.com/phydev/PyBlog/blob/main/posts.html) | this file contains the list of posts and it's generated as output by deploy.py|
| [index.html](https://github.com/phydev/PyBlog/blob/main/index.html) | website main page - we will import posts.html here |
|  [main.yml](https://github.com/phydev/PyBlog/blob/main/.github/workflows/main.yml) | This is the workflow ran by Actions  |
