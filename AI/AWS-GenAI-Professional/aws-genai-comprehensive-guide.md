# Foundation Model

## Types

1. General-purpose model: perform many different kinds of tasks across various domains, reducing the need for multiple
   specialized models. Cost-effective for diverse workloads.

2. Specialized model: perform a single, critical task that requires high precision in a specific domain, Reduces errors
   in high-stakes scenarios

## Integration Approaches

1. Amazon Bedrock integration(unified api)

- provide a unified api to access multiple foundation models without managing infrastructure.
- pay-per-use pricing based on API calls,
- lack of model configuration control
- best when you want to focus on application logic rather than infrastructure.

2. Amazon SageMaker AI integration (self-host):

- enables custom model deployment and training with full control over model configuration.
- charges based on compute resources and storage
- Fully control over deployment settings, instance types, and scaling policies
- best for custom model,applications requiring extensive fine-tuning, specialized requirements

3. Amazon AI Factories integration(on premises)

- Bring fully managed AI infrastructure directly to your data centers
- Best for organizations with data residency requirements, regulated industries with strict compliance needs

4. Direct AI provider integration (direct api)

- integrating with model providers like Anthropic or OpenAI through their native APIs or frameworks like LangChain.
- Access to provider-specific capabilities, flexibility in integration patterns, and potential for early access to new
  features.
- Best for specifc provider or feature not available in Bedrock

## Customize Model Approaches

1. Prompt Engineering

- optimizes input prompts to achieve better outputs without modifying the model itself.
- cost-effective approach
- Best for improving model performance when fine-tuning isn't feasible or necessary.

2. Continued Pre-Training (CPT)

- broadens a model's general knowledge with lots of unlabeled, domain-specific text (like medical journals) using the
  original training method (e.g., next-word prediction) to improve core understanding,
- Amazon SageMaker's Nova CPT
- when you need the model to deeply understand a new, vast area of knowledge (like a whole new language or scientific
  field) and have lots of raw text data.

3. Fine-tuning

- Adapt the model to specific tasks, formats, or behaviors
- Need smaller, high-quality labeled datasets with specific input-output pairs
- through Modifies model weights (sometimes all, sometimes just parts via PEFT like LoRA) to align with task
  instructions.
- when you want the model to perform specific actions or follow instructions precisely

4. Nova Forge

- building custom frontier models with Amazon's Nova technology, providing infrastructure and tools to create large
  language models from scratch
- up to 1 trillion parameters with flexible deployment
- good for organizations needing highly specialized AI capabilities beyond adapting existing models.

5. Model Distillation

- where a smaller, efficient "student" model learns from a larger, powerful "teacher" model, transferring its knowledge
  to create a compact model that performs nearly as well
- The teacher processes input data and generates detailed outputs (like probabilities or "thought processes") that act
  as training signals for the student.
- Faster inference, lower memory/compute needs, reduced costs
- Easier to run in resource-constrained environments.
- Achieves near-teacher accuracy, overcoming the limitations of small models trained only on raw data.

6. Retrieval-augmented generation (RAG)

- overcome foundation models have knowledge cutoffs and lack access to your specific or proprietary information, leading
  to outdated responses or hallucinations
- connects foundation models with external knowledge sources, retrieving relevant information to ground responses in
  factual sources.
- When applications need current information beyond model training cutoffs, require domain-specific knowledge, must
  reduce hallucinations, or need source attribution.

## Model Orchestration

Complex generative AI applications often require connecting multiple models or services to create sophisticated
workflows that handle multi-step processing.

1. Model Chaining

- Connecting multiple AI models or services to create complex but structured workflows with predetermined paths
- Sequential chaining/Parallel processing/Conditional branching/Feedback loops

2. AWS Orchestration services

- AWS step functions
- AWS lambda

3. Agentic AI

- Dynamic, autonomous decision-making, choosing tools and paths in real-time to solve complex, open-ended problems
- Autonomous agents use reasoning to plan, select tools (like search, code execution), and take actions dynamically to
  achieve a goal, adapting to changing conditions and requirements.

# AWS GenAI services

## Bedrock

- Inference API
- Knowledge base integration (database:open search, document:s3)
- Agents
- Model Evaluation

## SageMaker

## Opean Search

# Non Functional requirement

1. scaling
2. Monitoring
3. Security
4. Goverance
