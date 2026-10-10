# Machine Learning

My hands-on machine learning work so far has been one AWS re/Start lab: training an XGBoost model in Amazon SageMaker.

That is a small start, so this page focuses on what I actually did rather than listing every ML service covered in the course as if I had used them all.

## Training an XGBoost Model

I used training and validation data stored in Amazon S3 and configured a SageMaker XGBoost training job. SageMaker ran the job, and the final resource status was **Completed**.

The exercise gave me practical exposure to the path from data stored in S3 to a model-training job running in SageMaker. It also helped connect the algorithm being used—XGBoost—with the AWS services providing the data and compute environment.

A completed training job tells me the training process ran to completion. By itself, it does not tell me how well the model performs; that depends on evaluating its results against appropriate data and metrics.

## Concepts Connected to the Lab

- **Training and validation data:** the model-training workflow uses separate data for fitting the model and checking it during development.
- **XGBoost:** a gradient-boosted decision-tree algorithm used for supervised learning.
- **Amazon S3:** the storage location for the data used by the training job.
- **Amazon SageMaker:** the managed environment used to run the training job.

## What I Want to Practise Next

My next step is to build more ML experience beyond this one training exercise. I want to work through the process more independently in Python, evaluate model performance, experiment with model settings, and then build another end-to-end workflow in AWS.

As I complete those exercises, I'll add the code, results, and lessons learned here. For now, this page records one completed training lab—not a claim of broad hands-on experience across AWS machine learning services.
