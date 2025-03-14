from enum import Enum
from src.config import ANTHROPIC_API_KEY, GROQ_API_KEY, OLLAMA_BASE_URL, OPENAI_API_KEY

class OpenAIModels(Enum):
	GPT_3_5_TURBO = 'gpt-3.5-turbo'
	GPT_3_5_TURBO_16K = 'gpt-3.5-turbo-0125'
	GPT_3_5_TURBO_MARCH = 'gpt-3.5-turbo-0301'
	GPT_4 = 'gpt-4'
	GPT_4_MARCH = 'gpt-4-0314'
	GPT_4_32K = 'gpt-4-32k'
	GPT_4_32K_MARCH = 'gpt-4-32k-0314'
	GPT_4_TURBO = 'gpt-4-0125-preview'
	GPT_4_VISION = 'gpt-4-vision-preview'
	GPT_4_OMNI = 'gpt-4o'
	EMBED_ADA = 'text-embedding-ada-002'
	TEXT_EMBED_3_SMALL = 'text-embedding-3-small'
	TEXT_EMBED_3_LARGE = 'text-embedding-3-large'

class OllamaModels(Enum):
	LLAMA_2 = 'llama2'
	LLAMA_2_7B = 'llama2:7b'
	CODE_LLAMA = 'codellama'
	VICUNA = 'vicuna'
	MISTRAL = 'mistral'
	NOMIC_EMBED_TEXT = 'nomic-embed-text'
	MXBAI_EMBED_LARGE = 'mxbai-embed-large'
	PHI3 = 'phi3'
	PHI3_14B = 'phi3:14b'
	
	
class ModelType(str, Enum):
	OPENAI_EMBED_ADA = 'openai-text-embedding-ada'
	OPENAI_TEXT_EMBED_3_SMALL = 'openai-text-embedding-3-small'
	OPENAI_TEXT_EMBED_3_LARGE = 'openai-text-embedding-3-large'
	OPENAI_GPT_3_5_TURBO_16K = 'openai-gpt-3.5-turbo-16k'
	OPENAI_GPT_4_TURBO_PREVIEW = 'openai-gpt-4-turbo-preview'
	OPENAI_GPT_4_VISION_PREVIEW = 'openai-gpt-4-vision-preview'
	OPENAI_GPT_4_OMNI = 'openai-gpt-4o'
	OLLAMA_LLAVA = 'ollama-llava'
	OLLAMA_BAKLLAVA = 'ollama-bakllava'
	OLLAMA_MISTRAL = 'ollama-mistral'
	OLLAMA_LLAMA_2 = 'ollama-llama2'
	OLLAMA_LLAMA_2_CHAT = 'ollama_chat-llama2'
	OLLAMA_LLAMA_3 = 'ollama-llama3'
	OLLAMA_LLAMA_3_CHAT = 'ollama_chat-llama3'
	OLLAMA_NOMIC_EMBED_TEXT = 'ollama-nomic-embed-text'
	OLLAMA_MXBAI_EMBED_LARGE = 'ollama-mxbai-embed-large'
	OLLAMA_PHI3 = 'ollama-phi3'
	OLLAMA_PHI3_14B = 'ollama-phi3-14b'
	GROQ_MIXTRAL = 'groq-mixtral'
	GROQ_GEMMA_7B_IT = 'groq-gemma-7b-it'
	GROQ_LLAMA_3_70B = 'groq-llama3-70b'
	ANTHROPIC_HAIKU = 'anthorpic-claude-3-haiku'
	ANTHROPIC_OPUS = 'anthorpic-claude-3-opus'
	ANTHROPIC_SONNET = 'anthorpic-claude-3-sonnet'
	
ACCEPTED_MULTIMODAL_MODELS = {
	ModelType.OLLAMA_BAKLLAVA.value,
	ModelType.OLLAMA_LLAVA.value,
	ModelType.OPENAI_GPT_4_VISION_PREVIEW.value,
	ModelType.OPENAI_GPT_4_OMNI.value,
	ModelType.ANTHROPIC_OPUS.value,
}

ACCEPTED_OPENAI_MODELS = {
	OpenAIModels.GPT_3_5_TURBO.value,
	OpenAIModels.GPT_3_5_TURBO_16K.value,
	OpenAIModels.GPT_4.value,
	OpenAIModels.GPT_4_32K.value,
	OpenAIModels.GPT_4_TURBO.value,
	OpenAIModels.GPT_4_VISION.value,
	OpenAIModels.EMBED_ADA.value,
	OpenAIModels.TEXT_EMBED_3_SMALL.value,
	OpenAIModels.TEXT_EMBED_3_LARGE.value,
	ModelType.OPENAI_GPT_3_5_TURBO_16K.value,
	ModelType.OPENAI_GPT_4_VISION_PREVIEW.value,
	ModelType.OPENAI_GPT_4_TURBO_PREVIEW.value,
	ModelType.OPENAI_GPT_4_OMNI.value,
}

ACCEPTED_OLLAMA_MODELS = {
	OllamaModels.LLAMA_2.value,
	OllamaModels.LLAMA_2_7B.value,
	OllamaModels.CODE_LLAMA.value,
	OllamaModels.VICUNA.value,
	OllamaModels.MISTRAL.value,
	ModelType.OLLAMA_LLAVA.value,
	ModelType.OLLAMA_BAKLLAVA.value,
	ModelType.OLLAMA_MISTRAL.value,
	ModelType.OLLAMA_LLAMA_2.value,
	ModelType.OLLAMA_LLAMA_3.value,
	ModelType.OLLAMA_LLAMA_2_CHAT.value,
	ModelType.OLLAMA_LLAMA_3_CHAT.value,
	ModelType.GROQ_MIXTRAL.value,
	ModelType.GROQ_GEMMA_7B_IT.value,
	ModelType.GROQ_LLAMA_3_70B.value,
	ModelType.OLLAMA_NOMIC_EMBED_TEXT.value,
	ModelType.OLLAMA_MXBAI_EMBED_LARGE.value,
	ModelType.OLLAMA_PHI3.value,
	ModelType.OLLAMA_PHI3_14B.value,
}

ACCEPTED_EMBEDDING_MODELS = {
	ModelType.OPENAI_EMBED_ADA.value,
	ModelType.OPENAI_TEXT_EMBED_3_SMALL.value,
	ModelType.OPENAI_TEXT_EMBED_3_LARGE.value,
	ModelType.OLLAMA_LLAMA_2.value,
	ModelType.OLLAMA_NOMIC_EMBED_TEXT.value,
	ModelType.OLLAMA_MXBAI_EMBED_LARGE.value,
}

class Embedding(str, Enum):
	EMBED_ADA = ModelType.OPENAI_EMBED_ADA.value
	TEXT_EMBED_3_SMALL = ModelType.OPENAI_TEXT_EMBED_3_SMALL.value
	TEXT_EMBED_3_LARGE = ModelType.OPENAI_TEXT_EMBED_3_LARGE.value
	NOMIC_EMBED_TEXT = ModelType.OLLAMA_NOMIC_EMBED_TEXT.value
	MXBAI_EMBED_LARGE = ModelType.OLLAMA_MXBAI_EMBED_LARGE.value

