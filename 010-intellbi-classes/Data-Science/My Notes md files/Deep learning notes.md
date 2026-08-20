### Q: Why was Deep Learning introduced when Machine Learning already existed?

>   Good answer:

-   Traditional Machine Learning works well for many structured-data problems but often depends on  
    manual feature engineering. Deep Learning was introduced to automatically learn complex pattern 
    from large datasets, making it highly effective for images, speech, text, and other unstructured data.
-----------------------------------------------------------------------------------------------------
### Q1. Why can't traditional Machine Learning solve every AI problem efficiently?

-   Traditional Machine Learning works well for structured/tabular data, but it struggles with 
    complex unstructured data such as images, audio, and text. It also often requires manual feature
    engineering, which becomes difficult for these types of data.
-----------------------------------------------------------------------------------------------------
### Q2. Biggest advantage of Deep Learning

-   Deep Learning can automatically learn complex features from large amounts of structured 
    and unstructured data, reducing the need for manual feature engineering.
-----------------------------------------------------------------------------------------------------
### Q3. Applications
    
    Face recognition
    Self-driving vehicle
    Speech recognition
-----------------------------------------------------------------------------------------------------

>   Deep Learning is a subset of Machine Learning and is particularly useful for complex problems 
    involving large amounts of data and unstructured inputs such as images, text, and audio.

-----------------------------------------------------------------------------------------------------
### Q3. Name the four main parts of a biological neuron.

              Dendrites
                  │
                  │
            +------------+
            |  Cell Body |
            +------------+
                  │
                Axon
                  │
                  ▼
          Axon Terminal
                  │
             Next Neuron
-----------------------------------------------------------------------------------------------------
### What is a Biological Neuron?

-   A neuron is a specialized nerve cell in the brain and nervous system.
------------------------------------------------------------------------------------------------------
###   Biological Neuron vs Artificial Neuron

| Biological Neuron             | Artificial Neuron                  |
|-------------------------------|------------------------------------|
| Receives signals              | Receives input data                |
| Processes signals             | Performs mathematical calculations |
| Decides whether to fire       | Produces an output value           |
| Sends signal to other neurons | Sends output to the next neuron    |

------------------------------------------------------------------------------------------------------
###  Why did the brain inspire Deep Learning

-   The human brain can automatically learn patterns from experience, process huge amounts of information,
    and make intelligent decisions. Researchers were inspired by this ability and designed artificial 
    neurons that imitate the basic working principle of biological neurons.

------------------------------------------------------------------------------------------------------
###  What is an Artificial Neuron?

-   An artificial neuron is the smallest computational unit of a neural network that receives inputs, 
    performs mathematical operations, and produces an output.

------------------------------------------------------------------------------------------------------
###  Biological Neuron vs Artificial Neuron

| Biological Neuron     | Artificial Neuron       |
|-----------------------|-------------------------|
| Dendrites             | Inputs (x₁, x₂, x₃...)  |
| Cell Body             | Mathematical Processing |
| Brain decides         | Activation Function     |
| Axon Terminal         | Output                  |
| Signal to next neuron | Output to next neuron   |

------------------------------------------------------------------------------------------------------
### Structure of an Artificial Neuron
             x₁
              │
             x₂
              │
             x₃
              │
      +------------------+
      | Artificial       |
      |    Neuron        |
      +------------------+
              │
              ▼
           Output (y)
------------------------------------------------------------------------------------------------------
###  Components of an Artificial Neuron

-   There are five main components.
>   Input (x)           :- 
>   Weight (w)          :-  "How important is each input?"  
>   Bias (b)            :-  Bias gives the neuron flexibility in making decisions.
>   Activation Function :-  "Should I pass this information forward?"   
                                transforms the neuron's computed value into an output,
>   Output (y)          :-  Is this image a cat?

------------------------------------------------------------------------------------------------------
###   What is an Artificial Neuron?

-   An artificial neuron is the basic computational unit of a neural network. 
    It receives input features, assigns weights to them, adds a bias, applies an activation function,
    and produces an output.

