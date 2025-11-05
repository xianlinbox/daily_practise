# How to design an agentic AI

## refelction pattern

1. user sent requirement
2. LLM-1 based requirement created v1 code
3. execute code v1, get the result
4. using LLM-2 to critique result, and create v2 code
5. execute v2 code to get the final resu;t

The main part is evalution the reflection:

1. code based eval is easier
2. build some ground examples
3. use LLM as a Judge
4. build Rubric based grading
5. add external info( like errors, result) in the reflection

## Tool Use
