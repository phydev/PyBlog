[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://phydev.github.io/PyBlog)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# PyBlog
Minimal serverless blog system powered by python and GitHub Actions.


| Files |  Description  |
| ------------------- | ------------------- |
|  [deploy.py](https://github.com/phydev/PyBlog/blob/main/deploy.py) |  the blog system's heart|
| [posts.html](https://github.com/phydev/PyBlog/blob/main/posts.html) | this file contains the list of posts and it's generated as output by deploy.py|
| [index.html](https://github.com/phydev/PyBlog/blob/main/index.html) | website main page - we will import posts.html here |
|  [main.yml](https://github.com/phydev/PyBlog/blob/main/.github/workflows/main.yml) | This is the workflow ran by Actions  |


# How to use

Clone this repository into your machine:

```
  git clone https://github.com/phydev/PyBlog.git
```

Then the following files must be edited:
1. Replace line [22](https://github.com/phydev/PyBlog/blob/85b8baf2ac72f76ea71f9289b2dca459b48aa57c/.github/workflows/main.yml#L22) and [23](https://github.com/phydev/PyBlog/blob/85b8baf2ac72f76ea71f9289b2dca459b48aa57c/.github/workflows/main.yml#L23) with your github credentials in the file [main.yml](https://github.com/phydev/PyBlog/blob/main/.github/workflows/main.yml). 

2. If you already have a website, you should copy the following lines into your index.html:
```html
<div id="posts-placeholder"></div>
<script>
    $(function(){
        $("#posts-placeholder").load("posts.html");
      });
</script>
```

The list of posts will appear in the div `posts-placeholder`. If you're starting a website from scratch now, you can just edit the [index.html](https://github.com/phydev/PyBlog/blob/main/index.html) provided in this  repository.

You must import jQuery to use the load function above, so add the following line between the `<head>` tag in your `index.html` file:
```html
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
```

3. Create a `posts` folder inside your website repository.

4. Start writting your posts! Don't forget to add in the first line of your html articles a comment with the metadata for the posts:
```
<!--{"title": "This is a blog post", "date": "03-07-2021", "status": "show", "order": "0"} -->
```

If you've a website copy [deploy.py](https://github.com/phydev/PyBlog/blob/main/deploy.py) into the root directory of your repository and [main.yml](https://github.com/phydev/PyBlog/blob/main/.github/workflows/main.yml) into `.github/workflows/`. Otherwise, just push all the files cloned with the edits above.


That's all!


