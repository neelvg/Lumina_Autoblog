# Lumina_Autoblog
This repository will automate the blogging in blogspot using Google bard AI it will also helps in such features like researches like keywords, compitiors research and generate content through bard than it will rewrite article by grammatically, anti plagiarisms, and paraphrasing after such things it will upload also on blogspot 

# installation on termux
here is the installation process on Termux:-

1. Install Termux on your Android device.
2. download the software files
3. Open Termux and type the following command to update the package list:

```
apt update
```

4. Type the following command to upgrade the package list

```
apt upgrade
```

5. Type the following command to install Python:

```
apt install python
```

6. Type the following command to install the Bard AI library:

```
pip install bard
```
7. Type the following command to install the Bard AI library:

```
pip install pytrends
```
8. Clone your GitHub repository to Termux:

```
git clone https://github.com/neelvg/Lumina_Autoblog.git
```
9. Type the following command to change the permissions on the main.py file so that it is executable.

```
chmod +x main.py
```
9. Change directory to the cloned repository:

```
cd Lumina_Autoblog
```
10. Set the MAX_POSTS_PER_DAY variable to a reasonable value.

```
export MAX_POSTS_PER_DAY= [no. of post per day]
```
11. Run the JavaScript file:

```
python main.py
```

The JavaScript file will now run and create new blog posts on your Blogger account.

Here are some additional instructions for non-Termux or GitHub users:

* If you do not have Termux installed, you can download it from the Google Play Store.
* If you do not have a GitHub account, you can create one for free.
* You can clone your GitHub repository to your computer using a Git client such as GitHub Desktop.
* Once you have cloned your repository, you can run the JavaScript file from your computer.

# test suite
The test suite for this project is located in the tests directory. The test suite consists of a number of unit tests that test the functionality of the JavaScript file.

To run the test suite, you can use the following command:
```
python -m unittest discover -s tests
```
The test suite will run all of the unit tests and report the results
