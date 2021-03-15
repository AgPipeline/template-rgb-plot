# Template-rgb-plot

## Description
This is an rgb image-based template that can be used to test plot-level algorithms for the Python programming language.

## Assumptions <a name="assumptions" />
It is assumed that:

* An image folder is located in the root of this directory that will provide images for the calculate()
function to process. Sample plot images can be [downloaded from CyVerse](https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip).
To retrieve these files manually, first create a folder titled images using the command `mkdir images`.
Next, navigate to that folder using the command `cd images`.
Now you are in the folder where your images will be located.
To bring the image files into this folder, one option is to download them from the link and then move them manually into the folder.
Another is to use the command `wget https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip`, which will download a zip file containing the image files.
To uncompress the zip file, use the command `unzip sample_plot_images.zip`.
Now you should have six .tif images located in the images directory.
If you would like to remove the .zip file afterwards, use the command `rm sample_plot_images.zip`

* You are generating a Docker image containing your algorithm and that you have Docker installed on your
computer

* You are familiar with Github template repositories, or know how to use git

## Sample Transformers
* [transformer-rgb-indices](https://github.com/AgPipeline/transformer-rgb-indices)

## Initial Setup
The following steps can be taken to clone this repo and generate a complete README.md
for your algorithm

1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/first_steps.html#learn-the-basics-of-cookiecutter-by-creating-a-cookiecutter) if you haven't already. The following command can be used ```pip install cookiecutter```
2. [Setup](#setup): Click the `Use this template` button in GitHub to make a clone of the source repository
3. [Definitions](#definitions): Fill in and modify the metadata in the cookiecutter.json file
4. [Run cookiecutter](#run_cc): Run cookiecutter to generate your code
5. [Create transformer](#transformer): Edit the created files to implement your algorithm
6. [Update blueprint.md](#update_blueprint): OPTIONAL: Change the contents of the README.md file
7. [Generate full README.md](#readme): OPTIONAL: Generate a new README.md file
8. [Testing](#testing): Testing your algorithm
9. Save your new transformer onto GitHub or another source control system

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
To fill in the needed definitions, first open the `cookiecutter.json` file in your favorite text editor.

The fields in the cookiecutter.json file will be used to populate and personalize your README once it is generated.

The `_project_name` variable will be used as the folder name when running cookiecutter to generate your code.

If you are modifying existing code, you should consider updating the version number definition: `version`.
It's assumed that [Semantic Version numbers](https://semver.org/) will be used, but any methodology can be used.

Editing the following definitions is optional as they are used to fill in the `blueprint.md` file.

Edit the algorithm definitions with the creator(s) of the algorithm: `author(s)`, `author_email(s)`, `algorithm_name`, and `algorithm_description`.
It's best if only one algorithm name is used, but call it what you want.
The safest algorithm naming convention to use is to convert any white-space and other special characters to periods (.) which makes it easier to change the name as needed

Next fill in the citation information that will be used in the generated README file: `citation_author`, `citation_title`, and `citation_year`.
Be sure to enter the citation information accurately since some systems may expect exact matches.

The names of the variables are used to determine the number of returned values your algorithm produces: `variable_names`.
Enter each variable name for each returned value, in the order they are returned, separated by a comma.
Be sure to enter them accurately since some systems may expect exact matches.
It is considered a runtime error to have a mismatch between the count of variables names and the count of returned values.

### Run cookiecutter <a name="run_cc"/>
Change to a folder where you'd like the transformer code to be generated.
The code will be placed into a sub-folder off the current folder

From the command line, run cookiecutter to generate the transformer code by specifying the path to the folder containing the template you just created.
```bash
# Change the path to the folder containing cookiecutter.json 
cookiecutter /path/to/folder
```

This will create a folder named after the project name and populate it with files.

### Configure your transformer <a name="transformer">

Now open `algorithm_rgb.py` and fill in the variables at the start of the file, and add your algorithm to calculate() function.
Be sure to return the values in the same order as specified in the VARIABLE_NAMES variable.
The values entered here should match the values used in the `cookiecutter.json` file.

A CSV file suitable for ingestion to [BETYdb](https://www.betydb.org/) is generated depending upon the value of the `WRITE_BETYDB_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

A CSV file suitable for ingestion to [TERRA REF Geostreams](https://docs.terraref.org/user-manual/data-products/environmental-conditions) is generated depending upon the value of the `WRITE_GEOSTREAMS_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

Be sure to save your changes.

Generate Dockerfile by running the `python3 generate.py`.
This will create `Dockerfile` in the current folder.
You may need to update Dockerfile 

### (OPTIONAL) Update blueprint.md <a name="update_blueprint" />
If you would like your README.md file to look different than it currently does, you can change the markdown text in blueprint.md in order to reflect how you would like for it to look.
Be sure to also change the contents of the file to contain the text you want.
You will need to follow the instructions in [(OPTIONAL) Generate full README.md](#readme) to update the README.

### (OPTIONAL) Generate full README <a name="readme" />

These steps may overwrite an existing README.md file; be sure to make a backup copy of the existing file before generating the README.md file.

After you perform this step, a README.md file will be generated that contains detailed information about how to generate, test, and publish the algorithm.
Follow the README.md generation instructions from the [readme generator](https://github.com/andreasbm/readme) on Github.
Instructions also follow, if that is preferred.

If you are not following the official instructions, make sure to perform the necessary installations:

1. first install @appnest/readme if you have not done so already.
The command `npm install @appnest/readme` will perform the install.
This will install the necessary components/packages needed to run the [readme generator](https://github.com/andreasbm/readme)
2. change to the directory in which you want the README.md file to be generated
3. next run the command ```npx @appnest/readme generate --output "./README.md" --package /path/to/cookiecutter.json --input /path/to/blueprint.md``` in order to generate a complete README.md file.
Be sure to replace `/path/to/` with the correct path to your cookiecutter.json and blueprint.md files

This will use the fields contained in cookiecutter.json to populate fields contained in double brackets {{}}. 
For example, upon encountering {{pkg._version}}, the readme generator will look in the cookiecutter.json file for a field called _version and then use that as the version number in the created README.md file.
 
The README will be located in the folder named after `_project_name` in the `cookiecutter.json` file.

### Testing your algorithm <a name="testing" />

Once you  have developed your algorithm, you can test it out.
This section assumes that you have [test images](#assumptions) available in a subfolder named "images".

#### Without Docker

Outside of Docker, you can run the "testing.py" script to test the algorithm.
This requires that a minimal set of necessary Python libraries are installed before a test can be successfuly run.

To use test this way, run the following command:
```bash
# The second parameter is the path to the test image file
./testing.py images/rgb_17_1_W.tif
```

Upon success, the results of the algorithm are displayed.
You can check the generated algorithm value for correctness.

#### With Docker

After building the Docker image, you can test that image and the algorithm.

The following command runs the Docker image and generates CSV file(s) in the `images` folder.
```bash
# The Docker image is named 'my_image' in this example; use your Docker image name instead
docker run --rm -v ${PWD}/images:/mnt my_image --working_space /mnt /mnt/rgb_17_7_W.tif
```

Refer to the [Docker run](https://docs.docker.com/engine/reference/commandline/run/) documentation for information on this command.

One or more CSV files will be generated in the "images" folder upon success.
Check the contents of the file(s) to determine if the algorithm is working and producing correct results.
