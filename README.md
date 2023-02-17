# Image2Gestures

## Goal for Feb. 24

(10-min presentation (maybe) showing a prototype of our project)
- Decide types of gesturewe want to classify, and how those gesture can potentially applied to real-life controls.

- Experiment with the camera configurations, find feasible position and zenith angle on the hand.

- Building a Machine Learning pipeline: 
    1. Data collection / labeling $\rightarrow$ Currently we just consider image, see if image does not working, can we also use motion and secondary data source?
    2. Think about models. If only using image, prpose a possible convolutional network, along with RNN/LSTM. If including motion data, open the discussion.

- Stick with Arduino 33, findout hardware pipeline to acieve 0/1 digit classification through camera. This is for testing the computing capability of the hardware. 