-----------------------------------------------------------------------------------------------------
###     Complete Flow

Input Features
      │
      ▼
Multiply by Weights
      │
      ▼
Add All Results
      │
      ▼
Add Bias
      │
      ▼
Activation Function
      │
      ▼
Output

---------------------------------------------------------------------------------------------------
### What does x represent?

x represents the input features provided to the neuron, such as age, salary, or years of experience.

---------------------------------------------------------------------------------------------------
### Why do we multiply by weights?

We multiply each input by its weight because different features contribute differently to the prediction.
The weights represent the importance of each feature and are learned automatically during training.

---------------------------------------------------------------------------------------------------
### Why is bias added?

Bias shifts the neuron's decision boundary, allowing it to make more flexible predictions 
even when the weighted inputs remain the same.

---------------------------------------------------------------------------------------------------
### What is the purpose of the activation function?

The activation function transforms the neuron's weighted sum into an output and introduces 
non-linearity, enabling neural networks to learn complex patterns.

-----------------------------------------------------------------------------------------------------
### Why is the neuron's calculation called a linear combination?
✅ Expected Answer

The neuron multiplies each input by its corresponding weight and adds them together with a bias.
Since this is a weighted sum of the inputs, it is called a linear combination.

----------------------------------------------------------------------------------------------------
### What is the difference between input features and weights?
✅ Expected Answer

Input features are the data values provided to the model (such as age or salary), 
while weights are learnable parameters that determine how important each feature is for 
making predictions.

----------------------------------------------------------------------------------------------------
### Are weights manually assigned?
✅ Expected Answer

No. In Deep Learning, weights are initialized and then automatically updated during training 
using optimization algorithms (such as Gradient Descent) to minimize the model's error.

---------------------------------------------------------------------------------------------------
### What happens if the bias is removed?
✅ Expected Answer

Without bias, the neuron becomes less flexible because its decision boundary cannot shift independently of the inputs.
This can reduce the model's ability to fit the data effectively.
------------------------------------------------------------------------------------------------
###     What is a Neural Network?

Definition:-
-   A Neural Network is a collection of interconnected artificial neurons organized into layers. 
    Each neuron processes information and passes its output to the next layer, 
    enabling the network to learn complex patterns from data.

Notice two important ideas:

Collection of neurons
Organized into layers

-----------------------------------------------------------------------------------------------------
###     Why do we need multiple neurons?

-   A single neuron can only learn simple relationships. Multiple neurons working together can 
    learn complex patterns and solve difficult problems such as image recognition and language 
    understanding.
-----------------------------------------------------------------------------------------------------
###     What are the three main layers?

Input Layer
Hidden Layer(s)
Output Layer

-----------------------------------------------------------------------------------------------------
###     Q4. Where does learning happen?

Learning primarily happens in the hidden layers, where the network adjusts weights and biases to 
learn useful representations of the data.

-----------------------------------------------------------------------------------------------------
###     Q5. Why is it called "Deep" Learning?

It is called Deep Learning because the neural network contains multiple hidden layers, 
allowing it to learn increasingly complex features.

-----------------------------------------------------------------------------------------------------
###     What is a Feed Forward Neural Network?

A Feed Forward Neural Network (FFNN) is the simplest type of artificial neural network.

Definition:-    A Feed Forward Neural Network is a neural network in which information flows in 
                only one direction:

Input Layer → Hidden Layer(s) → Output Layer

There are no loops, no cycles, and no feedback connections.

The word Feed Forward simply means that information always moves forward, 
never backward during prediction.
-----------------------------------------------------------------------------------------------------
###     Where is FFNN Used?

FFNN is commonly used for:

House Price Prediction
Loan Approval
Employee Attrition Prediction
Credit Risk Prediction
Sales Prediction
Basic Classification Problems

-----------------------------------------------------------------------------------------------------
###     Where Does FFNN Fail?

Language Translation
Stock Market Prediction
Speech Recognition

