try:
    from langchain_ollama import OllamaLLM
    from langchain_core.prompts import PromptTemplate
except Exception:
    OllamaLLM = None
    PromptTemplate = None


def load_llm(model_name="mistral"):
    if OllamaLLM is None:
        return None
    return OllamaLLM(model=model_name)


def summarize(llm, content: str) -> str:
    if llm is None or PromptTemplate is None:
        return "(LLM unavailable)"

    prompt = PromptTemplate(
        input_variables=["content"],
        template="Summarize the following content concisely:\n{content}",
    )

    return llm.invoke(prompt.format(content=content[:6000]))
