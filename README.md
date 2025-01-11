# dsa

- this is a collection of data structures and algorithms, will probably be pretty leetcode heavy at first

# project structure

```bash
├── src
│    ├── algorithms - contains a collection algorithms
│    ├── data_structures - contains a collection data_structures
│    └── leetcode - contains a collection of leetcode problems with links to the problem
├── test
│    ├── algorithms_test - pytest for algorithms
│    ├── data_structures_test - pytest for data_structures
│    └── leetcode_test - pytest for leetcode questions
```

# How to get code and use it?

**1. install python interpreter**

- you can use homebrew, pyenv, etc...
- I am currently using python 3.13.1

**2. clone this project**

```bash
git clone git@github.com:dallasgere/dsa.git
```

**3. navigate into the root of this directory**

```bash
cd dsa/
```

**4. create a python virtual environment**

```bash
# I call mine venv but you can call it whatever you like
python3 -m venv venv
```

**5. activate the virtual environment**

```bash
# unix
source venv/bin/activate

# powershell
.\venv\Scripts\Activate.ps1
```

**6. install pip dependencies**

```bash
pip install -r requirements.txt
```

# testing solutions

- all solutions should be tested with pytest in the test folder
- you can write test cases for solutions and run them with pytest

```bash
# how to run test cases
pytest
```

# git branching

- Given this is a hobby project with me as the only contributor right now, I am just using main branch right now

  - however if anyone wanted to work on this as well I would enforce git best practices
  - I just feel silly approving my own PR's :)

- I promise in my professional dev job I use git branching extensively🙈

# formatting

- I am currently using black to format the python code
  - link: https://github.com/psf/black
- you can pip install and then run black .
- or you can use the vscode extension
  - https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter
