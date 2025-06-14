# datascav-switch

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/langchain-ecosystem-blueviolet)](https://github.com/langchain-ai/langchain)
[![OpenAI](https://img.shields.io/badge/openai-required-important)](https://platform.openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**datascav-switch** é um pacote Python para conversão inteligente de formatos de documentos, utilizando IA generativa (OpenAI) e arquitetura escalável. O projeto faz parte de uma suíte de ferramentas para automação, extração e transformação de dados.

---

## Principais Features

- Conversão de PDF para Markdown com preservação de layout
- Suporte a múltiplos formatos de entrada (arquivo, URL, base64, bytes)
- Processamento paralelo e logging dinâmico
- Tracking detalhado de tokens
- Integração nativa com [LangChain](https://github.com/langchain-ai/langchain) e tracing via LangSmith

---

## Instalação

```bash
pip install datascav-switch
```

> **Requisitos:**
> - Python 3.10+
> - Chave de API da OpenAI (`OPENAI_API_KEY`)

---

## Uso Rápido

```python
from scav_switch.converters.pdf import ScavToMarkdown
scav = ScavToMarkdown(model='gpt-4.1', verbose=True)
markdown = scav.dig('/caminho/para/arquivo.pdf')
print(markdown)
```

Para exemplos completos e documentação detalhada, consulte a pasta [`docs/`](docs/) e os notebooks de cada módulo.

---

## Documentação

- Documentação detalhada e exemplos de uso estão disponíveis em cada subpasta de [`docs/`](docs/), incluindo notebooks como [`docs/conveters/pdf/ScavToMarkdown/ScavToMarkdown.ipynb`](docs/conveters/pdf/ScavToMarkdown/ScavToMarkdown.ipynb).
- Consulte também a [documentação oficial do LangChain](https://github.com/langchain-ai/langchain) para integração avançada.

---

## Licença

MIT
