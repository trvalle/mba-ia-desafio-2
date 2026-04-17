"""
Executa avaliação completa com output detalhado
"""
import sys
import os
from pathlib import Path

# Garantir que estamos no diretório src
src_dir = Path(__file__).parent / "src"
os.chdir(src_dir)
sys.path.insert(0, str(src_dir))

# Importar e executar
from evaluate import main

if __name__ == "__main__":
    print("🚀 Iniciando avaliação completa...")
    print(f"📂 Diretório de trabalho: {os.getcwd()}\n")
    
    try:
        main()
        print("\n✅ Avaliação concluída com sucesso!")
    except KeyboardInterrupt:
        print("\n⚠️  Avaliação interrompida pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro durante avaliação: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
