# Domain 1: Foundation Model selection, Data Management and Compliance

## Task 1:

Select appropriate FMs that align with business needs and technical constraints.

Develop technical prototypes using Amazon Bedrock.

Create standardized technical components.

Apply AWS Well-Architected Framework principles to GenAI solutions.

## Task 2

Assess and select FMs based on performance, capabilities, and limitations.

Create flexible architectures that enable dynamic model selection and provider switching.

Design resilient AI systems that maintain operation during potential service disruptions.

## Task 3

Create comprehensive data validation workflows for FM consumption.

Develop data processing workflows to handle complex, multimodal data types.

Format input data correctly for various FM interfaces and requirements.

Enhance input data to improve FM response quality and consistency.

## Task 4: enhance FMs using vector database solutions. Key steps involve creating knowledge bases, building metadata frameworks, connecting data sources, and setting up systems for deployment and maintenance.

## Task 5: design retrieval methods for enhancing FMs. This means creating document segmentation, implementing embeddings, configuring vector and semantic searches, managing queries, and setting up access to call interfaces for vector stores.

## Task 6: implement effective prompt engineering strategies and governance for FM interactions.

# Products

## Bedrock

a fully managed service that offers a choice of high-performing Foundation Models. focus on supporting Application
Developers who want to integrate AI.

### Functionalities

Single API Access

Knowledge Base(RAG)

Agents

Guardrails support multimodal toxicity detection for images

#### Model Evaluation:

1. Automatic Way

- Create new evaluation under under "Assessment & deployment" in Amazon Bedrock Console.
- Choose Automatic Evaluation type and Select the corresponding Task type (General Text, Text Classification etc)
- Select the models and built-in metrics (Accuracy, Robustness, Toxicity) or Custom Metric (LLM-as-a-Judge).
- Select the Dataset (built-in or upload your own one)
- Run and Analysis, sepecify the bucket for the outputs, Bedrock generates a Report Card showing comparisons

2. Manual Way

#### Model Customization

### Patterns

The "Converse API" Pattern (The Modern Standard)

Reliability Pattern: Cross-Region Inference

Cost Pattern: Batch Inference

"System Prompt" Placement Pattern

Access Pattern: On-Demand vs. Provisioned Throughput

Safety Pattern: Guardrails Integration

Streaming Pattern (User Experience)

### SageMaker AI

Offers complementary capabilities for custom model development and deployment. Focusing on supporting developers and
data scientists full control to build, train, and deploy their own machine learning models (both traditional ML and
Generative AI).

### Kendra

enhances the Amazon Bedrock retrieval-augmented generation capabilities with enterprise search functionality.

### Prompt Skills

1. Zero-shot
2. Few shots
3. Chain of thoughts
4. Self-consistency: prompts the model to sample a variety of reasoning paths. Then, the model aggregates the final
   answer based on multiple data points from the various paths.
5. Tree of thoughts
6. Automatic Reasoning and Tool-use (ART): a prompting technique that builds on the chain-of-thought process.
   deconstructs complex tasks by helping you select demonstrations of multiple, or few-shot, examples from the task
   library
7. ReAct: generate both reasoning traces and task-specific actions that are based on external tools, such as Wikipedia
   pages or SQL databases. This external context leads to more accurate and reliable output.

# Vector Store

## Data Sources Integration

1. public documentation: using crawler to extract content, metadata and store them in the pipeline
2. Internal Wiki Systems (confluence. MediaWiki): using API integration for data, and using webhook for update
   notification
3. Document Manage system(sharepoint, google doc):

- change detection
- incremental update

## Service Selection

1. Knowledge Bases: the service that manages the RAG workflow. You must choose a storage backend for it.

2. OpenSearch(Serverless): The "Default" & Most Flexible Choice. it support hybrid search (combine semantic search with
   keyword matching). highly scalable and customizable.
3. Kendra:, not just a vector story, is a fully Retriever service. make you enterprise data searchable with zero setup.
   not customizable.