-----------------------------------------------------------------------------------------------------
### What is a Feed Forward Neural Network?

A Feed Forward Neural Network is the simplest neural network architecture in which information flows
only in one direction—from the input layer through one or more hidden layers to the output layer—with
no feedback connections or cycles.

-----------------------------------------------------------------------------------------------------
### What is the biggest limitation of an FFNN?

The biggest limitation of an FFNN is that it has no memory. 
It processes each input independently and cannot capture sequential or temporal relationships.

----------------------------------------------------------------------------------------------------
### Can FFNN solve image classification?

Yes, but it is generally not the preferred architecture for image data because it does not exploit
spatial relationships between pixels. CNNs are better suited for image-related tasks.
----------------------------------------------------------------------------------------------------
### 

| Problem                | Best Choice (Commonly)                                 | Why?                                        |
|------------------------|--------------------------------------------------------|---------------------------------------------|
| House Price Prediction | Linear Regression / XGBoost / FFNN (depending on data) | Structured tabular data                     |
| Customer Churn         | Logistic Regression, Random Forest, XGBoost, FFNN      | Classification on tabular data              |
| Image Classification   | CNN                                                    | Learns spatial features                     |
| Machine Translation    | RNN, LSTM, Transformer                                 | Needs sequence understanding                |
| ChatGPT-like Models    | Transformer                                            | Handles long-range dependencies efficiently |

------------------------------------------------------------------------------------------------------------------------------------

### Definition of RNN

>   Definition

-   A Recurrent Neural Network (RNN) is a type of neural network designed to process sequential data 
    by maintaining a memory (hidden state) of previous inputs.

Notice the two key phrases:

Sequential Data
Memory (Hidden State)

These are the heart of RNN.

-----------------------------------------------------------------------------------------------------
###     Architecture of an RNN

Unlike FFNN,

an RNN has a feedback connection.

           Hidden State
               ▲
               │
Input ───► Hidden Layer ───► Output
               │
               └────────────► Next Time Step

----------------------------------------------------------------------------------------------------
###     FFNN vs RNN

| Feature         | FFNN         | RNN                    |
|-----------------|--------------|------------------------|
| Memory          | ❌ No         | ✅ Yes                  |
| Sequential Data | ❌ No         | ✅ Yes                  |
| Language Tasks  | ❌ Poor       | ✅ Good                 |
| Time Series     | ❌ Poor       | ✅ Good                 |
| Data Flow       | Forward only | Forward + Hidden State | 

---------------------------------------------------------------------------------------------------
###     Real-World Applications

RNNs are commonly used for:

Speech Recognition
Language Translation
Text Generation
Chatbots (earlier generations)
Sentiment Analysis
Time-Series Forecasting
Stock Price Prediction
Weather Forecasting

--------------------------------------------------------------------------------------------------
###     Why was RNN invented?

-   RNN was invented to process sequential data. Unlike FFNN, it maintains a hidden state (memory) that
allows it to use information from previous inputs.

-------------------------------------------------------------------------------------------------
###     What is sequential data?

-   Sequential data is data where the order of elements matters, such as text, speech, stock prices,
or time-series data.

---------------------------------------------------------------------------------------------------
### What is the Hidden State?

-   The hidden state is the internal memory of an RNN. It stores useful information from previous time
steps and passes it to the next step to provide context.

------------------------------------------------------------------------------------------------------

### What is the biggest advantage of an RNN over an FFNN?

-   The biggest advantage is that an RNN can remember previous information using its hidden state, 
making it suitable for sequential data.

---------------------------------------------------------------------------------------------------
### Why isn't FFNN suitable for speech recognition?

-   Speech is sequential, and each word depends on previous words. FFNN processes each 
input independently and has no memory, whereas an RNN can preserve context through its hidden state.

---------------------------------------------------------------------------------------------------
### 
FFNN
│
├── No Memory
├── Independent Data
└── House Price, Loan Approval

↓

RNN
│
├── Has Memory (Hidden State)
├── Sequential Data
├── Uses Previous Context
└── Text, Speech, Time-Series

