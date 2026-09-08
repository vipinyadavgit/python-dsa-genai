Classification metrics: Accuracy, precision, recall, f1-score, ROC-AUC

- The choice of evaluation metrics depends on the business problem, cost of error (False positive, False negative), 
    class imbalance (Output variable: true: 150, false:50)
- There is no "best" metrics universally

Confusion metrics: True positive (TP), True Negative (TN), False Positive (FP), False Negative (FN)

1. TP: Actual positive and predicted positive
2. TN: Actual NEGATIVE and predicted NEGATIVE
3. FP: Actual NEGATIVE and predicted POSITIVE  (false alarm)
4. FN: Actual POSITIVE and predicted NEGATIVE  (Missed detection)

1. Accuracy: Out of all predictions made, how many were correct?
	When to use:
		a. When classes are balanced.
		b. Cost of FP & FN are almost same. 
	E.g.: 
		a. Cat vs dog classification
		b. hand written digits classification
	When not to use:
		a. We have 1000 patients, 990 healthy, 10 diabetes (Actual: 99% patients are healthy). Model predicts-everyone is healthy.  

2. Precision: Out of all predictions made as positive, how many were actually positive. 
This means: Can i trust the model when it says the output as "YES"?
	E.g.: Model predicted 100 fraud transactions. actually only 80 were fraud.
		Precsision = 80%,. 20 were false alarm
When precision matters: When False positive are Costly. 
	E.g. Spam detection: Wrongly classifing IMPORTANT mails as SPAM.
	     Medical diagnosis: Unnecasasry treatment to be avoided

3. RECALL(Sensitivity): Out of all the actual positive cases, how many did we detect?
This means: Did we actually catch everyone
	E.g.: 100 diabetic patients, model identified 95. Recall 95%. Missed-5 patients
When recall matters: When missing the positive cases is dangerous
	E.g.: Fraud detection: is we miss detecting fraud, it will a huge financial loss. 
		Fire/Smoke detection

4. F1 score: Sometimes both precision and recall will matter. 
When to use F1: - Both FP & FN are equally important, dataset is imbalanced
	E.g.: Cancer detection, etc.

5. ROC Curve (Receiver operating characteristics):
It plots: True positive (Recall) v/s False positive rate.
If we have threshold of 0.5, we will check for all the area under the curve from 0-1 (0- worst, 0.5- threshold, 1- perfect classfier)
ROC: 0.85: Then model seperates positive and negative classes with 85% accuracy.
When to use:
	a. Compare multiple models
	b. Probability based classifier
	c. Threshold is not fixed.

E.g. Hospital wants AI. 
a. Cancer detection: Missing cancer can be dangerous: RECALL
b. Spam filtering: sending important email to spam: PRECISION
c. Face recognition: Allowing stranger inside hospital: PRECISION
d. Credit card fraud: Need to catch the fraud, but dont want to block genuine users: F1-score











