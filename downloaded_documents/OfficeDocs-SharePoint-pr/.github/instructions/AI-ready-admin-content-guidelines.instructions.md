---
applyTo: '**'
---

# AI-ready content reviewer instructions for admin content

Apply the following instructions to all markdown files. Make each change separately, and ensure that the content is ready for AI processing.

## Metadata
- Ensure the file contains a `<metadata>` block at the top with the following fields:
  - `title`: A concise and descriptive title of the content.
  - `description`: A brief summary of the content, ideally between 150-160 characters.
  - `keywords`: A comma-separated list of relevant keywords for SEO purposes.
  - `audience`: The primary audience for the content (e.g., Developers, IT Professionals, End Users).
  - `ms.topic`: The type of content (e.g., overview, how-to, reference).
  - `ms.service`: The main service or product the content relates to (e.g., SharePoint, Microsoft 365).
  - `ms.date`: The date when the content was last updated in YYYY-MM-DD format. If it is older than 6 months, suggest an update.
  - `content-intent`: The intent of the content, such as "As an IT admin, I want to prepare my organization for Microsoft 365 Copilot."


## Content
- Ensure the content is clear, concise, and free of jargon.
- Ensure the content is written in conversational tone, using "you" and "your" to address the reader directly.
- Use headings and subheadings to organize the content logically.
- Include step-by-step instructions where applicable, using numbered lists for sequences and bullet points for lists of items.
- Add relevant links to related content or external resources for further reading.  
- Ensure any technical terms are explained or linked to definitions.
- Use `<alert>` blocks to highlight important information, warnings, or tips.
- Ensure the content is accessible, using appropriate HTML tags and attributes.
- Verify that any code snippets or commands are accurate and up-to-date.
- Ensure that any images or diagrams have appropriate alt text for accessibility.
- Review the content for SEO best practices, including the use of keywords in headings and throughout the text.
- Ensure that any references to features or products are current and reflect the latest updates from Microsoft.
- If the content is outdated or no longer relevant, suggest updates or removal.

## Semantic chunking
- Break down large sections of text into smaller, manageable chunks.
- Use paragraphs, lists, and subheadings to improve readability.
- Ensure that each chunk of content focuses on a single idea or topic.
- Rewrite headings in the format of questions, followed by a concise answer in the content. This helps with clarity and reduces AI hallucination.


## Headings
- Use clear and descriptive headings to guide the reader through the content.
- Ensure that headings are structured hierarchically (e.g., H1 for the main title, H2 for sections, H3 for subsections).

## Review Process
- After making the necessary changes, review the content for clarity and accuracy.
- Ensure that the tone and style are consistent with Microsoft documentation standards.
- Submit the updated content for final review and approval.


