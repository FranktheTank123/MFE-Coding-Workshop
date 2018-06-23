## Topics

- Version Control
- Advanced Python
- Production Python


## Version Control


## Advanced Python

### Setup

0. Pro tip: use Python3

#### Anaconda
Anaconda is very good Python package manager + environment manager + additional scientific libraries. Highly recommend for local development. Not recommend for servers, as its ~3GB.
1. Download and install Anaconda Python 3.6 [here](https://www.anaconda.com/download/#macos)
2. Create environment `conda create --name test --file conda-requirements.txt`
3. `source activate test` (vs. `source deactivate`)
4. `whichp python`

Note that the `test` environment folder is usually stored with your `anaconda`. To check, try `which conda`.  

#### `pip` + `virtualenv`
`pip` is light-weigt Python pacakge manager. `virtualenv` is light-weight Python environment manager.

1. Install [Python3](http://docs.python-guide.org/en/latest/starting/install3/osx/)
2. Go to the folder where you want to install your env, usually the repo.
3. Setup environment `virtualenv env -p python3` 
4. `source env/bin/activate` (vs. `deactivate`)
5. `pip install -r requirements.txt`
6. `which python`



### 

## Production Python

### Development Environment

* **Local/Development**: your laptop or a sandbox on a development server 
* **Testing**: for all the tests, shares the same environement as `staging` and `production`
* **Staging**: an environment for final testing immediately prior to deploying to production. A mirror of `production`, but not facing to the users.
* **Production**: the environment that users/clients directly interact with

![img](img/deployment-plan.gif)

### Python Debug

* Why bother debugging? 
* You need to debug when:
	- you see a Shape ratio of 40
	- you are trying to understand your teammate's code
* How many of you debug via:
	- `print(...)`
	- Binary search
	- `pdb`/`ipdb`
* Examples 
	- debug in `ipdb` (make sure you `pip install ipdb`)
	- debug in `ipython notebook` (use the magic command `%debug` after you see an error)

### Python Tests

* Why bother testings?
	- Collborations
	- Too big to fail
	- Know who to blame
* Different types of tests
	- lint checks
	- unit test
	- integration test
	- regression test
	- ...

#### Lint

#### Unit Test

#### Continuous Integration

Continuous Integration (CI) tools help you stick to your team’s quality standards by running tests every time you push a new commit and reporting the results to a pull request.

Examples:
	- [Travis CI](https://github.com/marketplace/travis-ci)
	- [Jenkins](https://jenkins.io/)