4. Aurora (PostgreSQL with pgvector): If your business data already lives in Postgres (e.g., User tables, Product
   tables), keeping the vectors in the same DB allows you to perform complex SQL joins along with vector search. make
   your db simpler.
5. Amazon DynamoDB: not a vector store, didn't support by knowledge base as a backend. used for session, history or
   metadata.

Chunking

1. mprove answer quality by giving the model more surrounding context. Hierarchical Chunking (Parent/Child).
2. Search only specific sets of documents (e.g., "Only search Engineering docs"). Metadata Filtering.
3. Parse specific file structures (e.g., Split strictly by HTML <div> tags). Custom Chunking (Lambda).

## Cross Region inference

1. implmented by change modelId to inference profile, not just a turn switch on.
2. Cross-region inference respects geographic boundaries
3. Pricing (No Extra Cost). Pay as usual
4. No Provisioned Throughput/ No route customization/
5. Request access to the model in ALL regions that the profile might use
6. Your IAM role needs permission to invoke the Inference Profile ARN, not just the base model ARN.

# Nova Family

Micro -> Lite -> Pro -> Premier -> Canvas -> Reel -> Sonic

# Agent vs AgentCore

Agent: an "out-of-the-box" solution where you simply configure the API schema and the Knowledge Base, and AWS handles
the orchestration logic

how it works:

- define "Action Groups" (OpenAPI schemas) and select a Foundation Model. Bedrock automatically generates the prompt
  engineering and manages the ReAct (Reason + Act) loop.

good for:

- Standard enterprise tasks
- Developers who do not want to write complex state management code
- Integration with Bedrock Knowledge Bases.

AgentCore: an Infrastructure Platform (PaaS). It is a dedicated serverless runtime designed to host and scale custom
agents built with code-first frameworks (like LangGraph, CrewAI, or AutoGen).

how it works:

- write your agent logic in Python using any framework (LangChain, LangGraph, CrewAI, Strands) and deploy it to the
  AgentCore Runtime.

good for:

- Multi-Agent Systems
- Long-Running Tasks
- Open Source Frameworks

# AWS strands vs Agent Squad vs promt flow vs step functions

- Step functions is an app orchestration
- Strands is a framework for develop an agent easier and deeper with code. LLM decide how to run the tasks
- promt flow: no code canvas, used for chain prompt, the execution loop is fixed by developer.
- Agent Squad is used for orchestrate multi-agents

# Foundation Model Deployment

Challenges:

- Sagemaker AI allowing more time to download and load big models and associated resources.
- SageMaker AI supports third-party model parallelization libraries, with FasterTransformer and DeepSpeed to handle
  large model deployments, provided they are compatible with SageMaker AI.
- ultra servers help worklaod which requiring significant processing power
- difference instance provide different optimized resource(cpu, memory)

Approaches:

1. Single Model enpoint: 1 Endpoint → →1 Container →→ One Model
2. Multi model endpoint: 1 Endpoint → →1 Container →→ Many Model Artifacts (in S3).
3. Multi container endpoint: 1 Endpoint → → Up to 15 Different Containers.
4. Serial inference Pipeline: Endpoint → → Container A (Pre-process) → → Container B (Model) → → Container C
   (Post-process).
5. Amazon Bedrock Custom Model Import allows add models trained in SageMaker AI to bedrock

Scaling polices:

1. Target Tracking Scaling (InvocationsPerInstance at 70.)
2. Step Scaling (If traffic > 100, add 5 instances (panic mode))
3. Scheduled Scaling (Every Friday at 6:00 PM, set MinInstances = 1.")
4. Scaling for Asynchronous Inference,(If Queue > 5, add instances.)
5. don't forgot the Cool Down Period

## Access to FM

1. Amazon Bedrock

- Access AWS/Partner Owned Models, can't check model weights
- Severless, managed by AWS
- Pay by token or provision throughput
- less custimization

good for:

- speed to market
- virable traffic
- roprietary Models

2. SageMaker AI endpoints

- Deploy your own custom model or an open-source model (Llama, Mistral) from SageMaker JumpStart. You have full control
  over weights and code. but you can't use Proprietary Models here.
- instanced based. user chose the instance to run the model
- pay by compute hours
- Full control on the model

good for:

- Custom Models
- Data Privacy/Security
- Full Control

# Token Efficiency

1. Token estimation and tracking: Pre-Flight Estimation/Post-Flight Tracking/Monitoring
2. context window optimization: Use System Prompts, document structure, placement matters
3. prompt compression: Summarization Chain (small to summary then to expensive), Few-Shot Optimization(few high),
   Representation(Use dense formats)
4. Context pruning: reranker(send the most relevant one),meta-filter( filter the exact wrong one)
5. response size controls: max_tokens & using stop sequence
6. Response Limiting (Architectural): using streaming with guardrail, when trigger, stop the generation

# The Cache mechanism in GenAI

1. Deterministic Request Hashing (Exact Match): compare hash
2. Semantic Match: compare embeddings
3. Prompt Caching (Input Processing Cache): caches the processing of the input, like the same context your provide in
   request
4. Result Fingerprinting (Cache Validation): use Prompt + Model_Version + Temperature + RAG_Data_Snapshot_ID as key to
   avoid wrong cache.
5. Edge Caching (Latency Reduction): same as the traditional one

# Chunking Strategy

1. hierarchy chunking: good for complex docs
2. semantic chunking: good for Q&A, FAQ
3. fixed size chunking: logs/feeds

# OpenSearch performance enhancement

1. Query Expansion Techniques

- Dictionary-Based Expansion (Synonyms)
- Neural Sparse Retrieval
- More Like This

2. Scoring Functions: Relevance Score for the search result
3. Combining Lexical Search (Keywords) with Vector Search (Neural)

# Incoporate FM capabilities into existing enterprice env

1. identity federation between FM services and enterprise systems
2. cross-environment AI solutions, secure routing between cloud and on-premises resources

# Async or Batch Invoke

1. StartAsyncInvoke only available for Reel
2. For other models, use CreateModelInvocationJob

# Guardrail policy

1. content filter: 6 categories: Hate, Insults, Sexual, Violence, Misconduct (criminal activity), and Prompt Attack
2. Denied Topics. like financial advice
3. Word Filters: like competitor names
4. Sensitive Information Filters (PII): Regex, build-in
5. Contextual Grounding Checks: avoid Hallucinations

# system Model evaluation framework

1. Dimensions:

- Accuracy / Quality: Bedrock Automatic Evaluation
- RAG Effectiveness: Knowledge Base Evaluation
- Safety & Security: Guardrails for Bedrock
- Performance: CloudWatch / Bedrock Metrics
- Robustness: Bedrock Automatic Evaluation

2. The Evaluation Pipeline

- Unit Testing (pytest + Amazon Bedrock):Syntax Check, keyword match, Safety Check
- Automatic System Evaluation (The "Judge"): The Judge model scores it (1–5) on "Coherence" and "Faithfulness" compared
  to the Golden Answer.
- Human Evaluation (The Gold Standard)

3. Implementation Guide (Step-by-Step)

- step 1: Create a dedicated S3 bucket structure for evaluation artifacts.
- step 2: Define the "Judge" Prompt (LLM-as-a-Judge)
- step 3: Run the Evaluation
- step 4: Continuous Improvement Loop

# SageMaker Goverance & Compliance

1. Lineage Tracking: track data used by which job, job created which model, model is used by which endpoints.
2. Cross-account lineage tracking: using the SageMaker AddAssociation API with appropriate IAM roles and permissions
3. Model Cards: A centralized doc to record what model is and how the model should be used (the business and ethical
   context)

# Responsible AI framework

1. Transparency Module

- Chain of thoughts
- Knowledge base with source attribution
- Agent tracing

2. Fairness module

- fairness metrics
- LLM as a judge
- Prompt Flows to test different prompts

3. Compliance Modudle

- Guardrails
- Model Cards
- Lambda Check

4. monitoring and dashboard. with cloud watch

# Obeseration framework for GenAI Application

1.

# Popular validation dataset

1. WikiText2 / WikiText103:Primarily used for language modeling and text generation.
2. RealToxicityPrompts: evaluate the toxicity of language generated by large language models
3. Bias in Open-Ended Language Generation Dataset(BOLD): audit various types of biases in LLM
4. TREx (TRIPLE Evaluation eXchange): knowledge base population, knowledge graph completion, relation extraction, and
   entity linking
5. SQuAD (Stanford Question Answering Dataset): question answering
6. GLUE (General Language Understanding Evaluation) / SuperGLUE Benchmarks: Comprehensive evaluation of general language
   understanding models.
7. IMDb Reviews / SST-2 (Stanford Sentiment Treebank): Sentiment analysis
8. CoNLL-2003: Named Entity Recognition (NER).
9. COCO (Common Objects in Context): computer vision tasks like object detection, segmentation, and image captioning
10. ImageNet: Image classification and object recognition

# metrics for GenAI observability

1. operational

- API/Service Uptime/Availability:
- Error Rates (Per Service/Endpoint/Model)
- Infrastructure Health (for self-managed endpoints):
- Deployment Success Rate / Rollback Rate:
- Data Pipeline Health (for fine-tuning/RAG):
- Rate Limit/Throttling Events:

2. Performance

- Latency
- Throughput
- Resource Utilization (Per Inference/Token):
- Queue Time

3. User interaction

- User Engagement
- User Feedback
- Content Safety & Guardrail Performance
- Hallucination Rate:
- Relevance / Helpfulness Score

4. Business Impact

- Cost Savings
- Revenue Generation
- Efficiency & Productivity Gains
- Customer Satisfaction
- Compliance & Risk Reduction

# SageMaker techs

## Batch Transform

a fully managed service that allows you to efficiently run inferences on entire datasets at once.

## Clarify:

a set of capabilities SageMaker provided for Bias Detection and Explainable AI

- Data Preparation (Pre-training Bias Detection): Analyze raw training data before model training to identify and
  mitigate bias in the dataset itself
- Model Training & Evaluation (Post-training Bias Detection & Explainability): Analyze the trained model's predictions
  on a test dataset,
- Model Deployment (Post-deployment Monitoring): Continuously monitor deployed models for bias and drift in explanations
  over time. This can be integrated with SageMaker Model Monitor.

## Model Monitor

detect and analyze drift in your deployed machine learning models.

1. Purpose

- Data drift: Changes in the statistical properties of the input data (features) or actual outcomes (labels)
- Model Quality drift: A decline in the model's actual performance (e.g., accuracy, precision, recall)

2. Process: baseline -> capture data -> compare -> response to result(report, alert etc).

# Cloud Watch GenAI capability

extends traditional observability (metrics, logs, traces) to address the unique challenges of GenAI, focusing on:

- Model Performance and Cost
- Output Quality and Behavior
- User Interaction
- Application Health

1. Metrics

- Bedrock Native Metrics(InvocationCount, ThrottlingEvent etc)
- SageMaker Endpoints Metrics (Invocations, CPU/Memory/GPU Utilization etc)
- Custom Application Metrics (Token Usage, RAG Metrics, Response Quality Proxies, Safety Metrics:bias/toxicity, Business
  Impact:CostPerInteraction)
- Infra Metrics

2. logs
3. traces with X-Ray
4. Alarms based on metrics
5. Dashboard

# LLM evaluation

Rogue(word overlapping), Bleu(translation), BERT (semantic similarity),

# Goverance

## Bedrock

1. Agent Tracking
2. Model Evaluation

# Bedrock Data Automation

An automated process of ingesting, processing, transforming, updating, and managing data used by Foundation Models (FMs)
within the Amazon Bedrock ecosystem.

Bluerpints: a pre-defined, reusable, and often templated architectural patterns or solutions that enable you to quickly
and consistently deploy common data automation workflows for Amazon Bedrock.
