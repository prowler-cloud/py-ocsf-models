from typing import List, Optional

from pydantic import BaseModel

from .kb_article import KBArticle


class Remediation(BaseModel):
    """
    Describes the remediation strategy for addressing findings, including detailed descriptions, related knowledgebase (KB) articles,
    and external references. This class supports comprehensive remediation planning and documentation.

    Attributes:
    - desc (str): Detailed description of the remediation strategy.
    - kb_article_list (Optional[List[KBArticle]]): A list of KB articles describing patches or updates related to the remediation.
    - references (Optional[List[str]]): URLs or references supporting the described remediation strategy.
    """

    desc: str
    kb_article_list: Optional[List[KBArticle]]
    references: Optional[List[str]]
