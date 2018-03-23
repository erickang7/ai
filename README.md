# AI Playground

**AI Playground** provides an easy way to setup a tensorflow, skit-learn and jupyter notebook playground as a docker container environment to help you easily start learning ML and AI basics without spending a few hours of your time to setup the environment.

I assume that you know the basics of Docker such as docker build and run. Thanks to Google, a good base image is available at [Docker Hub: Tensorflow repository](https://hub.docker.com/r/tensorflow/tensorflow). We can simply start from a Google's tensorflow image as the base docker image and add layers on top of it as we need. For example, I included skit-learn version 2.0-dev package instead of the version 0.19x stable since the version 0.20-dev has many bug fixes and new features that we need to follow sample codes from a very useful reference, [Hands-on Machine Learning with Skit-Learn and Tensorflow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291/ref=sr_1_2?ie=UTF8&qid=1521836305&sr=8-2&keywords=hands-on+machine+learning+with+scikit-learn+%26+tensorflow) If you haven't read this book, I recommend getting a copy.

## Prepare AI Playground docker image
First, login to your laptop or PC. I assume either your are using Linux desktop or mac. Use can use Windows as well but I didn't test it.
If you haven't installed docker on your PC, install docker by following instructions at [Docker Installation](https://docs.docker.com/install/)
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
Let's spind up a new container 'tensorflow'. Run the following command.

```bash
docker run \
--name tensorflow \
-v $HOME/projects/ai/practice:/notebooks/workspace \
--mount source=tfvol,target=/notebooks/models \
-p 8888:8888 \
-p 6006:6006 \
-d aiplayground/tensorflow:practice
```

Then run 
```bash
docker logs tensorflow | grep token
```

This command will spin up a new container called 'tensorflow'. Note that your local folder ```$HOME/projects/ai/practice``` is mounted at ```/notebooks/workspace``` folder in the container. Use this folder to create, write and save notebook files to persist them to your local folder. If you create aor copy files into the local folder, it will automatically be available in the container as well. Also I mounted a docker volume ```tfvol``` to ```/notebooks/models```. The use of this folder is optional. I have included ```/gitclone_models.sh``` in the container to make it easy to download sample tensorflow models from tensorflow tutorial git repository.  

You should see the following result. In the following sample result, ```http://localhost:8888/?token=83a3719cec38fb6849d708fb757d5adec1f72b159f73b172``` is the URL to connect Jupyter Notebook running in the docker container we just spun up.

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



