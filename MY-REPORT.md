![GenI-Banner](https://github.com/genilab-fau/genial-fau.github.io/blob/8f1a2d3523f879e1082918c7bba19553cb6e7212/images/geni-lab-banner.png?raw=true)

# PromptOS: Building the Next-Gen AI Study Assistant with Smart Prompting, Dynamic Learning, and Real-Time Adaptability

Optimizing prompt engineering techniques to enhance automated requirements analysis for AI-driven software development.

* Authors: [Sathvik Gajula (Z23734253)](sgajula2023@fau.edu), [Satya Teja Yannam (Z23792803)](syannam2024@fau.edu), [Shashidhar Rameshwaram (Z23751768)](srameshwaram2024@fau.edu)
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)

## Research Question
This study investigates how different prompt engineering techniques can enhance the quality, completeness, and efficiency of automated requirements analysis for specialized software solutions. Given the dependency of large language models (LLMs) on prompt structure, we aim to identify the best strategies for eliciting comprehensive and precise software requirements.

## Arguments

### What is already known about this topic:
- Prompt engineering is crucial in optimizing LLM outputs.
- Chain-of-Thought (CoT) prompting improves multi-step reasoning by guiding models through logical sequences.
- Few-shot learning enhances domain-specific accuracy by providing contextual examples.
- Ensuring consistency and completeness in AI-generated requirements remains challenging.
- Techniques like self-consistency and recursive prompting reinforce accuracy and prevent deviations.
- Multi-step prompting progressively refines responses, leading to structured and logical outputs.

### What this research is exploring:
- A comparative analysis of ten prompt engineering techniques to determine their effectiveness in generating software requirements.
- An evaluation of Chain-of-Thought Prompting, Automatic Chain-of-Thought (Auto-CoT), Few-Shot Learning, Meta-Prompting, Self-Consistency, Two-Level Prompting, Contrastive Prompting, Multi-Turn Prompting, Recursive Prompting, and Role-Based Prompting.
- The impact of model parameters, such as temperature, context window, and prediction length, on response quality and clarity.

## Implications for Practice

- Automating requirement generation to reduce manual effort and accelerate development lifecycles.
- Enhancing precision in domain-specific applications using structured prompting methodologies.
- Improving functional and non-functional requirement separation using Two-Level and Meta-Prompting.
- Enabling development teams to create robust specifications with minimal manual intervention.

## Research Method

This study was conducted using the *llama3.2 model via Ollama, testing each of the ten prompting techniques for generating requirements of a **Physics Discord Bot*. The evaluation criteria included:

- *Output Comprehensiveness*: Assessing the depth and structure of generated requirements.
- *Processing Efficiency*: Measuring response time and computational load.
- *Readability and Clarity*: Evaluating the logical coherence and ease of understanding.
- *Uniqueness and Redundancy*: Identifying novel insights vs. repeated information.
- *Parameter Impact Analysis*: Analyzing the influence of temperature, context window size, and token limits.

## Techniques Evaluated

### 1. Chain-of-Thought Prompting
This technique enhances reasoning by instructing the model to logically break down its responses step by step. It is effective in structuring outputs but may introduce unnecessary complexity for straightforward tasks.

### 2. Automatic Chain-of-Thought (Auto-CoT)
Auto-CoT automates the reasoning chain generation, reducing manual effort. However, it may sometimes introduce redundant steps or errors due to automated clustering and sampling.

### 3. Few-Shot Learning
Few-shot learning provides domain-specific examples to guide response generation. While this technique is fast, it often lacks depth and elaboration beyond the provided examples.

### 4. Meta-Prompting
Meta-prompting structures the prompt into explicit categories, such as security, integrations, and performance. This approach consistently produces well-organized, comprehensive, and detailed outputs.

### 5. Self-Consistency
This method generates multiple variations of a response and selects the most consistent version. It ensures logical coherence but may lead to minor redundancy across outputs.

### 6. Two-Level Prompting
Two-Level Prompting first generates high-level requirement categories and then refines them into detailed specifications. This approach effectively separates functional and non-functional requirements while maintaining clarity.

### 7. Contrastive Prompting
Contrastive Prompting compares requirement styles, helping refine distinctions between different approaches. It enhances analytical tasks but slightly increases processing time.

### 8. Multi-Turn Prompting
This interactive technique breaks down requirement generation into sequential steps, enhancing refinement. However, it increases response latency due to iterative feedback loops.

### 9. Recursive Prompting
Recursive Prompting instructs the model to iteratively review and improve its responses, resulting in high-quality outputs. However, it significantly extends processing time.

### 10. Role-Based Prompting
Role-Based Prompting adjusts responses based on target audience expertise. It simplifies explanations for beginners while ensuring depth and technical precision for experts.

## Results

### Output Comprehensiveness
- *Meta-Prompting* produced the most detailed and structured requirements.
- *Chain-of-Thought* and *Two-Level Prompting* generated logical, well-structured outputs.
- *Self-Consistency* provided well-structured responses but was prone to minor redundancy.
- *Few-Shot Learning* generated the least detailed responses.
- *Auto-CoT* occasionally introduced errors due to its automated nature.

### Processing Efficiency
- *Few-Shot Learning* was the fastest technique.
- *Multi-Turn and Role-Based Prompting* followed with slightly higher latency.
- *Recursive Prompting* had the longest processing time due to its iterative refinement process.
- *Techniques like Two-Level Prompting and Chain-of-Thought* required additional processing but delivered superior clarity.

### Parameter Impact
- *Lower temperature settings (0.3-0.4)* resulted in more concise and focused outputs.
- *Higher temperatures (0.7+)* introduced variability but reduced consistency.
- *Expanding the context window* improved requirement detail but increased computational load.
- *Higher token limits* facilitated better-structured responses but extended processing time.

### Quality Assessment
- *Meta-Prompting and Self-Consistency* produced the most structured and practical requirements.
- *Two-Level Prompting* effectively separated different requirement categories.
- *Chain-of-Thought* added logical breakdowns but occasionally introduced unnecessary complexity.
- *Few-Shot Learning* was the least effective in producing detailed, implementable requirements.
- *Auto-CoT* was efficient but sometimes generated redundant or suboptimal reasoning chains.

## Further Research

1. *Pipeline Optimization*: Combining techniques like Few-Shot with Self-Consistency to improve efficiency and quality.
2. *Domain-Specific Adaptation*: Extending this study to fields like medicine, finance, and education.
3. *Automated Prompt Generation*: Investigating AI-driven automatic generation of optimized prompt templates.
4. *Validation Mechanisms*: Implementing post-processing steps to validate AI-generated requirements against real-world standards.
5. *Multi-Model Comparisons*: Expanding beyond llama3.2 to test different LLM architectures.
6. *Human-AI Collaboration*: Developing interactive frameworks where human experts refine AI-generated requirements in real time.

This study establishes a structured foundation for optimizing AI-driven requirements engineering, leading to more accurate and efficient software development workflows.
