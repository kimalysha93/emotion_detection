#  Course Project: AI-based Emotion Detection Web App

## By: Alysha Kim

Last Updated: March 2025

## Introduction
This Project was completed as part of the [IBM Full Stack Software Developer Professional Certificate: IBM Developing AI Applications Using Python and Flask](https://www.coursera.org/account/accomplishments/professional-cert/Z511W9DZQBE2) course by coursera


## About the Project
- Starting project code is forked from [here](https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai)

## Using the Emotion Predict function of the Watson NLP Library:

```js
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
```
