INFO = {
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
            ### The Solution

            The project consists of an autoencoder (artifical neural network)
            pipeline packed into an interactive application that fetches data
            from a specific period in `cfd` format from the NASA's Open Data
            portal for a minor adjustment of model's parameters in order to 
            identify anomalies in the solar wind. More details about the model
            used are provided in the corresponding section.

            Check our working model in the [aplication section](/Application).
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

ANOMALY_DETECTION = [
    """
    # Anomaly Detection (Srivignesh, 2021)

    Anomaly detection is the process of finding abnormalities in data. Abnormal 
    data (an anomaly) is defined as the ones that deviate significantly from 
    the general behavior of the data. Some of the applications of anomaly 
    detection include fraud detection, fault detection, and intrusion detection. 
    Anomaly Detection is also referred to as outlier detection.

    ### What is an anomaly? (Gavrilova, 2021)

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
    """, """
    #### Contextual outliers

    When an outlier is called contextual it means that its value doesn't 
    correspond with what we expect to observe for a similar data point in the 
    same context. Contexts are usually temporal, and the same situation observed 
    at different times can be not an outlier.
    """, """
    #### Collective outliers

    Collective outliers are represented by a subset of data points that deviate 
    from the normal behavior.
    """, """
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

    **In our case, we will use an autoencoder to detect anomalies in the solar
    wind data.**

    ### References

    - Serokell Software Development Company. 2022. Anomaly Detection in Machine Learning. [online] Available at: <https://serokell.io/blog/anomaly-detection-in-machine-learning> [Accessed 2 October 2022].
    - R, S., 2022. Anomaly Detection using AutoEncoders | A Walk-Through in Python. [online] Analytics Vidhya. Available at: <https://www.analyticsvidhya.com/blog/2021/05/anomaly-detection-using-autoencoders-a-walk-through-in-python/> [Accessed 2 October 2022].
"""
]

ANOMALY_DETECTION_IMGS = [
    "https://serokell.io/files/58/58bpyam1.3_(6)_(1).png",
    "https://serokell.io/files/r0/r03raoc3.4_(9)_(1).png",
    "https://serokell.io/files/up/upyiiyo4.5_(8)_(1).png"
]

AUTOENCODERS = [
    """
    ### What are autoencoders? (Canziani, 2022)

    Autoencoders are artificial neural networks, trained in an unsupervised 
    manner, that aim to first learn encoded representations of our data and 
    then generate the input data (as closely as possible) from the learned 
    encoded representations. Thus, the output of an autoencoder is its 
    prediction for the input.""", """
    The previous figure shows the architecture of a basic autoencoder. We 
    start from the bottom with the input which is subjected to an encoder 
    (affine transformation). This results in the intermediate hidden layer 
    subjected to the decoder (another affine transformation). This produces 
    the output, which is our model's prediction/reconstruction of the input. 
    We can represent the above network mathematically by using the following 
    equations:
    """, """
    Where:
    """, """
    ### Why do we use autoencoders?
    """, """
    The primary applications of an autoencoder is for anomaly detection or
    denoising. An autoencoder's task is to be able to reconstruct data
    that lives on the manifold i.e. given a data manifold, we would want our
    autoencoder to be able to reconstruct only the input that exists in that
    manifold. Thus we constrain the model to reconstruct things that have
    been observed during training, and so any variation present in new inputs
    will be removed because the model would be insensitive to those kinds of
    perturbations. 
    
    ##### This is why autoencoders are used for anomaly detection in our project.

    ### References

    - Alfredo Canziani 2022. Introduction to autoencoders · Deep Learning. [online] Available at: <https://atcold.github.io/pytorch-Deep-Learning/en/week07/07-3/> [Accessed 2 October 2022].
    """
]

AUTOENCODERS_IMGS = [
    "https://atcold.github.io/pytorch-Deep-Learning/images/week07/07-3/13_ae_structure.png",
    "https://math.vercel.app/?from=%5Cbegin%7Bequation%7D%0A%5Cbegin%7Bsplit%7D%0A%5Cboldsymbol%7Bh%7D%20%3D%20f%28%5Cboldsymbol%7BW_h%7D%5Cboldsymbol%7Bx%7D%20%2B%20%5Cboldsymbol%7Bb_h%7D%29%20%5C%5C%0A%5Cboldsymbol%7B%5Chat%7Bx%7D%7D%20%3D%20g%28%5Cboldsymbol%7BW_x%7D%5Cboldsymbol%7Bh%7D%20%2B%20%5Cboldsymbol%7Bb_x%7D%29%0A%5Cend%7Bsplit%7D%0A%5Cend%7Bequation%7D.svg",
    "https://math.vercel.app/?from=%5Cbegin%7Bequation%7D%0A%5Cbegin%7Bsplit%7D%0A%0A%5Cboldsymbol%7Bx%7D%2C%5Cboldsymbol%7B%5Chat%7Bx%7D%7D%20%5Cin%20%5Cmathbb%7BR%7D%5En%5C%5C%20%0A%5Cboldsymbol%7Bh%7D%20%5Cin%20%5Cmathbb%7BR%7D%5Ed%5C%5C%20%0A%5Cboldsymbol%7BW_h%7D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bd%20%5Ctimes%20n%7D%5C%5C%20%0A%5Cboldsymbol%7BW_x%7D%20%5Cin%20%5Cmathbb%7BR%7D%5E%7Bn%20%5Ctimes%20d%7D%0A%0A%5Cend%7Bsplit%7D%0A%5Cend%7Bequation%7D.svg",
    "https://atcold.github.io/pytorch-Deep-Learning/images/week07/07-3/15_denoising_ae.png"
]

RESULTS = [
    """
    ## Results

    ### Current pipeline method (An overview)

    According to Space Apps Challenge (2022), at present, the raw data are
    converted to physics units using a calibration table, summed over the
    sensor segments, and recast as phase space distribution functions. A
    variety  of ad hoc operations are invoked in order to tweak the
    background subtraction, isolate the physically relevant sub-range in
    voltage, and remove transients. Then a Gaussian peak fitting is performed.
    The parameters of the Gaussian map directly to _(n, w, |v|)_. Finally, the
    ratios between the signal peak values are fed into a table lookup to
    estimate the flow angle and complete the velocity vector.

    ### Our approach

    As mentioned in the previous sections, we are using autoencoders for:
    1. Denoising
    2. Then, **anomaly detection**

    ### Models

    We trained 2 different models for our project. Both models are
    **Denoising Autoencoders**.

    > The idea was to explore different data features and train a model in
    > order to reconstruct original data. The reconstructed data is then
    > compared with the original data to find the difference between them.
    > The difference is then used to find the anomalies in the data.

    ##### Model 1 (Full features)

    The first model was trained on the raw data. 

    _More details will be added._

    ##### Model 2 (Compressed data representation)

    The second model was trained on a compressed representation of data.
    The raw data corresponding to coordinates in `BGSE` format was converted
    into a single Real Number value using the norm of the vector.

    > Note:
    > - **BGSE:** Geocentric Solar Ecliptic system. This has its X-axis
    >    pointing from the Earth toward the Sun and its Y-axis is chosen to
    >    be in the ecliptic plane pointing towards dusk (thus opposing
    >    planetary motion). Its Z-axis is parallel to the ecliptic pole.
    >    Relative to an inertial system this system has a yearly rotation.
    > - **BGSM:** Geocentric Solar Magnetospheric system. This has its X-axis
    >    from the Earth to the Sun. The Y-axis is defined to be perpendicular
    >    to the Earth's magnetic dipole so that the X-Z plane contains the
    >    dipole axis. The positive Z-axis is chosen to be in the same sense
    >    as the northern magnetic pole. The difference between the GSM and
    >    GSE systems is simply a rotation about the X-axis.

    This led us to have a 2-column dataset, with the first column corresponding
    to the mentioned norm of the coordinates, and with the second column
    corresponding to `BF1` values from the
    [_Wind dataset_](https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h2/2022/).

    _More details will be added._
    """, """
    ### References

    - Space Apps Challenge. 2022. Notional DSCOVR Faraday Cup Instrument “Calibration” and Data Analysis Procedure. [online] Available at: <https://www.spaceappschallenge.org/space-apps-challenge-2022-example-resource-save-the-earth-from-another-carrington-event/> [Accessed 2 October 2022].
    - Grab N Go Info. 2022. Autoencoder For Anomaly Detection Using Tensorflow Keras - Grab N Go Info. [online] Available at: <https://grabngoinfo.com/autoencoder-for-anomaly-detection-using-tensorflow-keras/> [Accessed 2 October 2022].
    - R, S., 2022. Anomaly Detection using AutoEncoders | A Walk-Through in Python. [online] Analytics Vidhya. Available at: <https://www.analyticsvidhya.com/blog/2021/05/anomaly-detection-using-autoencoders-a-walk-through-in-python/> [Accessed 2 October 2022].
    - Team, K., 2022. Keras documentation: Timeseries anomaly detection using an Autoencoder. [online] Keras.io. Available at: <https://keras.io/examples/timeseries/timeseries_anomaly_detection/> [Accessed 2 October 2022].
    """
]

RESULTS_IMGS = ["assets/results.png"]
