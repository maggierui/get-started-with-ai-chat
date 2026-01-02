import json
import logging
from typing import Optional, Dict, Any
from azure.ai.inference.aio import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage

logger = logging.getLogger(__name__)

class MetadataInference:
    """
    Class to infer metadata fields from a user query using an LLM.
    """

    MS_TOPIC_ALLOWLIST = {
        "archived": "Use for archived content only.",
        "article": "Use for general articles that don’t map to the intent of a pattern in the Content Pattern Library.",
        "best-practice": "Use for content that offers recommendations for working with a service or feature.",
        "blog": "Use only for the Learn Platform blog.",
        "browse-hub": "Use for pages that include a Filter pane for customers to scope results.",
        "checklist": "Use for content that contains a list of requirements or tasks to complete.",
        "concept-article": "Use for content that provides an in-depth explanation of functionality.",
        "contributor-guide": "Use for content published in a contributor guide.",
        "design-pattern": "Use for content that provides software design patterns used in architecture.",
        "end-user-help": "Use for content aimed at end users that provides a resolution on a specific issue.",
        "episode": "Use for individual pages in the Show section of Learn.",
        "error-reference": "Use for reference content that documents error codes.",
        "example-scenario": "Use for content that describes a solution architecture and suggested best practices.",
        "faq": "Use for question-and-answer formatted content.",
        "feature-availability": "Use for an article that contains all service/feature availability.",
        "feature-guide": "Use for articles that describe a service or product feature.",
        "generated-reference": "Use for consistently-structured documentation of a technical artifact.",
        "get-started": "Use for an article pattern that helps users get started using a particular product or service.",
        "glossary": "Use for an article pattern that lists relevant terms.",
        "how-to": "Use for content that shows the customer how to complete a task.",
        "hub-page": "Use for collections of related services, products, languages, and training.",
        "include": "Use in [!INCLUDE] files only.",
        "install-set-up-deploy": "Use to provide the basic structure of a Install, set up, deploy article pattern.",
        "integration": "Use for an article pattern that shows users how to connect applications, data, products, services, and devices.",
        "interactive-tutorial": "Use only for a legacy guided content experience.",
        "landing-page": "Use for content that surfaces the top customer tasks or features.",
        "language-reference": "Use for conceptual details about a specific programming language.",
        "learning-path": "Use for collections of related training and learning modules.",
        "legal": "Use for content such as EULA, terms of use, and other agreements.",
        "lifecycle": "Use for articles that document product release information.",
        "limits-and-quotas": "Use to list out the extent or thresholds to which resources and settings can be allocated.",
        "marketing-hub": "Use for top-level site pages designed to promote a product, subject, or program.",
        "module": "Use for modules that teach knowledge or skills.",
        "module-build-your-first": "Use for a training module that teaches how to use a product and guides customers through their first use.",
        "module-challenge-project": "Use for a training module that describes a real-world problem.",
        "module-choose-best-product": "Use for a training module that helps customers select the best product.",
        "module-guided-project": "Use for a training module that leads the customer step-by-step through the solution.",
        "module-intro-to-product": "Use for a training module that helps users decide whether the product will meet their needs.",
        "module-standard-concept-based": "Use for a training module that teaches what something is or explains an abstract idea.",
        "module-standard-task-based": "Use for a training module that teaches a skill via a sequence of concept units.",
        "overview": "Use for content that describes what a product or service is and what it’s used for.",
        "partner-tools": "Use for an article to list partner tools supported by a product or service.",
        "product-comparison": "Use for an article pattern that guides a customer to select the best product or service.",
        "quickstart": "Use for content that provides fundamental day-one instructions.",
        "quickstart-arm": "Use for the ARM template quickstart pattern.",
        "quickstart-bicep": "Use for the Bicep quickstart pattern.",
        "quickstart-sdk": "Use for an SDK quickstart article.",
        "reference": "Use for consistently-structured documentation of a technical artifact.",
        "reference-architecture": "Use for content that describes the architectural specification for a solution.",
        "release-notes": "Use for content that highlights capabilities, features, and enhancements.",
        "reliability-article": "Use to provide the customer with information about the reliability offerings.",
        "retired": "Use for technical content that is out of a standard support lifecycle.",
        "sample": "Use for a code project that users can download, open, build, and deploy.",
        "solution-idea": "Use for content that summarizes the overall architecture.",
        "solution-overview": "Helps administrators understand and learn how to deploy, implement, or configure.",
        "system-utilities": "Use for content describing and providing programs or applications.",
        "topic-hub": "Use for the Training career path and product pages.",
        "troubleshooting": "Use for content that helps customers resolve problems they're experiencing.",
        "troubleshooting-error-codes": "Use for developing articles that list error codes.",
        "troubleshooting-general": "Use for developing articles that help customers resolve problems.",
        "troubleshooting-known-issue": "Use for developing articles that describe known issues.",
        "troubleshooting-problem-resolution": "Use for developing articles that help customers identify the cause of the problem.",
        "tutorial": "Use for content that walks a user through a concept.",
        "ui-reference": "Use to identify a reference article linked to from an in-product menu.",
        "unit": "Use for units that teach a distinct skill step or piece of information.",
        "upgrade-and-migration-article": "Use for an article pattern that helps users upgrade or migrate.",
        "whats-new": "Use for content that describes the differences in a product or service."
    }

    def __init__(self, chat_client: ChatCompletionsClient, model_name: str):
        self._chat_client = chat_client
        self._model_name = model_name

    async def infer_metadata(self, query: str) -> Dict[str, Any]:
        """
        Infer metadata fields from the user query.
        
        :param query: The user's natural language query.
        :return: A dictionary containing inferred metadata fields.
        """
        system_prompt = self._build_system_prompt()
        
        try:
            response = await self._chat_client.complete(
                messages=[
                    SystemMessage(content=system_prompt),
                    UserMessage(content=query)
                ],
                model=self._model_name,
                temperature=0.0,  # Deterministic output
            )
            
            content = response.choices[0].message.content
            if not content:
                return {}
            
            # Clean markdown code blocks if present
            content = content.strip()
            if content.startswith("```json"):
                content = content[7:]
            elif content.startswith("```"):
                content = content[3:]
            
            if content.endswith("```"):
                content = content[:-3]
            
            content = content.strip()
                
            return json.loads(content)
        except Exception as e:
            logger.error(f"Error inferring metadata: {e}")
            return {}

    def _build_system_prompt(self) -> str:
        topic_list = "\n".join([f"- {k}: {v}" for k, v in self.MS_TOPIC_ALLOWLIST.items()])
        
        return f"""
You are a metadata extraction assistant for a Microsoft documentation search system.
Your goal is to analyze the user's query and extract the following metadata fields:

1. ms_topic: The type of content requested. You MUST choose from the following allowed values based on the user's intent:
{topic_list}

2. audience: The target audience if explicitly mentioned (e.g., "Admin", "Developer", "ITPro").

Output JSON format:
{{
    "ms_topic": "string or null",
    "audience": "string or null"
}}

Rules:
- If a field cannot be confidently inferred, set it to null.
- For ms_topic, prefer "how-to" for "how do I" questions, "overview" or "concept-article" for "what is" questions, "troubleshooting" for error/issue questions.
"""
