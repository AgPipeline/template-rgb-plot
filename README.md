# Template-rgb-plot

## Description
This is an rgb image-based template that can be used to test plot-level algorithms.

## Assumptions
It is assumed that:

* An image folder is located in the root of this directory that will provide images for the calculate()
function to process. Sample plot images can be found [here](https://drive.google.com/file/d/1xWRU0YgK3Y9aUy5TdRxj14gmjLlozGxo/view)

* You are generating a Docker image containing your algorithm and that you have Docker installed on your
computer

* You are familiar with Github template repositories, or know how to use git

## Sample Transformers
* [transformer-rgb-indices](https://github.com/AgPipeline/transformer-rgb-indices)

## Initial Setup
The following steps can be taken to clone this repo and generate a complete README.md
for your algorithm

1. [Setup](#setup): Click the `Use this template` button in GitHub to make a copy of this repository (or run `git clone`)
2. [Definitions](#definitions): Fill in and modify the metadata in the codemeta.json file
3. [Generate full README.md](#readme): Run the command `npm install @appnest/readme -D` to install a module that can generate the final README
   and follow the steps below

### Setup your repo <a name="setup"/>
The first thing to do is to create a copy of this repository has a meaningful name and that you are able to modify.
In GitHub this is easy, browse to this [repository](https://github.com/AgPipeline/template-rgb-plot) and click the `Use this template` button.
You will be led through the steps necessary to create a clone in a location of your choosing.

If you are not on GitHub, you will need to setup your `git` environment and clone the repository.

### Fill in your definitions <a name="definitions" />
To fill in the needed definitions, first open the `codemeta.json` file in your favorite editor.

If you are modifying your existing code, you should consider updating the version number definition: `version`.
It's assumed that [Semantic Version numbers](https://semver.org/) will be used, but any methodology can be used.

Fill in the algorithm definitions with the creator(s) of the algorithm: `author(s)`, `author_email(s)`, `algorithm_name`, and `algorithm_description`.
It's best if only one algorithm name is used, but call it what you want.
The safest algorithm naming convention to use is to convert any white-space or other characters to periods (.) which allows different systems to more-easily change the name, if needed.

Next fill in the citation information that will be used in the generated CSV file: `citation_author`, `citation_title`, and `citation_year`.
Be sure to enter the citation information accurately since some systems may expect exact matches.

The names of the variables are used to determine the number of returned values your algorithm produces: `variable_names`.
Enter each variable name for each returned value, in the order they are returned, separated by a comma.
Be sure to enter them accurately since some systems may expect exact matches.
It is considered an error to have a mismatch between the number of variables names and the number of returned values.

Now open algorithm_rgb.py

A CSV file suitable for ingestion to [BETYdb](https://www.betydb.org/) is generated depending upon the value of the `WRITE_BETYDB_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

A CSV file suitable for ingestion to [TERRA REF Geostreams](https://docs.terraref.org/user-manual/data-products/environmental-conditions) is generated depending upon the value of the `WRITE_GEOSTREAMS_CSV` variable.
Setting this value to `False` will suppress the generation of this file by default.

Be sure to save your changes.


### Generate full README <a name="readme" />

After you perform this step, a second README.md file should be generated that contains detailed information about how to generate, test, and publish the algorithm. 
Following the README.md generation instructions from [this GitHub repo](https://github.com/andreasbm/readme#usage), first install @appnest/readme if you have not done
so already using the command `npm install @appnest/readme`. Next run the command ```npx @appnest/readme generate --package codemeta.json``` in order to generate a 
complete README.md file