-----------------------------------------------------------------------------------------------------
###     What is the Long-Term Dependency Problem?

Definition

The Long-Term Dependency Problem occurs when an RNN cannot effectively retain important information 
from earlier time steps in a long sequence.

In simple words:

Short sentence → RNN performs well.
Long sentence → RNN starts forgetting earlier information.

-----------------------------------------------------------------------------------------------------
###     Why Was LSTM Invented?

Researchers asked:

"Can we build a neural network that remembers important information for a long time and forgets 
unimportant information?"

---------------------------------------------------------------------------------------------------------------
###     Why Was LSTM Invented?
Definition

LSTM is a special type of Recurrent Neural Network designed to remember important information 
for long periods and forget unnecessary information using a controlled memory mechanism.

-----------------------------------------------------------------------------------------------------
###     RNN vs LSTM

| Feature                | RNN       | LSTM                    |
|------------------------|-----------|-------------------------|
| Memory                 | Limited   | Long-term memory        |
| Long Sequences         | Poor      | Better                  |
| Long-Term Dependencies | Struggles | Handles much better     |
| Cell State             | ❌ No      | ✅ Yes                   |
| Gates                  | ❌ No      | ✅ Forget, Input, Output |

---------------------------------------------------------------------------------------------------
###     Overall LSTM Flow
Previous Cell State
        │
        ▼
   Forget Gate
        │
        ▼
    Input Gate
        │
        ▼
 Updated Cell State
        │
        ▼
   Output Gate
        │
        ▼
Hidden State / Output

------------------------------------------------------------------------------------------------
### Why was LSTM invented?
✅ Expected Answer

LSTM was invented to overcome the long-term dependency problem of RNN by introducing a cell state
and gates that help preserve important information over long sequences.

--------------------------------------------------------------------------------------------------
###     What is the Long-Term Dependency Problem?
✅ Expected Answer

It is the problem where a standard RNN struggles to retain important information from earlier time
steps when processing long sequences.

--------------------------------------------------------------------------------------------------
###     What is the Cell State?
✅ Expected Answer

The Cell State is the long-term memory of an LSTM.
It carries important information across time steps and helps preserve context over long sequences.

--------------------------------------------------------------------------------------------------
###     Name the three gates of an LSTM.
✅ Expected Answer
Forget Gate
Input Gate
Output Gate

--------------------------------------------------------------------------------------------------
###     What is the role of the Forget Gate?
✅ Expected Answer

The Forget Gate decides which information from the previous cell state should be discarded
because it is no longer useful.

--------------------------------------------------------------------------------------------------
###     Can LSTM be used for stock price prediction?
✅ Expected Answer

Yes. Stock prices form a time-series sequence where previous values influence future values, 
making LSTM a suitable model for capturing long-term patterns.

------------------------------------------------------------------------------------------------
                
                Artificial Neuron
                        │
                        ▼
                Neural Network (Many Neurons)
                        │
                        ▼
                Feed Forward Neural Network (FFNN)
                        │
                        │  ❌ No Memory
                        ▼
                Recurrent Neural Network (RNN)
                        │
                        │  ❌ Cannot Remember Long Sequences
                        ▼
                Long Short-Term Memory (LSTM)
                        │
                        │  ✅ Better Long-Term Memory
                        ▼
                Convolutional Neural Network (CNN)
                        │
                        │  Specialized for Images
                        ▼
                Transformers
                        │
                        │  Better Long-Range Context + Parallel Processing
                        ▼
                Modern LLMs (ChatGPT, Gemini, Claude, etc.)

----------------------------------------------------------------------------------------------------
###     CNN vs FFNN

| Feature                         | FFNN      | CNN        |
|---------------------------------|-----------|------------|
| Best for Images                 | ❌ No      | ✅ Yes      |
| Understands Spatial Information | ❌ No      | ✅ Yes      |
| Number of Parameters            | Very High | Much Lower |
| Learns Local Patterns           | ❌ No      | ✅ Yes      |
| Edge Detection                  | ❌ No      | ✅ Yes      |

