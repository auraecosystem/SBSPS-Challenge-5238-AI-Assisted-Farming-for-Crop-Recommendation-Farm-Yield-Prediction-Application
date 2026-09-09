import litellm

def track_cost(kwargs, completion_response, start_time, end_time):
    print("Cost:", kwargs.get("response_cost", 0))

litellm.success_callback = [track_cost]

litellm.completion(
  model="gpt-5.6-terra",
  messages=[{"role": "user", "content": "Hello!"}],
  stream=True
)
