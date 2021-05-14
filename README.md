# Template-rgb-plot

### Launch with myBinder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AgPipeline/template-rgb-plot/earthcube)

## Description
This is an rgb image-based template that can be used to test plot-level algorithms in Python and Docker.

## Assumptions <a name="assumptions" />
It is assumed that:

* An image folder is located in the root of this directory that will provide images for the calculate()
function to process. Sample plot images can be [downloaded from CyVerse](https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip).
To retrieve image files manually, first create a folder titled with the name you would like using the command `mkdir <folder name>`.
Next, navigate to that folder using the command `cd <folder name>`.
Now you are in the folder where your images will be located.
To bring the image files into this folder, one option is to download them from the link and then move them manually into the folder.
Another is to use the command `wget https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip`, which will download a zip file containing the image files.
To uncompress the zip file, use the command `unzip sample_plot_images.zip`.
Now you should have six .tif images located in the images directory.
If you would like to remove the .zip file afterwards, use the command `rm sample_plot_images.zip`

* You are generating a Docker image containing your algorithm and that you have [Docker](https://www.docker.com) installed on your
computer

* You are familiar with Github template repositories, or know how to use git

## Sample Transformer
* [transformer-rgb-indices](https://github.com/AgPipeline/transformer-rgb-indices)

## Initial Setup
The following steps can be taken to develop your algorithm for inclusion into a processing pipeline.

1. [Setup](#setup): Click the `Use this template` button in GitHub to make a clone of the source repository
2. [Definitions](#definitions): Fill in and modify the fields in the algorithm_rgb.py file
3. [Design Algorithm](#algorithm): Replace the code in the `calculate` function in algorithm_rgb.py with your algorithm
4. [Testing Your Algorithm](#testing): Run the `testing.py` script to run your algorithm on the image files you would like to use and validate the results
5. [Update README.md](#update_readme): Change the contents of the README.md file to better describe your algorithm
6. [Generate Dockerfile](#generate_dockerfile): Use the provided `generate.py` script in order to generate a Dockerfile 
7. [Build A Docker Image](#build_docker): Create a Docker image for your algorithm
8. [Running Your Docker Image](#run_docker): Run the created Docker image
9. [Finishing Algorithm Development](#finishing): Finish up your development efforts


### Setup <a name="setup"/>
The first thing to do is to create a copy of this repository that has a meaningful name and that you are able to modify.
In GitHub this is easy, browse to the [template-rgb-plot repository](https://github.com/AgPipeline/template-rgb-plot) and click the `Use this template` button.
You will be led through the steps necessary to create a clone in a location of your choosing.

If you are not on GitHub, you will need to clone the repository using the command line.
You can use the following command which will create a sub-folder named template-rgb-plot in the current directory:
```bash
git clone --depth 1 -b main https://github.com/AgPipeline/template-rgb-plot
```


### Fill in your definitions <a name="definitions" />
To fill in the needed definitions, first open the `algorithm_rgb.py` file in your favorite text editor.

If you are modifying existing code, you should consider updating the version number definition: `VERSION`.
It's assumed that [Semantic Version numbers](https://semver.org/) will be used, but any methodology can be used.

Edit the initial algorithm definitions with the creator(s) of the algorithm: `ALGORITHM_AUTHOR`, `ALGORITHM_AUTHOR_EMAIL`, and `ALGORITHM_CONTRIBUTORS` 

Next name and describe the algorithm by updating 
`ALGORITHM_NAME` and `ALGORITHM_DESCRIPTION`.
It's best if only one algorithm name is used, but ultimately it is up to you.
The safest algorithm naming convention to use is to convert any white-space and other special characters to periods (.) which makes it easier to change the name as needed

Next fill in the citation information: `CITATION_AUTHOR`, `CITATION_TITLE`, and `CITATION_YEAR`.
Be sure to enter the citation information accurately since some systems may expect exact matches.

Now consider the variable names, which are used to determine the number of returned values your algorithm produces: `VARIABLE_NAMES`.
Enter each variable name for each returned value, in the order they are returned, separated by a comma.
Be sure to enter them accurately since some systems may expect exact matches.
It is considered a runtime error to have a mismatch between the count of variables names and the count of returned values.

A CSV file suitable for ingestion to [BETYdb](https://www.betydb.org/) is generated depending upon the value of the `WRITE_BETYDB_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

A CSV file suitable for ingestion to [TERRA REF Geostreams](https://docs.terraref.org/user-manual/data-products/environmental-conditions) is generated depending upon the value of the `WRITE_GEOSTREAMS_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

Be sure to save your changes.


### Design Your Algorithm <a name="algorithm">

In `algorithm_rgb.py`, scroll down to the calculate() function and replace it with your algorithm.
Be sure to return the values in the same order as specified in the VARIABLE_NAMES variable so that they will be matched correctly.


### Test your algorithm <a name="testing"/>
A testing script named `testing.py` is provided for testing your algorithm.
It checks whether the configuration is correct for testing the files by making sure that the arguments in algorithm_rgb as well as the image files are in the correct format

The testing script requires `numpy` and `gdal` to be installed on the testing system.

If your files reside in `/user/myself/test_images` the command to test could be the following:
```./testing.py /user/myself/test_images```

What isn't provided in the template repository are the plot-level RGB images to test against.
It's expected that you will either provide the images or use a standard set that can be downloaded.
The following commands can be used to retrieve and extract the test images:
```bash
mkdir test_images
curl -X GET https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip -o test_images/sample_plot_images.zip
unzip test_images/sample_plot_images.zip -d test_images/
```

The testing script expects to have either a list of source plot image files, or a folder name, or both specified on the command line.


### Update the README.md <a name="update_readme"/>
Replace this `README.md` file with one that describes and documents your algorithm. The `README.md` should give users an overview of your project and include enough information so that users can understand and use the project. Guidlines for formatting a `README.md` file can be found at [this link](https://guides.github.com/features/wikis/)


### Generate a Dockerfile <a name="generate_dockerfile">
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


### Build your docker image <a name="build_docker" />
Now that you have generated your `Dockerfile` as described [above](#generate) and specified any Python modules and other packages needed by your algorithm, you are ready to create a Docker image of your algorithm.

A sample Docker build command could be: ```docker build -t <algorithm name>:<algorithm version> ./```
Please refer to the Docker documentation for additional information on building a docker image.

Once the image is built, you can run it locally or push it to an image repository, such as [DockerHub](https://hub.docker.com/).
Please note that there may be naming requirements for pushing images to a repository.


### Run Your Docker Image <a name="run_docker" />
In order to test your docker image for production, you can use a command similar to:

```bash
docker run --rm -v "${PWD}:/mnt,type=bind" <algorithm name>:<algorithm version<> --working_space "/mnt" --metadata "mnt/<metadata file>.yml" "/mnt/<test images>"
```

Breaking apart this command line, we have the following pieces:
- `docker run` tells Docker to run an instance of the image (specified later in the command) (Refer to [docker run](https://docs.docker.com/engine/reference/run/) documentation)
- `--rm` tells Docker to remove the container (an image instance) when it's completed
- `-v "${PWD}":/mnt,type=bind` bind mounts a volume to the docker container so that the current working directory (given by the value of ${PWD}) will be copied into the volume
- `<algorithm name>:<algorithm version>` is the image to run (the running image is known as a *container*)
- `--working_space "/mnt"` lets the software in the container know where its working disk space is located; files are created here
- `--metadata "mnt/<metadata file>.yml"` specifies that the metadata file experiment.yml will be made available to the container
- `"/mnt/<test images>"` mounts the sample plot images to the running docker container

#### Additional notes on running your docker image
- The `--mount` command line parameter is important since it allows the running container to access the local file system.
The container can then load the images from the file system directly, without having to perform any copies.
The parameters after the Docker image name are all relative to the target folder specified with this command line parameter.

- Once the image files have been processed, the resulting CSV file(s) will be located in the folder at the working directory (in this example).

- The result.json file should tell you what errors were found in the checks from testing.py (make sure to check the output in the CSV file(s) even if the result.json file does not find errors)

- If you want to run the testing.py script inside of the running Docker container, you can use a command similar to:

```bash
docker run --rm -it -v `pwd`:/mnt --entrypoint /mnt/testing.py <algorithm name>:<algorithm version> /mnt/<test images>

- `it` allows you to have a stdin stream and terminal driver added to the docker container allowing an interactive session
```
Output when using testing.py should be in the format of image name and calculated value for that image on a single line for each of the images in the images folder.
Example output from the images in the [sample image set]() is shown below for the plot sample images folder, which is titled test_images: 

```Filename,size of image channels -  (pixels),
/mnt/test_images/rgb_17_7_W.tif,7000
/mnt/test_images/rgb_40_11_W.tif,7000
/mnt/test_images/rgb_6_1_E.tif,7000
/mnt/test_images/rgb_1_2_E.tif,7000
/mnt/test_images/rgb_33_8_W.tif,7000
/mnt/test_images/rgb_5_11_W.tif,7000
```


### Finishing Algorithm Development <a name="finishing" />
Now that you're created your algorithm, there's a few more things to take care of:

1. Make sure you've checked in your changes into source control; you don't want to lose all that hard work! To do this, first
make sure that your git remote is set to the right place. To do this, use `git remote -v`. If it is not, use the command
`git remote set-url origin <repository url>` Next, using `git add .` will add all files and folders in the current directory. 
Then do `git commit -m <message>` in order to add a message describing the changes you made. Use `git push` in order
 to push those changes to GitHub.

2. Submit any requests to our ticketing system on GitHub:  https://github.com/AgPipeline/computing-pipeline/issues/new/choose