from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, pipeline
import gradio
model = DistilBertForSequenceClassification.from_pretrained("./savedModel")
tokenizer = DistilBertTokenizerFast.from_pretrained("./savedModel")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)


def makeGuess(input):
    if (input == ""):
        return "enter some text pwease:)"
    classification = classifier(input)[0]['label']
    score = classifier(input)[0]['score']
    classification = 'Positive :) ' if classification == "LABEL_1" else "Negative :( "
    state = f"The given text is classified as {classification}, with score {score} . . ."
    return state


description = "This is something that is supposed to work, check if it works.\nBtw, it was a fun course. : )\nEnter the text you want to analyse and see the model's prediction on the left, magic"
demo = gradio.Interface(fn=makeGuess, inputs="text",
                        description=description,
                        outputs="text", title="The Final Outcome : Sentiment Analysis using DistilBERT")

if __name__ == "__main__":
    demo.launch()
