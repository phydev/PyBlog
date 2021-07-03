import os

def generateIndex(folder, output, extensions = ['html']):
    """
    this function is responsible for reading the posts stored in `folder` 
    and generating an html file with a content table based on the metadata
    provided as comment in the first line of each post file.
    
    metadata format:
    <!--{"title": "", "date": "DD-MM-YYYY", "status": "hidden/show", "order": "0"} -->
    
    you may adapt it and add other informations to create more complex structures, 
    for example, you can add tags to build a word cloud and organise by topics
    """
    articles = []
    for file in os.listdir('./'+folder):
        if any(x in file for x in extensions):
            articles.append(file)


    metadata = {}
    patterns = {}
    article_number = 0
    for n, article in enumerate(articles):
        link="/"+folder+"/"+article
        with open("."+link) as file:
            line = file.readline() # read metadata from the first line
            metadata[n] = dict(eval(line[4:-4])) # remove html comment tags

        metadata[n]['link'] = link
        
        if metadata[n]['status'] == 'show':
            patterns[metadata[n]["order"]] = "<p><a href='"+metadata[n]['link']+"'> "+ str(metadata[n]["order"])+ " - " + metadata[n]["title"]+" </a></p>"
            article_number +=1

    with open(output, "w") as file:
        for line in range(0, article_number):
            file.write(patterns[str(line)])

# you can call this function several times and generate different lists for your site
generateIndex(folder="posts", output="posts.html")
