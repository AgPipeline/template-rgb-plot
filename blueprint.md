# [ {{ pkg._project_name}} ]({{ pkg._url }})
# name
{{pkg._project_name}}

# url
{{pkg._url}}

## Version 
{{pkg._version}}

## Author(s)
{{pkg._author(s)}}

#### Author Email(s)
{{pkg._author_email(s)}}

## Description
{{pkg._algorithm_description}}

### Methods
{{pkg._methods}}

## Assumptions
It is assumed that:

* An image folder is located in the root of this directory that will provide images for the calculate() function to process.
 
* Sample plot images can be found [here](https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip)
To retrieve these files, first create a folder titled images using the command `mkdir images`. Next, navigate to that
folder using the command `cd images`. Now you are in the folder where your images will be located. To bring the image
files into this folder, one option is to download them from the link and then move them manually into the folder. Another
is to use the command `wget https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip`, which
will download a zip file containing the image files. To uncompress the zip file, use the command `unzip sample_plot_images.zip`.
Now you should have six .tif images located in the images directory. If you would like to remove the .zip file afterwards,
use the command `rm sample_plot_images.zip`

* You are generating a Docker image containing your algorithm and you have Docker installed on your
computer

* You are familiar with Github template repositories, or know how to use git

## Sample Transformers
* [transformer-rgb-indices](https://github.com/AgPipeline/transformer-rgb-indices)

## Steps to take
The following steps can be taken to develop your algorithm for inclusion into a processing pipeline.

1. [Algorithm](#algorithm): Replace the code in the `calculate` function with your algorithm
2. [Generate](#generate): Run `generate.py` to create a Dockerfile
3. [Test](#test): Run the `testing.py` script to run your algorithm and validate the results
4. [Docker](#build_docker): Create a Docker image for your algorithm and publish it
5. [Testing Your docker image](#test_docker): OPTIONAL
6. [Testing Image Production](#production): OPTIONAL
7. [Generating Your Local Repository](#generate_repository): OPTIONAL
8. [Finishing Algorithm Development](#finishing): Finish up your development efforts


### Add your algorithm <a name="algorithm" />
Open the `algorithm_rgb.py` file in your favorite editor, if it isn't opened already.

Scroll to the bottom of the file to the function named `calculate`.

Replace the comment starting with `# ALGORITHM` and the line below with your calculation(s).
As needed, change the name of array used in your algorithm to the function's parameter `pxarray`.

Once you have your algorithm in place, replace the comment starting with `# RETURN` and the line below with your return values.
Remember to order your return values to match the declared names in the `VARIABLE_NAMES` definition.

Modify the rest of the file as necessary if there are additional import statements, functions, classes, and other code needed by your algorithm.

Be sure to save your changes.

### Generate the Docker build command file <a name="generate" />
It's time to generate the Dockerfile that's used to build Docker images.

Docker images can be used as part of a workflow

To assist in this effort we've provided a script named `generate.py` to produce a file containing the Docker commands needed.
Running this script will not only produce a Docker command file, named `Dockerfile` but also two other files that can be used to install additional dependencies your algorithm needs.
These two other files are named `requirements.txt` for additional Python modules and `packages.txt` for other dependencies.

To generate these files, just run `generate.py`.

If your algorithm has additional python module dependencies, edit `requirements.txt` and add the names of the modules.
The listed modules will then be installed as part of the Docker build process.

If there are other dependencies needed by your algorithm, add them to the `packages.txt` file.
The packages listed will be installed using `apt-get` as part of the Docker build process.

### Test your algorithm <a name="test"/>
A testing script named `testing.py` is provided for testing your algorithm.
It checks whether the configuration is correct for testing the files by making sure that the arguments in algorithm_rgb as well as the image files are in the correct format

The testing script requires `numpy` and `gdal` to be installed on the testing system.

If your files reside in `/user/myself/test_images` the command to test could be the following:
```./testing.py /user/myself/test_images```

What isn't provided in the template repository are the plot-level RGB images to test against.
It's expected that you will either provide the images or use a standard set that can be downloaded from [Google Drive](https://drive.google.com/file/d/1xWRU0YgK3Y9aUy5TdRxj14gmjLlozGxo/view?usp=sharing).

The testing script expects to have either a list of source plot image files, or a folder name, or both specified on the command line.

### Create the Docker image <a name="build_docker" />
Now that you have generated your `Dockerfile` as described [above](#generate) and specified any Python modules and other packages needed by your algorithm, you are ready to create a Docker image of your algorithm.

A sample Docker build command could be: ```docker build -t my_algorithm:latest ./```
Please refer to the Docker documentation for additional information on building a docker image.

Once the image is built, you can run it locally or push it to an image repository, such as [DockerHub](https://hub.docker.com/).
Please note that there may be naming requirements for pushing images to a repository.

#### (OPTIONAL) Using Docker to run testing.py <a name="test_docker">

In order to test your docker image, you can use the command:

```docker run --rm -it -v `pwd`:/mnt --entrypoint /mnt/testing.py my_algorithm:latest /mnt/images```

Breaking apart this command line, we have the following pieces:
- `docker run` tells Docker to run an instance of the image (specified later in the command) (Refer to [docker run](https://docs.docker.com/engine/reference/run/) documentation)
- `--rm` tells Docker to remove the container (an image instance) when it's completed
- `it` allows you to have a stdin stream and terminal driver added to the docker container allowing an interactive session
- `-v "pwd":/mnt` bind mounts a volume to the docker container so that the current working directory (given by pwd) will be copied into the volume
- `--entrypoint /mnt/testing.py` defines the Docker container that will be run, with testing.py mounted to that container 
- `my_algorithm:latest` is the image to run (the running image is known as a *container*)
- `/mnt/images` mounts the sample plot images to the running docker container

Output should be in the format of image name and calculated value for that image on a single line for each of the images in the images folder.
Example output from the images in the [Google Drive](https://drive.google.com/file/d/1xWRU0YgK3Y9aUy5TdRxj14gmjLlozGxo/view?usp=sharing) 
is contained below for plot images folder, which is titled sample_plot_images: 

```Filename,size of image channels -  (pixels),
/mnt/sample_plot_images/rgb_17_7_W.tif,7000
/mnt/sample_plot_images/rgb_40_11_W.tif,7000
/mnt/sample_plot_images/rgb_6_1_E.tif,7000
/mnt/sample_plot_images/rgb_1_2_E.tif,7000
/mnt/sample_plot_images/rgb_33_8_W.tif,7000
/mnt/sample_plot_images/rgb_5_11_W.tif,7000
```

#### (OPTIONAL) Production Testing of Image <a name="production" />

Using the same image setup as used when testing your algorithm, a sample command line to run the image could be:

docker run --rm -v "${PWD}:/mnt,type=bind" default:latest --working_space "/mnt" --metadata "mnt/experiment.yml" "/mnt/sample_plot_images"


Breaking apart this command line, we have the following pieces:
- `docker run` tells Docker to run an instance of the image (specified later in the command) (Refer to [docker run](https://docs.docker.com/engine/reference/run/) documentation)
- `--rm` tells Docker to remove the container (an image instance) when it's completed
- `--mount "src=/user/myself,target=/mnt,type=bind"` specifies the */user/myself* path is to be made available as */mnt* in the container
- `my_algorithm:latest` is the image to run (the running image is known as a *container*)
- `--working_space "/mnt"` lets the software in the container know where its working disk space is located; files are created here
- `--metadata "mnt/experiment.yml"` specifies that the metadata file experiment.yml will be made available to the container
- `"/mnt/images"` specifies where the plot-level image files are located

The `--mount` command line parameter is important since it allows the running container to access the local file system.
The container can then load the images from the file system directly, without having to perform any copies.
The parameters after the Docker image name are all relative to the target folder specified with this command line parameter.

Once the image files have been processed, the resulting CSV file(s) will be located in the folder at `/user/myself` (in this example).

The result.json file should tell you what errors were found in the checks from testing.py (make sure to check the output in the CSV file(s) 
even if the result.json file does not find errors)

### (OPTIONAL) Generating your local repository <a name=generate_repository />
In order to generate your own local repository from this one, [Cookiecutter](https://github.com/cookiecutter/cookiecutter/blob/master/README.md)
will be used. Cookiecutter will use the cookiecutter.json file in order to create a personalized repository out of this template

Change your directory to be one directory above "template-rgb-plot" using `cd..`. Run the following command to generate
your repository

```cookiecutter template-rgb-plot```

This will create a folder with the name that you chose for {{cookiecutter._project_name}} in the directory you are now in/
the parent directory of template-rgb-plot.

Update the blueprint.md file if there are extra changes you need to make. Then run
```npx @appnest/readme generate --output "{{cookiecutter._project_name}}/README.md" --package cookiecutter.json```,
filling out the sections with information on your algorithm; others will want to know so they can use it!

### Finishing Algorithm Development <a name="finishing" />
Now that you're created your algorithm, there's a few more things to take care of:

1. Make sure you've checked in your changes into source control; you don't want to lose all that hard work! To do this, first
make sure that your git remote is set to the right place. To do this, use `git remote -v`. If it is not, use the command
`git remote set-url origin <repository url>` Next, using `git add .` will add all files and folders in the current directory. 
Then do `git commit -m <message>` in order to add a message describing the changes you made. Use `git push` in order
 to push those changes to GitHub.

2. Make sure to generate your repository again if needed using ```cookiecutter template-rgb-plot``` from the parent directory
of template-rgb-plot!

3. Submit any requests to our ticketing system on GitHub:  https://github.com/AgPipeline/computing-pipeline/issues/new/choose