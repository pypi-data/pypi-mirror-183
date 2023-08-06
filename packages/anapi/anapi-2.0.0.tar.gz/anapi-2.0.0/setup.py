
import setuptools

setuptools.setup(
	name="anapi",
	version="2.0.0",
	author="WiSpace",
	author_email="wiforumit@gmail.com",
	description="AnAPI lib",
	long_description="""
# AnAPI

## Class ChatAI

Arguments:
version="last",
api_key="standart_key"

**API key is not needed for API version 1.**

Functions:
get_answer(text: str) -> str — return answer from API
create(filename: str) -> str — create new AI and return API key
upload(filename: str) — edit AI


# Example

```py
import anapi

AI = anapi.ChatAI(2, api_key="Your api key")

while True:
    answer = AI.get_answer(input("You: "))

    print("ChatBot:", answer)

```
""",
	long_description_content_type="text/markdown",
	url="https://ai.wispace.ru/",
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)