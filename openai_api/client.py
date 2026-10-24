from openai import APIError, OpenAI

from config import settings

client = OpenAI(timeout=30.0, max_retries=3, api_key=settings.OPENAI_API_KEY)

MODEL = 'gpt-6-luna'
MAX_CHARS = 250

INSTRUCTIONS = f"""
Você escreve descrições para anúncios de veículos em português do Brasil.

Contexto:
A descrição aparece abaixo de uma ficha que já exibe marca, modelo,
ano, placa e preço. Sua função é complementar essa ficha.

Regras:
- Não repita marca, modelo, ano, placa ou preço.
- Escreva uma ou duas frases naturais, em um único parágrafo.
- Use no máximo {MAX_CHARS} caracteres, incluindo espaços.
- Use um tom sóbrio, direto e convidativo, sem exageros publicitários.
- Destaque o apelo do veículo para seu público, sem inventar características.
- Não afirme estado de conservação, revisão, quilometragem, equipamentos,
  economia, segurança, procedência ou garantia sem esses dados.
- Evite clichês como "oportunidade imperdível", "venha se encantar",
  "perfeito para você" e "cheio de estilo e personalidade".
- Retorne somente a descrição, sem título, aspas ou explicações.

Exemplo de tom para um veículo antigo:
"Uma opção para quem aprecia o visual de época e a nostalgia dos carros
que marcaram gerações."
""".strip()


def get_car_ai_bio(*, brand: str, model: str, year: int) -> str:
    prompt = (
        'Use os dados abaixo apenas como contexto para escrever a descrição. '
        'Eles já aparecem na ficha do anúncio e não devem ser repetidos.\n\n'
        f'Marca: {brand}\n'
        f'Modelo: {model}\n'
        f'Ano: {year}'
    )
    try:
        response = client.responses.create(
            model=MODEL,
            instructions=INSTRUCTIONS,
            input=prompt,
            max_output_tokens=400,
        )
    except APIError as exc:
        raise RuntimeError(f'Falha ao gerar descrição: {exc}') from exc

    text = ' '.join(response.output_text.split())
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS].rsplit(' ', 1)[0] + '…'
    return text
