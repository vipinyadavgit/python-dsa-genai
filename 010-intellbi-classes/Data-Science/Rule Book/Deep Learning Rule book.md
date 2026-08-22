1. Understand the problem statement in detail. On the basis of this, you will able to identify which are the input variables and what is the output variable.
2. Import the libraries
3. Load the dataset
4. EDA (these arent the fixed series of steps to be followed, it can vary, you can change te series of steps depending on the problem statement and dataset)
    a. Basic dataset check:
        i. df.shape - dimension of rows and columns
        ii. df.info() - it will print the information of the dataset i.e. datatypes, column names, number of not null values
        iii. df.describe() - Generate descriptive statistics.
        iv. print df.head() - gives first 5 rows / df.tail() - gives last 5 rows.
    b. Delete all the columns that have all the values in it as unique or all the values in it as same.- 
        because it doesnt add any value in the data science- drop it using df.drop("column name")
    c. Handling null values:
        i. Check if the are null values - df.isnull().sum()
        ii. Ways to handle null values:
                - Delete the rows that have null value using dropna() (When there are small number of missing rows)
                  - Delete columns using df.drop() when there are more than 50% of the values in a particular column as null
                 - If the column has categorical datatype: Impute/Replace with mode
            - if the column has continuous numerical dataype: Impute/replace with mean
            - if the column has discrete numerical dataype: Impute/replace with median
    d. Handling duplicates:
        i. Check the duplicate rows in dataset - df.duplicated().sum()
        ii. Ways to handle duplicate values:
            - Remove duplicate using df.drop_duplicates()
    e. Split the dataset into categorical and numerical columns
        i. cat = df.select_dtypes(include = "object").columns
        ii. num = df.select_dtypes(exclude= "object").columns
    f. Handling error values: Error values can be anything (?, @, etc)
        i. Replace the error value with null using df.replace("?", np.NaN). 
        ii. Once all the errors are converted into Null, apply step c.
    g. Handling Outliers:
        i. Detect outliers using IQR method:
            - Find Q1 = df.quantile(0.25), Q3= df.quantile(0.75)
            - Find IQR =  Q3 - Q1
            - LB = Q1 - 1.5*IQR, UB = Q3 + 1.5*IQR
            - Remove all the values less than LB and greater than UB
    h. Categorical to numerical conversion:
        i. Label encoding: When we have a large number of nominal columns.using sklearn.preprocessing.LabelEncoder()
           Disadv: It can be misleading to algorithms
        ii. .map() -Best when there are only a few categories and you want to manually map the encodings
           Disadv: Not suitable when we have many categories in the dataset
        iii. Ordinal encoding: When categories have natural order of ranking
           Disadv: it has be done manually
        iv. One hot encoding: Each category becomes a seperate column
    i. Univariate analysis (analysis done on single variable)and bivariate analysis (analysis done on 2 variables)
        i. Univariate- Plot histogram of every/major columns, Check for the unique values in each column
        ii. Bivariate - Sales vs (TV, Radio, Newspaper), correlation analysis, pair plot analyis
   
   ###	5. DL model building:
       a. Dividing the data into X,y
       b. Dividing the data into train-test-split
       c. Create validation set (1000 samples: 700 (Training), 150 (Validation), Testing (150))
       d. Forward propogation: Moving from i/p -> Hidden layer -> Predicted o/p
           i. Mention the activation function (ReLU, Sigmoid, TanH, Softmax, Linear)
       e. Loss function: Compare the predicted o/p vs actual o/p. 
           i. Binary cross entropy ( Binary classification)
           ii. Categorical cross entropy (Multi class classification)
           iii. MSE (for continous numerical value)
       f. Build the deep learning model
           - Using model.add(Dense(<number of neurons>, activation= <function>)
           - Dense: It creates a fully connected layers of neurons
       g. Choose the output layer correctly:
           - Binary classification : Dense(1, sigmoid), Loss function:  Binary cross entropy 
           - Multiclass classification: Dense(<number of classes>, softmax), Loss function:  Categorical cross entropy
           - Regression: Dense(1, linear), Loss function: MSE
       h. Compile the model:
           - model.compile(optimizer + loss function + metrics)
       i. Optimizer (they decide how your model weights are updated): Adam, SGD, Adagrad, RMSProp
           - Decide the learning rate (how large step the optimizer can take when updating weights)
           - optimizer = <Name of optimizer> (learning rate = <rate>)
       j. Backward propogation  (learning from the mistake to minimize the loss function)
           a. Calculate the gradient using learning rate
           b. Choose the optimizers (Stochastic Gradient Descent, Adam, RMSProp, Adagrad)
           c. Update the weights
       k. Train the model
           - history = model.fit(X_train, y_train, 
                       validation_split=0.2,  ## Use 20% of training data for validation
                         epochs=100,  ## Train for 100 epochs
                           batch_size=32,  ## Batch size of 32
                           callbacks=[early_stopping],  ## Use early stopping callback
                           verbose=1  ## Show progress bar
                         )
           - Epoch: how many times model will see the data, if epoch is 50-> model will see the data 50 times and learn from the dataset
           - batch_size : (16,32,64,128): if the batch size is 32, model will process approx 32 records at a time before performing the 
                   parameter update. This is chosen based on Dataset size, GPU/CPU memory)
       l. Plot the training history: to understand the patterns learnt -> if overfitting happens or not
               - Training loss (reducing), validation loss (reducing) -> Good
               - Training loss (reducing drasctically), validation loss (growing)-> overfitting (model is learning the training data too 
                                                       fast without understanding the patterns in it)
               - Training performance(poor), validation performance(poor)-> undertiffing
       m. In case of Overfitting: Perform Dropout
               - from tensorflow.keras.layers import Dropout
               - model.add(Dropout(0.3)) -> this will randomly disables a fractional of activations during the training.
       n. Early stopping: instead of blindly training for max epoch, we can stop in between if the model validation loss is not improving	
               -  from tensorflow.keras.callbacks import EarlyStopping
               - early_stopping = EarlyStopping(monitor = "val_loss", patience= 5, restore_best_weights = True)
       o. model checkpoint (to save the best model during the training)
               -  from tensorflow.keras.callbacks import ModelCheckpoint
               - checkpoint = ModelCheckpoint("best_model.keras", monitor = "val_loss", save_best_only= True)
   -------- Model development is complete -------- 
6. Final model evalaution:
	a. model.evalate(X_test, y_test)
	b. Make predictions:
		- y_pred = model.predict(X_test)
	c. Import metrics:
		- Classification: accuracy_score, precision_score, recall_score, f1_score, roc_auc
		- Regression: MAE, MSE, RMSE
7. Model summary: used to inspect the model architecture which we built
	- model.summary()
		- this tells you: layer, output shape, number of para, trainable para
8. Save the model, preproccessing object
-------- Deep learning  is complete -------- 
9. Hyperparameter tuning: 
	- Once the baseline model works, tune:
		- No. of layers
		- No. of neurons
		- Learning rate
		- Batch size
		- Epochs
		- Dropout
-------- Deep learning  is complete -------- 
9. If it is asked to predict on new dataset: Inference
	- New data -> same saved preprocessing -> same feature order -> model -> predict the output















