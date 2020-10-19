# Template-rgb-plot

## Description
This is an rgb image-based template that can be used to test plot-level algorithms.

## Assumptions
It is assumed that:

* An image folder is located in the root of this directory that will provide images for the calculate()
function to process. Sample plot images can be found [here](https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip)
To retrieve these files, first create a folder titled images using the command `mkdir images`. Next, navigate to that
folder using the command `cd images`. Now you are in the folder where your images will be located. To bring the image
files into this folder, one option is to download them from the link and then move them manually into the folder. Another
is to use the command `wget https://de.cyverse.org/dl/d/4108BB75-AAA3-48E1-BBD4-E10B06CADF54/sample_plot_images.zip`, which
will download a zip file containing the image files. To uncompress the zip file, use the command `unzip sample_plot_images.zip`.
Now you should have six .tif images located in the images directory. If you would like to remove the .zip file afterwards,
use the command `rm sample_plot_images.zip`

* You are generating a Docker image containing your algorithm and that you have Docker installed on your
computer

* You are familiar with Github template repositories, or know how to use git

## Sample Transformers
* [transformer-rgb-indices](https://github.com/AgPipeline/transformer-rgb-indices)

## Initial Setup
The following steps can be taken to clone this repo and generate a complete README.md
for your algorithm

1. [Setup](#setup): Click the `Use this template` button in GitHub to make a copy of this repository (or run `git clone`)
2. [Definitions](#definitions): Fill in and modify the metadata in the cookiecutter.json file
3. [Generate full README.md](#readme): Run the command `npm install @appnest/readme -D` to install a module that can generate the final README
   and follow the steps below
4. [Update blueprint.md](#update_blueprint): OPTIONAL

### Setup your repo <a name="setup"/>
The first thing to do is to create a copy of this repository has a meaningful name and that you are able to modify.
In GitHub this is easy, browse to this [repository](https://github.com/AgPipeline/template-rgb-plot) and you can do one of
the following:

1. click the `Use this template` button.
You will be led through the steps necessary to create a clone in a location of your choosing.

2. If you are not on GitHub, you will need to setup your `git` environment and clone the repository. You can use the command
`git clone https://github.com/AgPipeline/template-rgb-plot.git`, which will create a repository called template-rgb-plot
in the current directory. Navigate to and open this folder

### Fill in your definitions <a name="definitions" />
To fill in the needed definitions, first open the `cookiecutter.json` file in your favorite text editor.

The fields in the cookiecutter.json file will be used to populate and personalize your readme once it is generated.

If you are modifying existing code, you should consider updating the version number definition: `version`.
It's assumed that [Semantic Version numbers](https://semver.org/) will be used, but any methodology can be used.

Fill in the algorithm definitions with the creator(s) of the algorithm: `author(s)`, `author_email(s)`, `algorithm_name`, and `algorithm_description`.
It's best if only one algorithm name is used, but call it what you want.
The safest algorithm naming convention to use is to convert any white-space and other special characters to periods (.) 
which assists in changing the name for different systems as needed

Next fill in the citation information that will be used in the generated CSV file: `citation_author`, `citation_title`, and `citation_year`.
Be sure to enter the citation information accurately since some systems may expect exact matches.

The names of the variables are used to determine the number of returned values your algorithm produces: `variable_names`.
Enter each variable name for each returned value, in the order they are returned, separated by a comma.
Be sure to enter them accurately since some systems may expect exact matches.
It is considered a runtime error to have a mismatch between the number of variables names and the number of returned values.

Now open algorithm_rgb.py

A CSV file suitable for ingestion to [BETYdb](https://www.betydb.org/) is generated depending upon the value of the `WRITE_BETYDB_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

A CSV file suitable for ingestion to [TERRA REF Geostreams](https://docs.terraref.org/user-manual/data-products/environmental-conditions) is generated depending upon the value of the `WRITE_GEOSTREAMS_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

Be sure to save your changes.

### Generate full README <a name="readme" />

After you perform this step, a second README.md file should be generated that contains detailed information about how to generate, test, and publish the algorithm. 
Follow the README.md generation instructions from [this readme generator](https://github.com/andreasbm/readme) on Github. The instructions are also below if 
that is preferred. Make sure to perform the necessary [installations](https://github.com/andreasbm/readme#-installation):

first install @appnest/readme if you have not done so already using the command `npm install @appnest/readme`. This will install the necessary components/packages
needed to run the [readme generator](https://github.com/andreasbm/readme) Next run the command 
```npx @appnest/readme generate --output "{{cookiecutter._project_name}}/README.md" --package cookiecutter.json```
in order to generate a complete README.md file. 

This will use the fields contained in cookiecutter.json to populate fields contained in double brackets {{}}. 
For instance the above {{pkg._version}} will look in the cookiecutter.json file for a field called 
_version and then use that as the version number in the created README.md file.
 
After performing the necessary [installations](https://github.com/andreasbm/readme#-installation)
 
The README will be located in the folder titled {{cookiecutter._project_name}}

### (OPTIONAL) Update blueprint.md <a name="update_blueprint" />
If you would like your README.md file to look different than it currently does, you can change the markdown text
in blueprint.md in order to reflect how you would like for it to look. Then you should [Generate full README.md](#readme)
again to update the README