-----------------------------------------------------------------------------------------------------
###     Why was CNN invented?
✅ Expected Answer

CNN was invented to efficiently process image data by preserving spatial relationships 
between pixels and automatically learning useful visual features.

-----------------------------------------------------------------------------------------------------
###     Why isn't FFNN suitable for images?
✅ Expected Answer

FFNN requires flattening the image into a one-dimensional vector,
which loses spatial information and creates a very large number of parameters.

-----------------------------------------------------------------------------------------------------
###     What is Convolution?
✅ Expected Answer

Convolution is the operation in which a small filter (kernel) slides across an image to extract
useful features such as edges, textures, and patterns.

--------------------------------------------------------------------------------------------------------
###     What is a Filter (Kernel)?
✅ Expected Answer

A filter is a small matrix that moves across an image during convolution to detect specific visual features.

-------------------------------------------------------------------------------------------------------
###     What is a Feature Map?
✅ Expected Answer

A Feature Map is the output generated after applying a filter to an image. It highlights the detected 
features.

------------------------------------------------------------------------------------------------------

FFNN
│
├── Best for tabular data
├── Flattens input
├── Loses spatial information
└── Many parameters

↓

CNN
│
├── Designed for images
├── Uses Convolution
├── Uses Filters (Kernels)
├── Produces Feature Maps
└── Preserves spatial relationships

-------------------------------------------------------------------------------------------------------
###     Why was CNN invented when FFNN already existed?

CNN was invented because FFNN is inefficient for image processing. FFNN requires flattening an image,
which destroys spatial relationships between pixels and creates a huge number of parameters.
CNN solves this by scanning small regions of the image using filters, preserving local patterns
while reducing computation.

------------------------------------------------------------------------------------------------------
###     What is the biggest drawback of flattening an image?

FFNN requires flattening the image into a one-dimensional vector,
which loses spatial information and creates a very large number of parameters.

-----------------------------------------------------------------------------------------------------
###     Explain Convolution using your own example.

Imagine checking a huge wall for cracks using a small flashlight. You move the flashlight across
different sections of the wall instead of looking at the whole wall at once. 
CNN works in a similar way by scanning small regions of an image.

----------------------------------------------------------------------------------------------------
###     What is a Filter (Kernel)?

A Filter (Kernel) is a small matrix that slides across an image during convolution.
It detects useful features such as edges, corners, textures, or patterns, and produces a feature map
highlighting those features.

----------------------------------------------------------------------------------------------------
###     What does CNN stand for?
✅ Expected Answer

CNN stands for Convolutional Neural Network, a deep learning architecture designed primarily for
processing image and other grid-like data.

----------------------------------------------------------------------------------------------------
###     What is the main advantage of CNN over FFNN?
✅ Expected Answer

CNN preserves spatial relationships between pixels and learns local visual features using convolution,
while FFNN loses this information after flattening the image.

------------------------------------------------------------------------------------------------------
###     What kinds of features can CNN learn?
✅ Expected Answer

CNN learns features hierarchically:

Early layers → Edges and lines
Middle layers → Corners and textures
Deeper layers → Shapes and object parts
Final layers → Complete objects (e.g., faces, cars, animals)

------------------------------------------------------------------------------------------------------
###     Are filters manually designed?
✅ Expected Answer

No. During training, the CNN automatically learns the most useful filter values from the training
data through backpropagation.

------------------------------------------------------------------------------------------------------
###     Why does CNN use small filters instead of analyzing the entire image at once?
✅ Expected Answer

Small filters reduce the number of parameters, preserve local patterns, and make learning much more
efficient while still allowing the network to recognize complex objects through multiple layers.

------------------------------------------------------------------------------------------------------
###     What is Pooling?
Definition

Pooling is a downsampling operation that reduces the size of the feature map while preserving the most important information.

In simple words:

Pooling = Compressing the Feature Map

