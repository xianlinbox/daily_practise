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

The embeding created, it need to saved into storage for futue use. Vector store is for this scenario. In this step, pick
the right vector store to balance cost/requirements is key point.

- Capabilities:

* Similarity Search
* Support Hybrid Search
* Index Updating
* Meta filtering
* Toolchain supported
* Self host or Cloud
* Multi-tenancy
* Security
* Scalability
* Persistence
* ...

Some benchmarks can be used for vector store choosing:

- ingest throghput
- query latency
- Precision/Recall of results
- Metadata filtering performance
- Query cost and memory use per query

### Step 5: Retrieval the context data based on question

All the embeded context data are landed in the vector store. The next process is find the most relevance chunk based on
questions, in this step:

1. Use the same embedding model (and version) for both indexing and querying.
2. Match the distance metric to the embedding model(eg:Cosine similarity, Euclidean/L2, Dot product)
3. If needed, apply metadata filtering to narrow down the search space and improve relevance.
4. Adjust top-K result to balance recall, performance and precision
5. If needed, Combine vector similarity with keyword-based search
6. Log metrics for adaptive reranking, active learning, and performance tuning
7. Apply strict namespace, user-level access control, or document filtering to avoid data leakage
8. If needed, use Post-Retrieval Reranking to improve relevance

### Step 6: Use retrieval context to augment prompt

The questions and context data is ready, The next move is combie them together and send it to LLM. In this step:

1. Design clear, repeatable templates that separate query, instructions, and context.
2. Embed structured metadata (source, date, type, confidence) to help the LLM with disambiguation or prioritization.
3. Guide the model’s tone, reasoning, and output formatting.
4. If your domain is narrow or technical, augment the prompt with a few examples
5. Use modern frameworks to simply prompt augmentation. eg: LangChain / LlamaIndex: Use PromptTemplate and custom
   context builders.

### Step 7: Generation the result

Got the result. User can assess and verify if the RAG application give an accurate answer.

### Step 8: Evaluating RAG Pipeline

To ensure that the system delivers accurate, relevant, and useful responses, The system need to evaluate mechanism to
check. The following method are provided:

- Ground truth comparison: Use curated test sets with gold answers.
- Automatic metric (BLEU, BERTScore)
- Faithfulness checker (RAGAS, GPT judge)
- Human rating: Capture user feedback and flag low-confidence or failed answers.

The evaluation result will feedback to RAG application to tuning on different stage of the workflow.

## An example RAG application in Databricks platform

## Summary

Building a robust RAG (Retrieval-Augmented Generation) application requires thoughtful integration of information
retrieval and generation techniques. From selecting the right embedding model and vector store to structuring context
chunks, embedding metadata, and designing effective prompt augmentation strategies, each step plays a crucial role in
delivering accurate, context-aware responses. Evaluation methods—both automated and human-in-the-loop—ensure that the
system continuously improves in relevance and reliability. Ultimately, a well-designed RAG system not only enhances the
performance of LLMs but also provides users with trustworthy, up-to-date answers grounded in real data—making it a
powerful solution for enterprise AI applications.
