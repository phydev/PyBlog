[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://phydev.github.io/PyBlog)
[![Python 3](https://pyup.io/repos/github/ocbe-uio/trajpy/python-3-shield.svg)](https://pyup.io/repos/github/ocbe-uio/trajpy/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# PyBlog
Minimal serverless blog system powered by python and GitHub Actions.


| Files |  Description  |
| ------------------- | ------------------- |
|  [deploy.py](https://github.com/phydev/PyBlog/blob/main/deploy.py) |  the blog system's heart|
| [posts.html](https://github.com/phydev/PyBlog/blob/main/posts.html) | this file contains the list of posts and it's generated as output by deploy.py|
| [index.html](https://github.com/phydev/PyBlog/blob/main/index.html) | website main page - we will import posts.html here |
|  [main.yml](https://github.com/phydev/PyBlog/blob/main/.github/workflows/main.yml) | This is the workflow ran by Actions  |

## Why?

I was looking for solutions that would allow me to have a list of posts generated automatically immediately after pushing new articles into my website repository. The challenge is to have such a system while you keep your website serverless with static html only.

The most well established method is [Jekyll](https://github.com/jekyll/jekyll), a static site generator that is the engine behind [GitHub Pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll). This method is great if you're not looking to customise your website too much - just select an available theme and use as it is. My problem with this method is that I found customization quite difficult and the configuration system is not very intuitive to navigate. I wanted to have just a simple professional website, but the available themes would not fit my purpose. 

So I understood the mechanisms behind Jekyll and decide to build something similar, but simpler and that would give me total control of my website. This is how PyBlog was born.

- Advantages
  - Easy to configure
  - Customizing is simple
  - It's free and the method can be adapted for creating more complex systems
- Weak points
  - At this point it's too simple, if you need something more you'll need to code yourself
  - As I'm the solo maintainer, requests might take a while to be implemented :)    

## How to use?

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

You must import jQuery to use the `load` function above, so add the following line between the `<head>` tag in your `index.html` file:
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


## How it works?

The system is devided into two main components represented in the flowcharts bellow. The first component is the executation of the `deploy.py` via GitHub Actions to read the articles that are stored in the subdirectory `/posts/`. The python script will generate a new file called `posts.html` which contains only a list of links for your posts. Then we use git add/commit/push to keep this new file into the repository. 

![PyBlog flowchart](https://github.com/phydev/PyBlog/blob/700c28a352072e341ca8e047e8a196da23681a0e/docs/PyBlog.png)

The second part is just static html. We use a jQuery function to load the posts list into the `index.html`. 

![PyBlog flowchart - part 2](https://github.com/phydev/PyBlog/blob/700c28a352072e341ca8e047e8a196da23681a0e/docs/PyBlog_jQuery.png) 


## Wish to become a contributor?
If you think this is an interesting project for you, let's talk via [twitter](https://twitter.com/phydev_) or send me an email. 

Feel free to [fork](https://github.com/phydev/PyBlog/fork) and submit pull requests. 

## Improvements
- Organize posts by date instead of providing explicit order
- Add keywords in the metadata and implement a word cloud solution