------------------------------------------------------------------------------------------------------
###     Max vs Average Pooling

| Max Pooling                  | Average Pooling                              |
|------------------------------|----------------------------------------------|
| Takes maximum value          | Takes average value                          |
| Preserves strongest features | Produces smoother representation             |
| Most commonly used           | Less common in modern CNNs                   |
| Better for feature detection | Better when overall information is preferred |

------------------------------------------------------------------------------------------------------
###     Advantages of Pooling

Pooling provides several benefits:

✅ 1. Reduces image size:-   Smaller feature maps mean faster processing.

✅ 2. Reduces computation:-  Fewer values mean fewer calculations.

✅ 3. Reduces overfitting:-  The model has fewer parameters to learn and is less likely to memorize training data.

✅ 4. Preserves important features:- Especially with Max Pooling, strong activations are retained.

✅ 5. Faster training:-  Smaller inputs make training more efficient.

------------------------------------------------------------------------------------------------------
###     

Input Image
      │
      ▼
Convolution
      │
      ▼
Feature Map
      │
      ▼
Pooling
      │
      ▼
Smaller Feature Map
      │
      ▼
Fully Connected Layer
      │
      ▼
Prediction

------------------------------------------------------------------------------------------------------
###     What is Pooling?
✅ Expected Answer

Pooling is a downsampling operation that reduces the size of a feature map while preserving 
important features. It helps decrease computation and improve efficiency.

------------------------------------------------------------------------------------------------------
###     Why is Pooling used?
✅ Expected Answer

Pooling reduces the spatial dimensions of feature maps, lowers computational cost, reduces overfitting,
and preserves important features.

-------------------------------------------------------------------------------------------------------
###     What is Max Pooling?
✅ Expected Answer

Max Pooling divides the feature map into small regions and selects the maximum value from each region.

-------------------------------------------------------------------------------------------------------
###     What is Average Pooling?
✅ Expected Answer

Average Pooling divides the feature map into small regions and replaces each region with its average
value.

------------------------------------------------------------------------------------------------------
###     Which pooling method is more commonly used?
✅ Expected Answer

Max Pooling is more commonly used because it preserves the strongest and most informative features.

------------------------------------------------------------------------------------------------------
###     Does Pooling have any trainable parameters?
✅ Expected Answer

No. Pooling is a fixed mathematical operation and does not learn any weights or biases.

------------------------------------------------------------------------------------------------------- 
### Which pooling technique is used most frequently in CNNs?
✅ Expected Answer

Max Pooling is the most commonly used because it preserves the strongest activations.

-------------------------------------------------------------------------------------------------------

### Can CNN work without Pooling?
✅ Expected Answer

Yes. Some modern CNN architectures replace pooling with strided convolutions,
but pooling remains a common and useful technique.

------------------------------------------------------------------------------------------------------
### What happens if we don't use Pooling?
✅ Expected Answer

The feature maps remain large, leading to higher computation, increased memory usage, slower training,
and a greater risk of overfitting.

-------------------------------------------------------------------------------------------------------
### Does Pooling detect edges?
✅ Expected Answer

No. Convolution detects edges and patterns. Pooling only reduces the size of the feature maps 
while preserving important information.

------------------------------------------------------------------------------------------------------
Image
   │
   ▼
Convolution ✅
   │
   ▼
Feature Map ✅
   │
   ▼
Pooling ✅
   │
   ▼
❓ Fully Connected Layer ← Today
   │
   ▼
Prediction
------------------------------------------------------------------------------------------------------
###     What is a Fully Connected Layer?

A Fully Connected Layer (also called a Dense Layer) connects every neuron from the previous layer to
every neuron in the current layer and uses the extracted features to make the final prediction.

In simple words:

Convolution finds features.

Pooling reduces the data.

Fully Connected Layer makes the final decision.

-----------------------------------------------------------------------------------------------------
###     What is Flattening?

Flattening converts a multi-dimensional feature map into a one-dimensional vector so it can be 
processed by the Fully Connected Layer.

