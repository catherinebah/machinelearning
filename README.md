# CEFR French Level Predictor

Estimating the difficulty level of French texts.
Given a text in French, we trained models to predict its difficulty level (A1, A2, B1, B2, C1, C2).

This research has been done in the framework of <a href="https://www.kaggle.com/competitions/estimating-the-difficulty-level-of-french-texts">that page</a>.

# Motivation

There is a global learning crisis which worsens inequalities between people with different means and infrastructure for education. COVID-19 has accentuated those disparities. This is of crucial importance and education is a lifeline for children, and generally people in crises.

In the context of our research, learning a language can be the first step towards opening doors to new opportunities for people who have the drive, motivation and will to create value in society, but not enough language skills to be able to communicate with different stakeholders located in the area of opportunity. 

Extensive reading is very important to learn a new language faster and more efficiently. 
In this project, we try to develop extensive reading into a better-tailored experience for language learners. 

# Current landscape and available solutions

<a href="https://www.researchgate.net/profile/Kensuke-Takii/publication/350994330_An_English_Picture-book_Recommender_System_for_Extensive_Reading_Using_Vocabulary_Knowledge_Map/links/607f5c208ea909241e121185/An-English-Picture-book-Recommender-System-for-Extensive-Reading-Using-Vocabulary-Knowledge-Map.pdf"> In that research paper</a>, a recommender system was developed with a focus on catering to users' English proficiency levels. The system's objective is to suggest text-image books specifically designed for Japanese learners, taking into account their individual language abilities.
Or, <a href="https://link.springer.com/article/10.1007/s40593-020-00201-7"> In that other paper</a>, they explore the application of NLP and hierarchical machine learning techniques for classifying text difficulty levels. The study investigates methods to effectively analyze and categorize the complexity of textual content.

Recognizing the significance of extensive reading for accelerated and efficient language learning, our project aims to enhance the tailored experience for language learners. We seek to predict levels of French texts/sentences into CEFR levels.

In terms of soltuions accessible online, we have not found a free source for french text classification, but we found two websites which classify english text by CEFR levels :

http://www.roadtogrammar.com/textanalysis/
https://hub.cathoven.com/?scene=analyser&core=cefr

Even among both of those websites, they frequently fail to return the same predicted CEFR level for the same phrase.

# Data

We encountered a challenge to find CEFR levelled reading sentences. The majority of these sentences are not accessible for free, making it difficult to gather a substantial amount of data. However, we managed to locate some sample sentences that were available without charge and we had the one on kaggle given as well. Initially, this collection was relatively small in size. To expand our dataset and obtain more data points, we employed the assistance of existing CEFR levelling tools to label additional texts.

In the end, our collective efforts resulted in a final dataset comprising 10,000 lines. Within this dataset, we have gathered 1,500 example texts that span across the six CEFR levels. These texts encompass a diverse range of formats, including dialogues, stories, articles, and various other text types. 

The dataset was then split into 80% training and 20% test.

# Training
## Hyper-parameter optimization to find the best solution for each model

Without doing any cleaning on the data we have search for the best parameters for each models and calculated the precision, recall, f1-score and accuracy.
Our results are in that table:
`table with results`

You can find the confusion matrixes for each model thanks to the codes in this GitHub repository.
The best model so far is the `best-model`.
