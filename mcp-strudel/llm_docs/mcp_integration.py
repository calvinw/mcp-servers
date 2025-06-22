
# Add these tools to your MCP server (server.py)

@mcp.tool()
def get_strudel_docs(query: str = "", category: str = "", function_name: str = "") -> str:
    """
    Get Strudel documentation. Can search by query, category, or function name.
    
    Args:
        query: Search term to find relevant documentation
        category: Specific category (learn, workshop, recipes, etc.)  
        function_name: Specific Strudel function to look up
    """
    docs_system = StrudelDocsSystem()
    
    if function_name:
        return docs_system.get_function_docs(function_name)
    elif category:
        return docs_system.get_category_docs(category)
    elif query:
        return docs_system.search_docs(query)
    else:
        return docs_system.get_overview()

@mcp.tool()
def get_strudel_examples(pattern_type: str = "all") -> str:
    """
    Get Strudel code examples by pattern type.
    
    Args:
        pattern_type: Type of pattern (drums, chords, effects, etc.)
    """
    docs_system = StrudelDocsSystem()
    return docs_system.get_examples(pattern_type)

@mcp.tool()
def search_strudel_functions(search_term: str) -> str:
    """
    Search for Strudel functions by name or description.
    
    Args:
        search_term: Function name or related keyword
    """
    docs_system = StrudelDocsSystem()
    return docs_system.search_functions(search_term)
