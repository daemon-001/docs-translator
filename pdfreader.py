from typing import List, Optional
from pypdf import PdfReader
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
import logging

class PdfSummarizer:
    def __init__(self, api_key: str, base_url: str = "https://openrouter.ai/api/v1"):
        """
        Initialize the PDF summarizer with OpenAI API credentials.
        
        Args:
            api_key: OpenRouter API key
            base_url: OpenRouter API base URL
        """
        self.llm = ChatOpenAI(
            base_url=base_url,
            api_key=api_key,
            temperature=0,
            model_name='gpt-3.5-turbo'
        )
        
        # Modified prompt template to only include 'text' variable

        self.prompt_template = '''
        Give detailed summary in proper allignment and formatting:

        {text}
        '''
        
        self.prompt = PromptTemplate(
            input_variables=['text'],
            template=self.prompt_template
        )
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract_text_from_pdf(self, pdf_path: str) -> Optional[str]:
        """
        Extract text content from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text content or None if extraction fails
        """
        try:
            pdf_reader = PdfReader(pdf_path)
            text = ''
            
            for page in pdf_reader.pages:
                content = page.extract_text()
                if content:
                    text += content
            print(text)
            return text if text else None
            
        except Exception as e:
            self.logger.error(f"Error extracting text from PDF: {str(e)}")
            return None

    def summarize(self, pdf_path: str, language: str = "English") -> Optional[str]:
        """
        
        
        Args:
            pdf_path: Path to the PDF file
            language: Target language for the summary (handled by model context)
            
        Returns:
            Generated summary or None if processing fails
        """
        try:
            # Extract text from PDF
            text = self.extract_text_from_pdf(pdf_path)
            if not text:
                raise ValueError("No text content extracted from PDF")

            # Add language instruction to the text
            text_with_language = f"Please precisely translate this summary in {language}\n\n{text}"

            # Create document
            docs = [Document(page_content=text_with_language)]

            # Initialize summarization chain
            chain = load_summarize_chain(
                self.llm,
                chain_type='stuff',
                prompt=self.prompt,
                verbose=False
            )

            # Generate summary
            summary = chain.run(docs)
            return summary

        except Exception as e:
            self.logger.error(f"Error generating summary: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize summarizer
    open_api_key = "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"  # Replace with your actual API key
    summarizer = PdfSummarizer(api_key=open_api_key)
    
    # Generate summary
    pdf_path = "D:/Workspace/Project/doc-translator/new/demo.pdf"

    ################## Change language here #########################
    summary = summarizer.summarize(pdf_path, language="hindi")
    
    if summary:
        print(summary)
    else:
        print("Failed to generate summary")
    