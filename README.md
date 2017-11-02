# review-board
Python Project to get the list of all the pull requests made to your repository. It has plugins for all popular websites like Github, Gitlab, Gerrit and Pagure.

## How to setup
* Install the **virtualenv** package using pip

Linux
```
pip3 install virtualenv
```
Windows
```
pip install virtualenv
```

* Setup a virtual environment
```
virtualenv myenv
```
* Activate the virtual environment

Linux
```
source myenv/bin/activate
```
Windows
```
myenv\Scripts\ activate
```
* Install all the needed packages using pip.

**Linux**
```
pip3 install -r requirement.txt
```
**Windows**
```
pip install -r requirement.txt
```
## How to run
Just run the app.py file along with the following flags:

**--site**  -  the website you want to get data from.

**--username**  -  username.

**--repo**  -  name of the repository.

**Linux**
```
python3 app.py --site github --username user --repo repo_name
```
**Windows**
```
python app.py --site github --username techytushar --repo repo_name
```
## Licensing
review-board is licensed under GPL-3.0. See [LICENSE](https://github.com/geeksocket/review-board/blob/master/LICENSE) for the full license text.
