# Setting up a dev environnement to build the sentiment analysis model

## Usage : 

```bash
vagrant up
vagrant ssh
cd /vagrant 
```

Then edit the file twitter.env with your own credentials. And run :

```bash
sudo sh start.sh
```
This last command runs Jupyter within a docker container.
You can access it through your favorite browser at http://localhost:8888/notebooks
