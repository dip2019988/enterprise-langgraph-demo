from typing import List, Dict, Any, TypedDict, Annotated
import operator

class IncidentState(TypedDict):
    # User Context
    user_name: str
    user_id: str
    department: str
    raw_query: str
    sanitized_query: str       # Query after PII redaction
    
    # Mem0 Context Integration
    user_preferences: List[str]
    
    # Security Guardrail Attributes
    guardrail_passed: bool
    guardrail_violation_reason: str
    
    # Classification & Routing Metadata
    intent: str
    sub_category: str
    
    # Context Aggregators
    retrieved_docs: List[Dict[str, Any]]
    telemetry_data: Dict[str, Any]
    code_analysis_data: Dict[str, Any]
    billing_data: Dict[str, Any]
    
    # Solution State
    solution: str
    confidence_score: int
    is_cached_response: bool
    
    # Operational Controls
    retry_count: int
    human_approved: bool
    human_feedback: str
    
    # Graph Execution Trace
    visited_nodes: Annotated[List[str], operator.add]
    execution_logs: Annotated[List[str], operator.add]
