

# from ..api.OAIService import OpenAIService, OpenAIRateLimiter

# # default to openai tier 1, gpt4-1106-preview
# OAIRateLimiter = OpenAIRateLimiter(
#     max_requests_per_minute = 50,
#     max_tokens_per_minute = 10000
# )

# OAIService = OpenAIService(
#     api_key = os.getenv("OPENAI_API_KEY"),
#     token_encoding_name = "cl100k_base",
#     max_attempts=5,
#     rate_limiter=OAIRateLimiter,
# )