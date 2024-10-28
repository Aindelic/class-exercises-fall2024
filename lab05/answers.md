# Lab 5: Package Management Tutorial

Please complete the hands-on activities associated with this lab outlined in the <a href="https://csci338.github.io/fall2024/assignments/lab05" target="_blank">Lab 5 Instructions</a> (on the course website). When you're done, answer the following questions. Feel free to use Google / ChatGPT to help you think about these questions (but keep in mind that you'll need to know them for the midterm exam).

## Part 1. Operating System Package Managers

Answer the questions for either Homebrew or apt (depending on whether you're using Linux / WSL or Windows)

1. What is Homebrew / apt, and why is it useful?
   It is a useful tool that can download update and remove packages, you can search for packages online and download apps and programs and much more.
2. What does the `update` command do (either `brew update` or `apt-get update`)?cur
   It updates all of the package information on the system.
3. Where are the packages that are managed by Homebrew / apt stored on your local computer?
   It should be in /var/cache/apt/archives

## Part 2.

1. What is a python virtual environment?
   it is an isolated enviroment where you can creat custom library installations so thet the global python system does not have conflicts.
2. What is Poetry, and how is it different from other Python package managers like pip?
   Poetry has some files that better organize the packages, like pyproject.toml and poetry.lock which make reproduciable enviroments.
3. What happened when you issued the `poetry new poetry-demo` command?
   It created a folder with the demo, the package manager, a place for tests, and a readme for documentation.
4. How do you run a python file using the poetry virtual environment?
   poetry run python script.py
5. What is the purpose of the `poetry.lock` file?
   For repeaatable enviroments and multiple instances

## Part 3.

1. What are some of the things that `package.json` is used for?
   Basic info like name and version, specify dependencies, make automations scripts for testing or building, manage cofig for the package managers.
2. Why wouldn't you want to check in the `node_modules` directory into GitHub?
   Its the location of all of the installed packages, this is a large amout of redundant data that could be downloaded locally and quickly instead with package.json or similar. otherwise pulls and pushes would be long and have redundant data.
