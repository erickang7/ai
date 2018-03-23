# AI Playground

**AI Playground** provides an easy way to setup a tensorflow, scikit-learn and jupyter notebook playground as a docker container environment to help you easily start learning ML and AI basics without spending a few hours to setup the environment.

I assume that you know the basics of Docker such as docker build and run. Thanks to Google, a good base image is available at [Docker Hub: Tensorflow repository](https://hub.docker.com/r/tensorflow/tensorflow). You can simply start from a Google's tensorflow image as the base docker image and add layers on top of it as you need. For example, I included scikit-learn version 2.0-dev package instead of the version 0.19x stable since the 0.20-dev version has many bug fixes and new features that we need to follow sample codes from a very useful reference, [Hands-on Machine Learning with Scikit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_2?ie=UTF8&qid=1521836305&sr=8-2&keywords=hands-on+machine+learning+with+scikit-learn+%26+tensorflow) If you haven't read this book, I recommend getting a copy.

## Prepare AI Playground docker image
First, login to your laptop or PC. I assume your laptop is either Linux desktop or mac. You can use Windows as well but I haven't tested it yet.
If you haven't installed Docker on your PC, install Docker first by following instructions at [Docker Installation](https://docs.docker.com/install/)

Once you have Docker running on your laptop, run following commands to prepare aiplayground docker image. I could have shared the docker image in a public repository but I decided rather not redistributing stuff without fully validating licenses. You can easily build your docker image by following instructions below anyways.

```bash
cd
mkdir -p projects
cd projects
git clone https://github.com/erickang7/ai
cd ai/tensorflow/docker
./build.sh
docker images | grep aiplayground
```
aiplayground/tensorflow:practice image should be created.

## Run aiplayground/tensorflow container
Let's spin up a new container and call it as 'tensorflow'. Simply run the following command.

```bash
docker run \
--name tensorflow \
-v $HOME/projects/ai/practice:/notebooks/workspace \
--mount source=tfvol,target=/notebooks/models \
-p 8888:8888 \
-p 6006:6006 \
-d aiplayground/tensorflow:practice
```

Then run the following command to get the entry URL to Jupyter notebook running in the container.

```bash
docker logs tensorflow | grep token
```

You should see a result similar to the sample output below. In the sample output, ```http://localhost:8888/?token=83a3719cec38fb6849d708fb757d5adec1f72b159f73b172``` is the URL for the Jupyter Notebook running in the docker container we just spun up.

```bash
[erickang@bluewood tensorflow]$ ./init.sh
0a6089b5b96d24de5bb8faa2027b0e2b5d23c61f2b784469db0206e1cacc1185
[I 20:50:51.681 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
[W 20:50:51.695 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 20:50:51.701 NotebookApp] Serving notebooks from local directory: /notebooks
[I 20:50:51.701 NotebookApp] 0 active kernels
[I 20:50:51.701 NotebookApp] The Jupyter Notebook is running at:
[I 20:50:51.701 NotebookApp] http://[all ip addresses on your system]:8888/?token=83a3719cec38fb6849d708fb757d5adec1f72b159f73b172
[I 20:50:51.701 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 20:50:51.702 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=83a3719cec38fb6849d708fb757d5adec1f72b159f73b172
```

Also note that Jupyter notebook is exposed at the port 8888.

## Validate environment
Open Jupyter notebook in your web browser by ```ctl+click``` the URL.
In the root file browser, open ```1_hello_tensorflow.ipynb``` file. Then run the hellow world notebook to validate your environment.

## Venture into samples and real-world practices
For tensorflow basics, go to [Getting Started for ML Beginner](https://www.tensorflow.org/get_started/get_started_for_beginners) on Tensorflow tutorial site. You can use ```workspace/tensorflow/tensorflow_iris.ipynb``` notebook while following the tutorial.

For ML in general, Again, I recommend [Hands-on Machine Learning with Scikit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_2?ie=UTF8&qid=1521836305&sr=8-2&keywords=hands-on+machine+learning+with+scikit-learn+%26+tensorflow). Read and practice it with sample codes in the book.

You can also play with data you already have such as telemtry data collected in mssql or auzre sqldb. To export all tables in a database to CSV, you can use ```dbexport``` program written in GO. Check out [dbexport git repository](https://github.com/erickang7/dbexport) for the details.

## Extra Tip
If you want to play with tensorflow samples which is written in python, you can do it by connecting to ```tensorflow``` container's bash terminal and using vim editor. To enter the container and test run the iris categorization DNN sample, run the following command.

```bash
docker exec -ti tensorflow bash
cp /gitclone_models.sh /notebooks
cd /notebooks
./gitclone_models.sh
cd /notebooks/models/samples/core/get_started
python premade_estimator.py
```

Enjoy!
