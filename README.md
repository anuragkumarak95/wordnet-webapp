# wordnet-webapp

Web Application of [WordNet](https://github.com/anuragkumarak95/wordnet) with Flask Framework.

## What is Flask

`Flask` is a micro web framework written in `Python` and based on the Werkzeug toolkit and Jinja2 template engine. It is BSD licensed. Applications that use the Flask framework include Pinterest, LinkedIn, and the community web page for Flask itself.

[here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) you can easily learn how to create an webapp using Flask Framework. (best that I have read)

![Made with python3.5](http://forthebadge.com/images/badges/made-with-python.svg)

## Way to go

1. `Clone this repository` and go to root directory (~wordnet-webapp) and `run` this script

        $pip install -r requirements.txt

1. Then `run` this script

        $python run.py

1. Then browse at  the address that is provided at your `console`.

**OR using Dockerfile**

1. `Pull` the Docker image from docker hub using below script

        $docker pull anuragkumarak1995/wordnet:latest

1. Then `run` the image container, application will be hosted on port 5000.

        $docker container run --rm --name wrdnt -p "5000:5000" -d anuragkumarak1995/wordnet:latest

1. To `test` that container is working look into docker container logs.
## Apis to use

        /api/net/<word>

fill `root` with a word that is present in `network_sample` file, and this link will produce a json list of words at ***1 - depth*** from this word as root in the network.

### output format

```js
{
'words':['word1','word2','word3','word4',...]
}

```

![BUILT WITH LOVE](http://forthebadge.com/images/badges/built-with-love.svg)

by [@Anurag](https://github.com/anuragkumarak95)
