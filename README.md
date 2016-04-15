# Twitter Hashtag Recommendation System
This Exploratory Project includes building a Hashtag Recommendation System for Twitter. 

### Background
This project is a part of the Exploratory Project included in semester IV of academic session 2015-16. It was carried out by *Deepak Yadav* and *Faizan Khan*, Department of Computer Science and Engineering, IIT(BHU), under the guidance of Associate Professor *Dr. S.K.Singh*. The primary aim of the project was to help the students apply their skills to a real world project and gain experience.

### Details
The major details for the coding project are as follows:

##### Problem Definition
Hashtags provide users with a tagging mechanism to help organize, group, and create visibility for their posts. This is a simple idea but can be challenging for the user in practice which leads to infrequent usage. Hashtag recommendation comes with numerous challenges including processing huge volumes of streaming data and content which is small and noisy. We will use preprocessing methods to reduce noise in the data and determine an effective method of hashtag recommendation to get better recommendations.

##### Objective
To build a Twitter Hashtag Recommendation System. The System will recommend the user other hashtags based on his/her given input. 
 - Domain : Twitter Tweets retrieved with the Twitter API
 - Purpose : Recommend similar hashtags to users
 - Personalization Level : Generic
 - Interfaces : Explicit Input, Recommended Output

 
## Contributing to the Project

We will be more than happy to improve upon this basic project. Any advice is appreciated. Here is how you can contribute to the project:
 - The easiest way to contribute is to point out issues.
 - Send us PRs with what you think can be enhanced in the project.
 - Contact us([see below](https://github.com/faizan-khan-iit/Hashtag_Recommender#contact-details)) with the features you would like to see in the project and are willing to contribute to.

### Requirements
The basic requirements of the project are as follows (Note: The project was developed with the following specifications and may also work with earlier versions):
 - Python v2.7
  - [twitter](https://pypi.python.org/pypi/twitter)
  - [HTMLParser](https://docs.python.org/2/library/htmlparser.html)
  - [Tkinter module](https://docs.python.org/2/library/tkinter.html)
 - R v3.2.2

### Resources used in the project

##### Getting Data
The recommender uses the [Twitter API](https://dev.twitter.com/overview/documentation) to obtain the raw tweets for preprocessing. To obtain a large volume of data, the [Streaming API](https://dev.twitter.com/streaming/overview) is used. [This tutorial](http://socialmedia-class.org/twittertutorial.html) provides a very basic introduction to getting tweets using a Python library called [Python Twitter Tools](https://pypi.python.org/pypi/twitter) to connect to Twitter API and downloading the data from Twitter.

##### Preprocessing
Cleaning the tweets before processing is done using various steps.
 - [This infographic](http://www.analyticsvidhya.com/blog/2015/06/quick-guide-text-data-cleaning-python/) provides some of the basic details about cleaning tweet text.
 - Most of the cleaning is done using Regular Expressions in [Python 2](https://docs.python.org/2/library/re.html)/[3](https://docs.python.org/3/library/re.html) and [R](https://stat.ethz.ch/R-manual/R-devel/library/base/html/regex.html). [This tutorial from Tutorials Point](http://www.tutorialspoint.com/python/python_reg_expressions.htm) may be helpful.
 - The stop words to remove from the tweets may be found [here](http://www.ranks.nl/stopwords).

##### App GUI
The app uses a very basic interface developed using the [Python Tkinter module](https://docs.python.org/2/library/tkinter.html). [This basic tutorial](http://www.tutorialspoint.com/python/python_gui_programming.htm) may be helpful.


### Contact details
Please contact us regarding any issues and/or suggestions

###### Deepak Yadav
B.Tech, Part II
Department of Computer Science and Engineering
IIT(BHU), Varanasi, India
[https://github.com/cryptomanic/]
[deepak.yadav.cse14@iitbhu.ac.in]
[deepakyadav.iitbhu@gmail.com]

###### Faizan Uddin Fahad Khan
Integrated Dual Degree, Part II
Department of Computer Science and Engineering
IIT(BHU), Varanasi, India
[https://github.com/faizan-khan-iit]
[fufahad.khan.cse14@iitbhu.ac.in]
[faizan.khan.iitbhu@gmail.com]