-----------------------------------------------------------------------------------------------------
###     What Does the Dense Layer Learn?

The Dense Layer learns combinations such as:

If ears + whiskers + eyes are present → likely Cat.
If floppy ears + long snout → likely Dog.

It combines the extracted features to make the final prediction.

-----------------------------------------------------------------------------------------------------
###     What is Softmax?

Softmax converts raw output scores into probabilities whose total equals 100% (or 1.0)

-----------------------------------------------------------------------------------------------------
###     Complete CNN Workflow

Image

↓

Convolution

↓

Feature Map

↓

Pooling

↓

Smaller Feature Map

↓

Flatten

↓

Fully Connected Layer

↓

Softmax

↓

Prediction

-----------------------------------------------------------------------------------------------------
###     CNN End-to-End

Let's summarize the role of each stage.

| Layer                 | Job                                                                |
|-----------------------|--------------------------------------------------------------------|
| Convolution           | Detect features such as edges, textures, shapes                    |
| Pooling               | Reduce the feature map size while preserving important information |
| Flatten               | Convert the feature map into a 1D vector                           |
| Fully Connected Layer | Combine learned features and make a decision                       |
| Softmax               | Convert scores into probabilities                                  |

-----------------------------------------------------------------------------------------------------
###     What is the purpose of a Fully Connected Layer?
✅ Expected Answer

The Fully Connected Layer combines the features extracted by previous CNN layers and uses them to
make the final classification or prediction.

-------------------------------------------------------------------------------------------------------
###     Why is Flattening required?
✅ Expected Answer

Flattening converts the multi-dimensional feature maps into a one-dimensional vector because
Dense Layers accept 1D input.

------------------------------------------------------------------------------------------------------
###     What is Softmax?
✅ Expected Answer

Softmax is an activation function that converts raw output scores into probabilities whose
sum equals 1 (or 100%).

------------------------------------------------------------------------------------------------------
###     Which layer actually makes the final prediction?
✅ Expected Answer

The Fully Connected Layer produces the classification scores, and Softmax converts those scores 
into probabilities for the final prediction.

------------------------------------------------------------------------------------------------------
###     Can CNN work without a Fully Connected Layer?
✅ Expected Answer

Yes. Some modern CNN architectures replace traditional Fully Connected Layers with alternatives like
Global Average Pooling for improved efficiency.
However, understanding the Fully Connected Layer is essential because it explains how many classic
CNNs perform classification.

-------------------------------------------------------------------------------------------------------
###     Why do we need a Fully Connected Layer if Convolution has already extracted the features?

Convolution extracts useful features from the image, but it does not perform the final classification.
The Fully Connected Layer combines all the extracted features and makes the final prediction.

---------------------------------------------------------------------------------------------------------
###     What is Flattening?

Flattening converts a multi-dimensional feature map into a one-dimensional vector so that 
it can be processed by the Fully Connected Layer.

--------------------------------------------------------------------------------------------------------
###     What is Softmax?

Softmax function changes raw input score into probability.

--------------------------------------------------------------------------------------------------------
###     CNN workflow

Convolution

↓

Pooling

↓

Flatten

↓

Fully Connected Layer

↓

Softmax

↓

Prediction

-------------------------------------------------------------------------------------------------------
Image

↓

Convolution

↓

Feature Map

↓

Pooling

↓

Smaller Feature Map

↓

Flatten

↓

Fully Connected Layer

↓

Softmax

↓

Prediction

-   A CNN starts by taking an input image.
-   The Convolution Layer applies filters to detect important features such as edges, textures, and shapes,
producing feature maps. 
-   Pooling then reduces the size of these feature maps while preserving the most useful information. 
-   The reduced feature maps are flattened into a one-dimensional vector, which is passed to the Fully Connected Layer. 
-   The Fully Connected Layer combines all the extracted features and generates classification scores.
-   Finally, the Softmax function converts these scores into probabilities, and the class with the 
highest probability becomes the final prediction.

-------------------------------------------------------------------------------------------------------