MODEL_LIST = [
	{
		"model_name": ModelType.OPENAI_EMBED_ADA,
		"embedding": True,
		"multimodal": False,
		"litellm_params": {
			"model": f"openai/{OpenAIModels.EMBED_ADA.value}",
			"api_key": OPENAI_API_KEY
		},
	},
	{
		"model_name": ModelType.OPENAI_TEXT_EMBED_3_SMALL,
		"embedding": True,
		"multimodal": False,
		"litellm_params": {
			"model": f"openai/{OpenAIModels.TEXT_EMBED_3_SMALL.value}",
			"api_key": OPENAI_API_KEY
		},
	},
	{
		"model_name": ModelType.OPENAI_TEXT_EMBED_3_LARGE,
		"embedding": True,
		"multimodal": False,
		"litellm_params": {
			"model": f"openai/{OpenAIModels.TEXT_EMBED_3_LARGE.value}",
			"api_key": OPENAI_API_KEY
		},
	},
	{
		"model_name": ModelType.OPENAI_GPT_3_5_TURBO_16K,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"openai/gpt-3.5-turbo-16k",
			"api_key": OPENAI_API_KEY
		},
	},
	# {
	# 	"model_name": ModelType.OPENAI_GPT_4_VISION_PREVIEW,
	# 	"multimodal": True,
	# 	"embedding": False,
	# 	"litellm_params": {
	# 		"model": f"openai/gpt-4-vision-preview",
	# 		"api_key": OPENAI_API_KEY
	# 	},
	# },
	# {
	# 	"model_name": ModelType.OPENAI_GPT_4_TURBO_PREVIEW,
	# 	"multimodal": False,
	# 	"embedding": False,
	# 	"litellm_params": {
	# 		"model": f"openai/gpt-4-turbo-preview",
	# 		"api_key": OPENAI_API_KEY
	# 	},
	# },
 	{
		"model_name": ModelType.OPENAI_GPT_4_OMNI,
		"multimodal": True,
		"embedding": False,
		"litellm_params": {
			"model": f"openai/gpt-4o",
			"api_key": OPENAI_API_KEY
		},
	},
	{
		"model_name": ModelType.OLLAMA_NOMIC_EMBED_TEXT,
		"embedding": True,
		"multimodal": False,
		"litellm_params": {
			"model": f"ollama/{OllamaModels.NOMIC_EMBED_TEXT.value}",
			"api_base": OLLAMA_BASE_URL
		},
	},
	{
		"model_name": ModelType.OLLAMA_MXBAI_EMBED_LARGE,
		"embedding": True,
		"multimodal": False,
		"litellm_params": {
			"model": f"ollama/{OllamaModels.MXBAI_EMBED_LARGE.value}",
			"api_base": OLLAMA_BASE_URL
		},
	},
 	{
		"model_name": ModelType.OLLAMA_PHI3,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"ollama/{OllamaModels.PHI3.value}",
			"api_base": OLLAMA_BASE_URL
		},
	},
  	{
		"model_name": ModelType.OLLAMA_PHI3_14B,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"ollama/{OllamaModels.PHI3_14B.value}",
			"api_base": OLLAMA_BASE_URL
		},
	},
	{
		"model_name": ModelType.OLLAMA_LLAVA,
		"embedding": False,
		"multimodal": True,
		"litellm_params": {
			"model": f"ollama/llava",
			"api_base": OLLAMA_BASE_URL
		},
	},
	{
		"model_name": ModelType.OLLAMA_BAKLLAVA,
		"embedding": False,
		"multimodal": True,
		"litellm_params": {
			"model": f"ollama/bakllava",
			"api_base": OLLAMA_BASE_URL
		},
	},
	{
		"model_name": ModelType.OLLAMA_MISTRAL,
		"embedding": False,
		"multimodal": True,
		"litellm_params": {
			"model": f"ollama/mistral",
			"api_base": OLLAMA_BASE_URL
		},
	},
	# {
	# 	"model_name": ModelType.OLLAMA_LLAMA_2,
	# 	"multimodal": False,
	# 	"embedding": True,
	# 	"litellm_params": {
	# 		"model": f"ollama/llama2",
	# 		"api_base": OLLAMA_BASE_URL
	# 	},
	# },
	# {
	# 	"model_name": ModelType.OLLAMA_LLAMA_3,
	# 	"multimodal": False,
	# 	"embedding": False,
	# 	"litellm_params": {
	# 		"model": f"ollama/llama3",
	# 		"api_base": OLLAMA_BASE_URL
	# 	},
	# },
	{
		"model_name": ModelType.OLLAMA_LLAMA_2_CHAT,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"ollama_chat/llama2",
			"api_base": OLLAMA_BASE_URL
		},
	},
	{
		"model_name": ModelType.OLLAMA_LLAMA_3_CHAT,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"ollama_chat/llama3",
			"api_base": OLLAMA_BASE_URL
		},
	},
	{
		"model_name": ModelType.GROQ_MIXTRAL,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"groq/mixtral-8x7b-32768",
			"api_key": GROQ_API_KEY
		},
	},
	{
		"model_name": ModelType.GROQ_GEMMA_7B_IT,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"groq/gemma-7b-it",
			"api_key": GROQ_API_KEY
		},
	},
	{
		"model_name": ModelType.GROQ_LLAMA_3_70B,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": f"groq/llama3-70b-8192",
			"api_key": GROQ_API_KEY
		},
	},
	{
		"model_name": ModelType.ANTHROPIC_HAIKU,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": "anthropic/claude-3-haiku-20240307",
			"api_key": ANTHROPIC_API_KEY
		},
	},
	{
		"model_name": ModelType.ANTHROPIC_OPUS,
		"multimodal": True,
		"embedding": False,
		"litellm_params": {
			"model": "anthropic/claude-3-opus-20240229",
			"api_key": ANTHROPIC_API_KEY
		},
	},
	{
		"model_name": ModelType.ANTHROPIC_SONNET,
		"multimodal": False,
		"embedding": False,
		"litellm_params": {
			"model": "anthropic/claude-3-sonnet-20240229",
			"api_key": ANTHROPIC_API_KEY
		},
	},
]

def filter_models(model_names):
	# Check if model_names is a single string or a list of strings
	if isinstance(model_names, str):
		# Find the model dictionary by name and return it
		return [next((model for model in MODEL_LIST if model['model_name'] == model_names), None)]
	elif isinstance(model_names, list):
		# Return a list of model dictionaries that match the names in model_names
		return [model for model in MODEL_LIST if model['model_name'] in model_names]
	else:
		# If the input is neither a string nor a list, raise an error
		raise ValueError("Input must be a string or a list of strings.")
	
def available_models(model_type=None):
    if model_type:
        return [
            {key: value for key, value in model.items() if key != "litellm_params"}
            for model in MODEL_LIST
            if model.get(model_type) and (model['litellm_params'].get('api_key') or model['litellm_params'].get('api_base'))
        ]
    else:
        return [
            {key: value for key, value in model.items() if key != "litellm_params"}
            for model in MODEL_LIST
            if model['litellm_params'].get('api_key') or model['litellm_params'].get('api_base')
        ]