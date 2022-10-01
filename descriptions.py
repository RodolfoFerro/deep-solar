TABS = {
    'challenge':
    """
            ### The Challenge

            If a major space weather event like the Carrington Event of 1859
            were to occur today, the impacts to society could be devastating.
            The challenge is to develop a machine learning algorithm or neural
            network pipeline to correctly track changes in the peak solar wind
            speed and provide an early warning of the next potential
            Carrington-like event.

            The complete description of the challenge can be found
            [here](https://2022.spaceappschallenge.org/challenges/2022-challenges/carrington-event/details).
        """,
    'solution':
    """
            ### About the project...

            The project consists of an autoencoder (artifical neural network)
            pipeline packed into an interactive application that fetches data
            from a specific period in `cfd` format from the official website
            to identify anomalies in the solar wind. More details about the
            model used are provided in the corresponding section, after the
            application section.

            The next section contains the instructions to use the machine
            learning application.
        """,
    'instructions':
    """
            ### How to use this application?

            The project consists of two columns. The first column is used to
            select a period of time to fetch data from the official website.
            The second column is used to display the results of the model
            trying to reconstruct the original data. This will allow the model
            to identify anomalies in the solar wind.
        """
}

DOCUMENTATION = """
<br />

------

## Project documentation 📚

### Anomaly Detection

Anomaly detection is the process of finding abnormalities in data. Abnormal 
data (an anomaly) is defined as the ones that deviate significantly from 
the general behavior of the data. Some of the applications of anomaly 
detection include fraud detection, fault detection, and intrusion detection. 
Anomaly Detection is also referred to as outlier detection.

### What is an anomaly?

Generally speaking, an anomaly is something that differs from a norm: a 
deviation, an exception. In software engineering, by anomaly we understand 
a rare occurrence or event that doesn't fit into the pattern, and, therefore, 
seems suspicious.

_**Common reasons for outliers are:** data preprocessing errors, noise, fraud, 
and attacks._

### Types of anomalies
#### Global outliers

When a data point assumes a value that is far outside all the other data 
point value ranges in the dataset, it can be considered a global anomaly. In 
other words, it's a rare event.

#### Contextual outliers

When an outlier is called contextual it means that its value doesn't 
correspond with what we expect to observe for a similar data point in the 
same context. Contexts are usually temporal, and the same situation observed 
at different times can be not an outlier.

#### Collective outliers

Collective outliers are represented by a subset of data points that deviate 
from the normal behavior.

### What are anomaly detection methods?

Anomaly detection methods are used to identify outliers in a dataset. 
Depending if the data is labeled, partially labeled, or not at all, 
a supervised, unsupervised, or semi-supervised approach can be used.

Some of the most common anomaly detection methods are:
- Local outlier factor (LOF)
- K-nearest neighbors
- Support vector machines
- DBSCAN
- Bayesian networks
- Autoencoders

In our case, we will use an autoencoder to detect anomalies in the solar
wind data.

### What are autoencoders?

Autoencoders are artificial neural networks, trained in an unsupervised 
manner, that aim to first learn encoded representations of our data and 
then generate the input data (as closely as possible) from the learned 
encoded representations. Thus, the output of an autoencoder is its 
prediction for the input.

<center>
    <img width="200px" src="https://atcold.github.io/pytorch-Deep-Learning/images/week07/07-3/13_ae_structure.png">
</center>

The previous figure shows the architecture of a basic autoencoder. We 
start from the bottom with the input which is subjected to an encoder 
(affine transformation). This results in the intermediate hidden layer 
subjected to the decoder (another affine transformation). This produces 
the output, which is our model's prediction/reconstruction of the input. 
We can represent the above network mathematically by using the following 
equations:
<center>
    <img src="https://math.vercel.app/?color=white&bgcolor=black&from=%5Cbegin%7Bequation%7D%0A%5Cbegin%7Bsplit%7D%0A%5Cboldsymbol%7Bh%7D%20%3D%20f%28%5Cboldsymbol%7BW_h%7D%5Cboldsymbol%7Bx%7D%20%2B%20%5Cboldsymbol%7Bb_h%7D%29%20%5C%5C%0A%5Cboldsymbol%7B%5Chat%7Bx%7D%7D%20%3D%20g%28%5Cboldsymbol%7BW_x%7D%5Cboldsymbol%7Bh%7D%20%2B%20%5Cboldsymbol%7Bb_x%7D%29%0A%5Cend%7Bsplit%7D%0A%5Cend%7Bequation%7D.svg">
</center>

Where:
<center>
    <img src="https://math.vercel.app/?color=white&bgcolor=black&from=%5Cbegin%7Bequation%7D%0A%5Cbegin%7Bsplit%7D%0A%0A%5Cboldsymbol%7Bx%7D%2C%5Cboldsymbol%7B%5Chat%7Bx%7D%7D%20%5Cin%20%5Cmathbb%7BR%7D%5En%5C%5C%20%0A%5Cboldsymbol%7Bh%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed%5C%5C%20%0A%5Cboldsymbol%7BW_h%7D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bd%20%5Ctimes%20n%7D%5C%5C%20%0A%5Cboldsymbol%7BW_x%7D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bn%20%5Ctimes%20d%7D%0A%0A%5Cend%7Bsplit%7D%0A%5Cend%7Bequation%7D.svg">
</center>

### Why do we use autoencoders?

The primary applications of an autoencoder is for anomaly detection or image 
denoising. An autoencoder's task is to be able to reconstruct data that lives 
on the manifold i.e. given a data manifold, we would want our autoencoder to 
be able to reconstruct only the input that exists in that manifold. Thus we 
constrain the model to reconstruct things that have been observed during 
training, and so any variation present in new inputs will be removed because 
the model would be insensitive to those kinds of perturbations.
<center>
    <img width="360px" src="https://atcold.github.io/pytorch-Deep-Learning/images/week07/07-3/15_denoising_ae.png">
</center>

### List of references:

- [What Is Anomaly Detection in Machine Learning?](https://serokell.io/blog/anomaly-detection-in-machine-learning)
- [Introduction to autoencoders](https://atcold.github.io/pytorch-Deep-Learning/en/week07/07-3/)
- [Anomaly Detection using AutoEncoders - A Walk-Through in Python](https://www.analyticsvidhya.com/blog/2021/05/anomaly-detection-using-autoencoders-a-walk-through-in-python/)
- [Autoencoder For Anomaly Detection Using Tensorflow Keras](https://grabngoinfo.com/autoencoder-for-anomaly-detection-using-tensorflow-keras/)
- [Intro to Autoencoders](https://www.tensorflow.org/tutorials/generative/autoencoder)
- [Timeseries anomaly detection using an Autoencoder](https://keras.io/examples/timeseries/timeseries_anomaly_detection/)
"""
