# Things you need to know about RAG

## What is RAG

Before talking RAG, Let's talk about how do LLM learn knowledges to give user accurate answers. There are 3 approaches:

1. Training a LLM from scratch: this need a huge datasets. trillions of tokens and a lot of money
2. Fine Tuning a pre-trained model: adapting a pre-trained model with specific domain data sets. this need a lot of
   domain specific examples.
3. Passing contextual information: combine LLM with external info retrieval.

RAG is a common way to implement the third approach. RAG stands for Retrieval-Augmented Generation — a technique in
AI/LLM systems that enhances LLM by letting them retrieve relevant information from external sources before generating
an answer

## The typical workflow of an RAG application

The rough concept of an RAG application is simple: Find the **most related context** and send it with questions to LLM,
then LLM can return the most accurate answer. To achieve this target, a typical workflow will be:

### Step 1: Prepare the raw context data

In RAG, the raw context data user have can be in many formats, like emails, csv, txt etc. but it must be converted to a
consistent structure for next steps (split into chunks + metadata, embeding). So in this step, we need to choose the
right toolchain (e.g., LangChain, LlamaIndex, Haystack) to load the data into system. And conquer the concerns may
appear in raw data.

| Concern              | Tip                                               |
| -------------------- | ------------------------------------------------- |
| Inconsistent formats | Normalize during preprocessing                    |
| Embedded images      | OCR if necessary (e.g., Tesseract)                |
| HTML tags/noise      | Clean with `BeautifulSoup` or `html2text`         |
| Multilingual data    | Store language as metadata                        |
| Temporal context     | Include timestamps if it affects answer relevance |
| Duplicate content    | Hash + deduplication pipeline                     |

### Step 2: Split the data into chunks

Prepare the raw context data: Split the context data into chunks, Chunk strategy Transform the chunk data to vector
represntation. Embeding model

2. Vector Store

3. Retrieval

4. Filtering and Reranking

5. Prompt Augmentation

6. Generatoon

## The tools in Databricks support RAG

## Summary
