# HolmesAssistant
Is an Agent that will help you during your carrer path. It will be able to understand your skills and profile, look up for desired jobs acrross jobs portal, find a match, recommend jobs and guide you through the best skills you should learn

# Key features
## 1. WebScrapper 
Will allow us to fetch data from different web pages. This aim to provide a dinamyc tool to get different jobs information
## 2. LLM Model
Large Language Model that will be used in our Chains and Agents. We'll use opensource models such as `llama2` or `mistral` .
## 3. VectorDB to store jobs
We need to store and access information with friendly format. This is why we'll use vectordb such as Chroma or Postgres Vector db
## 4. Chain/Agent to process job offers and store structured data
We'll implement LCEL Langchain common expresion language. Some Distpatcher chain and output parsers
## 5. Chain/Agent to Match your profile with stored jobs
We need to match existing information about job oppenings and user profile. This can be done easily with some chain approach or enhanced with some advaced ML model.
## 6. We'll use simple auth + langserve deployed in aws ec2 + docker
We are interested in people using the solution, that's why we are going to deploy in some easy to access cloud environment 

## Deployment
- We'll use "local" running model powered by `ollama`, using `llama2` model.
- Deploy monitoring (TBD)

#Iterations & Next steps
## First Iteration: 
1. We'll mock scrapping data and use json files to store structured information about the job positions 
2. We use ollama + llama2 to run models
3. We won't use vectordb to store jobs
4. We'll use simple chain to extract ("You will", "You have"). Where "You will" refers taks to do within the position, "You have" referes to skills needed. And output in simple formated json "output_json. 
5. We'll use a simple chain to match profile mocked in "user_profile" with "output_json" using some simple matching approach
6. We'll use langserve to deploy locally


# Second Iteration:
3. We'll use vectordb such as local chroma or (add other option). And implement ETL (including embeddings) process to upload json contents into vector db. Embed and store users information
4. We'll implement agents + Use the vectordb data
5. We'll implement agents + Use the vectordb data


# Third Iteration:
5. Implement some ML matching model as tool for the Agent
6. Deploy in Cloud

# Fourth Iteration:
1. Implement web scrapping for 3 different web pages
3. Embed and store incoming data
