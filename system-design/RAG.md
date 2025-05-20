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
consistent structure for next steps (break into chunks + metadata, embeding). So in this step, we need to choose the
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

### Step 2: Break the raw data into meaningful chunks

After raw data loaded, it need to break into small chunks. In this step, we need to think what is the best chunk
strategy for this application:

1. what is the best chunk size? (100 words, 1000 words?)
2. Semantic Boundaries: sentenced based or paragraphn based?
3. Use Overlap to preserve context (eg:sliding window)
4. Attach metadat to each trunk to support filter retrieval

### Step 3: Create vector representation of chunks for embedding

After the chunks of raw data created, it need to transform to vector format. then it can be used to calculate similarity
or relevance easily. In this step, the things need to take care are:

1. Model choice: choose the state-of-the-art embedding models which matches your domain
2. Keep embedding model versioning for consistency and reprocessing
3. Avoid embedding sensitive/PII data without encryption or masking.

Reminder: It's best to test several models with your real context + questions before finalizing your choice.

### Step 4: Choose the right vector store for embedding saving and efficient retrieval

The embeding creted, it need to saved into storage for futue use. Vector store is

### Step 5:

5. Vector Store

6. Retrieval

7. Filtering and Reranking

8. Prompt Augmentation

9. Generatoon

## The tools in Databricks support RAG

## Summary
