"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    @pytest.fixture(scope="class")
    def prompt_v2(self):
        """Carrega o prompt v2 para os testes."""
        prompt_path = Path(__file__).parent.parent / "prompts" / "bug_to_user_story_v2.yml"
        return load_prompts(str(prompt_path))
    
    def test_prompt_has_system_prompt(self, prompt_v2):
        """Verifica se o campo 'system_prompt' existe e não está vazio."""
        # Verifica se tem mensagens
        assert 'messages' in prompt_v2, "Prompt deve ter campo 'messages'"
        
        messages = prompt_v2['messages']
        assert len(messages) > 0, "Lista de mensagens não pode estar vazia"
        
        # Verifica se tem pelo menos uma mensagem do tipo 'system'
        system_messages = [msg for msg in messages if msg.get('type') == 'system']
        assert len(system_messages) > 0, "Prompt deve ter pelo menos uma mensagem 'system'"
        
        # Verifica se o conteúdo não está vazio
        system_content = system_messages[0].get('content', '')
        assert len(system_content.strip()) > 0, "Conteúdo da mensagem system não pode estar vazio"

    def test_prompt_has_role_definition(self, prompt_v2):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        # Junta todo o conteúdo do prompt
        full_content = ""
        for msg in prompt_v2.get('messages', []):
            full_content += msg.get('content', '') + " "
        
        full_content_lower = full_content.lower()
        
        # Verifica se contém definição de papel/persona
        role_keywords = [
            "você é",
            "product manager",
            "seu papel",
            "sua missão",
            "sua especialidade"
        ]
        
        has_role = any(keyword in full_content_lower for keyword in role_keywords)
        assert has_role, "Prompt deve definir uma persona ou papel (ex: 'Você é um Product Manager')"

    def test_prompt_mentions_format(self, prompt_v2):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        # Junta todo o conteúdo do prompt
        full_content = ""
        for msg in prompt_v2.get('messages', []):
            full_content += msg.get('content', '') + " "
        
        full_content_lower = full_content.lower()
        
        # Verifica se menciona formato de saída
        format_keywords = [
            "markdown",
            "user story",
            "formato",
            "estrutura",
            "como um",
            "eu quero",
            "para que"
        ]
        
        has_format = any(keyword in full_content_lower for keyword in format_keywords)
        assert has_format, "Prompt deve especificar formato de saída (Markdown / User Story)"

    def test_prompt_has_few_shot_examples(self, prompt_v2):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        # Junta todo o conteúdo do prompt
        full_content = ""
        for msg in prompt_v2.get('messages', []):
            full_content += msg.get('content', '') + " "
        
        full_content_lower = full_content.lower()
        
        # Verifica se contém exemplos
        example_keywords = [
            "exemplo",
            "example",
            "bug report:",
            "user story:"
        ]
        
        example_count = sum(full_content_lower.count(keyword) for keyword in example_keywords)
        
        # Deve ter pelo menos 2 menções de exemplos (indicando múltiplos exemplos)
        assert example_count >= 2, f"Prompt deve conter exemplos Few-shot (encontrado {example_count} menções, esperado >= 2)"

    def test_prompt_no_todos(self, prompt_v2):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        # Junta todo o conteúdo do prompt
        full_content = ""
        for msg in prompt_v2.get('messages', []):
            full_content += msg.get('content', '') + " "
        
        # Também verifica metadata
        metadata_str = str(prompt_v2.get('metadata', {}))
        full_content += metadata_str
        
        # Verifica padrões de TODO
        todo_patterns = ['[todo]', 'todo:', '# todo', 'fixme', '[tbd]']
        
        found_todos = []
        for pattern in todo_patterns:
            if pattern in full_content.lower():
                found_todos.append(pattern)
        
        assert len(found_todos) == 0, f"Prompt não deve conter TODOs ou placeholders: {found_todos}"

    def test_minimum_techniques(self, prompt_v2):
        """Verifica (através dos metadados do yaml) se pelo menos 2 técnicas foram listadas."""
        # Verifica se há metadados
        assert 'metadata' in prompt_v2, "Prompt deve ter campo 'metadata'"
        
        metadata = prompt_v2['metadata']
        assert 'techniques' in metadata, "Metadata deve ter campo 'techniques'"
        
        techniques = metadata['techniques']
        assert isinstance(techniques, list), "Campo 'techniques' deve ser uma lista"
        
        # Deve ter pelo menos 2 técnicas (Few-shot é obrigatória + 1 adicional)
        assert len(techniques) >= 2, f"Prompt deve usar pelo menos 2 técnicas (encontrado: {len(techniques)})"
        
        # Verifica se Few-shot Learning está presente
        techniques_lower = [t.lower() for t in techniques]
        has_few_shot = any('few' in t and 'shot' in t for t in techniques_lower)
        assert has_few_shot, "Uma das técnicas deve ser 'Few-shot Learning'"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])