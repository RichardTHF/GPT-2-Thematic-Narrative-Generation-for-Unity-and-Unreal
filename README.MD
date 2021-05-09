# GPT-2 Unity Thematic Dalogue API

## Library requirements

- tensorflow 1.14
- simple-2-gpt
- flask

## Instructions

### Training / Finetuning 

To Train the models, simply modify the import.py script on line 14 to include the .csv or .txt file you have with your sample text. 

### Running the API

Simply run api.py, it will be accessable at http://ip?speech=a&style=b&trunc=c&length=d

*a* refers to a string which will include a prefix text you want to start the dialogue with. 

*b* refers to the thematic / style of text you want to generate, this is in a string and is the models you have trained. 

*c* is if you want to truncate the text, this is done by a string and it denotes any stop words you want to curtail the generated response with.

*d* is the length of the response, by default this is set to 100, but can go up to 1000. This is an interger. 